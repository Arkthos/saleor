# C9 final evidence and interpretation checkpoint — 2026-10-18

## Tested source and outcomes

- Tested source SHA: `55efe73188a31c495da14f9b11687ec71c15af07`.
- Focused security CI: https://github.com/Arkthos/saleor/actions/runs/39144176073 — SUCCESS; **59 PASS, 2 expected XFAIL, 0 FAIL, 0 ERROR, 0 SKIP**; three pytest warnings. Includes six new CM-T27 exact-mask variants.
- Linters: https://github.com/Arkthos/saleor/actions/runs/39144176064 — SUCCESS.
- E2E: https://github.com/Arkthos/saleor/actions/runs/39144176063 — SUCCESS.
- Changelog: https://github.com/Arkthos/saleor/actions/runs/39144176134 — SUCCESS.
- General tests: https://github.com/Arkthos/saleor/actions/runs/39144176059 — **IN PROGRESS at last inspection**; cannot claim final full CI green.
- Focused JUnit artifact: `12142658762`, `sha256:5388e596ad14d052f716d7b861092112095a24b694c0f0f5bf59af0fa9f6ba9a`.
- Static-review artifact: `12142880893`, `sha256:7139fc6bb1ad4c07da3e06304d4c8f7c6d5b94d7247f367b99ac55d498e45b90`.
- Artifacts expire 2026-11-17. Digest values above are GitHub artifact archive digests; per-file hashes are contained in the uploaded `SHA256SUMS` and should be audited before final archival certification.

## Experimental interpretations

- CM-T23 (6 PASS): two nonowner actors obtain three unmasked synthetic personal fields with known UUID.
- CM-T24 (3 PASS): owner positive controls obtain same fields.
- CM-T25 (6 PASS): nonowners receive changed values on legacy-number route.
- CM-T26 (2 PASS): nonexistent UUID returns no order.
- CM-T27 (6 PASS): legacy nonowner fields match `obfuscate_email` and `obfuscate_string` exactly. Email retains domain and first local character; streets retain first character and string length.
- CM-T22 (2 XFAIL): provisional owner-only email expectation is unmet. **Neither Saleor vulnerability nor approved policy nonconformance is established.**

## Traceability and scope

- 27 case IDs CM-T01–CM-T27; 13 risk IDs R01–R13 mapped, not certified.
- Matrix updated after successful run to record CM-T23–T27 as `EXECUTED_PASS`.
- Evidence types must remain distinct: security contracts, observational characterization, proposed-policy XFAIL.
- No real deployed HTTP/HTTPS security testing; see `C10_live_validation_plan.md`.

## Remaining closure tasks

1. Confirm general test run conclusion and, if necessary, remediate test-harness-only defects.
2. Validate final PR-head CI after documentation commits (avoid conflating the tested SHA with newer documentation-only SHAs).
3. Independently archive/reconcile individual JUnit variant rows, generated summary/coverage, and per-file hashes.
4. Record unapproved P-ORDER-01 and residual open questions (UUID capability semantics, staff/app field matrix, invalid ID behavior, deployment configuration) as **future research**, not undisclosed test failures.
5. Freeze evidence before drafting; do not edit the approved Avance 1.

## Interpretation guidance for academic analysis

Organize by authentication, sessions, authorization, data disclosure, GraphQL abuse controls and delegated app permissions. State observed behavior first, then requirement applicability, then inference and uncertainty. Avoid reporting passing tests as complete ASVS compliance.

## Final closure addendum — independently audited 2026-10-18

**Supersedes the earlier “IN PROGRESS” status above.** The same tested PR-head SHA `63cadee4e9a1b43bfc07103aecbfeb61fbc33112` now has completed SUCCESS runs: general tests [39144885841](https://github.com/Arkthos/saleor/actions/runs/39144885841), CyberMarket focused [39144885995](https://github.com/Arkthos/saleor/actions/runs/39144885995), linters [39144885812](https://github.com/Arkthos/saleor/actions/runs/39144885812), E2E [39144885821](https://github.com/Arkthos/saleor/actions/runs/39144885821), and changelog [39144885986](https://github.com/Arkthos/saleor/actions/runs/39144885986). Earlier cancelled general run 39144176059 is superseded, not relabeled successful.

The independent artifact audit recorded **17,613 PASS + 2 expected XFAIL = 17,615 general JUnit testcases**, and **59 PASS + 2 expected XFAIL = 61 focused JUnit testcases** (focused tests are included in general totals, so do not add totals). All 27 CM-T IDs reconciled; 26 contract PASS, 33 characterization PASS, 2 provisional-policy XFAIL; 13 mapped risks remain `NO_DETERMINADO`. Three focused warnings and 33 general warnings do not change these test verdicts. Static Bandit B105 LOW/MEDIUM on cookie name `refreshToken` is a reviewed false-positive classification, not an omitted finding.

Artifact provenance: focused artifact 12142029921 archive SHA256 `b8c38641cab220debac6c0d806b74141016f1baa0ad109caeb02647f0ac5412e`; SAST artifact 12143311107 archive SHA256 `de680b13d3b1fc5ddd35970d8e999f97c4d65fffea4fda802515ede9c4b8e37f`; general JUnit artifact 12143532461 archive SHA256 `809f7933869efe42bd1114e6a44d1d55f1c6df66b3d0560c31f55f8d17aae54a`. Independent validation matched these archive digests and all available per-file SHA256SUMS. Checkout/merge SHA `98645a24a56e9764e48fdefeea6b2e9a4095ad4a` differs from the branch SHA.

**Scope decision:** C2–C9 is complete as a synthetic, CI-based experiment, not as a deployed penetration test. UUID access to synthetic raw email and streets is observed for known IDs; old-number path masks those fields; no UUID enumeration, official Saleor security-policy violation, or real-user compromise is established. P-ORDER-01 remains proposed. HTTPS, browser, proxy, external deployment, exhaustive staff/app matrix and malformed identifiers are explicitly outside this experimental phase; C10 remains planned. Preserve raw ZIP artifacts before GitHub Actions retention expiry; this Markdown is a durable result/provenance record, not a substitute for the ZIP bytes.
