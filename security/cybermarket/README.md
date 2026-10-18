# CyberMarket CR — Security testing, cycle 1

**Status:** implemented test candidates; CI results pending. **Research baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090` (do not silently rebase to a new Saleor version).

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

**IMPORTANT on CM-T05:** In this pinned Saleor revision, pre-existing upstream tests
`test_query_order_fields_order_with_new_id_by_anonymous_user` and
`test_query_order_fields_order_with_new_id_by_staff_no_perm`
explicitly assert the returned address/email fields. Our test reproduces that described behavior for research, without deciding whether exposure violates the system's intended business policy. Its green status **must not** be reported as security conformance. The object/reference authorization boundary needs an agreed threat model, requirement interpretation, and independent controlled verification.

## Requirement mapping (preliminary, NOT ASVS certification)

| Case | OWASP ASVS 5.0.0 relevant requirement(s) | WSTG 4.2 relevant technique |
| --- | --- | --- |
| CM-T01 | v5.0.0-8.2.2; v5.0.0-8.2.3 | WSTG-ATHZ-02 |
| CM-T02 | v5.0.0-7.4.1 | WSTG-SESS-06 (backend adaptation) |
| CM-T03 | v5.0.0-3.5.1; v5.0.0-9.2.2 | WSTG-SESS-05 |
| CM-T04 | v5.0.0-8.2.1 | WSTG-ATHZ-02 |
| CM-T05 | v5.0.0-8.2.2; v5.0.0-8.2.3 | WSTG-ATHZ-04 |

These are candidate mappings only. A passing test is **not** evidence of comprehensive coverage of any standard section.

## Execution

A dedicated GitHub Actions workflow is provided:
`.github/workflows/cybermarket-security.yaml`.
It runs pytest against the repository's pinned `uv.lock` with isolated PostgreSQL and Valkey services, and uploads a JUnit XML file whether tests pass or fail.

Equivalent local command (requires the repository development environment, a test PostgreSQL database, cache and the normal test settings):

```bash
uv sync --locked
mkdir -p security-results
uv run pytest saleor/graphql/tests/test_cybermarket_security_contracts.py -q --junitxml=security-results/cybermarket-junit.xml -o junit_family=legacy
```

**Do not upload usable JWTs, cookies, passwords, personal data or raw production logs.** The JUnit report contains only case and requirement identifiers in `record_property` metadata; the test source uses synthetic fixtures.

## Evidence and classification

- Capture run ID, commit, tool versions, fixture description, execution time, test case IDs, JUnit, outcome and artifact checksum.
- Distinguish `PASS`, `FAIL`, `SKIP`, `ERROR` as raw execution outcomes from `CONFORME`, `NO_CONFORME`, `NO_DETERMINADO`, `NO_APLICABLE` as academic assessments.
- A `FAIL` may represent a test/environment defect; a `PASS` in CM-T05 **characterizes an exposure** rather than proving authorization.
- Any potential security deviation must be manually replicated, scoped and tied to an applicable ASVS requirement before it can be called a confirmed finding.
- Keep `H01–H15` as documentary observations and `R01–R13` as hypothetical risks until backed by tests. Record uncertainties separately.

## Checkpoints / next iterations

1. **C1 / implemented:** scenario IDs, code, traceability and dedicated CI workflow committed in a draft PR.
2. **C2 / execution:** review targeted workflow and JUnit, collect failure logs, fix only confirmed test defects.
3. **C3 / coverage:** add authenticated client A/client B cross-object checks, staff permissions, legacy-ID field behavior; agree on the intended exposure policy for new IDs first.
4. **C4 / depth:** expand token type/audience, cookie settings, login rate limits and GraphQL query-cost tests using bounded synthetic fixtures.
5. **C5 / interpretation:** EvidenceSynth MAP/GAP/AUDIT, per-case records and regression runs. Update this document after each iteration.

Do not merge while CI failures or security requirements are unresolved. The Avance 1 DOCX validated by the user remains unchanged.
