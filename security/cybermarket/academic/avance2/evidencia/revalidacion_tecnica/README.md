# Revalidación técnica — fase cerrada

**Estado: COMPLETADA en el alcance planificado, 2026-11-02.** Todas las ejecuciones finales terminaron. Fuente eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7; checkout 90455ca8abb7d72f707e0137e3ac80fab7a06dec.

- [Cierre técnico detallado](../../CIERRE_PRUEBAS_TECNICAS.md).
- [Manifiesto de ejecuciones, resultados y límites](CIERRE_TECNICO.json).
- [Linters finales](LINTERS_FINALES.json) y [licencias finales](LICENCIAS_FINALES.json).
- [Conservación de originales](ARCHIVO_ORIGINALES_FINAL.json).
- [Conciliación técnica de las catorce observaciones](conciliacion_hallazgos_tecnicos.csv), insumo pendiente de incorporar a A2-07.

| Batería | Resultado final |
|---|---|
| General | 17.613 PASS / 2 XFAIL previstos |
| Focal, subconjunto de general | 59 PASS / 2 XFAIL previstos |
| Unidades/validadores independientes | 42 PASS: 30 producto + 12 evidencia |
| C10 HTTP/HTTPS/Chromium | 26 PASS |
| E2E original | 211 PASS |
| Fronteras de licencias | 6 PASS, repetidas por fuente; negativo GPL verificado |
| Licencias | 502 entradas aprobadas por fuente |
| Estática | Semgrep 2.608 archivos / 0 hallazgos; Bandit B105 cookie-name revisado |
| Calidad | 10 hooks PASS |

No sumar subconjuntos ni duplicar los seis controles de licencia por ejecutarse en dos fuentes. Los dos XFAIL pertenecen a la política P-ORDER-01 provisional.

Los directorios final_general, final_lab, final_e2e, final_focal, final_static y licencias_final contienen la evidencia de cierre. En general/licencias se publican public.zip depurados y se guardan por separado los originales. Los intentos previos y sus fallos permanecen con sus nombres, fechas y hashes. Sus estados de bloqueo o pendientes son históricos y no describen el cierre actual. No se generó otro entregable académico.
