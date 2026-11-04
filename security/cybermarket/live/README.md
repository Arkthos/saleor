# Laboratorio C10 — guía de acceso actual

Las pruebas están cerradas en el alcance planificado. Para recuperarlas o
repetirlas usar [la guía de reproducción](../../../reproduction/README.md).
Los workflows activos del repositorio limpio solo verifican integridad.
La configuración histórica está en `reproduction/reference/workflows/e2e.yml`.

El texto siguiente conserva la descripción y los procedimientos de la
instantánea del 2 de noviembre de 2026. Sus instrucciones de rama/Actions
son históricas; no describen la interfaz actual de ejecución.

---

# C10 private ASGI validation laboratory

**Status:** CLOSED within the planned private-lab scope. Source eb5d3ecb / checkout 90455ca8; run 41522626093: 26 C10, 42 independent and 211 E2E PASS, focal 59 PASS/2 expected XFAIL. Current general regression, static/quality and license checks also completed. See the academic-folder technical closure manifest; no new academic PDF/Word was generated.

## Run the prepared workflow

The lab now runs automatically on pull requests to this fork. For an explicit rerun, open Actions. Select **e2e suite**, choose **Run workflow**, and select branch **research/cybermarket-security-tests-v1**. This branch's workflow includes the original E2E job and the new **CyberMarket current integration and C10 loopback lab** job. Do not merge to main, deploy publicly, add secrets or enable a paid service as part of this procedure.

The lab job installs locked Saleor dependencies plus an explicitly pinned Playwright 1.56.0 overlay, starts disposable PostgreSQL 15 and Valkey 8.1 services, records checkout and image provenance, and runs focal integration, independent units/validators, C10 and scoped SAST. Existing Tests and Linters workflows provide general regression and pre-commit on the same PR source. A manual include_regression input can additionally repeat them inside the laboratory job. Failed test steps retain a failed outcome while later independent checks still run. The original E2E job preserves a separate artifact. Results must be reconciled by source SHA and artifact hashes before any case is marked completed.

## Implemented matrix

| Case | Real execution path | Oracle and boundary |
|---|---|---|
| LIVE-01 | Loopback HTTP ASGI health, valid GraphQL and malformed JSON | Exact HTTP/response contracts; health alone does not establish working DB-backed GraphQL |
| LIVE-02 | UUID, owner/peer/anonymous, three fields each | Exact synthetic values; characterization, not policy approval |
| LIVE-03 | Legacy ID, same actor/field matrix | Independent literal masks and owner positive control |
| LIVE-04 | Missing UUID/legacy ID, wrong type, malformed global ID | No order and no changed row counts; exact malformed-ID diagnostic |
| LIVE-05 | Anonymous/customer/staff/app/delegated user-app permissions | Eight permission variants plus a strict-writer diagnostic; exact permission/code and data absence plus unchanged rows |
| LIVE-06 | HTTPS refresh cookie, missing/invalid/valid CSRF; actual Chromium across two origins | CA verification enabled, Secure/HttpOnly/SameSite, JS invisibility and CORS browser enforcement. Direct forwarded-proto handling is characterized as an ingress trust boundary |
| LIVE-07 | Authenticated owner's order list, peer list, ID sharing, token revocation and reuse | The ID is obtained through a legitimate API flow. No external storefront was deployed; bearer-capability policy remains unapproved |

The initial 25 variants executed with **23 PASS / 2 FAIL** in run 41515853470. Their output is preserved. The corrections add a strict-writer diagnostic, giving **26 variants, all passed in run 41517858406**. They use actual TCP ASGI requests, not Django's test client. The optional probe page exists only in the test wrapper for the browser's origin and is never added to Saleor product routes.

The product middleware profile excludes only `restrict_writer_middleware`, which `saleor.tests.settings` adds as a SQL-routing diagnostic. SecurityMiddleware and JWT refresh-cookie middleware remain asserted. A separate real-HTTP case retains the stricter guard and its exact error; no product permissions or implementation are changed. Both genuine database aliases point to the disposable pytest database before serving threads start. This validates request-thread behavior, not physical replication.

The HTTP client uses a bounded requests Session, rejects non-loopback targets, disables environment proxies and requires TLS verification. Raw immutable SAST/CI evidence is exempt only from whitespace/EOF rewriting; source remains checked.

## Safety and fidelity

- Services bind to loopback; identities and addresses are synthetic, integrations/plugins disabled and email in memory. No public ingress is provisioned.
- TLS uses a disposable CA and certificate, with normal requests verification and an ephemeral Chromium NSS trust entry removed at teardown. No ignore-certificate-errors option is used.
- Pytest's socket allowlist and browser request routing restrict application probes to loopback. Package installation is a separate setup step with registry access.
- Test fixtures simplify hashing and external services. This is not production performance, production password-cost or distributed-load evidence.
- Server startup/shutdown has finite bounds. A local HTTP/HTTPS health smoke initially exposed a shutdown problem; explicit server timeouts and closed connections corrected it, and both protocols then passed with closed-port teardown checks.
- Only allowlisted outcome metadata enters JUnit properties. An artifact sanitizer removes JWTs, email addresses, private-key blocks and synthetic address sentinels before checksums and upload. Raw test logs require review before source-control publication.
- P-ORDER-01 remains provisional; executing a characterization does not approve it. No functional Saleor change is included.

## Evidence and closure

Artifacts: `cybermarket-current-technical-evidence` and `cybermarket-current-e2e-evidence`. Preserve both successful and failed runs. Capture the run/checkout/branch SHAs, package versions, PostgreSQL/Valkey digests, JUnit outcomes and SHA256SUMS; inspect redaction before committing evidence. The focal suite is a subset of general regression and must not be added to that total.

Do not close the academic technical gate until the new runtime results have been reviewed, unexpected failures resolved or characterized with valid criteria, all selected cases accounted for, and teardown verified. No academic PDF/Word should be regenerated while this gate is open.

Primary implementation reference: https://playwright.dev/python/docs/library. Playwright is an optional lab overlay, not a Saleor runtime dependency. The academic Word generator likewise uses its separate artifact environment and is excluded only from the production dependency audit; its source remains under the other quality checks.
