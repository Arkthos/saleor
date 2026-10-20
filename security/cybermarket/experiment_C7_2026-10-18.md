# CyberMarket CR — C7 normative mapping and inclusive static triage

**Stage:** VERIFIED focused pytest, traceability and widened static scan. Repository-wide CI still requires closure on final PR head. No Saleor production runtime code changed.

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

## Verified C7 run

- [GitHub Actions 39132273808](https://github.com/Arkthos/saleor/actions/runs/39132273808), PR branch head `b41bca99ec8dd198c67bb86ce8111c87962d3c4f`; synthetic PR checkout commit `01bb2db5761abb0d1b06251882ec0544c5f400ae`.
- **Pytest:** 36 PASS, 0 FAIL, 0 ERROR, 0 SKIP, spanning 21 cases.
- **Coverage gate:** 21 cases reconciled, 13/13 risks mapped, 16 versioned ASVS IDs from the reviewed corpus. No risk automatically labelled conformant.
- Runtime artifact `cybermarket-security-junit`, ID `12138189278`; ZIP SHA-256 `010ea7d5d5eb36dda17c217d1969cc8e9064a0b1c44949981b6687d0069469db`.
- JUnit SHA-256 `4de7bfc174f31a72c5a6786d04c72d52098e4cbe3c16c74ea3dbddb9a3b4faab`; sanitized summary `bd2be3c7b1ca99dbf3de1e3c4fd4dbf3fbd0804b8832da4df548572c0b625839`; coverage JSON `79a70afcc4ff430218c098f4737133970650f66be5b2e0b02452dffd0f6866de`.
- SAST artifact ID `12138009652`; ZIP SHA-256 `c202a0845c8a0f0ad5366a92d3d577001eaad24d028f78319561eab3547e2424`; Bandit JSON SHA-256 `8efe9fd730687dca776884d77d74a9e8eb03b302d2f6be8f08a461ae5f9c50b9`.

### B105 classification — reviewed false positive

- Scanner/version: Bandit 1.8.6, `-l -ii`, 4,629 source lines.
- Diagnostic: `B105 hardcoded_password_string` | **LOW** severity | **MEDIUM** confidence.
- Location: [`saleor/core/jwt.py:23`](https://github.com/Arkthos/saleor/blob/4cb1609a90eade14b6275a407bc7a00c35698090/saleor/core/jwt.py#L23).
- Exact code: `JWT_REFRESH_TOKEN_COOKIE_NAME = "refreshToken"`.
- **Classification: FALSE POSITIVE / Not a credential.** The literal specifies an HTTP cookie **name**, not an authentication password or token **value**. The middleware uses the constant to name the cookie whose value is generated at runtime. The scanner's heuristic flags password-like hardcoded strings by name/context, but the specific reported source line contains no secret.
- Corrective decision: **do not alter Saleor product code and do not suppress the rule**. Preserve the raw alert for audit and annotate the classification with the relevant source lines. No confirmed issue from this Bandit finding.

## Final scope status

The in-process C2–C7 functional and static review is reproducible and evidence-backed. It is **not** a deployed HTTPS/proxy/browser DAST audit, not a comprehensive GraphQL fuzzing exercise, and not a statement of ASVS compliance. The legacy versus new UUID access-policy contrast and context-specific deployment gaps remain unresolved until target policy/environment evidence exists.

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

C7 changes to `-l -ii` (LOW-or-higher severity, MEDIUM-or-higher confidence) to preserve **the actual finding record** and permit line-level review. **DONE:** retrieved Bandit JSON; B105 at `saleor/core/jwt.py:23` was classified as a documented false positive on an HTTP cookie name. Retained original JSON, tool version, severity/confidence and SHA-256, with no scanner suppression.

## Current security and test-execution verdict

- The in-process test suite has 21 case IDs and 36 test invocations. C6 verified 36 PASS.
- R01/R02 deployment trust; R06 real-browser CSRF/cookie transport; R11 access-policy semantics; R13 downstream app enforcement; and JWT audience enforcement remain **context-dependent or partially tested**.
- No code-path observation is to be reported as a confirmed vulnerability without independent test and requirement context.
- **C7 exit:** new coverage gate passes with normalized IDs, raw Bandit finding is examined, repository lint/tests/e2e outcome recorded, remaining environment gaps documented.
- No academic manuscript drafting or production code modifications. PR remains draft.
