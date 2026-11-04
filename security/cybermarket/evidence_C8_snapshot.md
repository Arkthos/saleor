# CyberMarket CR — Durable per-case outcome snapshot (C8)

**Origin:** [GitHub Actions C8 run 39135116746](https://github.com/Arkthos/saleor/actions/runs/39135116746), PR head `e7db02c49697dbf666f3151371f89a635ff6a13c`, checkout merge SHA `613accc94dc4dd8e9d00fc49ed5d7c4e366d2254`.
**Integrity:** Original artifact ID 12139890289 and SHA-256 digests are recorded in [experiment C8](experiment_C8_2026-10-18.md). This snapshot is *derived*, not a replacement for the raw JUnit XML.
**Extraction:** The actual artifact's JUnit, sanitized summary and coverage report were decoded and cross-checked; all three SHA-256 values matched `SHA256SUMS`.

## Case outcomes (persisted independently of 30-day Actions artifact retention)

| Case | Pytest outcomes | Evidence type | Risk ID(s) |
| --- | --- | --- | --- |
| CM-T01 | 1 PASS | Contract | R10 |
| CM-T02 | 1 PASS | Contract | R07 |
| CM-T03 | 4 PASS | Contract | R06 |
| CM-T04 | 1 PASS | Contract | R09 |
| CM-T05 | 1 PASS | Characterization | R11 |
| CM-T06 | 1 PASS | Characterization | R11 |
| CM-T07 | 1 PASS | Contract | R11 |
| CM-T08 | 1 PASS | Contract | R04, R08 |
| CM-T09 | 2 PASS | Contract | R03 |
| CM-T10 | 1 PASS | Contract | R05 |
| CM-T11 | 1 PASS | Contract | R08 |
| CM-T12 | 1 PASS | Contract | R10 |
| CM-T13 | 1 PASS | Contract | R10 |
| CM-T14 | 2 PASS | Characterization | R06 |
| CM-T15 | 1 PASS | Contract | R12 |
| CM-T16 | 1 PASS | Contract | R12 |
| CM-T17 | 3 PASS | Characterization | R01 |
| CM-T18 | 3 PASS | Characterization | R01, R02 |
| CM-T19 | 6 PASS | Contract | R02 |
| CM-T20 | 2 PASS | Contract | R13 |
| CM-T21 | 1 PASS | Contract | R08 |
| CM-T22 | **2 XFAIL** | Unapproved proposed policy P-ORDER-01 | R11 |

Totals: **22 unique IDs; 38 executions; 36 PASS; 2 XFAIL; 0 FAIL; 0 ERROR; 0 SKIP.** Both XFAIL records came from CM-T22, one unrelated authenticated customer and one anonymous request; the recorded pytest type was `pytest.xfail`.

## Risk evidence disposition

| Risk ID | Class from the verified C8 coverage file |
| --- | --- |
| R01 | CHARACTERIZED_ONLY |
| R02 | MIXED_EVIDENCE_REVIEW_PENDING |
| R03 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R04 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R05 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R06 | MIXED_EVIDENCE_REVIEW_PENDING |
| R07 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R08 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R09 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R10 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R11 | **PROPOSED_POLICY_GAP_REVIEW_PENDING** |
| R12 | CONTRACT_EVIDENCE_REVIEW_PENDING |
| R13 | CONTRACT_EVIDENCE_REVIEW_PENDING |

All 13 risks map to test IDs. Their formal `security_verdict` remains `NO_DETERMINADO`; linkage is **not** proof of a successful control or complete treatment of that risk.

## Static review and open decision

Bandit 1.8.6 on selected authentication/JWT/order modules completed. One B105 / LOW / MEDIUM signal in `saleor/core/jwt.py:23` corresponds to the constant `JWT_REFRESH_TOKEN_COOKIE_NAME = "refreshToken"`. The literal is the name of an HTTP cookie, not a hardcoded credential; retain the finding and its reviewed false-positive classification.

The UUID path returned selected email/street fields to a different user and anonymous actor in synthetic tests, and the old-order ID path masks those fields. `P-ORDER-01` proposes a stricter CyberMarket-only access policy, not an authoritative Saleor rule. CM-T22's two XFAIL outcomes demonstrate the proposed requirement gap **only if that policy is later adopted**. Do not call this a confirmed exploitable Saleor vulnerability without independent business-policy and deployment verification.

Repository-wide CI must be accepted on the latest code SHA separately. Do not infer a complete external/browser/proxy penetration test from these results. No academic manuscript has been drafted in this cycle.
