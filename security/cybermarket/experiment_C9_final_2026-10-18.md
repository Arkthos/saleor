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
