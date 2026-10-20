"""CyberMarket CR C5: trust-boundary and delegated-permission characterization.

These tests verify selected source-code semantics with synthetic inputs.
They do NOT model the proxy, production rate limiting, or third-party apps.
"""

import jwt
import pytest

from saleor.account.throttling import MAX_DELAY, get_delay_time
from saleor.core.auth import get_token_from_request
from saleor.core.jwt import create_access_token_for_app, jwt_decode
from saleor.core.utils import get_client_ip


def _record(record_property, case_id, risks, observations, kind):
    record_property("cybermarket_case_id", case_id)
    record_property("risk_id", risks)
    record_property("observation_id", observations)
    record_property("evidence_type", kind)


@pytest.mark.parametrize(
    ("bearer_header", "authorization_header", "expected"),
    [
        ("preferred", "Bearer fallback", "preferred"),
        (None, "JWT fallback", "fallback"),
        (None, "Basic ignored", None),
    ],
)
def test_cm_t17_authentication_header_precedence(
    rf, record_property, bearer_header, authorization_header, expected
):
    """CM-T17: document the two supported authentication header pathways."""
    _record(record_property, "CM-T17", "R01", "H01", "characterization_only")
    request = rf.get("/", HTTP_AUTHORIZATION=authorization_header)
    if bearer_header is not None:
        request.META["HTTP_AUTHORIZATION_BEARER"] = bearer_header
    assert get_token_from_request(request) == expected


@pytest.mark.parametrize(
    ("forwarded", "expected_source"),
    [
        ("198.51.100.20, 203.0.113.22", "198.51.100.20"),
        ("untrusted-not-an-ip", "192.0.2.10"),
        ("203.0.113.42", "203.0.113.42"),
    ],
)
def test_cm_t18_forwarded_client_ip_precedence(
    rf, record_property, forwarded, expected_source
):
    """CM-T18: document first valid forwarded IP and REMOTE_ADDR fallback."""
    _record(record_property, "CM-T18", "R01;R02", "H14", "characterization_only")
    request = rf.get("/", HTTP_X_FORWARDED_FOR=forwarded, REMOTE_ADDR="192.0.2.10")
    assert get_client_ip(request) == expected_source


@pytest.mark.parametrize(
    ("ip_count", "ip_user_count", "expected"),
    [
        (1, 0, 1),
        (11, 0, 2),
        (21, 0, 4),
        (1, 3, 4),
        (100, 1, MAX_DELAY),
        (1, 10, MAX_DELAY),
    ],
)
def test_cm_t19_throttling_delay_algorithm(
    record_property, ip_count, ip_user_count, expected
):
    """CM-T19: bounded deterministic backoff; NOT a deployed-proxy test."""
    _record(record_property, "CM-T19", "R02", "H02", "security_contract")
    assert get_delay_time(ip_count, ip_user_count) == expected


@pytest.mark.parametrize("intersection", ["overlap", "disjoint"])
def test_cm_t20_delegated_application_permission_intersection(
    app,
    staff_user,
    permission_manage_apps,
    permission_manage_products,
    record_property,
    intersection,
):
    """CM-T20: delegated token permissions are the user/app intersection."""
    _record(record_property, "CM-T20", "R13", "H15", "security_contract")
    staff_user.user_permissions.set([permission_manage_products])
    if intersection == "overlap":
        app.permissions.set([permission_manage_products, permission_manage_apps])
        expected = {"MANAGE_PRODUCTS"}
    else:
        app.permissions.set([permission_manage_apps])
        expected = set()

    token = create_access_token_for_app(app=app, user=staff_user)
    claims = jwt_decode(token)
    assert set(claims["permissions"]) == expected
    assert set(claims["user_permissions"]) == {"MANAGE_PRODUCTS"}


def test_cm_t21_unsigned_jwt_is_not_accepted(record_property):
    """CM-T21: unsigned 'none' algorithm must not be decoded as trusted."""
    _record(record_property, "CM-T21", "R08", "H09", "security_contract")
    unsigned = jwt.encode({"sub": "synthetic"}, key="", algorithm="none")
    with pytest.raises(jwt.PyJWTError):
        jwt_decode(unsigned)
