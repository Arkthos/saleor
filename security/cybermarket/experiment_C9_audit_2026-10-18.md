# C9 — Independent evidence audit and P-ORDER-01 decision gate (2026-10-18)

Status: REVIEW IN PROGRESS; no policy approved, no product changes.

## Provenance
- PR #1 head previously validated: `dc66ac7fe4328651085012091170f66667325321`.
- Dedicated run: https://github.com/Arkthos/saleor/actions/runs/39135827489 (JUnit artifact 12139604110; SAST artifact 12139702424).
- Historical C8 run: https://github.com/Arkthos/saleor/actions/runs/39135116746 ; original case-level results in `evidence_C8_snapshot.md`.
- Counts from C8 snapshot: 36 PASS, 2 XFAIL, 0 unexpected failures; no new test execution claimed here.

## Independent code audit
- CM-T05: anonymous actor with known order UUID; compares raw email, billing street, shipping street against synthetic fixture (characterization).
- CM-T06: owner, unrelated authenticated customer, anonymous actor; compares those three fields (characterization).
- CM-T07: legacy order-number path; checks nonowners' three fields differ from raw values. Does not independently establish adequacy of masking.
- CM-T22: two actor variants, strict XFAIL, but the sole final policy assertion checks `userEmail` (or null order), **not billing or shipping street independently**. Thus 2 XFAIL establish failure of the proposed email expectation, not independently each address-field requirement.
- 22 case IDs and 13 mapped risk IDs indicate traceability coverage, not verified security conformance or complete threat coverage.
- No confirmed Saleor vulnerability verdict is justified from this evidence alone.

## Required next experimental gates
1. Preserve current oracle and historical JUnit. Introduce independently attributable P-ORDER-01 field-level assertions for email, billing street and shipping street for unrelated and anonymous actors. Ensure strict XPASS requires manual review; report outcomes per field and actor without leaking fixture PII.
2. Add owner positive-control, missing/invalid identifier, staff/app delegated permission and intended bearer/share-link cases as separate, explicitly scoped tests where fixtures support them.
3. Test actual masking/redaction semantics, not just `!= raw`; define allowed output and partial-information leakage criterion before declaring conformance.
4. Reconcile new JUnit to test matrix, risk coverage, raw artifacts, checksums, SHA, and final-head CI; do not infer results from test source alone.
5. Separately determine intended order UUID bearer semantics, recipient sharing, expiry/revocation, authorization boundaries and field entitlements. A known UUID is a precondition, not evidence of guessability or a real-world disclosure path.
6. Require a documented CyberMarket policy-owner decision to adopt, modify or reject P-ORDER-01 before assigning NO_CONFORME. Deployment-specific exploitability requires an authorized representative environment.

## Current verdict
PASS: 36 historical experimental invocations (including characterization); XFAIL: 2 historical provisional email-policy expectations. PROVISIONAL GAP: P-ORDER-01/R11, pending owner decision. CONFIRMED VULNERABILITY: none established. This checkpoint is a review, not a new test run or policy approval.

Restrictions: do not alter Saleor functional code, Avance 1, oracles to hide findings, or merge PR #1.
