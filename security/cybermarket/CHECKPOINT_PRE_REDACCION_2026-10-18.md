# CHECKPOINT DEFINITIVO — CyberMarket CR, antes de redacción

**Estado:** fase experimental C2–C9 CERRADA dentro del alcance sintético CI; análisis técnico de resultados auditado; **redacción académica NO iniciada**. Fecha: 2026-10-18.

## Reanudación rápida

Repositorio: `Arkthos/saleor`; PR #1 draft; rama `research/cybermarket-security-tests-v1`. **Documento canónico de resultados:** [INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md](INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md). Complementos: [experiment_C9_final_2026-10-18.md](experiment_C9_final_2026-10-18.md), [test_matrix.csv](test_matrix.csv), [POLICY_ORDER_P01_PROVISIONAL.md](POLICY_ORDER_P01_PROVISIONAL.md), [C10_live_validation_plan.md](C10_live_validation_plan.md).

**Tested branch SHA:** `63cadee4e9a1b43bfc07103aecbfeb61fbc33112`; checkout/merge SHA `98645a24a56e9764e48fdefeea6b2e9a4095ad4a`. Later commits containing the analysis/report/checkpoint are documentation-only and **are not themselves the tested baseline**.

## All checks verified

- General tests [39144885841](https://github.com/Arkthos/saleor/actions/runs/39144885841): SUCCESS; 17,613 PASS, 2 expected XFAIL, 0 FAIL/ERROR.
- Focused CyberMarket [39144885995](https://github.com/Arkthos/saleor/actions/runs/39144885995): SUCCESS; 59 PASS, 2 expected XFAIL, 0 FAIL/ERROR/SKIP.
- Linters [39144885812](https://github.com/Arkthos/saleor/actions/runs/39144885812): SUCCESS.
- E2E [39144885821](https://github.com/Arkthos/saleor/actions/runs/39144885821): SUCCESS.
- Changelog [39144885986](https://github.com/Arkthos/saleor/actions/runs/39144885986): SUCCESS.
- Historical cancelled general run 39144176059 superseded by successful 39144885841; never label cancelled run successful.

**Traceability:** 27 unique case IDs, 61 invocations, 26 contract PASS, 33 characterization PASS, 2 expected provisional-policy XFAIL; 13 risks mapped, all `NO_DETERMINADO`. The general run includes the focused cases; do not double-count.

**Artifact ZIP IDs / SHA256:** focused 12142029921 / `b8c38641cab220debac6c0d806b74141016f1baa0ad109caeb02647f0ac5412e`; static 12143311107 / `de680b13d3b1fc5ddd35970d8e999f97c4d65fffea4fda802515ede9c4b8e37f`; general 12143532461 / `809f7933869efe42bd1114e6a44d1d55f1c6df66b3d0560c31f55f8d17aae54a`. Independent per-file SHA256SUMS validation and full case inventory recorded in canonical report. Artifacts are retention-limited; raw ZIPs should be copied to long-term storage if required.

## Conclusions and decision boundaries

- Known UUID order queries exposed original **synthetic** email and two street fields to unrelated/anonymous actors; legacy number path obfuscated them; owner and missing-ID controls characterized.
- Two strict XFAIL cover proposed owner-only **email** policy for two actors. P-ORDER-01 is unapproved; no official Saleor violation, practical UUID guessing, or live exploit established.
- Bandit B105 cookie-name `refreshToken` signal reviewed as false positive, not suppressed.
- Live HTTPS/browser/proxy deployment, CORS, frontend identifier leakage, malformed IDs and exhaustive staff/app field permissions are **out of scope** for C2–C9 and deferred to classmate-executable C10. No live result exists.

## Next-session instruction

**Begin with academic analysis/writing ONLY when user asks.** Use canonical closure report and matrix; apply EvidenceSynth, Tutor and Humanizer, with claim-level provenance, APA 7, distinction of observation/inference/normative requirement, and explicit limitations. Do not overwrite approved Avance 1. Independently plan classmate C10 live deployment using existing guide when requested. Do not modify Saleor functional code or merge PR #1.

**Stop here: immediately before drafting.**

## Addendum prospectivo — contenidos de semana 7 (2026-10-20)

**No modifica la validación C2–C9 de arriba.** Se agregó el plan [CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md](CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md) con una taxonomía explícita de análisis estático, unitarias aisladas, integración, dinámica/DAST y regresión, junto con backlog W7-A–W7-F. Es **un checkpoint de planificación**, no una ejecución ni una reapertura del cierre C9. Cuando se retome el proyecto, consultar primero el documento nuevo, el plan maestro y el handoff C10; no redactar el Avance 2 hasta solicitud expresa.
