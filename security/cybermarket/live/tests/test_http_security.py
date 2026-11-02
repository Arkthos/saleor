"""C10 probes against real loopback ASGI sockets and disposable PostgreSQL data.

No Django test client is used. Tokens and response bodies stay in memory.
Run only through the isolated live-validation job, never against an external URL.
"""

import datetime
import importlib
import ipaddress
import os
import socket
import threading
import time
import uuid
from contextlib import contextmanager

import graphene
import pytest
import requests
import uvicorn
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID
from django.core.cache import cache

import saleor.asgi as saleor_asgi
from saleor.account.models import User
from saleor.core.jwt import create_access_token, create_access_token_for_app
from saleor.order.models import Order

CREATE = """mutation($email:String!,$password:String!){tokenCreate(email:$email,password:$password){token refreshToken csrfToken errors{code field}}}"""
REFRESH = """mutation($token:String,$csrf:String){tokenRefresh(refreshToken:$token,csrfToken:$csrf){token errors{code field}}}"""
REVOKE = """mutation{tokensDeactivateAll{errors{code field}}}"""
ME = "query{me{id email}}"
ORDER = """query($id:ID!){order(id:$id){id userEmail billingAddress{streetAddress1} shippingAddress{streetAddress1}}}"""
EXTERNAL = """query($ref:String){order(externalReference:$ref){id}}"""
FIELDS = (
    "userEmail",
    "billingAddress.streetAddress1",
    "shippingAddress.streetAddress1",
)
pytestmark = pytest.mark.django_db(transaction=True)


def record(record_property, case, variant, result, status=200):
    """Write an allowlisted observation without body, identifiers or credentials."""
    for key, value in {
        "cybermarket_live_id": case,
        "variant": variant,
        "observed_class": result,
        "http_status": str(status),
        "tested_source_sha": os.environ.get("CYBERMARKET_SOURCE_SHA", "LOCAL_UNPINNED"),
    }.items():
        record_property(key, value)


def post(base, query, variables=None, token=None, session=None, verify=True, **headers):
    assert base.startswith(("http://127.0.0.1:", "https://127.0.0.1:"))
    client = session or requests
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = client.post(
        base + "/graphql/",
        json={"query": query, "variables": variables or {}},
        headers=headers,
        timeout=15,
        verify=verify,
        allow_redirects=False,
    )
    assert response.status_code == 200, f"Unexpected HTTP status {response.status_code}"
    return response, response.json()


def value(payload, field):
    for part in field.split("."):
        if payload is None:
            return None
        payload = payload[part]
    return payload


@pytest.fixture
def lab_config(settings, transactional_db):
    settings.DEBUG = False
    settings.PLAYGROUND_ENABLED = False
    settings.ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
    settings.SECURE_SSL_REDIRECT = False
    settings.SEND_USAGE_TELEMETRY = False
    settings.PLUGINS = []
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    settings.CELERY_TASK_ALWAYS_EAGER = True
    cache.clear()
    yield
    cache.clear()


@contextmanager
def serving(application, cert=None, key=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    config = uvicorn.Config(
        application,
        host="127.0.0.1",
        port=port,
        access_log=False,
        log_level="critical",
        lifespan="off",
        proxy_headers=False,
        timeout_keep_alive=1,
        timeout_graceful_shutdown=3,
        loop="asyncio",
        ssl_certfile=str(cert) if cert else None,
        ssl_keyfile=str(key) if key else None,
    )
    server = uvicorn.Server(config)
    worker = threading.Thread(
        target=server.run, kwargs={"sockets": [sock]}, daemon=True
    )
    worker.start()
    deadline = time.monotonic() + 20
    while not server.started and worker.is_alive() and time.monotonic() < deadline:
        time.sleep(0.02)
    assert server.started is True, "Loopback ASGI server did not start"
    base = f"{'https' if cert else 'http'}://127.0.0.1:{port}"
    try:
        yield base
    finally:
        server.should_exit = True
        worker.join(timeout=15)
        sock.close()
        assert worker.is_alive() is False, "ASGI worker did not stop"
        with pytest.raises(ConnectionRefusedError):
            socket.create_connection(("127.0.0.1", port), timeout=1)


@pytest.fixture
def http_service(lab_config):
    # The import is intentionally deferred until laboratory settings are active.
    application = importlib.reload(saleor_asgi).application

    with serving(application) as base:
        yield base


@pytest.fixture
def synthetic_order(order, customer_user, customer_user2):
    assert order.user_id == customer_user.pk
    assert customer_user.pk != customer_user2.pk
    order.user_email = "owner@cybermarket.test"
    order.external_reference = f"cm-live-{uuid.uuid4()}"
    order.billing_address.street_address_1 = "CM Billing Sentinel"
    order.billing_address.save(update_fields=["street_address_1"])
    # The standard fixture may share billing/shipping; clone before changing it.
    order.shipping_address = order.billing_address.get_copy()
    order.shipping_address.street_address_1 = "CM Shipping Sentinel"
    order.shipping_address.save(update_fields=["street_address_1"])
    order.save(update_fields=["user_email", "external_reference", "shipping_address"])
    return order


@pytest.fixture
def tls_material(tmp_path):
    now = datetime.datetime.now(datetime.UTC)
    ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ca_name = x509.Name(
        [x509.NameAttribute(NameOID.COMMON_NAME, "CyberMarket disposable lab CA")]
    )
    ca = (
        x509.CertificateBuilder()
        .subject_name(ca_name)
        .issuer_name(ca_name)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=1))
        .not_valid_after(now + datetime.timedelta(days=1))
        .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
        .add_extension(
            x509.KeyUsage(True, False, False, False, False, True, True, False, False),
            critical=True,
        )
        .sign(ca_key, hashes.SHA256())
    )
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    cert = (
        x509.CertificateBuilder()
        .subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")]))
        .issuer_name(ca_name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=1))
        .not_valid_after(now + datetime.timedelta(days=1))
        .add_extension(
            x509.SubjectAlternativeName(
                [
                    x509.DNSName("localhost"),
                    x509.IPAddress(ipaddress.ip_address("127.0.0.1")),
                ]
            ),
            critical=False,
        )
        .add_extension(
            x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False
        )
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(ca_key, hashes.SHA256())
    )
    ca_path, cert_path, key_path = [
        tmp_path / name for name in ["ca.pem", "server.pem", "server.key"]
    ]
    ca_path.write_bytes(ca.public_bytes(serialization.Encoding.PEM))
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    key_path.write_bytes(
        key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
    )
    key_path.chmod(0o600)
    return ca_path, cert_path, key_path


def test_live_01_health_and_real_http(http_service, record_property):
    health = requests.get(http_service + "/health/", timeout=10)
    assert health.status_code == 200
    _, result = post(http_service, "query{__typename}")
    assert result == {"data": {"__typename": "Query"}}
    response = requests.post(
        http_service + "/graphql/",
        data="{",
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    assert response.status_code == 400
    record(record_property, "LIVE-01", "health-valid-malformed", "REACHABLE", 200)


@pytest.mark.parametrize("actor", ["owner", "peer", "anonymous"])
@pytest.mark.parametrize("kind", ["uuid", "legacy"])
def test_live_02_03_actor_fields(
    http_service,
    synthetic_order,
    customer_user,
    customer_user2,
    actor,
    kind,
    record_property,
):
    order = synthetic_order
    if kind == "legacy":
        order.use_old_id = True
        order.save(update_fields=["use_old_id"])
    token = {
        "owner": create_access_token(customer_user),
        "peer": create_access_token(customer_user2),
        "anonymous": None,
    }[actor]
    gid = graphene.Node.to_global_id(
        "Order", order.pk if kind == "uuid" else order.number
    )
    _, result = post(http_service, ORDER, {"id": gid}, token)
    assert result.get("errors", []) == []
    observed = result["data"]["order"]
    raw = ["owner@cybermarket.test", "CM Billing Sentinel", "CM Shipping Sentinel"]
    masked = ["o...@cybermarket.test", "C" + "." * 18, "C" + "." * 19]
    # Literal expectations are independent of the implementation's masking helpers.
    expected = raw if kind == "uuid" or actor == "owner" else masked
    assert [value(observed, f) for f in FIELDS] == expected
    record(
        record_property,
        "LIVE-02" if kind == "uuid" else "LIVE-03",
        f"{kind}:{actor}:three-fields",
        "RAW" if expected == raw else "MASKED",
    )


@pytest.mark.parametrize(
    ("_case", "gid"),
    [
        (
            "missing-uuid",
            graphene.Node.to_global_id("Order", "00000000-0000-4000-8000-000000000000"),
        ),
        ("missing-legacy", graphene.Node.to_global_id("Order", -1)),
        ("wrong-type", graphene.Node.to_global_id("User", -1)),
        ("malformed", "not-valid-global-id"),
    ],
)
def test_live_04_invalid_ids(
    http_service, synthetic_order, _case, gid, record_property
):
    before = Order.objects.count()
    _, result = post(http_service, ORDER, {"id": gid})
    data = result.get("data")
    assert data is None or data["order"] is None
    if _case == "malformed":
        assert len(result["errors"]) == 1
        assert result["errors"][0]["message"] == f"Invalid ID: {gid}. Expected: Order."
        assert result["errors"][0]["path"] == ["order"]
    else:
        assert result.get("errors", []) == []
    assert Order.objects.count() == before
    record(record_property, "LIVE-04", _case, "NO_ORDER")


@pytest.mark.parametrize(
    ("_case", "actor", "permission", "allowed"),
    [
        ("anonymous", "anonymous", False, False),
        ("customer", "customer", False, False),
        ("staff-without", "staff", False, False),
        ("staff-with", "staff", True, True),
        ("app-without", "app", False, False),
        ("app-with", "app", True, True),
        ("delegated-without-overlap", "delegated", False, False),
        ("delegated-with-overlap", "delegated", True, True),
    ],
)
def test_live_05_entitlements(
    http_service,
    synthetic_order,
    customer_user,
    staff_user,
    app_with_token,
    permission_manage_orders,
    _case,
    actor,
    permission,
    allowed,
    record_property,
):
    token = None
    if actor == "customer":
        token = create_access_token(customer_user)
    elif actor == "staff":
        if permission:
            staff_user.user_permissions.add(permission_manage_orders)
        token = create_access_token(staff_user)
    elif actor == "delegated":
        staff_user.user_permissions.add(permission_manage_orders)
        if permission:
            app_with_token.permissions.add(permission_manage_orders)
        token = create_access_token_for_app(app_with_token, staff_user)
    elif actor == "app":
        if permission:
            app_with_token.permissions.add(permission_manage_orders)
        _, token = app_with_token.tokens.create(name="cybermarket-live")
    before = (Order.objects.count(), User.objects.count())
    _, result = post(
        http_service, EXTERNAL, {"ref": synthetic_order.external_reference}, token
    )
    if allowed:
        assert result.get("errors", []) == []
        assert result["data"]["order"] == {
            "id": graphene.Node.to_global_id("Order", synthetic_order.pk)
        }
    else:
        assert result.get("data", {}).get("order") is None
        assert len(result["errors"]) == 1
        assert (
            result["errors"][0]["extensions"]["exception"]["code"] == "PermissionDenied"
        )
    assert (Order.objects.count(), User.objects.count()) == before
    record(record_property, "LIVE-05", _case, "ALLOWED" if allowed else "DENIED")


@pytest.mark.parametrize(
    ("_case", "csrf_kind", "expected"),
    [
        ("valid", "valid", None),
        ("missing", "missing", "REQUIRED"),
        ("invalid", "invalid", "JWT_INVALID_CSRF_TOKEN"),
    ],
)
def test_live_06_https_cookie_csrf(
    lab_config, tls_material, customer_user, _case, csrf_kind, expected, record_property
):
    application = importlib.reload(saleor_asgi).application

    ca, cert, key = tls_material
    with serving(application, cert, key) as base, requests.Session() as session:
        _, body = post(
            base,
            CREATE,
            {"email": customer_user.email, "password": customer_user._password},
            session=session,
            verify=str(ca),
        )
        issued = body["data"]["tokenCreate"]
        assert issued["errors"] == []
        cookie = next(c for c in session.cookies if c.name == "refreshToken")
        assert cookie.secure is True
        assert cookie.has_nonstandard_attr("HttpOnly") is True
        assert cookie.get_nonstandard_attr("SameSite") == "None"
        assert cookie.path == "/"
        csrf = (
            issued["csrfToken"]
            if csrf_kind == "valid"
            else None
            if csrf_kind == "missing"
            else "invalid-lab-csrf"
        )
        _, body = post(base, REFRESH, {"csrf": csrf}, session=session, verify=str(ca))
        refreshed = body["data"]["tokenRefresh"]
        assert [x["code"] for x in refreshed["errors"]] == (
            [] if expected is None else [expected]
        )
        assert (refreshed["token"] is not None) is (expected is None)
    record(
        record_property,
        "LIVE-06",
        "https-cookie-csrf:" + _case,
        "ALLOWED" if expected is None else "DENIED",
    )


def test_live_06_origins_and_forwarded_scheme(http_service, settings, record_property):
    settings.ALLOWED_GRAPHQL_ORIGINS = ["https://allowed.cybermarket.test"]
    for origin, status in [
        ("https://allowed.cybermarket.test", 200),
        ("https://denied.cybermarket.test", 400),
    ]:
        response = requests.options(
            http_service + "/graphql/",
            headers={
                "Origin": origin,
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type",
            },
            timeout=10,
        )
        assert response.status_code == status
        assert response.headers.get("Access-Control-Allow-Origin") == (
            origin if status == 200 else None
        )
    settings.SECURE_SSL_REDIRECT = True
    with serving(importlib.reload(saleor_asgi).application) as redirect_base:
        response = requests.get(
            redirect_base + "/graphql/", timeout=10, allow_redirects=False
        )
        assert response.status_code == 301
        assert response.headers["Location"].startswith("https://")
        # This deliberately characterizes direct-header trust before a sanitizing ingress.
        forwarded = requests.get(
            redirect_base + "/graphql/",
            headers={"X-Forwarded-Proto": "https"},
            timeout=10,
            allow_redirects=False,
        )
        assert forwarded.status_code == 405
    record(
        record_property,
        "LIVE-06",
        "cors-and-direct-forwarded-proto",
        "INGRESS_TRUST_BOUNDARY",
    )


def test_live_07_legitimate_id_and_revocation(
    http_service, synthetic_order, customer_user, customer_user2, record_property
):
    _, body = post(
        http_service,
        CREATE,
        {"email": customer_user.email, "password": customer_user._password},
    )
    issued = body["data"]["tokenCreate"]
    assert issued["errors"] == []
    query = "query{me{orders(first:10){edges{node{id}}}}}"
    _, own = post(http_service, query, token=issued["token"])
    assert own.get("errors", []) == []
    gid = graphene.Node.to_global_id("Order", synthetic_order.pk)
    assert [edge["node"]["id"] for edge in own["data"]["me"]["orders"]["edges"]] == [
        gid
    ]
    _, peer = post(http_service, query, token=create_access_token(customer_user2))
    assert peer["data"]["me"]["orders"]["edges"] == []
    _, shared = post(http_service, ORDER, {"id": gid})
    assert shared["data"]["order"]["id"] == gid
    _, revoke = post(http_service, REVOKE, token=issued["token"])
    assert revoke["data"]["tokensDeactivateAll"]["errors"] == []
    _, stale = post(http_service, ME, token=issued["token"])
    assert stale["data"]["me"] is None
    assert len(stale["errors"]) == 1
    assert stale["errors"][0]["extensions"]["exception"]["code"] == "InvalidTokenError"
    _, refresh = post(
        http_service,
        REFRESH,
        {"token": issued["refreshToken"], "csrf": issued["csrfToken"]},
    )
    assert refresh["data"]["tokenRefresh"]["token"] is None
    assert [x["code"] for x in refresh["data"]["tokenRefresh"]["errors"]] == [
        "JWT_INVALID_TOKEN"
    ]
    # A UUID already shared remains resolvable after authentication revocation.
    _, shared_after = post(http_service, ORDER, {"id": gid})
    assert shared_after["data"]["order"]["id"] == gid
    record(
        record_property,
        "LIVE-07",
        "owner-list-peer-list-shared-id-revocation",
        "CAPABILITY_PERSISTS",
    )
