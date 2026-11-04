"""C10 browser enforcement on two private HTTPS origins with an ephemeral CA."""

import importlib
import subprocess
import uuid
from pathlib import Path
from urllib.parse import urlsplit

import pytest
from playwright.sync_api import sync_playwright

import saleor.asgi as saleor_asgi

from .test_http_security import (
    CREATE,
    REFRESH,
    record,
    serving,
)

pytestmark = pytest.mark.django_db(transaction=True)


@pytest.fixture
def browser_ca(tls_material):
    ca, _, _ = tls_material
    database = Path.home() / ".pki" / "nssdb"
    database.mkdir(parents=True, exist_ok=True)
    directory = f"sql:{database}"
    if not (database / "cert9.db").exists():
        subprocess.run(
            ["certutil", "-N", "--empty-password", "-d", directory],
            check=True,
            capture_output=True,
            timeout=15,
        )
    nickname = "cybermarket-lab-" + str(uuid.uuid4())
    subprocess.run(
        ["certutil", "-A", "-d", directory, "-n", nickname, "-t", "C,,", "-i", str(ca)],
        check=True,
        capture_output=True,
        timeout=15,
    )
    try:
        yield
    finally:
        subprocess.run(
            ["certutil", "-D", "-d", directory, "-n", nickname],
            check=True,
            capture_output=True,
            timeout=15,
        )


def test_live_06_browser_cors_cookie_csrf(
    lab_config, tls_material, browser_ca, customer_user, settings, record_property
):
    ca, cert, key = tls_material
    application = importlib.reload(saleor_asgi).application

    async def with_probe(scope, receive, send):
        if scope.get("type") == "http" and scope["path"] == "/__cybermarket_probe__/":
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [(b"content-type", b"text/html")],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": b"<!doctype html><title>CyberMarket private probe</title>",
                }
            )
        else:
            await application(scope, receive, send)

    with (
        serving(with_probe, cert, key) as frontend,
        serving(application, cert, key) as api,
        sync_playwright() as playwright,
    ):
        settings.ALLOWED_GRAPHQL_ORIGINS = [frontend]
        browser = playwright.chromium.launch()
        try:
            context = browser.new_context(ignore_https_errors=False)
            context.route(
                "**/*",
                lambda route: route.continue_()
                if urlsplit(route.request.url).hostname == "127.0.0.1"
                else route.abort(),
            )
            page = context.new_page()
            page.goto(frontend + "/__cybermarket_probe__/")
            run = """async ({api,query,variables}) => {
              try {
                const response = await fetch(api+'/graphql/', {method:'POST',credentials:'include',headers:{'Content-Type':'application/json'},body:JSON.stringify({query,variables})});
                return {readable:true,status:response.status,body:await response.json()};
              } catch(error) {return {readable:false,error:error.name};}
            }"""
            issued = page.evaluate(
                run,
                {
                    "api": api,
                    "query": CREATE,
                    "variables": {
                        "email": customer_user.email,
                        "password": customer_user._password,
                    },
                },
            )
            assert issued["readable"] is True
            assert issued["status"] == 200
            payload = issued["body"]["data"]["tokenCreate"]
            assert payload["errors"] == []
            cookies = context.cookies([api])
            cookie = next(c for c in cookies if c["name"] == "refreshToken")
            assert cookie["secure"] is True
            assert cookie["httpOnly"] is True
            assert cookie["sameSite"] == "None"
            assert page.evaluate("document.cookie") == ""
            good = page.evaluate(
                run,
                {
                    "api": api,
                    "query": REFRESH,
                    "variables": {"csrf": payload["csrfToken"]},
                },
            )
            assert good["body"]["data"]["tokenRefresh"]["errors"] == []
            missing = page.evaluate(
                run, {"api": api, "query": REFRESH, "variables": {}}
            )
            assert missing["body"]["data"]["tokenRefresh"]["token"] is None
            assert [
                e["code"] for e in missing["body"]["data"]["tokenRefresh"]["errors"]
            ] == ["REQUIRED"]
            context.close()
            settings.ALLOWED_GRAPHQL_ORIGINS = []
            denied = browser.new_context(ignore_https_errors=False)
            denied.route(
                "**/*",
                lambda route: route.continue_()
                if urlsplit(route.request.url).hostname == "127.0.0.1"
                else route.abort(),
            )
            denied_page = denied.new_page()
            denied_page.goto(frontend + "/__cybermarket_probe__/")
            blocked = denied_page.evaluate(
                run, {"api": api, "query": "query{__typename}", "variables": {}}
            )
            assert blocked == {"readable": False, "error": "TypeError"}
            denied.close()
        finally:
            browser.close()
    record(
        record_property,
        "LIVE-06",
        "chromium-trusted-ca-two-origins",
        "CORS_COOKIE_CSRF_ENFORCED",
    )
