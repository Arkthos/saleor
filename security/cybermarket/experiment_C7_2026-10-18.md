# CyberMarket CR — C7 normative mapping and inclusive static triage

**Stage:** Implemented; latest C7 CI results pending. No change to the Saleor runtime code or the behavior tested by C2–C6.

## Verified C6 baseline

- GitHub Actions: [run 39131644653](https://github.com/Arkthos/saleor/actions/runs/39131644653).
- Pytest: **36/36 PASS**, 21 cases `CM-T01`–`CM-T21`.
- Coverage generator ran successfully: **21/21 JUnit case IDs matched the matrix** and all 13 risk IDs have at least one mapped test.
- `cybermarket-coverage.json` reports every risk's security verdict as `NO_DETERMINADO` until a manual normative/operational decision.
- Runtime artifact ID `12137409694` (ZIP SHA-256 `dd58f42a27069c792a45ce92b5c571fde885a7138f27893dfabd84f96a63fb7e`).
- JUnit XML SHA-256 `d3776b6e870269dd2ca965acb14b6fb8f7ed96e5c9202c784b439ff3d789999b`.
- Summary JSON SHA-256 `e3775ed0031feb05eb9bbfb2f4f039f3e0f961e72c088e9b8fd50a158f434f3d`.
- Coverage JSON SHA-256 `fb6648079351b96130cdb9f6208592b8e8bb0b45aa13e1ade2eec6d34d56b01e`.
- Scoped SAST artifact ID `12137289818` (ZIP SHA-256 `1799f35f6e3fb2959a810ad91c0504ed5407b433e83f2367706ffbbb1c44169b`).

## C7 normative correction — source provenance

The initial matrix used provisional normative IDs. Compared those against the **frozen ASVS 5.0.0 corpus** retained in the research checkpoint `requisitos_ASVS_priorizados.csv` (23 exact requirements and references) and the **OWASP WSTG 4.2 versioned techniques**. All IDs now linked in the matrix belong to the reviewed subset, rather than arbitrary chapter numbers.

Key corrections:
- CM-T08–T11: JWT lifetime/type/audience `9.2.1`, `9.2.2`, `9.2.3` (audience **presence/propagation**, not proof of audience enforcement).
- CM-T09: anti-enumeration `6.3.8`, WSTG-IDNT-04 (versioned account-enumeration technique).
- CM-T14: cookie `3.3.1` Secure, `3.3.2` SameSite and `3.3.4` HttpOnly.
- CM-T15/T16: GraphQL query/amount limits `4.3.1`, WSTG-APIT-01.
- CM-T17: authentication pathways `6.1.3`, WSTG-ATHN-04; CM-T18: throttle-relevant IP routing `6.3.1`, WSTG-ATHN-03.
- CM-T21: JWT cryptographic allowlist `9.1.2` with WSTG-ATHN-04 as a related but broader authentication technique.

The `build_coverage.py` executable gate rejects IDs outside the inspected ASVS/WSTG subset; future expansion requires a new source verification rather than guessed identifiers. **This confirms identifier validity, not requirement conformity.**

Versioned guides:
- ASVS 5.0.0: https://github.com/OWASP/ASVS/releases/tag/v5.0.0
- WSTG 4.2: https://wstg.owasp.org/v4.2/
- WSTG-IDNT-04: https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account/

## Bandit static-triage depth

Previous C4–C6 runs used Bandit `-ll -ii` (minimum MEDIUM severity and MEDIUM confidence), which yielded zero reported matches while aggregate counts included **one LOW-severity, MEDIUM-confidence signal**.

C7 changes to `-l -ii` (LOW-or-higher severity, MEDIUM-or-higher confidence) to preserve **the actual finding record** and permit line-level review. **PENDING:** retrieve new JSON report, identify its test ID/file/line, classify according to source evidence (not merely tool severity) and preserve all results as an immutable C7 checkpoint.

## Current security and test-execution verdict

- The in-process test suite has 21 case IDs and 36 test invocations. C6 verified 36 PASS.
- R01/R02 deployment trust; R06 real-browser CSRF/cookie transport; R11 access-policy semantics; R13 downstream app enforcement; and JWT audience enforcement remain **context-dependent or partially tested**.
- No code-path observation is to be reported as a confirmed vulnerability without independent test and requirement context.
- **C7 exit:** new coverage gate passes with normalized IDs, raw Bandit finding is examined, repository lint/tests/e2e outcome recorded, remaining environment gaps documented.
- No academic manuscript drafting or production code modifications. PR remains draft.
