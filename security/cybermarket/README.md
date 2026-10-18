# CyberMarket CR — Reproducible software-security test suite

**Status:** C8 fixture-backed suite VERIFIED: 22 identified cases, 38 invocations (36 PASS + 2 policy-specific XFAIL), 13/13 risks mapped without conformance claims. Static Bandit scan reviewed (one LOW B105 false positive). Repository-wide CI on final documentation/formatting head still requires confirmation. See [C8 checkpoint](experiment_C8_2026-10-18.md), [durable result snapshot](evidence_C8_snapshot.md) and [provisional policy](POLICY_ORDER_P01_PROVISIONAL.md).

**Research baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090` (do not silently rebase to a new Saleor version).

## Scope, rationale and existing coverage

This research harness complements, rather than replaces, Saleor's established pytest suites:
- `saleor/graphql/account/tests/mutations/authentication/test_token_create.py`
- `.../test_token_refresh.py` and `.../test_tokens_deactivate_all.py`
- `saleor/graphql/account/tests/queries/test_me.py` and `test_user.py`
- `saleor/graphql/order/tests/queries/test_order.py`

The test in `saleor/graphql/tests/test_cybermarket_security_contracts.py` adds **cross-operation contracts** and explicitly records one **observational characterization**. All inputs use test fixtures and synthetic data. There is no external scanning, password spraying, or production testing.

## Executable scenarios

| ID | Purpose | R/H linkage | Evaluation type |
| --- | --- | --- | --- |
| CM-T01 | Anonymous vs signed-in `me` | R10 / H11 | Security contract |
| CM-T02 | Revoke then try old access **and** refresh JWT | R07 / H08 | Security contract |
| CM-T03 | Refresh by argument vs cookie; valid, missing, invalid CSRF | R06 / H05–H07 | Security contract; 4 parametrized cases |
| CM-T04 | `order(externalReference:)` requires `MANAGE_ORDERS` | R09 / H12 | Security contract |
| CM-T05 | Observe full address/email disclosure from `order(id: UUID)` to anonymous request | R11 / H12 | **Characterization only**, not proof of compliant security |
| CM-T06 | Compare same new-UUID order fields as owner, unrelated customer and anonymous actor | R11 / H12 | **Characterization only**, expected exposure is not approved policy |
| CM-T07 | Compare old-number order fields as owner, unrelated customer and anonymous actor | R11 / H12 | Security contract: owner sees full fields, other actors see masked fields |
| CM-T08 | `tokenCreate`: access/refresh types, TTL and custom audience | R04/R08; H03/H04/H09 | Contract |
| CM-T09 | Known account/unknown email with invalid credentials | R03/H03 | Contract; two variants |
| CM-T10 | Reject an access JWT as a refresh token | R05/H05/H09 | Contract |
| CM-T11 | Preserve custom audience on refresh | R08/H05/H09 | Contract |
| CM-T12 | Restrict `user` query for unrelated and anonymous actors | R10/H11 | Contract |
| CM-T13 | Partition staff/customer `user` visibility by role | R10/H11 | Contract |
| CM-T14 | Characterize cookie flags with DEBUG true/false | R06/H07 | **Characterization only**; two variants |
| CM-T15 | Bound two GraphQL aliases against configured limit 1 | R12/H13 | Contract; no stress testing |
| CM-T16 | Reject mutation count above configured limit | R12/H13 | Contract; no mutation execution |
| CM-T17 | Characterize special versus standard authorization header precedence | R01/H01 | Characterization only; 3 variants |
| CM-T18 | Characterize forwarded IP parsing and remote address fallback | R01/R02/H14 | Characterization only; 3 variants |
| CM-T19 | Check bounded login delay algorithm thresholds | R02/H02 | Contract; 6 variants, not production throttling |
| CM-T20 | Verify app delegated token permission intersections | R13/H15 | Contract; overlap/disjoint variants |
| CM-T21 | Reject unsigned JWT algorithm | R08/H09 | Narrow contract |
| CM-T22 | Probe proposed CyberMarket CR owner-only order-UUID privacy for unrelated/anonymous actors | R11/H12 | **Provisional policy**: strict XFAIL expected, not Saleor nonconformance |

**IMPORTANT on CM-T05 / CM-T06:** In this pinned Saleor revision, pre-existing upstream tests
`test_query_order_fields_order_with_new_id_by_anonymous_user` and
`test_query_order_fields_order_with_new_id_by_staff_no_perm`
explicitly assert the returned address/email fields. Our test reproduces that described behavior for research, without deciding whether exposure violates the system's intended business policy. Their green status **must not** be reported as security conformance. The object/reference authorization boundary needs an agreed threat model, requirement interpretation, and independent controlled verification.

## Requirement mapping (preliminary, NOT ASVS certification)

| Case | OWASP ASVS 5.0.0 relevant requirement(s) | WSTG 4.2 relevant technique |
| --- | --- | --- |
| CM-T01 | v5.0.0-8.2.2; v5.0.0-8.2.3 | WSTG-ATHZ-02 |
| CM-T02 | v5.0.0-7.4.1 | WSTG-SESS-06 (backend adaptation) |
| CM-T03 | v5.0.0-3.5.1; v5.0.0-9.2.2 | WSTG-SESS-05 |
| CM-T04 | v5.0.0-8.2.1 | WSTG-ATHZ-02 |
| CM-T05 | v5.0.0-8.2.2; v5.0.0-8.2.3 | WSTG-ATHZ-04 |
| CM-T06 | v5.0.0-8.2.2; v5.0.0-8.2.3 | WSTG-ATHZ-04 |
| CM-T07 | v5.0.0-8.2.2; v5.0.0-8.2.3 | WSTG-ATHZ-04 |

These are candidate mappings only. A passing test is **not** evidence of comprehensive coverage of any standard section.

## Execution

A dedicated GitHub Actions workflow is provided:
`.github/workflows/cybermarket-security.yaml`.
It runs pytest against the repository's pinned `uv.lock` with isolated PostgreSQL and Valkey services; it publishes JUnit XML, a sanitized per-case summary, a risk-coverage report (`build_coverage.py` enforces matrix/JUnit consistency), and SHA-256 checksums. A separate job invokes pinned Bandit 1.8.6 over selected authentication, JWT and order modules; its JSON report is untriaged SAST evidence, not a list of confirmed vulnerabilities.

Equivalent local command (requires the repository development environment, a test PostgreSQL database, cache and the normal test settings):

```bash
uv sync --locked
mkdir -p security-results
uv run pytest saleor/graphql/tests/test_cybermarket_security_*.py -q --junitxml=security-results/cybermarket-junit.xml -o junit_family=legacy
python security/cybermarket/summarize_junit.py --junit security-results/cybermarket-junit.xml --output security-results/cybermarket-summary.json
python security/cybermarket/build_coverage.py --matrix security/cybermarket/test_matrix.csv --summary security-results/cybermarket-summary.json --output security-results/cybermarket-coverage.json
```

**Do not upload usable JWTs, cookies, passwords, personal data or raw production logs.** The JUnit report contains only case and requirement identifiers in `record_property` metadata; the test source uses synthetic fixtures.

## C8 final evidence checkpoint

- [C8 experimental workflow 39135116746](https://github.com/Arkthos/saleor/actions/runs/39135116746): 36 PASS + 2 XFAIL, zero unexpected failures, 22/22 matrix case IDs and 13/13 risks associated with evidence. The two XFAIL are **unmet provisional expectations**, not confirmed Saleor vulnerabilities.
- [Verified hashes, run SHA and static B105 triage](experiment_C8_2026-10-18.md); [durable per-case archive](evidence_C8_snapshot.md). Raw GitHub Actions artifacts have limited retention, so keep these source-controlled records.
- New source formatter-only corrections to three research files are committed. **Do not claim final CI accepted until linters, tests and E2E succeed on the final SHA.**
- No actual HTTPS/proxy/browser DAST is claimed. `P-ORDER-01` is not an approved access policy.

## Current execution checkpoint

- **C2:** [run 39127189591](https://github.com/Arkthos/saleor/actions/runs/39127189591) passed 8/8 tests for CM-T01–T05; JUnit artifact 12136417662.
- **C3:** [initial run 39128224126](https://github.com/Arkthos/saleor/actions/runs/39128224126) produced 9 PASS / 1 FAIL due to an incorrect CM-T07 full-object-denial expectation; the code actually masked fields. After correcting the test oracle in commit `3b8064b08b07d71e2fd3a0e8c89c572de7e36c4e`, [run 39128693170](https://github.com/Arkthos/saleor/actions/runs/39128693170) produced **10 PASS / 0 FAIL / 0 ERROR / 0 SKIP**. CM-T05/CM-T06 remain characterization-only and do not establish compliant access policy.
- Do not conflate a test **PASS** with a requirement verdict. Capture a run + commit + artifact for every claim.

## Evidence and classification

- Capture run ID, commit, tool versions, fixture description, execution time, test case IDs, JUnit, outcome and artifact checksum.
- Distinguish `PASS`, `FAIL`, `SKIP`, `ERROR` as raw execution outcomes from `CONFORME`, `NO_CONFORME`, `NO_DETERMINADO`, `NO_APLICABLE` as academic assessments.
- A `FAIL` may represent a test/environment defect; a `PASS` in CM-T05 or CM-T06 **characterizes an exposure** rather than proving authorization. Cross-customer results remain security-policy ambiguous until authorized product requirements are known.
- Any potential security deviation must be manually replicated, scoped and tied to an applicable ASVS requirement before it can be called a confirmed finding.
- Keep `H01–H15` as documentary observations and `R01–R13` as hypothetical risks until backed by tests. Record uncertainties separately.

## Proposed policy and failed expectations (C8)

- [P-ORDER-01: PROPOSED, not approved](POLICY_ORDER_P01_PROVISIONAL.md) specifies a stricter owner-only PII policy for the fictional CyberMarket CR scenario. It does **not** override Saleor's intended semantics or establish a vulnerability.
- CM-T22 is deliberately `pytest.mark.xfail(strict=True)` for unrelated/anonymous requests with a known new order UUID. XFAIL records the proposed requirement gap and must be reported distinctly from PASS/SKIP.
- `summarize_junit.py` and `build_coverage.py` preserve `XFAIL` and `PROPOSED_POLICY_GAP_REVIEW_PENDING`; strict XPASS produces a failing pipeline so the requirement must be reevaluated.
- **No production-code correction** will be made until the intended access policy is authorized and the exposure independently verified.

## Scope and honest coverage boundaries

- These checks run **in-process Django/GraphQL requests** against isolated fixture-backed services. They are dynamic behavioral/integration tests but **not** an external-browser DAST scan and do not demonstrate actual HTTPS/proxy isolation.
- C4 covers more of token creation, refresh, user-permission partitioning and GraphQL query boundaries. It does not prove missing risks R01 (intermediaries), R02 (effective throttling behind proxy), or R13 (delegated app permissions). These need independent controls and test protocols.
- Bandit 1.8.6 scanned 4,629 lines of selected Python code in [C4 run 39130431874](https://github.com/Arkthos/saleor/actions/runs/39130431874) with `-ll -ii`, showing no matches above that initial filter; C7 uses `-l -ii`; it captured B105 on `JWT_REFRESH_TOKEN_COOKIE_NAME = "refreshToken"` and the code review classified this cookie **name** as a false-positive hardcoded-password alert. Scanner findings are never automatically classified as vulnerabilities. See [C7 evidence](experiment_C7_2026-10-18.md).
- C7 verifies that the ASVS/WSTG identifiers in the matrix come from a reviewed, versioned subset and rejects out-of-catalog IDs. Applicability and control conformity still require individual human judgment.
- Generated evidence expires after GitHub retention; selected results, hashes, SHA and interpretations must be committed as checkpoints with no tokens or production data.

## Checkpoints / next iterations

1. **C1 / implemented:** scenario IDs, code, traceability and dedicated CI workflow committed in a draft PR.
2. **C2 / executed:** Initial 8/8, no failures/errors/skips; original run 39127189591. Contract performance is narrow, not full ASVS compliance. The C2 checkpoint records SHA-256 and interpretation.
3. **C3 / implementation:** CM-T06 compares owner/peer/anonymous for new UUID, observational only; CM-T07 checks legacy-number ownership. The initial CI showed a test-oracle mismatch on CM-T07; the corrected field-masking contract passed in C3's 10/10 rerun. The new-UUID access policy still requires a documented decision. Staff-permission cases and a business decision on new-UUID privacy remain outstanding.
4. **C4 / verified:** CM-T08–T16 and prior C2/C3 cases executed 21/21 in run 39130431874; scoped Bandit SAST executed and evidence archived.
5. **C5 / verified:** CM-T17–T21 include source-level R01/R02/R13, delegated permission intersection, and unsigned JWT rejection; 36/36 in [run 39131023314](https://github.com/Arkthos/saleor/actions/runs/39131023314). See [C5 checkpoint](experiment_C5_2026-10-18.md).
6. **C6 / verified:** [Consolidated experiment evidence](experiment_C6_2026-10-18.md) and [run 39131644653](https://github.com/Arkthos/saleor/actions/runs/39131644653) verify 36/36, 21/21 case mappings and 13/13 mapped risks with **no automatic security conformity decisions**.
7. **C7 / verified:** [Normative audit and SAST triage](experiment_C7_2026-10-18.md) documents 36/36 PASS in [run 39132273808](https://github.com/Arkthos/saleor/actions/runs/39132273808); ASVS/WSTG IDs enforced by the checked allowlist. Bandit B105 on the literal cookie name `refreshToken` was reviewed and classified **false positive**, with original report and hashes preserved. Final repo-wide CI and independent policy verdicts are still pending.

Do not merge while CI failures or security requirements are unresolved. The Avance 1 DOCX validated by the user remains unchanged.

## Current research status — audited C2–C9 closure (2026-10-18)

**The earlier C7 status above is historical.** C2–C9 synthetic CI experiments are complete and independently audited. On tested branch SHA `63cadee4e9a1b43bfc07103aecbfeb61fbc33112`, general tests [39144885841](https://github.com/Arkthos/saleor/actions/runs/39144885841), focused GraphQL security [39144885995](https://github.com/Arkthos/saleor/actions/runs/39144885995), linters [39144885812](https://github.com/Arkthos/saleor/actions/runs/39144885812), E2E [39144885821](https://github.com/Arkthos/saleor/actions/runs/39144885821) and changelog [39144885986](https://github.com/Arkthos/saleor/actions/runs/39144885986) all finished SUCCESS.

General suite: **17,613 PASS + 2 expected XFAIL**. Focused subset: **59 PASS + 2 expected XFAIL**, 27 case IDs / 61 variants / 13 mapped risks; no unexpected failures. Risk verdicts remain `NO_DETERMINADO`; proposed P-ORDER-01 is not an authoritative Saleor policy. The source-controlled report preserves independently verified artifact hashes and per-case interpretations.

**Read first:** [Audited closure report](INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md) → [Final pre-writing checkpoint](CHECKPOINT_PRE_REDACCION_2026-10-18.md) → [Test matrix](test_matrix.csv). For future teammate-executed deployment see [C10 live validation plan](C10_live_validation_plan.md). No live deployment has been performed. This PR stays draft and unmerged; approved Avance 1 and functional Saleor code were not modified in this closure.

## Software engineering assurance review and live deployment handoff

- [Detailed C2–C9 engineering/assurance review](REPORTE_INGENIERIA_ASEGURAMIENTO_C2_C9_2026-10-18.md): 27 case-by-case interpretations, 13 risk analyses, software harness weaknesses QA-01–QA-11, explicit normative decision boundary and source provenance.
- [C10 team execution roadmap](C10_live_validation_roadmap_team_handoff.md): gated isolated deployment, owners, LIVE-01–LIVE-07, evidence schema, teardown, checkpoints and acceptance criteria.
- The [matrix](test_matrix.csv) now records all 16 contracts as `REVIEWED_LOCAL_ORACLE_PASS_NORMATIVE_NOT_ADJUDICATED`, 10 characterizations as `REVIEWED_OBSERVED_NO_SECURITY_VERDICT` and the 2-variant CM-T22 as `REVIEWED_PROVISIONAL_POLICY_MISMATCH_NOT_APPROVED`. These are reviewed evidence states, **not** formal ASVS conformity decisions. Historic `REVIEW_PENDING` strings in older snapshots/derived coverage describe the earlier state and are not rewritten retroactively.

**No C10 deployment has been performed.** The engineering review documents actionable harness improvements; it does not claim those changes have been implemented. Preserve the original tested SHA and rerun/inspect CI on the current PR HEAD after documentation and matrix updates.
