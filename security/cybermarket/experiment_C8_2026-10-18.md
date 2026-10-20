# CyberMarket CR — C8 policy-sensitive acceptance and CI gates

**State:** FOCUSED C8 VERIFIED (36 PASS + 2 XFAIL); repository-wide CI REVALIDATION PENDING after Ruff-only corrections.
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

## Verified C8 execution and proof integrity

- **PR-head tested:** `e7db02c49697dbf666f3151371f89a635ff6a13c`; Actions PR checkout merge SHA: `613accc94dc4dd8e9d00fc49ed5d7c4e366d2254`.
- **Workflow:** [CyberMarket security evidence run 39135116746](https://github.com/Arkthos/saleor/actions/runs/39135116746), conclusion SUCCESS.
- **Pytest results:** 38 execution records, 36 PASS, **2 XFAIL** (both CM-T22 actor variants), 0 FAIL, 0 ERROR, 0 SKIP.
- **Coverage:** 22/22 case IDs reconciled, R01–R13 mapped; R11 classified as `PROPOSED_POLICY_GAP_REVIEW_PENDING` with security verdict **NO_DETERMINADO**, NOT confirmed Saleor nonconformance.
- **Runtime artifact:** 12139890289; ZIP SHA-256 `f7bd0a3ba8e8caa9c318c883acc49d5461fa01d6299fc71a02fe4e270e5a388f`.
- **JUnit SHA-256:** `5367a3918e1a213ae52eee9d223960bbb083e40eebfbc341b1d094407d3d1d9c`.
- **Sanitized summary SHA-256:** `7a80b4b33b4bd3ac50d068b28d51fd34dbd2fc599021c87341622f125f3459fd`.
- **Coverage SHA-256:** `3c5253676592685db7a9e38879c3d18a2d0a3e92c347b2eb78e4316bde0d4a5c`.
- **Manifest validation:** all three digests in `SHA256SUMS` independently matched the extracted files.
- **Bandit:** success; artifact 12139701187, ZIP SHA-256 `bfb94b2a58258de440025287ab4e5c6b4b2c47f761aa7a9d708e5d165c003df4`. One diagnostic B105, LOW severity/MEDIUM confidence, `saleor/core/jwt.py:23`, same documented cookie-name false positive.

### CI review and correction record

- The C8 full linter run [39135116761](https://github.com/Arkthos/saleor/actions/runs/39135116761) was **not accepted**. Ruff detected only autoformat adjustments in three research files; mypy, deptry, Semgrep, uv-lock, migrations and GraphQL schema passed.
- Applied exactly the formatter's line changes, with no production-code changes, no test-oracle changes and no semantic evidence-generator changes. Commits: `47a2e9f8103c88f5b550f4d0f4de56ca33e90f61`, `bf632caa682f017210693bf4a13636e4797ae752`, `d4d48e389b4253719f8a2b7c1e2b14ae4df743aa`.
- The matrix and this checkpoint were then updated to record **EXECUTED_XFAIL**. A final all-checks CI cycle must complete on the new PR head before the *technical PR* is accepted; prior focused JUnit remains valid for the unchanged test behavior.
- CI general unit/E2E results should be recorded from the newest complete final-head run, not inherited from cancelled intermediate commits.

### Conserved interpretation

The 2 XFAILs are **unmet provisional expectations** under P-ORDER-01, not evidence that Saleor's own access policy was violated. The suite itself and the product's security posture are different acceptance targets. The proposed policy requires stakeholder approval; absent a representative HTTP/TLS/proxy/browser environment, production controls remain outside verified scope.

Long-term summary: see `evidence_C8_snapshot.md` for a durable, in-repository per-case record; raw JUnit/SAST remain accessible through GitHub Actions only during their configured artifact retention window.
