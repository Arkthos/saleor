# CyberMarket CR — C10 deployment and live security validation roadmap

**Version:** 1.0 — 2026-10-18. **Status:** READY FOR TEAM EXECUTION PLAN; NOT DEPLOYED; NO LIVE RESULTS. **Owner:** class team, with designated deployment lead and evidence reviewer. **Branch:** `research/cybermarket-security-tests-v1`, PR #1 draft. **Baseline:** Saleor source `4cb1609a90eade14b6275a407bc7a00c35698090` plus experimental test-only changes. Never merge or modify functional Saleor code as part of this plan.

## 1. Goal and measurable deliverables

Test the **actual GraphQL HTTP service**, not merely Django test-client fixtures, to discriminate source-level behavior from transport, proxy, cookie, browser and deployment policy. Preserve a reproducible container deployment, sanitized raw HTTP evidence, request correlation, per-actor/field outcomes, configuration snapshots, image/source digests and independent review. Do not declare a vulnerability without a valid requirement and impact evidence.

**Definition of done:** an authorized, isolated deployment with build SHA/image digest; completed LIVE-01–LIVE-07 or explicit `BLOCKED` reasons; actor/field matrix with observed HTTP status, GraphQL errors and sanitized outputs; recorded policy decision; verified evidence hashes; reproducible teardown; independent reviewer sign-off; no synthetic secrets or raw PII in Git.

## 2. Work packages, order and gates

| Phase | Lead | Task | Exit gate / evidence |
| --- | --- | --- | --- |
| C10-00 Authorization | Coordinator | Define lab owner, allowed hosts, permitted tools, test window, synthetic data and no-external-integration rule | Written scope/authorization, prohibited targets, named reviewer |
| C10-01 Baseline | Software engineer | Pin repository SHA, container image digest, Python/dependency lock, PostgreSQL/Valkey image versions, migration revision | `environment_manifest.json`, `sha256sum` |
| C10-02 Architecture | Deployment lead | Isolated Compose/Kubernetes namespace, nonpublic binding, disposable DB/cache, controlled DNS/network, secret injection | Network diagram, ingress/egress policy, rollback and teardown |
| C10-03 Seeding | Data/test lead | Synthetic owner, unrelated customer, anonymous client, staff roles, delegated app and two orders (UUID/legacy) | Seed manifest with opaque IDs; no real email/payment/webhooks |
| C10-04 Smoke | QA | Start app, run migrations, verify health and negative HTTP path | LIVE-01, server logs and build provenance |
| C10-05 Core HTTP | Security QA | Run LIVE-02/03/04 against GraphQL with bounded requests | 9 UUID actor/field outcomes; 9 legacy; missing/malformed ID cases |
| C10-06 Entitlements | Security reviewer | Execute LIVE-05 role and app permission matrix; document expected policy per field | Actor × object × field × capability matrix |
| C10-07 Transport | Deployment/security | Execute LIVE-06 with browser/client and optional private HTTPS proxy | Cookies, CSRF, CORS, origin, forwarded headers, TLS config evidence |
| C10-08 Identifier lifecycle | Product/QA | Trace legitimate order UUID creation/exposure/sharing and LIVE-07 | Documented intended bearer-capability semantics and exposure pathways |
| C10-09 Adjudication | Requirements owner | Approve/reject/revise P-ORDER-01 and field exceptions | Signed requirement decision and traceability |
| C10-10 Closure | Evidence reviewer | Reconcile expected vs executed variants, inspect sanitized traces, verify hashes and teardown | Independent report, zero unexplained missing tests, final checkpoint |

## 3. Deployment architecture

**Stage A, required:** isolated local Docker Compose lab (Saleor API, PostgreSQL, Valkey, disposable volumes), application bound to loopback/private network. Build from pinned source; do not use `latest` images. Do not reuse real credentials, customers or production databases. Block outgoing mail, payment, SMS, webhook and analytics endpoints; use synthetic destinations or mock services. Set explicit app secrets through ephemeral environment injection, not committed files. Set `DEBUG=False` for security-relevant runs, then optionally compare `DEBUG=True` only in an isolated controlled test.

**Stage B, conditional:** private HTTPS reverse proxy, restricted IP/VPN access, controlled test DNS and disposable certificate; required for realistic `Secure` cookies, proxy trust and browser origin checks. Stage B cannot be declared tested merely because Stage A passed. Never expose the environment publicly by default.

**Startup checklist:** record `git rev-parse HEAD`, `docker image inspect` digest, Compose configuration checksum (redact secrets), `uv.lock` checksum, DB migration status, app startup logs, GraphQL schema revision, test users/roles manifest, health status and egress-block confirmation. **Rollback:** stop test clients, revoke synthetic tokens, delete containers/volumes/secrets and confirm endpoint no longer reachable.

## 4. Live test cases and expected evidence

| ID | Request matrix | Assertions and evidence | Stop condition |
| --- | --- | --- | --- |
| LIVE-01 | Valid/invalid GraphQL POST; health probe | HTTP status, schema response, request ID, app SHA, no unexpected 5xx | Service not stable |
| LIVE-02 | UUID known; owner/unrelated/anonymous × email/billing street/shipping street (9) | Distinguish raw/masked/null/denied/error for every actor-field; compare synthetic sentinel only in memory | Real PII observed |
| LIVE-03 | Legacy ID; same 3 × 3 matrix (9) | Exact representation, partial information retained, compare against approved masking expectation if one exists | Ambiguous fixture or unexpected disclosure |
| LIVE-04 | Missing UUID, invalid global ID, malformed encoding, wrong object type, nonexisting legacy number; bounded actors | No unhandled exception, error classification, response consistency; no inference of enumeration without measured evidence | Repeated 5xx or instability |
| LIVE-05 | Anonymous/owner/peer/staff-permission variants/app scopes; object/field permutations | Explicit allow/deny/obfuscation matrix with source of entitlement | Missing authority for roles |
| LIVE-06 | Token argument vs cookie, CSRF missing/invalid, same/cross-origin, trusted/untrusted proxy, HTTP vs HTTPS | Cookie Secure/HttpOnly/SameSite/Path, CORS, forwarded headers, CSRF error class, reverse proxy config | TLS or egress safety failure |
| LIVE-07 | Legitimate order flow, email/link/order reference, guest checkout and any sharing flow | Where UUID appears, audience, expiration/revocation, bearer semantics, redacted flow capture | Requires public access or non-synthetic accounts |

Each result must contain `test_id`, `variant_id`, `timestamp_utc`, `tested_source_sha`, `image_digest`, `actor_role`, `order_id_kind`, `field`, `expected_contract_id_or_null`, `http_status`, `graphql_error_code_or_null`, `observed_class` (RAW/MASKED/NULL/DENIED/ERROR), `evidence_file_sha256`, `reviewer_decision`. Never save raw tokens, emails, cookies, addresses, full response bodies or credentials in source control.

## 5. Minimal team handoff and ownership

- **Deployment lead:** environment, service health, network isolation, pinned digests, teardown.
- **Test lead:** seed and execute HTTP/GraphQL cases, compare fixtures, produce JUnit/NDJSON.
- **Security reviewer:** independently verify assertions, negative paths, transport controls and redaction.
- **Requirements owner:** determine legitimate access rules and decide P-ORDER-01; cannot be replaced by pytest.
- **Evidence custodian:** hash, archive and cross-reference artifacts and final report.

Each role may be fulfilled by one person in a small class team, but the final reviewer should be distinct from the test executor where possible.

## 6. Evidence retention and reproducibility contract

Suggested layout (artifact storage; commit only sanitized manifests):
```text
c10-evidence/
  manifest.json
  environment_manifest.json
  seed_manifest_redacted.json
  live_results.ndjson
  live_junit.xml
  proxy_headers_redacted.ndjson
  source_trace.md
  requirement_decisions.md
  SHA256SUMS
  teardown_attestation.md
```
Generate SHA256SUMS over every evidence file, verify it independently, record collection timestamp, tool versions and storage retention. Upload encrypted or access-restricted raw archives to approved storage; GitHub repository receives only redacted metadata and the verified findings report. Ensure the source/test branch SHA is immutable in each record.

## 7. Failure handling and checkpoint discipline

At the end of each work package write a checkpoint: completed tests, PASS/FAIL/XFAIL/SKIP/BLOCKED, unexecuted variants, exact commit/image/run IDs, evidence SHA, reason for failures and next action. Never overwrite a failed run with a passing rerun; preserve both. No silent XFAIL, no weak assertions, no blanket `--continue-on-collection-errors`, no `|| true` to mask test failure. Any unexpected raw disclosure or external egress pauses execution and requires review. On interruption resume from last verified checkpoint, not an assumed state.

## 8. Normative decision and reporting protocol

First record observed behavior, then the applicable requirement and its authority, then whether evidence is sufficient, then residual uncertainty. For P-ORDER-01 decide whether known UUID is an authorized bearer capability, whether anonymous order viewing is required, which personal fields are allowed, and whether masked partial values are acceptable. An unapproved proposed policy is not a confirmed Saleor violation. Report a vulnerability only with authorized scope, verified reproduction, applicable contract and demonstrated impact. No credential guessing, bulk enumeration, production scanning or customer data.

## 9. Execution readiness checklist

- [ ] Lab owner/authorization documented
- [ ] Pinned source/image and dependency digests
- [ ] Isolated network and blocked outgoing integrations
- [ ] Synthetic identities/orders seeded
- [ ] Rollback/teardown rehearsed
- [ ] LIVE-01 through LIVE-07 variant manifest agreed
- [ ] Evidence sanitizer and hashing verified
- [ ] Browser/proxy Stage B decision recorded
- [ ] P-ORDER-01 decision authority identified
- [ ] Independent reviewer and final acceptance gates agreed

**No item above is represented as already executed.** See [C2–C9 assurance report](REPORTE_INGENIERIA_ASEGURAMIENTO_C2_C9_2026-10-18.md) for test-design findings to incorporate in the live harness.
