# CyberMarket CR — C6 consolidated research evidence

**Scope:** pinned Saleor fork implementation, pytest/Django/GraphQL fixture-backed checks and selected Python Bandit static scan. This is **not** an academic manuscript or a production penetration-test report.

**Pinned Saleor baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090`
**Source:** [Arkthos/saleor PR #1](https://github.com/Arkthos/saleor/pull/1), draft.

## Immutable execution chronology

| Cycle | GitHub Actions run | Executions | Raw outcomes | Evidence |
| --- | --- | ---: | --- | --- |
| C2 | [39127189591](https://github.com/Arkthos/saleor/actions/runs/39127189591) | 8 | 8 PASS | `experiment_C2_2026-10-18.md` |
| C3 initial | [39128224126](https://github.com/Arkthos/saleor/actions/runs/39128224126) | 10 | 9 PASS, 1 FAIL | Original CM-T07 test oracle expected full object denial |
| C3 corrected | [39128693170](https://github.com/Arkthos/saleor/actions/runs/39128693170) | 10 | 10 PASS | Correctly asserts legacy-ID field masking |
| C4 | [39130431874](https://github.com/Arkthos/saleor/actions/runs/39130431874) | 21 | 21 PASS | Added identity/JWT/GraphQL bounded limits + SAST |
| C5 | [39131023314](https://github.com/Arkthos/saleor/actions/runs/39131023314) | 36 | 36 PASS | Added header/IP/throttle/app-permission/JWT-none cases + SAST |

**The row counts are cumulative snapshots, not additive independent tests.** Current suite: 21 distinct case IDs, 36 pytest invocations, 13 risks mapped to at least one case. There are **zero confirmed exploitability findings** in this harness; this does not prove absence of vulnerabilities.

## Evidence integrity and sources

Each detailed C2–C5 checkpoint preserves tested/merge code SHA, run URL, artifact IDs, JUnit SHA-256 and relevant ZIP hashes. Synthetic fixtures only; no production tokens, customer data, external API scanning, destructive stress tests or real authentication secrets.

The workflow now produces three runtime files:
1. `cybermarket-junit.xml` — unmodified pytest results (includes only synthetic fixture data).
2. `cybermarket-summary.json` — intentionally sanitized execution properties/outcomes.
3. `cybermarket-coverage.json` — **C6 additional gate**, generated from the committed matrix and current JUnit summary; rejects missing, extra or misclassified case IDs and **never** declares ASVS conformance.

`SHA256SUMS` covers these files. A parallel Bandit 1.8.6 job saves its JSON report and checksums. New C6 coverage-generator CI must be verified separately; C5 PASS does not imply C6 PASS.

## EvidenceSynth MAP — risk coverage with controlled interpretation

| Risk | Direct cases | Evidence kind | Meaningful remaining gap |
| --- | --- | --- | --- |
| R01 | CM-T17/T18 | Characterization only | Proxy/header normalization in a deployed reverse proxy |
| R02 | CM-T18/T19 | Characterization + algorithm contract | Real cache state, concurrency and spoof-proof client IP |
| R03 | CM-T09 | Contract | Timing/transport differences and larger valid samples |
| R04 | CM-T08 | Contract | Effective production TTL and revocation policy |
| R05 | CM-T10 | Contract | All refresh/issuer/audience call paths |
| R06 | CM-T03/T14 | Contract + characterization | Real browser cross-origin, cookie origin and TLS |
| R07 | CM-T02 | Contract | All token categories and service nodes |
| R08 | CM-T08/T11/T21 | Contracts | Audience enforcement policy, rotation/key provenance |
| R09 | CM-T04 | Contract | Other mutation-specific permission paths |
| R10 | CM-T01/T12/T13 | Contracts | Additional fields and staff/app role combinations |
| R11 | CM-T05/T06/T07 | Characterization + contract | **Undecided new-UUID full PII visibility policy** |
| R12 | CM-T15/T16 | Contracts | Real configured cost map, bounded query-cost performance |
| R13 | CM-T20 | Contract | Downstream consumption of app delegated permissions |

MAP coverage is 13/13 for **association with test cases**, NOT 13/13 validated mitigations. Several risk evaluations remain **NO_DETERMINADO** and will stay that way until a defensible requirement, environment or additional test exists.

## EvidenceSynth GAP — known limits

- The lab uses Django's in-process GraphQL test client, not a real reverse proxy, browser or production-like TLS termination.
- The code itself accepts X-Forwarded-For as a valid IP; trust and spoofing controls depend on the deployment configuration.
- The new UUID order path returned synthetic email and street fields for both unrelated and anonymous actors; legacy-ID paths masked selected fields for nonowners. Do not label the difference as an exploit without confirmed intended access semantics.
- `Bandit -ll -ii` filters out low-severity signals. The scan found no results meeting both configured severity/confidence thresholds in 4,629 analyzed lines, not 0 possible weaknesses.
- No broader fuzzing, rate/volume denial-of-service trial, external GraphQL DAST scan or production deployment configuration audit has been executed. These are scope boundaries, not completed tests.
- ASVS 5.0.0 and WSTG 4.2 IDs in `test_matrix.csv` are preliminary labels; their normative wording and applicability must be validated before assigning compliance.

## EvidenceSynth AUDIT — classification and decision record

1. **Positive observation:** targeted issuance, refresh, revocation, role partitioning, GraphQL alias and mutation-count checks matched their intended source-level behavior in synthetic fixture runs.
2. **Revision correction:** C3 initially assumed a legacy order query would be fully denied. Runtime showed selected fields were masked; the test was corrected and rerun. Both old failed and new successful JUnit artifacts remain preserved.
3. **Unresolved security policy:** CM-T05/CM-T06 passing confirms returned fields under known UUIDs. It is **not** a proof of compliant access.
4. **No product code remediation:** no exploitable finding has been independently established and no Saleor production implementation code has been changed.
5. **CI quality gates:** finish repository-wide lint/unit/e2e on final head, rerun evidence generator checks, and retain run + SHA for the final documentation commit.

## Exit criteria for this in-process test suite

- All 21 case IDs executed with documented outcomes and matrix correspondence.
- Dedicated workflow + selected SAST jobs succeed and publish XML, sanitized summary, coverage and hashes.
- Repository-wide checks reviewed; any exception specifically justified.
- The unresolved policy, environmental limits and untested scopes remain explicitly documented.
- Only the **research testing infrastructure** may be considered complete under these gates; a full production/security certification is neither possible nor claimed.

**Next optional separate lab stage:** instrument a private HTTPS+reverse-proxy/browser deployment, run bounded authenticated HTTP GraphQL DAST, validate actual origin/CSRF/cookie configurations and client-IP trust semantics. Requires that environment and explicit target approval. No manuscript drafting in this phase.
