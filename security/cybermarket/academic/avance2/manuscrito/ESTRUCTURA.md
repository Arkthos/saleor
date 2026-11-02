# Estructura propuesta del segundo avance

**Estado:** arquitectura del documento; no es un borrador redactado ni contiene resultados nuevos. Mantener IEEE y producir una copia nueva. No hay un límite de páginas indicado en la consigna recibida.

| Sección propuesta | Función y contenido | Base que se reutiliza | Criterios |
|---|---|---|---|
| Título, autores, resumen y palabras clave | Identificar entrega y alcance; ajustar resumen a lo realmente completado | Título y alcance del avance 1; revisar requisito de resumen del manual | O4, R6 |
| I. Continuidad y alcance | Relación con primer avance; ausencia de feedback recibido; versiones, objetivos y límites | AJUSTES_AVANCE1 y línea base | R1, O1 |
| II. Metodología de desarrollo y verificación | Unidades, instrumentos, configuración, selección y reglas de interpretación | I01–I07, matriz derivada, manifiestos | M1, R3, R4 |
| III. Codificación segura | Prácticas aplicadas, componentes, evidencia, límites y recomendaciones | Revisión de código, fuentes y análisis A2-03 | R2, O3 |
| IV. Análisis estático y dinámico | Métodos/herramientas por separado; resultados, triage, cobertura y limitaciones | A2-03, A2-05, decisión A2-06 | R3, O3 |
| V. Pruebas de seguridad | Casos y oráculos; actores y recursos; resultados reconciliados y muestra detallada de fichas | Plan, JUnit/JSON, fichas y matriz | R4, O3 |
| VI. Hallazgos y recomendaciones | Diez o más entradas sustantivas, síntesis por tema, tratamiento y retest | Catálogo A2-Hxx con vínculo H/R/norma/caso | O2, M1 |
| VII. Discusión y límites | Qué responde a objetivos, qué queda sin determinar, efecto de CI/despliegue/política | Análisis A2-07 y validez | M1, R6 |
| VIII. Cierre del avance y siguiente fase | Balance acotado y continuidad; no afirmar mantenimiento/despliegue realizados | Resultados y roadmap | R6 |
| Referencias | IEEE, fuentes realmente citadas y verificadas | Bibliografía vigente y nuevas fuentes pertinentes | R5 |
| Anexos | Fichas completas, matrices, detalles reproducibles y revisión de rúbrica | Productos propios y evidencia depurada | R3–R5 |

La numeración es propuesta y se ajustará al ensamblar la nueva entrega. No se renumeran retrospectivamente las secciones del Word ya presentado. Si se exige entregar un documento acumulativo, integrar la primera parte como copia preservada y documentar los cambios en la versión nueva.

Tablas recomendadas: línea base, prácticas de codificación, alcance por herramienta, clasificación de pruebas, resumen de resultados y catálogo de hallazgos. Figuras solo cuando aclaren arquitectura o flujo de evidencia. El cuerpo del PDF debe explicar los resultados principales sin depender de abrir enlaces de GitHub.

Defensa prevista: explicar la diferencia entre autenticación y autorización; un contrato y una caracterización; unidad e integración; CI y navegador; un hallazgo sustentado y una hipótesis; y por qué una política provisional no prueba una vulnerabilidad oficial.
