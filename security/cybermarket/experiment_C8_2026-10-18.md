# CyberMarket CR — C8 policy-sensitive acceptance and CI gates

**State:** IMPLEMENTED; **DO NOT REPORT AS VERIFIED until a C8 JUnit and repository CI results are inspected.**
**Baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090` (unmodified Saleor product).
**PR:** https://github.com/Arkthos/saleor/pull/1 (draft).

## Why the previous green suite was not enough

C7 produced 36/36 PASS across 21 cases and reconciled all 13 risk identifiers. However R11 remains undecided: characterization tests CM-T05 and CM-T06 show selected email/address fields to unrelated actors given a known order UUID. Such green characterization does **not** answer whether the intended CyberMarket security policy is satisfied.

C8 introduces **P-ORDER-01 PROVISIONAL**, a *proposed policy* restricted to the fictional CyberMarket scenario. It requires no raw personal email/street details returned solely on possession of an order UUID to a different user or anonymous actor. This policy is **NOT APPROVED**, and does not claim nonconformance with Saleor's own published access model.

## New experiment: CM-T22

- `CM-T22[unrelated_customer]` — owner A's synthetic order requested by distinct client B using new UUID.
- `CM-T22[anonymous]` — same synthetic order requested by anonymous actor.
- Both are marked `pytest.mark.xfail(strict=True)` and `evidence_type=proposed_policy_expected_fail`.
- **Expected from pinned implementation:** the proposed privacy restriction is not met; each test is recorded as `XFAIL`. The result is a proposed policy gap **not a confirmed vulnerability**.
- An `XPASS` is strictly treated as failure to force manual review of changed code or policy; it must not be silently counted as a passed control.
- JUnit summary now distinguishes `XFAIL` from ordinary `SKIP`; the coverage generator includes `unmet_proposed_policy_cases` and marks R11 `PROPOSED_POLICY_GAP_REVIEW_PENDING`.

## Acceptance gates

| Gate | Required evidence | State |
| --- | --- | --- |
| G1 technical | Focused pytest all existing contract cases pass; new proposed-policy probes XFAIL exactly as marked | PENDING |
| G2 traceability | JUnit case IDs reconcile exactly with `test_matrix.csv` including CM-T22 and its two variants | PENDING |
| G3 integrity | JUnit, sanitized summary, coverage, Bandit JSON, checksums and tested SHA stored | PENDING |
| G4 repository | Full linters, tests, E2E and changelog checks checked for final PR SHA; fix repo-local defects | PENDING |
| G5 analysis | B105 low-severity Bandit is documented false positive (cookie **name**); unresolved contexts expressly listed | C7 EVIDENCE; RECHECK |
| G6 integrity of claims | Raw outcome vs policy assumption vs actual vulnerability distinguished; no ASVS claim from PASS | REQUIRES MANUAL AUDIT |
| G7 scope | HTTPS browser/proxy origin, actual rate limiting, real client/app integrations and UUID entitlement defined or marked outside scope | OPEN / ENVIRONMENT UNAVAILABLE |
| G8 deliverable | Reviewer-ready research packet and reproducibility instructions; no Avance 2 prose produced | PENDING |

The **in-process suite** may be accepted once G1–G6 and G8 pass and G7's absence is disclosed. A **complete deployed security validation** cannot be accepted until G7 has a representative environment and authorization. Preserve both statuses separately.

## Evidence to add after CI

- PR SHA and pull-request merge SHA (if different).
- Workflow run IDs and their conclusions (focused tests, Bandit, lint/full unit/E2E).
- JUnit `PASS/FAIL/ERROR/SKIP/XFAIL` counts and all case IDs.
- Artifact IDs, SHA-256 and Bandit alert classification.
- G1–G8 statuses with explicit remaining gaps and corrective steps.
- The `CM-T22` policy decision must remain provisional until CyberMarket CR's hypothetical owner/security stakeholders confirm its intended rule.

**Change control:** No merge, production-code adjustment, broad active DAST or academic manuscript drafting in this cycle.
