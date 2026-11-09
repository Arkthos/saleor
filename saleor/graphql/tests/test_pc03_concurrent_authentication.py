
"""PC-03: Concurrent authentication throttling.

Verify that simultaneous authentication attempts from the same IP
respect Saleor's blocking mechanism.

Uses synthetic credentials and an isolated cache. This test does
not represent production traffic or a distributed deployment.
"""

from concurrent.futures import ThreadPoolExecutor
from threading import Event, Lock
from unittest.mock import patch

import pytest
from django.core.cache import caches
from django.core.exceptions import ValidationError
from django.test import override_settings

from saleor.account.error_codes import AccountErrorCode
from saleor.account.throttling import (
    authenticate_with_throttling,
    get_cache_key_blocked_ip,
    get_cache_key_failed_ip,
)


@pytest.mark.django_db(transaction=True)
def test_pc03_concurrent_authentication_same_ip(
    rf, customer_user, record_property
):
    """Verify that only the first request crosses the blocking gate."""

    record_property("cybermarket_case_id", "PC-03")
    record_property("evidence_type", "concurrency_characterization")
    record_property("scenario", "simultaneous_invalid_password_same_ip")

    ip = "192.0.2.30"
    workers = 6

    first_request_entered = Event()
    release_first_request = Event()
    first_request_lock = Lock()
    first_request_seen = False

    cache_settings = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "pc03-isolated-authentication",
        }
    }

    def controlled_retrieve(email):
        nonlocal first_request_seen

        with first_request_lock:
            is_first = not first_request_seen
            if is_first:
                first_request_seen = True

        if is_first:
            first_request_entered.set()
            if not release_first_request.wait(timeout=15):
                raise TimeoutError(
                    "The first authentication request was not released."
                )

        return None

    def attempt(_):
        request = rf.post("/", REMOTE_ADDR=ip)

        try:
            result = authenticate_with_throttling(
                request,
                customer_user.email,
                "incorrect-pc03-password",
            )
            return "processed" if result is None else "authenticated"

        except ValidationError as exc:
            if exc.code == AccountErrorCode.LOGIN_ATTEMPT_DELAYED.value:
                return "delayed"
            return f"validation:{exc.code}"

    with override_settings(CACHES=cache_settings):
        test_cache = caches["default"]
        test_cache.clear()

        try:
            with patch(
                "saleor.account.throttling.cache", test_cache
            ), patch(
                "saleor.account.throttling.retrieve_user_by_email",
                side_effect=controlled_retrieve,
            ):
                with ThreadPoolExecutor(max_workers=workers) as executor:
                    first_future = executor.submit(attempt, 0)

                    assert first_request_entered.wait(timeout=10), (
                        "The first request did not reach the authentication gate."
                    )

                    other_futures = [
                        executor.submit(attempt, i)
                        for i in range(1, workers)
                    ]

                    try:
                        other_outcomes = [
                            future.result(timeout=10)
                            for future in other_futures
                        ]
                    finally:
                        release_first_request.set()

                    first_outcome = first_future.result(timeout=10)

                outcomes = [first_outcome, *other_outcomes]

                processed = outcomes.count("processed")
                delayed = outcomes.count("delayed")
                authenticated = outcomes.count("authenticated")

                failed_count = test_cache.get(
                    get_cache_key_failed_ip(ip), 0
                )
                blocked_until = test_cache.get(
                    get_cache_key_blocked_ip(ip)
                )

                record_property("attempts_total", str(workers))
                record_property("attempts_processed", str(processed))
                record_property("attempts_delayed", str(delayed))
                record_property("attempts_authenticated", str(authenticated))
                record_property("failed_counter", str(failed_count))
                record_property("blocking_active", str(blocked_until is not None))

                assert authenticated == 0
                assert processed == 1, (
                    f"Unexpected authentication outcomes: {outcomes}"
                )
                assert delayed == workers - 1, (
                    f"Unexpected blocking outcomes: {outcomes}"
                )
                assert failed_count == 1
                assert blocked_until is not None

        finally:
            release_first_request.set()
            test_cache.clear()
