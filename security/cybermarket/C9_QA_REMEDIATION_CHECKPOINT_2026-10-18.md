# C9 QA remediation checkpoint — 2026-10-18

**Status:** fixes committed; **GitHub CI verification pending**. Do not relabel prior successful SHA as verification of these new commits.

## Root cause and scope

The detailed assurance review identified evidence-integrity weaknesses QA-03 (variant cardinality), QA-04 (required metadata), QA-05 (unsafe test identifiers) and QA-06 (missing JUnit allowed to bypass summary generation). These are harness quality risks, **not confirmed Saleor product vulnerabilities**. The test matrix's formal ASVS review remains a separate requirement decision.

## Corrections implemented

- `security/cybermarket/validate_evidence.py`: explicit reviewed expected cardinalities for CM-T01–T27 (61 total); rejects missing/duplicate variants, unexpected outcomes, invalid evidence types, malformed identifiers and mismatch of JUnit summary counts; requires exactly 2 XFAIL for provisional CM-T22 and PASS for all other variants.
- `security/cybermarket/test_validate_evidence.py`: six synthetic regression checks (valid manifest and five negative cases: missing, duplicate, unsafe, unexpected XFAIL and inconsistent counts).
- `.github/workflows/cybermarket-security.yaml`: runs validator regression tests, validates focused JUnit before generating coverage, fails explicitly when JUnit is absent. Artifact upload remains `always()` for diagnostic retention.
- No original GraphQL test oracles changed; no Saleor functional code modified.

## Caveats and next verification

- Cardinality manifest is deliberately fixed to the C9 baseline. A future addition must update it in the same reviewed commit; an unintended variant change should fail closed.
- Validator checks cardinality and uniqueness of test names but not a golden list of every parametrized name; a malicious one-for-one substitution remains possible and requires a stronger manifest if threat model demands it.
- No claim of successful GitHub Actions verification of these fixes until new run IDs and outcomes are observed. The historical reference SHA `63cadee4e9a1b43bfc07103aecbfeb61fbc33112` remains the last fully audited experimental execution.
- Pending: QA-01/02 require approved requirement interpretations; QA-07 workflow cancellation coordination; QA-08/09/10 are field and deployment scope questions for C10; QA-11 is scope-limited SAST.

## Acceptance gates

1. Evidence validator regression suite PASS.
2. Focused GraphQL JUnit: 27 IDs, 61 variants, 59 PASS, 2 expected XFAIL, no unexpected outcomes.
3. Coverage generation succeeds only after validator.
4. Repository-wide tests, linters and E2E PASS on the same PR head or documented reason for skipped paths.
5. Record exact SHA, run IDs, JUnit/archive SHA256 and update this checkpoint after results are known.

**No security verdict is automatically changed by this QA hardening.**
