# CHECKPOINT — Semana 7: estrategia de pruebas multinivel (2026-10-20)

**Proyecto:** CY-703 Seguridad de Software · CyberMarket CR (escenario ficticio) · fork `Arkthos/saleor`.  
**Propósito:** preservar una decisión metodológica y un plan de continuación; **NO** es un resultado de pruebas, un nuevo avance académico ni una ampliación ya ejecutada.  
**Estado de este checkpoint:** DOCUMENTADO / PENDIENTE DE IMPLEMENTACIÓN.  
**Repositorio/PR:** [Arkthos/saleor PR #1](https://github.com/Arkthos/saleor/pull/1), rama `research/cybermarket-security-tests-v1`, PR en borrador y sin merge.  
**Commit Saleor fijado para investigación:** `4cb1609a90eade14b6275a407bc7a00c35698090`.  
**HEAD observado al planear este checkpoint:** `b2a30a2900280b7c169133858857abebf53923c4` (metadatos y documentación posteriores pueden variar; volver a consultar GitHub).  
**Avance 1:** validado por el usuario; no modificarlo ni reinterpretarlo retrospectivamente.

## 1. Origen del ajuste: materiales nuevos y conversación académica

Fuentes docentes incorporadas a la biblioteca del curso:

1. `Seguridad de Software S7 V1 Análisis Estático.pdf`: análisis sin ejecución; tipos de análisis de **control, datos, fallas e interfaces**, ventajas/limitaciones, revisión por pares.
2. `Seguridad de Software S7 V2 Análisis Dinámico.pdf`: pruebas con ejecución; **caja negra, caja blanca y caja gris**; métodos funcionales, integración, regresión, caminos y cobertura.
3. `Seguridad de Software S7 V3 Pruebas Unitarias.pdf`: aislamiento de funciones/clases, **límites, lógica, excepciones, estado de objetos, mocks y stubs**, automatización, TDD y regresión.
4. `Programa del curso Seguridad de Software (14 semanas).pdf`: **semana 7**, análisis estático/dinámico y pruebas unitarias; **semana 8**, integración y pruebas de software; **semana 9**, entrega del Avance 2. Las fechas de calendario y la rúbrica específica deben verificarse cuando se retome.
5. Conversación de seguimiento de contenidos del curso, compartida por el usuario: `https://chatgpt.com/g/g-p-6a9eeb4a76e8819192c2d243b1e2c80b/c/6a9eed93-b9ec-83e8-a900-6a7b47e3c4a6`. Se recuperaron decisiones y una síntesis de investigación con **Consensus** y **Sider Scholar**, pero **no una transcripción íntegra comprobada**. Conservar sus autores/trabajos mencionados como **candidatos de lectura, no referencias verificadas**; recuperar DOI, artículo y texto completo antes de citarlos.

**Conclusión derivada de los materiales:** el planteamiento previo es válido, pero la evidencia debe clasificarse como una **estrategia de aseguramiento multinivel**. Ningún tipo de prueba, por sí solo, demuestra seguridad global. No describir una prueba de integración GraphQL como una prueba unitaria por usar pytest.

## 2. Línea base C2–C9: preservar sin repetir ni inflar resultados

**Fuente canónica:** `INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md`, `experiment_C9_final_2026-10-18.md`, `CHECKPOINT_PRE_REDACCION_2026-10-18.md`, `test_matrix.csv`, `REPORTE_INGENIERIA_ASEGURAMIENTO_C2_C9_2026-10-18.md`.

Evidencia registrada para el **SHA experimentado** `63cadee4e9a1b43bfc07103aecbfeb61fbc33112`:
- [Suite CyberMarket C9: run 39144885995](https://github.com/Arkthos/saleor/actions/runs/39144885995): **27 IDs, 61 invocaciones; 59 PASS y 2 XFAIL esperados**; no fallos ni errores inesperados.
- [Suite general: run 39144885841](https://github.com/Arkthos/saleor/actions/runs/39144885841): **17 613 PASS y 2 XFAIL esperados**. **Incluye** los casos específicos; no sumar los conteos.
- [Linters: run 39144885812](https://github.com/Arkthos/saleor/actions/runs/39144885812): SUCCESS; [E2E: 39144885821](https://github.com/Arkthos/saleor/actions/runs/39144885821): SUCCESS; [changelog: 39144885986](https://github.com/Arkthos/saleor/actions/runs/39144885986): SUCCESS.
- **R01–R13** tienen al menos un caso trazado, **no** trece riesgos cerrados o conformes; dictamen normativo `NO_DETERMINADO` donde corresponda.
- El comportamiento por UUID de pedidos y la ofuscación en la ruta legacy están observados con datos sintéticos. **P-ORDER-01 sigue provisional y no autorizada**. Las dos XFAIL documentan esa política hipotética, no una vulnerabilidad confirmada de Saleor.
- SAST Bandit acotado; B105 LOW/MEDIUM sobre el literal `refreshToken` es un nombre de cookie, clasificado documentalmente como falso positivo. No implica ausencia de otras debilidades.
- Artefactos JUnit y SAST, identificadores y hashes se conservan en el cierre C9; los artefactos Actions caducan. Priorizar archivo externo de los ZIP si se requiere reproducción byte a byte.
- El SHA observado hoy es posterior al SHA evaluado. **No asignar el resultado de CI del SHA experimentado al HEAD vigente sin revalidación.**

**Estado aprobado del trabajo histórico:** C2–C9 cerrado **solo como evaluación sintética CI**, no como una auditoría de despliegue real. El estudio con C10 aún no tiene resultados ejecutados.

## 3. Matriz de tipificación metodológica que debemos incorporar

| Tipo de evaluación | Situación actual | Acción futura / criterio |
| --- | --- | --- |
| Inspección y revisión estática | Revisión manual, Bandit y Semgrep en checks | Elaborar matriz de control/datos/fallas/interfaces, alcance y triage de alertas con anclas de código |
| Pruebas unitarias **aisladas** | No demostradas como estrato independiente por la suite GraphQL | Añadir tests directos de funciones pequeñas con mocks/stubs donde proceda, sin DB/red |
| Pruebas de integración | Suite pytest GraphQL fixture-backed ya ejecutada | Etiquetar casos existentes con dependencias DB/caché, subsistemas, alcance y limitaciones |
| Pruebas de regresión | C2–C9 y reejecuciones de CI | Relacionar cada defecto de harness o producto con un caso y con el run/commit de revalidación |
| Dinámica de caja blanca/gris | Tests de Django diseñados con acceso a implementación | Declarar explícitamente el conocimiento de código y el nivel de aislamiento de cada caso |
| Dinámica externa/negra o gris sobre HTTP | **No ejecutada** como C10 | C10 planificado: servidor aislado y autorizado, HTTP/HTTPS, navegador, proxy, cookies, CORS, TLS, logs depurados |
| Cobertura y criterio de salida | 27 IDs / 13 riesgos asociados | No usar recuento de tests como cobertura de ramas, calidad de oráculos o cierre ASVS; aportar métricas reales si se instrumentan |

## 4. Backlog ejecutable (aún NO implementado)

**W7-A / P0 — Taxonomía y mapa de cobertura.** Añadir `test_level`, `test_design` (black/white/gray), `dependencies`, `assertion_scope`, `normative_status` y `evidence_ref` a un manifiesto **sin alterar ni destruir** el CSV histórico. Identificar qué casos CM-T01–CM-T27 requieren etiquetas distintas y separar expectativas funcionales, seguridad y caracterización. Aceptación: ningún test sin tipo, ningún XFAIL contado como conformidad; validación automatizada de consistencia y justificación de cualquier categoría ambigua.

**W7-B / P0 — Pruebas unitarias reales.** Diseñar casos `CM-U01...` (IDs reservados, **no existen todavía**) para lógica aislable: validación de tipo JWT, valores CSRF sin red, ofuscación `obfuscate_email`/`obfuscate_string`, utilidades de identificación de IP y ramas de validación de límites. Seleccionar primero la función concreta y sus invariantes; usar parametrización para valores normales, bordes e inválidos, `monkeypatch`/`Mock` para dependencias, y pruebas de errores. Aceptación: ejecución sin DB ni servicios externos cuando sea viable, JUnit con IDs, límites y condiciones de regresión, enlace a código fuente. **No duplicar la lógica GraphQL como supuesto test unitario.**

**W7-C / P1 — Revisión estática ampliada.** Documentar cuatro dimensiones docentes (control/datos/fallas/interfaces), revisar código y flujos de autorización/estado concretos, registrar regla/archivo/línea/contexto/estado. Reaprovechar Bandit, Semgrep, mypy y revisiones ya disponibles; evaluar SCA/dependencias solamente si añade valor verificable. Aceptación: índice de rutas y resultados/ausencia de hallazgos delimitados por herramienta; justificar falsos positivos sin ocultar alertas; no inferir cobertura absoluta del código.

**W7-D / P1 — Calidad de pruebas/regresión.** Inventario de oráculos, fixtures, tests positivos/negativos, condiciones límite y excepción, fragilidad de mocks. Seleccionar un conjunto pequeño y relevante para cobertura de línea/rama o pruebas de mutación **si las herramientas y tiempos lo permiten**; no inventar porcentajes. Aceptación: métrica obtenida con herramienta, commit y módulo, o limitación documentada. Comprobar integridad y depuración de reportes.

**W7-E / P1 — Continuidad C10 desplegado.** Reusar `C10_live_validation_plan.md` y `C10_live_validation_roadmap_team_handoff.md`, no crear un despliegue público por defecto. Probar con un servidor efímero, identidades sintéticas, versiones fijadas, acceso autorizado, controles de salida y teardown. Aceptación: LIVE-01–LIVE-07 con trazas HTTP, diferencia entre comportamiento Django y transporte/proxy/navegador, resultados reales, JUnit u otro formato verificable, hashes y brechas explícitas. Si no hay entorno, marcar `BLOCKED/NOT_EXECUTED`, **nunca PASS**.

**W7-F / P2 — Evidencia académica y síntesis.** Contrastar la clasificación de pruebas con el material de la semana 7, programa de semanas 8–9 y artículos académicos **verificados** (Consensus/Sider Scholar solo candidatos hasta confirmar DOI/texto). Aplicar EvidenceSynth MAP/GAP/AUDIT y preservar qué aporta y qué no cada nivel. **No redactar el Avance 2** hasta orden posterior del usuario. Mantener la convención de referencias aprobada para el manuscrito y confirmar la rúbrica antes de elegir/alterar IEEE o APA.

## 5. Contrato de ejecución y aceptación para retomar

1. Revisar HEAD/PR/CI actuales y leer este checkpoint junto con el informe de cierre C9 y el plan maestro.
2. Seleccionar un ítem W7-A...W7-F por ciclo; registrar propuesta, casos, dependencias, oráculos, criterios de salida y fuentes.
3. Implementar únicamente en la rama del PR; no reescribir historia de casos C2–C9 ni modificar código funcional de Saleor para forzar pruebas verdes.
4. Ejecutar GitHub Actions en el SHA preciso. Recoger JUnit, análisis estático, cobertura, versiones, manifest SHA256 y razón de cada FAIL/ERROR/SKIP/XFAIL.
5. Corregir defectos de harness/CI comprobados y repetir; no sustituir el criterio de seguridad por el comportamiento observado para conseguir PASS.
6. Clasificar cada evidencia como observación, inferencia, requisito adoptado o propuesto, brecha normativa o hallazgo confirmado. `PASS` no equivale a cumplimiento ASVS.
7. Actualizar la matriz derivada, checkpoint, plan maestro y README **tras** verificar resultados; permitir excepciones de CI solo justificadas.
8. No fusionar PR, no modificar Avance 1 ni redactar entrega hasta indicación expresa. Preservar artefactos antes de su caducidad.

## 6. Gate de retoma y decisiones pendientes

- **Primer paso futuro recomendado:** W7-A (clasificación/matriz), **después W7-B** (unitarias aisladas). W7-C puede desarrollarse en paralelo documentalmente, sin claims de ejecución.
- **Decisiones externas pendientes:** legitimidad de P-ORDER-01; alcance real y acceso al despliegue C10; conformidad con rúbrica específica del Avance 2.
- **No convertir tareas planificadas en resultados:** este archivo es un checkpoint **prospectivo**. No contiene ejecución nueva y no altera la conclusión de C2–C9.
- **No perder la trazabilidad:** conservar SHA experimentado, branch SHA actualizado, run IDs, fuente docente y caducidad de artefactos.
- **Reconexión con la investigación académica:** recuperar bibliografía primaria y metadatos de los estudios candidatos antes de agregar referencias al corpus formal.

### Prompt sugerido para reanudar

> Continuemos CyberMarket CR desde `security/cybermarket/CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md`. Lee el cierre C2–C9, `PLAN_MAESTRO_SEGURIDAD_SOFTWARE_CY703.md`, `test_matrix.csv` y el plan C10. Verifica HEAD, PR #1 y CI. Ejecuta W7-A y luego W7-B con checkpoints y evidencias, no redactes el Avance 2 ni alteres Avance 1, no fusiones la rama, distingue pruebas unitarias/integración/SAST/DAST y no declares conformidad por un PASS. 
