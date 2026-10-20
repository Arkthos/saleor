# CyberMarket CR — C2–C9 audited experimental closure

Date: 2026-10-18. Status: **C2–C9 completed within synthetic CI experiment scope; academic writing not started.**

## Source provenance and CI

- Repository PR: https://github.com/Arkthos/saleor/pull/1 (draft; do not merge).
- Tested branch SHA: `63cadee4e9a1b43bfc07103aecbfeb61fbc33112`.
- Tested checkout/merge SHA: `98645a24a56e9764e48fdefeea6b2e9a4095ad4a` (distinct from branch SHA).
- Focused security [39144885995](https://github.com/Arkthos/saleor/actions/runs/39144885995): SUCCESS; **59 PASS, 2 expected XFAIL, 0 FAIL/ERROR/SKIP**, 3 warnings.
- General unit tests [39144885841](https://github.com/Arkthos/saleor/actions/runs/39144885841): SUCCESS; **17,613 PASS, 2 expected XFAIL, 0 FAIL/ERROR**, 33 warnings; **17,615 JUnit testcases**. Focused cases are a subset of general results, not additive.
- Linters [39144885812](https://github.com/Arkthos/saleor/actions/runs/39144885812), E2E [39144885821](https://github.com/Arkthos/saleor/actions/runs/39144885821), changelog [39144885986](https://github.com/Arkthos/saleor/actions/runs/39144885986): SUCCESS.
- Previous general run 39144176059: CANCELLED; not counted as a success. Load-test publication and test-environment deployment SKIPPED (not within this phase).

## Independently verified artifact provenance

The original ZIP archives were downloaded and independently SHA256-verified, and embedded `SHA256SUMS` matched their component files:

| Artifact | GitHub artifact ID | SHA256 ZIP |
| --- | --- | --- |
| Focused JUnit, summary, coverage | 12142029921 | `b8c38641cab220debac6c0d806b74141016f1baa0ad109caeb02647f0ac5412e` |
| Scoped Bandit SAST | 12143311107 | `de680b13d3b1fc5ddd35970d8e999f97c4d65fffea4fda802515ede9c4b8e37f` |
| General JUnit | 12143532461 | `809f7933869efe42bd1114e6a44d1d55f1c6df66b3d0560c31f55f8d17aae54a` |

Selected verified file SHA256: focused JUnit `2eac7bdfc730eee6f60bc32be07a9811600806c50d2510401744ba00077018a5`; focused summary `cd498c3c2f229a238fe59eab8f54360f9fd9037e3cc18060e2b2883d7041b382`; risk coverage `47a659f32ce404ecfc7aa44e202324ca6d2d6363b080634bc0aaaf2a1db99956`; Bandit JSON `1d2f1b73235965b74469d7a7179f708c710c7e6687e15ae575e6821000a337de`; general JUnit `78aa585610644e50b4c2b3cfe68aab18450b9895e8b2ceb1594a7ce41b1cfcb7`.

**Artifact retention:** focused and SAST ZIPs expire 2026-11-17. The source-controlled report preserves hashes, counts and interpretation; raw ZIP bytes remain in GitHub Actions until expiry and should be downloaded to durable storage separately.

## Reconciled per-case evidence

| ID | Outcomes | Evidence class | Risks |
| --- | --- | --- | --- |
| CM-T01 | 1 PASS | contract | R10 |
| CM-T02 | 1 PASS | contract | R07 |
| CM-T03 | 4 PASS | contract | R06 |
| CM-T04 | 1 PASS | contract | R09 |
| CM-T05 | 1 PASS | characterization | R11 |
| CM-T06 | 1 PASS | characterization | R11 |
| CM-T07 | 1 PASS | contract | R11 |
| CM-T08 | 1 PASS | contract | R04, R08 |
| CM-T09 | 2 PASS | contract | R03 |
| CM-T10 | 1 PASS | contract | R05 |
| CM-T11 | 1 PASS | contract | R08 |
| CM-T12 | 1 PASS | contract | R10 |
| CM-T13 | 1 PASS | contract | R10 |
| CM-T14 | 2 PASS | characterization | R06 |
| CM-T15 | 1 PASS | contract | R12 |
| CM-T16 | 1 PASS | contract | R12 |
| CM-T17 | 3 PASS | characterization | R01 |
| CM-T18 | 3 PASS | characterization | R01, R02 |
| CM-T19 | 6 PASS | contract | R02 |
| CM-T20 | 2 PASS | contract | R13 |
| CM-T21 | 1 PASS | contract | R08 |
| CM-T22 | 2 expected XFAIL | proposed policy, not approved | R11 |
| CM-T23 | 6 PASS | characterization | R11 |
| CM-T24 | 3 PASS | characterization | R11 |
| CM-T25 | 6 PASS | characterization | R11 |
| CM-T26 | 2 PASS | characterization | R11 |
| CM-T27 | 6 PASS | characterization | R11 |

Totals: **27 unique IDs, 61 variants, 26 contract PASS, 33 characterization PASS, 2 proposed-policy XFAIL, 13 mapped risk IDs**. All 13 risk `security_verdict` fields remain `NO_DETERMINADO`. Mapping and a PASS are not proof of global ASVS compliance or a security guarantee.

## Complete technical interpretation within experimental scope

**Authentication/JWT/sessions:** Synthetic contracts exercised identity boundaries, token invalidation, refresh CSRF, JWT type/audience, unsigned-token rejection and deterministic login throttling. Cookie flags, auth-header precedence and forwarded client-IP logic were characterized, not validated under a real browser/reverse proxy.

**Authorization/GraphQL:** Synthetic contracts for external order reference, user/staff access, delegated app permissions, configured alias and mutation limits passed. No exhaustive field-level staff/app entitlement matrix or distributed-load abuse test was performed.

**Known order UUID and personal fields:** CM-T23 demonstrated raw synthetic email, billing street and shipping street for unrelated authenticated and anonymous actors (2 × 3 = 6). CM-T24 positive owner controls passed (3). CM-T26 nonexistent UUID yielded null for both nonowner actors (2). This does **not** establish UUID enumeration, a real frontend disclosure path or production PII compromise.

**Legacy order number:** CM-T25 showed changed values (6); CM-T27 verified exact obfuscation (6). Email masking retains the first local-part character and domain; street masking retains the first character and string length. Whether this satisfies a valid business requirement remains undecided.

**Provisional P-ORDER-01:** CM-T22 contains two strict XFAIL for **email only** (anonymous/unrelated actor). Street exposure is observational, not separately asserted as normative XFAIL. Proposed CyberMarket owner-only policy is unapproved; therefore no authoritative Saleor violation or exploitable vulnerability has been established.

**Static review:** Bandit 1.8.6 reported B105 LOW/MEDIUM on `saleor/core/jwt.py:23` because `refreshToken` resembles a hardcoded secret; it is an HTTP cookie name, reviewed as false positive. Preserve the signal; a successful workflow does not mean zero Bandit findings.

## Phase boundary and remaining external work

All 27 scoped cases executed and reconciled, and the complete CI checks passed on the same tested SHA. **C2–C9 can be frozen as a completed synthetic CI experiment.** No production or live deployment, HTTPS, CORS, browser cookies, reverse proxy, frontend UUID sharing, malformed identifiers, exhaustive staff/app permissions, scale abuse or approved P-ORDER-01 were evaluated. These are explicitly *out of scope*, to be addressed in the separately documented C10 classmate lab, not disguised as unresolved C9 failures.

This document records research evidence and interpretation, **not the academic manuscript**. Do not alter approved Avance 1, Saleor product code or merge PR #1.


## Post-remediation CI revalidation (2026-10-18)

This is a later, independently checked execution of the **experimental QA harness**; it supersedes the earlier tested branch SHA for CI status, but does not change the earlier security interpretation.

- PR #1 remains open and draft. Tested branch HEAD: `6722e120a90d39dc34ef83a4b53ce4dd064fd5df`; Actions checkout/merge SHA embedded in the evidence: `a88da0ae6a01471ad3f1737e5936529fe6f7d286` (do not confuse the two).
- Linters [39155789280](https://github.com/Arkthos/saleor/actions/runs/39155789280): **SUCCESS** (Ruff, Ruff format, mypy, deptry, Semgrep, migrations and GraphQL schema).
- Focused GraphQL and SAST [39155789357](https://github.com/Arkthos/saleor/actions/runs/39155789357): **SUCCESS**; evidence-validator regression gates **6 PASS**; focused **59 PASS, 2 expected XFAIL, 0 FAIL/ERROR/SKIP**, 61 executions, 27 case IDs, 3 warnings. The two strict XFAIL concern unapproved P-ORDER-01, not an established Saleor vulnerability.
- General [39155789296](https://github.com/Arkthos/saleor/actions/runs/39155789296): **SUCCESS**, **17,613 PASS, 2 expected XFAIL, 0 FAIL/ERROR**, 34 warnings, 17,615 JUnit testcases. Focused cases are included, not additional.
- E2E [39155789292](https://github.com/Arkthos/saleor/actions/runs/39155789292): **SUCCESS**, 211 PASS, 3 warnings. Changelog [39155789376](https://github.com/Arkthos/saleor/actions/runs/39155789376): **SUCCESS**. Deployment/load publication skipped, outside C2–C9.
- Independently downloaded and SHA256-verified artifact ZIPs and their embedded `SHA256SUMS`: focused artifact **12146918425**, ZIP `983aae404ad5c29155575a642cfb26a427477c6dd5a6d317dd1190c273200e44`, JUnit `6cef50dc3d21f61a5bcc1e7541cf6461206a5d704c82d001932daec0d807a13d`; SAST artifact **12147131033**, ZIP `83b590fdabd328955cc0fd89533e69aa5e4ae9424e445986a1330fd53601051f`; general JUnit artifact **12147144111**, ZIP `ed5ec8f271df32887fe4457be06073691ed8441edb4891777bb2423ef5f91f40`, XML `3266fd55c8839b2b09334b9c93adde2a1d3e3821b4c0dca911c86998ebbc956e`.
- Artifact XML independently parsed: focused 61 testcases, 0 failures/errors, 2 `pytest.xfail`; general 17,615 testcases, 0 failures/errors, 2 `pytest.xfail`. Summary and coverage JUnit hashes match. All 13 mapped risks still carry `NO_DETERMINADO` security verdicts.
- Scoped Bandit 1.8.6 produced the same **LOW B105** alert on the `refreshToken` cookie-name constant; reviewed as a false positive, **not** a clean zero-finding scan.

**Evidence-integrity residual:** the current validator checks that the sum of reported outcome counts equals the case count, but not that the reported PASS/XFAIL histogram matches individual cases. Independent XML/JSON inspection above reconciled the actual distribution, so this does not invalidate the audited run; strengthening this gate remains a non-product QA improvement. Formal requirement approval, live browser/HTTPS/proxy behavior and C10 remain external/out-of-scope. This appendix is an evidence record, not authorization to start academic writing or merge the PR.
