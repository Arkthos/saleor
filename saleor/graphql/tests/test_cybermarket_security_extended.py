"""CyberMarket CR C4: bounded GraphQL authentication and validation contracts.

Synthetic fixtures only; passing code-level checks are not general ASVS certification.
Read security/cybermarket/README.md for policy decisions and evidence classes.
"""

import json
from unittest.mock import patch

import graphene
import pytest

from saleor.account.error_codes import AccountErrorCode
from saleor.core.jwt import (
    JWT_ACCESS_TYPE,
    JWT_REFRESH_TYPE,
    create_access_token,
    create_refresh_token,
    jwt_decode,
)
from saleor.graphql.tests.utils import assert_no_permission, get_graphql_content


MUTATION_CREATE = """
mutation CyberMarketCreate($email: String!, $password: String!, $aud: String) {
  tokenCreate(email: $email, password: $password, audience: $aud) {
    token
    refreshToken
    csrfToken
    errors { code field }
  }
}
"""

MUTATION_REFRESH = """
mutation CyberMarketRefresh($refresh: String) {
  tokenRefresh(refreshToken: $refresh) {
    token
    errors { code field }
  }
}
"""

QUERY_USER = """
query CyberMarketUser($id: ID!) { user(id: $id) { id email isStaff } }
"""


def _record(record_property, case_id, risk_ids, observation_ids, kind="security_contract"):
    for key, value in {
        "cybermarket_case_id": case_id,
        "risk_id": risk_ids,
        "observation_id": observation_ids,
        "evidence_type": kind,
    }.items():
        record_property(key, value)


@patch("saleor.account.throttling.cache")
def test_cm_t08_create_token_audience_and_expiry(
    _cache, api_client, customer_user, settings, record_property
):
    """CM-T08: tokenCreate issues typed credentials with configured expiry/audience."""
    _record(record_property, "CM-T08", "R04;R08", "H03;H04;H09")
    response = api_client.post_graphql(
        MUTATION_CREATE,
        {
            "email": customer_user.email,
            "password": customer_user._password,
            "aud": "cybermarket-lab",
        },
    )
    data = get_graphql_content(response)["data"]["tokenCreate"]
    assert data["errors"] == []
    assert data["csrfToken"]
    access = jwt_decode(data["token"])
    refresh = jwt_decode(data["refreshToken"])
    assert access["type"] == JWT_ACCESS_TYPE
    assert refresh["type"] == JWT_REFRESH_TYPE
    assert access["aud"] == refresh["aud"] == "custom:cybermarket-lab"
    assert access["exp"] - access["iat"] == int(settings.JWT_TTL_ACCESS.total_seconds())
    assert refresh["exp"] - refresh["iat"] == int(
        settings.JWT_TTL_REFRESH.total_seconds()
    )


@patch("saleor.account.throttling.cache")
@pytest.mark.parametrize("identity", ["known", "unknown"])
def test_cm_t09_token_create_invalid_credentials(
    _cache, api_client, customer_user, record_property, identity
):
    """CM-T09: invalid password and unknown user share an error code."""
    _record(record_property, "CM-T09", "R03", "H03")
    email = (
        customer_user.email
        if identity == "known"
        else "nonexistent-cybermarket@example.invalid"
    )
    response = api_client.post_graphql(
        MUTATION_CREATE, {"email": email, "password": "invalid-synthetic"}
    )
    data = get_graphql_content(response)["data"]["tokenCreate"]
    assert data["token"] is None
    assert data["refreshToken"] is None
    assert [error["code"] for error in data["errors"]] == [
        AccountErrorCode.INVALID_CREDENTIALS.name
    ]


def test_cm_t10_access_token_cannot_be_used_as_refresh(
    api_client, customer_user, record_property
):
    """CM-T10: reject a validly signed JWT of the wrong token type."""
    _record(record_property, "CM-T10", "R05", "H05;H09")
    access = create_access_token(customer_user)
    response = api_client.post_graphql(MUTATION_REFRESH, {"refresh": access})
    result = get_graphql_content(response)["data"]["tokenRefresh"]
    assert result["token"] is None
    assert [x["code"] for x in result["errors"]] == [
        AccountErrorCode.JWT_INVALID_TOKEN.name
    ]


def test_cm_t11_refresh_preserves_audience(
    api_client, customer_user, record_property
):
    """CM-T11: verify the audience claim remains attached on renewal."""
    _record(record_property, "CM-T11", "R08", "H05;H09")
    audience = "custom:cybermarket-lab"
    token = create_refresh_token(
        customer_user, {"csrfToken": "synthetic", "aud": audience}
    )
    result = get_graphql_content(
        api_client.post_graphql(MUTATION_REFRESH, {"refresh": token})
    )["data"]["tokenRefresh"]
    assert result["errors"] == []
    assert jwt_decode(result["token"])["aud"] == audience


def test_cm_t12_user_query_requires_privileges(
    api_client, user2_api_client, customer_user, record_property
):
    """CM-T12: unrelated and anonymous actors cannot query the target user."""
    _record(record_property, "CM-T12", "R10", "H11")
    variables = {"id": graphene.Node.to_global_id("User", customer_user.pk)}
    assert_no_permission(api_client.post_graphql(QUERY_USER, variables))
    assert_no_permission(user2_api_client.post_graphql(QUERY_USER, variables))


def test_cm_t13_staff_permissions_partition_customer_and_staff_records(
    staff_api_client,
    staff_user,
    customer_user,
    permission_manage_users,
    permission_manage_staff,
    record_property,
):
    """CM-T13: role-specific user resolution filters customer vs staff targets."""
    _record(record_property, "CM-T13", "R10", "H11")
    customer = {"id": graphene.Node.to_global_id("User", customer_user.pk)}
    staff = {"id": graphene.Node.to_global_id("User", staff_user.pk)}

    staff_api_client.user.user_permissions.add(permission_manage_users)
    customer_result = get_graphql_content(
        staff_api_client.post_graphql(QUERY_USER, customer)
    )
    staff_result = get_graphql_content(
        staff_api_client.post_graphql(QUERY_USER, staff)
    )
    assert customer_result["data"]["user"]["email"] == customer_user.email
    assert staff_result["data"]["user"] is None

    staff_api_client.user.user_permissions.remove(permission_manage_users)
    staff_api_client.user.user_permissions.add(permission_manage_staff)
    customer_result = get_graphql_content(
        staff_api_client.post_graphql(QUERY_USER, customer)
    )
    staff_result = get_graphql_content(
        staff_api_client.post_graphql(QUERY_USER, staff)
    )
    assert customer_result["data"]["user"] is None
    assert staff_result["data"]["user"]["email"] == staff_user.email


@pytest.mark.parametrize(
    ("debug", "expected_secure", "expected_samesite"),
    [(False, True, "None"), (True, False, "Lax")],
)
@patch("saleor.account.throttling.cache")
def test_cm_t14_refresh_cookie_flags_by_debug_setting(
    _cache,
    api_client,
    customer_user,
    settings,
    record_property,
    debug,
    expected_secure,
    expected_samesite,
):
    """CM-T14: characterize production/debug cookie policy, not TLS transport."""
    _record(record_property, "CM-T14", "R06", "H07", "characterization_only")
    settings.DEBUG = debug
    response = api_client.post_graphql(
        MUTATION_CREATE,
        {"email": customer_user.email, "password": customer_user._password},
    )
    data = get_graphql_content(response)["data"]["tokenCreate"]
    assert data["errors"] == []
    cookie = response.cookies["refreshToken"]
    assert cookie["httponly"] is True
    assert bool(cookie["secure"]) is expected_secure
    assert cookie["samesite"] == expected_samesite


def test_cm_t15_graphql_alias_limit_denies_excess(
    api_client, settings, record_property
):
    """CM-T15: reject a bounded two-alias query at configured limit=1."""
    _record(record_property, "CM-T15", "R12", "H13")
    settings.GRAPHQL_ALIAS_COUNT_LIMIT = 1
    response = api_client.post_graphql(
        "query CyberMarketAliases { first: me { id } second: me { id } }"
    )
    payload = json.loads(response.content.decode("utf-8"))
    assert any(
        "Number of aliases exceed the limit of 1" in err.get("message", "")
        for err in payload.get("errors", [])
    )


def test_cm_t16_graphql_mutation_count_limit_denies_excess(
    user_api_client, settings, record_property
):
    """CM-T16: reject two selected mutations without executing either."""
    _record(record_property, "CM-T16", "R12", "H13")
    settings.GRAPHQL_MUTATION_COUNT_LIMIT = 1
    request = """
    mutation CyberMarketMutationLimit {
      first: tokensDeactivateAll { errors { code } }
      second: tokensDeactivateAll { errors { code } }
    }
    """
    response = user_api_client.post_graphql(request)
    payload = json.loads(response.content.decode("utf-8"))
    assert any(
        "Number of mutations exceed the limit of 1" in err.get("message", "")
        for err in payload.get("errors", [])
    )
