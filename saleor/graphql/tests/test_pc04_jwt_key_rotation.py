"""PC-04: JWT signing key rotation.

Verify token validation before and after rotating the RSA signing key.
All private keys are generated temporarily for this test.
"""

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from django.test import override_settings
from jwt import InvalidSignatureError

from saleor.core import jwt_manager
from saleor.core.jwt_manager import JWTManager


def generate_private_key_pem():
    """Generate a temporary RSA private key for testing."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")


def reset_jwt_key_cache():
    """Reload the signing and verification keys."""
    JWTManager.get_private_key.cache_clear()
    JWTManager.get_public_key.cache_clear()
    jwt_manager.PUBLIC_KEY = None


def test_pc04_jwt_key_rotation(record_property):
    """Verify JWT behavior across a complete RSA key rotation."""

    record_property("cybermarket_case_id", "PC-04")
    record_property("evidence_type", "jwt_key_rotation")
    record_property("algorithm", "RS256")

    original_key = generate_private_key_pem()
    rotated_key = generate_private_key_pem()

    payload = {
        "sub": "pc04-synthetic-user",
        "purpose": "jwt-key-rotation-test",
    }

    try:
        with override_settings(
            RSA_PRIVATE_KEY=original_key,
        ):
            reset_jwt_key_cache()

            old_token = JWTManager.encode(payload)
            old_key_id = JWTManager.get_key_id()

            decoded_before_rotation = JWTManager.decode(old_token)

            assert decoded_before_rotation["sub"] == payload["sub"]

            with override_settings(
                RSA_PRIVATE_KEY=rotated_key,
            ):
                reset_jwt_key_cache()

                new_token = JWTManager.encode(payload)
                new_key_id = JWTManager.get_key_id()

                assert old_key_id != new_key_id

                with pytest.raises(InvalidSignatureError):
                    JWTManager.decode(old_token)

                decoded_after_rotation = JWTManager.decode(new_token)

                assert decoded_after_rotation["sub"] == payload["sub"]

                record_property("old_token_before_rotation", "accepted")
                record_property("old_token_after_rotation", "rejected")
                record_property("new_token_after_rotation", "accepted")
                record_property("key_id_changed", "true")

    finally:
        reset_jwt_key_cache()
