# CyberMarket CR — Experiment checkpoint C2

**Execution date:** 2026-10-18 (UTC)
**Repository:** Arkthos/saleor
**Initial implementation commit (tested):** `f66c7ad83a43573d862331a4c4727391d30ed651`
**Pinned research baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090`
**GitHub Actions workflow:** [CyberMarket GraphQL security evidence — run 39127189591](https://github.com/Arkthos/saleor/actions/runs/39127189591)
**Artifact:** `cybermarket-security-junit` (artifact ID 12136417662), containing `cybermarket-junit.xml`
**Artifact ZIP SHA-256:** `b1768d8afd47dc34e97317113dcd6f68d891110c6abc7ca4cffa820ce9bd4b42`
**JUnit XML SHA-256:** `9d12dce77bb7c642c93a0c2b7a9e03fba080f1cf81aabb6ec42b5c4ddaa00c9d`

## Raw test results

| Outcome | Count |
| --- | ---: |
| Pytest tests (includes parameterized CM-T03) | 8 |
| Passed | 8 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Pytest-reported suite duration | 150.819 seconds |

Case identifiers and evidence types are stored in the JUnit properties:
- CM-T01: identity (security contract).
- CM-T02: revoke + reuse access and refresh credentials (security contract).
- CM-T03: argument-no-csrf / cookie-valid / cookie-missing / cookie-bad (four contract tests).
- CM-T04: external-reference order permission gate (security contract).
- CM-T05: anonymous new-UUID order field visibility (**characterization only**).

**Academic interpretation:** Raw PASS means the coded expectation matched the observed runtime response in the fixture-backed GitHub Actions environment. It is **not** a general ASVS compliance certificate, nor does it prove safety for other configuration, actors or deployments.

**CM-T05 remains potentially important:** Current Saleor behavior and upstream tests expose order address/email fields for new UUIDs to anonymous requests. This must be evaluated against a documented policy and complete resolver chain before asserting a vulnerability. PASS here confirms observation only; status `NO_DETERMINADO_CHARACTERIZATION`.

## Follow-up / completion criteria

1. Await repository's general lint, unit and e2e workflows and address actionable CI failures.
2. Review JUnit's test properties and confirm no secrets or personal data were emitted (only synthetic fixture metadata expected).
3. Add a second customer using the existing `customer_user2` fixture and compare access to another customer's order (R11/H12).
4. Examine the intended new-UUID vs old-ID order access semantics and field-level policy, then separate observation from security requirement verdict.
5. Incrementally add bounded tests for token audience/type, CSRF in browser context, and GraphQL cost limits.
6. For every run, save input commit, code SHA, artifacts, tool versions, logs, outcomes, GAP/AUDIT assessment and remediation plan. Do not silently overwrite earlier checkpoints.

The user-validated Avance 1 is not changed by this work.
