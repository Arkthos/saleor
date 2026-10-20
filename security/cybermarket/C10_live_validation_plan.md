# C10 — Live Saleor security validation plan (2026-10-18)

Status: PLANNED; NO LIVE DEPLOYMENT OR LIVE TEST RESULTS CLAIMED.

## Objective

Reproduce the C9 fixture-backed GraphQL observations against an **authorized, isolated Saleor deployment** with synthetic accounts and orders, then distinguish transport/configuration effects from application-level access semantics.

## Environment decision

Preferred first stage: ephemeral local/container deployment pinned to Saleor source baseline `4cb1609a90eade14b6275a407bc7a00c35698090` and the experiment branch's test-only changes. PostgreSQL and Valkey must be isolated; never connect to real customers, production tokens, production email/SMS gateways, payment providers or public storefronts.

Stage two (only if needed): private HTTPS test endpoint with a reverse proxy and explicit network access controls. Do not expose a fresh test deployment publicly without authorization and configuration review.

## Preflight / acceptance gates

1. Pin image digest and source SHA, record deployment config versions, DB migrations and seed script.
2. Use unique synthetic owner, unrelated customer, anonymous actor, staff and delegated-app identities. Seed a UUID order and a legacy-number order with unmistakably synthetic PII.
3. Disable outgoing integrations, external email, payments and webhooks; use disposable secrets and ephemeral storage.
4. Confirm GraphQL health, authentication and authorization endpoints, request logging with credential/PII redaction, and an HTTPS termination plan if testing browser/session controls.
5. Establish rollback and automatic teardown; publish only sanitized requests/responses and SHA256 checksums.

## Live experiment matrix

| ID | Question | Method | Evidence / exit criterion |
|---|---|---|---|
| LIVE-01 | Is the GraphQL service reachable as intended? | Real HTTP request and negative-path health check | HTTP status, response shape, build SHA |
| LIVE-02 | Does UUID order field disclosure reproduce over HTTP? | Owner, unrelated, anonymous x email/billing/shipping on seeded UUID | Nine actor/field outcomes and request correlation IDs |
| LIVE-03 | What exactly does legacy masking reveal? | Repeat same actors/fields using legacy identifier | Exact sanitized mask representation, no raw PII in artifacts |
| LIVE-04 | Do invalid/missing identifiers leak? | Missing UUID and malformed ID with bounded requests | Status, GraphQL error class, no order data |
| LIVE-05 | What are staff/app permission boundaries? | Scoped identities and permissions, least privilege | Field-level role matrix |
| LIVE-06 | Are cookies, CSRF, CORS, proxy headers and auth transport configured safely? | Browser-compatible HTTP/HTTPS client and proxy configuration review | Header/cookie attributes and bounded negative tests |
| LIVE-07 | Does a UUID behave as an intended bearer/share capability? | Trace legitimate storefront/order retrieval flow and any share/token mechanism | Documented source of UUID, permitted audience and lifecycle; no claims of guessability without evidence |

## Stop / interpretation rules

- Only test infrastructure under explicit control and authorization.
- No brute force, credential stuffing, bulk enumeration or production scanning.
- A returned field in a synthetic order is an observed disclosure, **not automatically a Saleor vulnerability**.
- Distinguish deployment misconfiguration, intended bearer capability, and CyberMarket-specific policy mismatch.
- Adopt/reject provisional P-ORDER-01 through the fictional business requirement process before assigning conformity.
- Preserve source SHA, build digest, deployment topology, test case ID, timestamp, JUnit/HTTP traces, redacted evidence and artifact hashes.

## Current checkpoint

C9 CI run 39141812626: 53 PASS + 2 XFAIL. CM-T27 adds six exact-mask tests in commit `5575bd23744a41fbe3d77a5d1c32ccbb7455a321` with matrix commit `352d7e2b6c5940ec8a2c7a733bc841e29fe60953`; **execution pending**. No live environment provisioned in this checkpoint.
