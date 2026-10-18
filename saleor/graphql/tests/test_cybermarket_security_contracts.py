"""CyberMarket CR: cross-operation security characterization and contract tests.

Research baseline: 4cb1609a90eade14b6275a407bc7a00c35698090.
Only synthetic fixture users, tokens and orders are used. No external targets.

IMPORTANT: A passing characterization test describes observed behavior; it does
not certify that the behavior satisfies the academic security requirement.
See security/cybermarket/README.md for test IDs and their interpretation.
"""

import json

import graphene
import pytest

from saleor.account.error_codes import AccountErrorCode
from saleor.core.jwt import (
    JWT_ACCESS_TYPE,
    JWT_REFRESH_TOKEN_COOKIE_NAME,
    create_access_token,
    create_refresh_token,
    jwt_decode,
)
from saleor.graphql.account.mutations.authentication.utils import _get_new_csrf_token
from saleor.graphql.tests.utils import (
    assert_no_permission,
    get_graphql_content,
)


QUERY_ME = """query CyberMarketMe { me { id email } }"""

MUTATION_REVOKE = """
mutation CyberMarketRevoke {
  tokensDeactivateAll { errors { code field } }
}
"""

MUTATION_REFRESH = """
mutation CyberMarketRefresh($token: String, $csrf: String) {
  tokenRefresh(refreshToken: $token, csrfToken: $csrf) {
    token
    errors { code field }
  }
}
"""

QUERY_ORDER_DETAILS = """
query CyberMarketOrder($id: ID!) {
  order(id: $id) {
    id
    userEmail
    billingAddress { streetAddress1 }
    shippingAddress { streetAddress1 }
  }
}
"""

QUERY_ORDER_EXTERNAL = """
query CyberMarketOrderExternal($externalReference: String) {
  order(externalReference: $externalReference) { id }
}
"""


def _case(record_property, case_id, risk_id, observation_id, evidence_type):
    """Persist non-sensitive case metadata in JUnit XML."""
    record_property("cybermarket_case_id", case_id)
    record_property("risk_id", risk_id)
    record_property("observation_id", observation_id)
    record_property("evidence_type", evidence_type)


def test_cm_t01_me_anonymous_and_authenticated(
    api_client, user_api_client, record_property
):
    """CM-T01: compare the same identity query across actors (R10/H11)."""
    _case(record_property, "CM-T01", "R10", "H11", "security_contract")

    anonymous = get_graphql_content(api_client.post_graphql(QUERY_ME))
    authenticated = get_graphql_content(user_api_client.post_graphql(QUERY_ME))

    assert anonymous["data"]["me"] is None
    assert authenticated["data"]["me"]["email"] == user_api_client.user.email
    assert authenticated["data"]["me"]["id"]


def test_cm_t02_revoke_invalidates_both_credentials(
    api_client, user_api_client, customer_user, record_property
):
    """CM-T02: revoke and reuse access + refresh tokens in one transaction (R07/H08)."""
    _case(record_property, "CM-T02", "R07", "H08", "security_contract")

    old_access = create_access_token(customer_user)
    csrf = _get_new_csrf_token()
    old_refresh = create_refresh_token(customer_user, {"csrfToken": csrf})
    user_api_client.token = old_access

    before = get_graphql_content(user_api_client.post_graphql(QUERY_ME))
    assert before["data"]["me"]["email"] == customer_user.email

    revoked = get_graphql_content(user_api_client.post_graphql(MUTATION_REVOKE))
    assert revoked["data"]["tokensDeactivateAll"]["errors"] == []

    # Invalid access JWT produces a top-level GraphQL error; do not use a
    # helper that asserts the complete absence of GraphQL errors.
    after_response = user_api_client.post_graphql(QUERY_ME)
    after = json.loads(after_response.content.decode("utf8"))
    assert after["data"]["me"] is None
    assert any(
        err.get("extensions", {}).get("exception", {}).get("code")
        == "InvalidTokenError"
        for err in after.get("errors", [])
    )

    refresh_response = api_client.post_graphql(
        MUTATION_REFRESH, {"token": old_refresh, "csrf": csrf}
    )
    refresh = get_graphql_content(refresh_response)["data"]["tokenRefresh"]
    assert refresh["token"] is None
    assert [e["code"] for e in refresh["errors"]] == [
        AccountErrorCode.JWT_INVALID_TOKEN.name
    ]


@pytest.mark.parametrize(
    ("transport", "csrf_input", "expected_error"),
    [
        ("argument", "none", None),
        ("cookie", "valid", None),
        ("cookie", "missing", AccountErrorCode.REQUIRED.name),
        (
            "cookie",
            "invalid",
            AccountErrorCode.JWT_INVALID_CSRF_TOKEN.name,
        ),
    ],
    ids=["argument-no-csrf", "cookie-valid-csrf", "cookie-missing-csrf", "cookie-bad-csrf"],
)
def test_cm_t03_refresh_transport_csrf_matrix(
    api_client, customer_user, record_property, transport, csrf_input, expected_error
):
    """CM-T03: CSRF requirement depends on refresh credential transport (R06/H05-H07)."""
    _case(record_property, "CM-T03", "R06", "H05-H07", "security_contract")

    csrf = _get_new_csrf_token()
    refresh_token = create_refresh_token(customer_user, {"csrfToken": csrf})
    variables = {"token": refresh_token if transport == "argument" else None}
    if transport == "cookie":
        api_client.cookies[JWT_REFRESH_TOKEN_COOKIE_NAME] = refresh_token

    if csrf_input == "valid":
        variables["csrf"] = csrf
    elif csrf_input == "invalid":
        variables["csrf"] = "incorrect-csrf"
    elif csrf_input == "none" and transport == "argument":
        variables["csrf"] = None

    content = get_graphql_content(
        api_client.post_graphql(MUTATION_REFRESH, variables)
    )
    result = content["data"]["tokenRefresh"]

    if expected_error is not None:
        assert result["token"] is None
        assert [error["code"] for error in result["errors"]] == [expected_error]
    else:
        assert result["errors"] == []
        assert jwt_decode(result["token"])["type"] == JWT_ACCESS_TYPE


def test_cm_t04_order_external_reference_requires_manage_orders(
    user_api_client, order, record_property
):
    """CM-T04: explicit external-reference permission gate (R09/H12)."""
    _case(record_property, "CM-T04", "R09", "H12", "security_contract")
    order.external_reference = "cm-reference-synthetic"
    order.save(update_fields=["external_reference"])

    response = user_api_client.post_graphql(
        QUERY_ORDER_EXTERNAL, {"externalReference": order.external_reference}
    )
    assert_no_permission(response)


def test_cm_t05_order_new_id_anonymous_field_visibility(
    api_client, order, record_property
):
    """CM-T05: describe new-ID field exposure; NOT a compliance assertion (R11/H12).

    Saleor's pre-existing tests explicitly document this behavior. The purpose
    here is to make that observation visible in the research test evidence; a
    passing test MUST NOT be interpreted as approval of its security policy.
    """
    _case(record_property, "CM-T05", "R11", "H12", "characterization_only")
    assert order.use_old_id is False

    variables = {"id": graphene.Node.to_global_id("Order", order.pk)}
    result = get_graphql_content(
        api_client.post_graphql(QUERY_ORDER_DETAILS, variables)
    )["data"]["order"]

    assert result is not None
    assert result["billingAddress"]["streetAddress1"] == (
        order.billing_address.street_address_1
    )
    assert result["shippingAddress"]["streetAddress1"] == (
        order.shipping_address.street_address_1
    )
    assert result["userEmail"] == order.user_email
def test_cm_t06_new_uuid_order_actor_matrix_characterization(
    api_client,
    user_api_client,
    user2_api_client,
    customer_user,
    customer_user2,
    order,
    record_property,
):
    """CM-T06: compare owner, unrelated client and anonymous UUID visibility.

    This test CHARACTERIZES the existing exposure; PASS does NOT mean that
    granting access to unrelated parties satisfies the business security policy.
    """
    _case(record_property, "CM-T06", "R11", "H12", "characterization_only")
    assert order.user_id == customer_user.pk
    assert customer_user2.pk != customer_user.pk
    assert order.use_old_id is False

    variables = {"id": graphene.Node.to_global_id("Order", order.pk)}
    expected = {
        "userEmail": order.user_email,
        "billingAddress": {
            "streetAddress1": order.billing_address.street_address_1
        },
        "shippingAddress": {
            "streetAddress1": order.shipping_address.street_address_1
        },
    }
    for client in (user_api_client, user2_api_client, api_client):
        response = get_graphql_content(
            client.post_graphql(QUERY_ORDER_DETAILS, variables)
        )
        actual = response["data"]["order"]
        assert actual is not None
        # Match only the selected fields; do not print fixture PII in reports.
        for field, value in expected.items():
            assert actual[field] == value


def test_cm_t07_old_id_owner_vs_nonowner_authorization(
    api_client,
    user_api_client,
    user2_api_client,
    customer_user,
    customer_user2,
    order,
    record_property,
):
    """CM-T07: legacy-number order ID access for owner versus other actors."""
    _case(record_property, "CM-T07", "R11", "H12", "security_contract")
    assert order.user_id == customer_user.pk
    assert customer_user2.pk != customer_user.pk
    order.use_old_id = True
    order.save(update_fields=["use_old_id"])

    variables = {"id": graphene.Node.to_global_id("Order", order.number)}
    owner_response = get_graphql_content(
        user_api_client.post_graphql(QUERY_ORDER_DETAILS, variables)
    )
    owner_order = owner_response["data"]["order"]
    assert owner_order is not None
    assert owner_order["userEmail"] == order.user_email

    assert_no_permission(
        user2_api_client.post_graphql(QUERY_ORDER_DETAILS, variables)
    )
    assert_no_permission(api_client.post_graphql(QUERY_ORDER_DETAILS, variables))
