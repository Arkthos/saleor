"""Focused CyberMarket units with no database or network dependency.

Isolated execution uses --noconftest to avoid repository-wide fixture services.
These tests exercise product functions, not copied implementations.
"""

from types import SimpleNamespace

import jwt
import pytest
from django.conf import settings
from django.middleware.csrf import _mask_cipher_secret
from freezegun import freeze_time

from saleor.account.throttling import get_delay_time
from saleor.core.anonymize import obfuscate_email, obfuscate_string
from saleor.core.auth import get_token_from_request
from saleor.core.jwt import jwt_decode
from saleor.core.utils import get_client_ip
from saleor.graphql.account.mutations.authentication.utils import _does_token_match


@pytest.fixture(autouse=True)
def synthetic_signing_settings(settings):
    """Use a synthetic key of adequate length without touching product settings."""
    settings.SECRET_KEY = "cybermarket-unit-only-synthetic-signing-key-32-plus"


def _record(record_property, case_id, component, kind="unit_contract"):
    record_property("cybermarket_unit_id", case_id)
    record_property("component", component)
    record_property("evidence_type", kind)


def test_signature_tamper_rejected(record_property):
    """CM-U01: establish valid control, then change signature bytes."""
    _record(record_property, "CM-U01", "jwt_signature")
    token = jwt.encode({"sub": "synthetic"}, settings.SECRET_KEY, algorithm="HS256")
    assert jwt_decode(token)["sub"] == "synthetic"
    header, payload, signature = token.split(".")
    changed = ("A" if signature[0] != "A" else "B") + signature[1:]
    assert changed != signature
    with pytest.raises(jwt.InvalidSignatureError):
        jwt_decode(".".join([header, payload, changed]))


@freeze_time("2026-11-02T12:00:00Z")
def test_expired_jwt_rejected(record_property):
    """CM-U02: signed token already expired under an explicit clock."""
    _record(record_property, "CM-U02", "jwt_exp")
    token = jwt.encode(
        {"sub": "synthetic", "exp": 1793620740}, settings.SECRET_KEY, algorithm="HS256"
    )
    with pytest.raises(jwt.ExpiredSignatureError):
        jwt_decode(token)


@freeze_time("2026-11-02T12:00:00Z")
def test_not_before_in_future_rejected(record_property):
    """CM-U03: signed token not valid yet must not be accepted."""
    _record(record_property, "CM-U03", "jwt_nbf")
    token = jwt.encode(
        {"sub": "synthetic", "nbf": 1793621400, "exp": 1793622000},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    with pytest.raises(jwt.ImmatureSignatureError):
        jwt_decode(token)


@pytest.mark.parametrize(
    ("_case", "other_secret", "expected"),
    [
        ("same secret remasked", "a" * 32, True),
        ("different secret", "b" * 32, False),
        ("different last character", "a" * 31 + "b", False),
    ],
)
def test_csrf_secret_comparison(record_property, _case, other_secret, expected):
    """CM-U04: use valid masks and compare secrets independently."""
    _record(record_property, "CM-U04", "csrf_compare")
    first = _mask_cipher_secret("a" * 32)
    second = _mask_cipher_secret(other_secret)
    assert _does_token_match(first, second) is expected


@pytest.mark.parametrize(
    ("_case", "value", "phone", "expected"),
    [
        ("empty", "", False, ""),
        ("none", None, False, ""),
        ("one character", "A", False, "A"),
        ("four characters", "ABCD", False, "A..."),
        ("phone", "123456", True, "123..."),
        ("short phone", "12", True, "12"),
    ],
)
def test_string_mask_literals(record_property, _case, value, phone, expected):
    """CM-U05: explicit output values expose residual characters/length."""
    _record(record_property, "CM-U05", "mask_string", "unit_characterization")
    assert obfuscate_string(value, phone=phone) == expected


@pytest.mark.parametrize(
    ("_case", "value", "expected"),
    [
        ("normal", "alice@example.test", "a...@example.test"),
        ("short local", "a@example.test", "a...@example.test"),
        ("empty local", "@example.test", "...@example.test"),
        ("no at sign", "ABCD", "A..."),
    ],
)
def test_email_mask_literals(record_property, _case, value, expected):
    """CM-U06: expected values do not call the function under test."""
    _record(record_property, "CM-U06", "mask_email", "unit_characterization")
    assert obfuscate_email(value) == expected


def test_email_multiple_at_signs_precondition(record_property):
    """CM-U07: document the helper's input assumption, not an API exploit."""
    _record(record_property, "CM-U07", "mask_email_input", "unit_characterization")
    with pytest.raises(ValueError, match=r"too many values to unpack \(expected 2\)"):
        obfuscate_email("a@b@example.test")


@pytest.mark.parametrize(
    ("_case", "forwarded", "expected"),
    [
        ("ipv6", "2001:db8::2", "2001:db8::2"),
        ("invalid then valid", "invalid,198.51.100.2", "198.51.100.2"),
        ("invalid fallback", "not-an-ip", "192.0.2.2"),
        ("empty fallback", "", "192.0.2.2"),
    ],
)
def test_ip_selection_boundaries(record_property, _case, forwarded, expected):
    """CM-U08: a request-shaped object isolates parsing, not proxy trust."""
    _record(record_property, "CM-U08", "client_ip", "unit_characterization")
    request = SimpleNamespace(
        META={"HTTP_X_FORWARDED_FOR": forwarded, "REMOTE_ADDR": "192.0.2.2"}
    )
    assert get_client_ip(request) == expected


@pytest.mark.parametrize(
    ("_case", "authorization", "expected"),
    [
        ("absent", "", None),
        ("incomplete", "Bearer", None),
        ("wrong prefix", "Basic sample", None),
        ("mixed case", "bEaReR sample", "sample"),
    ],
)
def test_auth_header_boundaries(record_property, _case, authorization, expected):
    """CM-U09: malformed/missing headers do not fabricate a credential."""
    _record(record_property, "CM-U09", "auth_header", "unit_characterization")
    request = SimpleNamespace(META={"HTTP_AUTHORIZATION": authorization})
    assert get_token_from_request(request) == expected


@pytest.mark.parametrize(
    ("_case", "ip_count", "user_count", "expected"),
    [
        ("zero", 0, 0, 1),
        ("ip threshold lower", 10, 0, 1),
        ("ip threshold upper", 11, 0, 2),
        ("last uncapped ip", 99, 0, 512),
        ("user below cap", 0, 9, 256),
    ],
)
def test_delay_boundaries(record_property, _case, ip_count, user_count, expected):
    """CM-U10: threshold checks complement, rather than simulate, abuse."""
    _record(record_property, "CM-U10", "login_delay")
    assert get_delay_time(ip_count, user_count) == expected
