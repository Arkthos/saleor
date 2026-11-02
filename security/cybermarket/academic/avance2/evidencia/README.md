# Conservación de evidencia del segundo avance

Esta carpeta empieza como guía. **Todavía no contiene resultados nuevos, una ejecución C10 ni una nueva adjudicación ASVS.**

Durante A2-01–07 guardar los productos descritos en el roadmap. Cada ejecución se archivará en una subcarpeta identificada por fecha y run, con manifest.json, configuración depurada, resultados, resumen por caso y SHA256SUMS. No crear archivos de resultados vacíos que parezcan ejecuciones realizadas.

Campos mínimos del manifiesto: evidence_id, stage_id, collected_at_utc, product_baseline_sha, tested_branch_sha, checkout_sha, run_url, tool_versions, configuration_ref, case_inventory_ref, outcome_counts, files y limitations. Cada archivo incluirá ruta, tamaño y SHA-256. El esquema debe adaptarse explícitamente si una fuente histórica no aporta un campo.

Reglas de interpretación:

- Registrar los estados reales, incluyendo cancelación, error, SKIP, XFAIL y bloqueo.
- Separar contratos, caracterización y políticas propuestas.
- Distinguir conteos de IDs, variantes, requisitos y riesgos; no sumar suites solapadas.
- No confundir nivel de prueba con conocimiento de caja negra/blanca/gris.
- Una alerta SAST requiere revisión y puede ser falso positivo; un PASS no adjudica todo un requisito.
- Conservar solicitudes/respuestas depuradas cuando aporten evidencia, sin tokens, cookies, contraseñas ni datos reales.
- Identificar qué se revisó de forma independiente y qué se tomó de un informe anterior.

La bitácora debe permitir reconstruir el razonamiento además del comando ejecutado. Si un resultado cambia, conservar el anterior y explicar cambio de código, entorno, oráculo o interpretación.
