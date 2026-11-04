"""C9 independent per-actor/per-field verification using synthetic orders.

These are characterization probes, not approval of P-ORDER-01.
Each pytest invocation emits its own actor/field identifier in JUnit.
"""

import graphene
import pytest

from saleor.core.anonymize import obfuscate_email, obfuscate_string
from saleor.graphql.tests.utils import get_graphql_content

QUERY = """
query CyberMarketC9($id: ID!) {
  order(id: $id) {
    userEmail
    billingAddress { streetAddress1 }
    shippingAddress { streetAddress1 }
  }
}
"""

FIELDS = (
    "userEmail",
    "billingAddress.streetAddress1",
    "shippingAddress.streetAddress1",
)
NONOWNERS = ("unrelated_customer", "anonymous")


def _value(payload, field):
    current = payload
    for part in field.split("."):
        if current is None:
            return None
        current = current[part]
    return current


def _expected(order, field):
    return {
        "userEmail": order.user_email,
        "billingAddress.streetAddress1": order.billing_address.street_address_1,
        "shippingAddress.streetAddress1": order.shipping_address.street_address_1,
    }[field]


def _record(record_property, case, variant):
    record_property("cybermarket_case_id", case)
    record_property("risk_id", "R11")
    record_property("observation_id", "H12")
    record_property("evidence_type", "characterization_only")
    record_property("variant", variant)


def _query(client, order_id):
    return get_graphql_content(client.post_graphql(QUERY, {"id": order_id}))["data"][
        "order"
    ]


@pytest.mark.parametrize("actor", NONOWNERS)
@pytest.mark.parametrize("field", FIELDS)
def test_cm_t23_uuid_nonowner_field_characterization(
    api_client,
    user2_api_client,
    customer_user,
    customer_user2,
    order,
    actor,
    field,
    record_property,
):
    """Prove each raw field independently for a known UUID; not conformance."""
    _record(record_property, "CM-T23", f"{actor}:{field}")
    assert order.user_id == customer_user.pk
    assert customer_user2.pk != order.user_id
    assert order.use_old_id is False
    client = user2_api_client if actor == "unrelated_customer" else api_client
    result = _query(client, graphene.Node.to_global_id("Order", order.pk))
    assert result is not None
    assert _value(result, field) == _expected(order, field)


@pytest.mark.parametrize("field", FIELDS)
def test_cm_t24_uuid_owner_positive_control(
    user_api_client,
    customer_user,
    order,
    field,
    record_property,
):
    """Owner's fields remain available in the same UUID access path."""
    _record(record_property, "CM-T24", f"owner:{field}")
    assert order.user_id == customer_user.pk
    assert order.use_old_id is False
    result = _query(user_api_client, graphene.Node.to_global_id("Order", order.pk))
    assert result is not None
    assert _value(result, field) == _expected(order, field)


@pytest.mark.parametrize("actor", NONOWNERS)
@pytest.mark.parametrize("field", FIELDS)
def test_cm_t25_legacy_nonowner_field_characterization(
    api_client,
    user2_api_client,
    customer_user,
    customer_user2,
    order,
    actor,
    field,
    record_property,
):
    """Check legacy path per field; unequal-to-raw is not masking adequacy."""
    _record(record_property, "CM-T25", f"{actor}:{field}")
    assert order.user_id == customer_user.pk
    assert customer_user2.pk != order.user_id
    order.use_old_id = True
    order.save(update_fields=["use_old_id"])
    client = user2_api_client if actor == "unrelated_customer" else api_client
    result = _query(client, graphene.Node.to_global_id("Order", order.number))
    assert result is not None
    assert _value(result, field) != _expected(order, field)


@pytest.mark.parametrize("actor", NONOWNERS)
def test_cm_t26_missing_uuid_no_order(
    api_client,
    user2_api_client,
    order,
    actor,
    record_property,
):
    """Nonexistent UUID must not return a synthetic order."""
    _record(record_property, "CM-T26", f"{actor}:missing_uuid")
    client = user2_api_client if actor == "unrelated_customer" else api_client
    missing = "00000000-0000-4000-8000-000000000000"
    assert str(order.pk) != missing
    result = _query(client, graphene.Node.to_global_id("Order", missing))
    assert result is None


@pytest.mark.parametrize("actor", NONOWNERS)
@pytest.mark.parametrize("field", FIELDS)
def test_cm_t27_legacy_exact_mask_characterization(
    api_client,
    user2_api_client,
    customer_user,
    customer_user2,
    order,
    actor,
    field,
    record_property,
):
    """Verify exact residual legacy masking, not merely changed strings."""
    _record(record_property, "CM-T27", f"{actor}:{field}")
    assert order.user_id == customer_user.pk
    assert customer_user2.pk != order.user_id
    order.use_old_id = True
    order.save(update_fields=["use_old_id"])
    client = user2_api_client if actor == "unrelated_customer" else api_client
    result = _query(client, graphene.Node.to_global_id("Order", order.number))
    assert result is not None
    raw = _expected(order, field)
    expected = obfuscate_email(raw) if field == "userEmail" else obfuscate_string(raw)
    assert _value(result, field) == expected
