# CyberMarket CR — Reproducible software-security test suite

**Status:** C2 8/8 verified; C3 10/10 verified; C4 deterministic cases and scoped SAST have been implemented and await CI validation. Historical results remain immutable in their own experiment checkpoints.

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
It runs pytest against the repository's pinned `uv.lock` with isolated PostgreSQL and Valkey services; it publishes the JUnit XML, a sanitized case summary and SHA-256 checksums. A separate job invokes pinned Bandit 1.8.6 over selected authentication, JWT and order modules; its JSON report is untriaged SAST evidence, not a list of confirmed vulnerabilities.

Equivalent local command (requires the repository development environment, a test PostgreSQL database, cache and the normal test settings):

```bash
uv sync --locked
mkdir -p security-results
uv run pytest saleor/graphql/tests/test_cybermarket_security_*.py -q --junitxml=security-results/cybermarket-junit.xml -o junit_family=legacy
python security/cybermarket/summarize_junit.py --junit security-results/cybermarket-junit.xml --output security-results/cybermarket-summary.json
```

**Do not upload usable JWTs, cookies, passwords, personal data or raw production logs.** The JUnit report contains only case and requirement identifiers in `record_property` metadata; the test source uses synthetic fixtures.

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

## Scope and honest coverage boundaries

- These checks run **in-process Django/GraphQL requests** against isolated fixture-backed services. They are dynamic behavioral/integration tests but **not** an external-browser DAST scan and do not demonstrate actual HTTPS/proxy isolation.
- C4 covers more of token creation, refresh, user-permission partitioning and GraphQL query boundaries. It does not prove missing risks R01 (intermediaries), R02 (effective throttling behind proxy), or R13 (delegated app permissions). These need independent controls and test protocols.
- The Bandit scan covers selected Python code only. Rule matches demand manual confirmation; a zero finding count does not establish secure software.
- Requirement ASVS/WSTG associations in the matrix are **candidates to validate against the normative standard text**, never conformance claims.
- Generated evidence expires after GitHub retention; selected results, hashes, SHA and interpretations must be committed as checkpoints with no tokens or production data.

## Checkpoints / next iterations

1. **C1 / implemented:** scenario IDs, code, traceability and dedicated CI workflow committed in a draft PR.
2. **C2 / executed:** Initial 8/8, no failures/errors/skips; original run 39127189591. Contract performance is narrow, not full ASVS compliance. The C2 checkpoint records SHA-256 and interpretation.
3. **C3 / implementation:** CM-T06 compares owner/peer/anonymous for new UUID, observational only; CM-T07 checks legacy-number ownership. The initial CI showed a test-oracle mismatch on CM-T07; the corrected field-masking contract passed in C3's 10/10 rerun. The new-UUID access policy still requires a documented decision. Staff-permission cases and a business decision on new-UUID privacy remain outstanding.
4. **C4 / implementation:** CM-T08–T16 implemented to cover auth, audience, role partitioning, cookie flags, alias and mutation limits; CI verdict pending. Scoped Bandit SAST added. Analyze unexpected results before updating test oracles.
5. **C5 / validation:** inspect targeted JUnit and sanitized manifest, verify SAST results, resolve lint and CI, then add scoped tests for missing R01/R02/R13 where reliable.
6. **C6 / interpretation:** EvidenceSynth MAP/GAP/AUDIT and security control evidence states with unresolved risks explicitly listed. No premature findings. Update per-cycle checkpoint with immutable run IDs and hashes.

Do not merge while CI failures or security requirements are unresolved. The Avance 1 DOCX validated by the user remains unchanged.
