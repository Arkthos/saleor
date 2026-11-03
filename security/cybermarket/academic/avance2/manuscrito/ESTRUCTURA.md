# Estructura propuesta del segundo avance

**Estado:** estructura de la continuación acumulativa del primer avance, aclarada el 2026-11-03. Mantener el documento base y IEEE; conservar la instantánea presentada. Este esquema no es un manuscrito nuevo ni una edición ya aplicada. No hay un límite de páginas indicado en la consigna recibida.

| Sección propuesta | Función y contenido | Base que se reutiliza | Criterios |
|---|---|---|---|
| Título, autores, resumen y palabras clave | Identificar entrega y alcance; ajustar resumen a lo realmente completado | Título y alcance del avance 1; revisar requisito de resumen del manual | O4, R6 |
| I. Planteamiento y fundamentos de la investigación | Conservar introducción, problema, justificación, pregunta, objetivos, antecedentes y fundamentos; actualizar el marco temporal y conectar con la segunda etapa | Primer avance presentado y revisión de continuidad | R1, O1 |
| II. Marco metodológico desarrollado | Ampliar la sección existente con método realmente aplicado, actores, instrumentos I01-I07, entorno, herramientas/versiones, selección y oráculos | Marco metodológico del primer avance, matrices y manifiestos | M1, R3, R4 |
| III. Codificación segura | Prácticas aplicadas, componentes, evidencia, límites y recomendaciones | Revisión de código, fuentes y análisis A2-03 | R2, O3 |
| IV. Análisis estático y dinámico | Métodos/herramientas por separado; resultados, triage, cobertura y limitaciones | A2-03, A2-05, decisión A2-06 | R3, O3 |
| V. Pruebas de seguridad | Casos y oráculos; actores y recursos; resultados reconciliados y muestra detallada de fichas | Plan, JUnit/JSON, fichas y matriz | R4, O3 |
| VI. Hallazgos y recomendaciones | Diez o más entradas sustantivas, síntesis por tema, tratamiento y retest | Catálogo A2-Hxx con vínculo H/R/norma/caso | O2, M1 |
| VII. Discusión y límites | Qué responde a objetivos, qué queda sin determinar, efecto de CI/despliegue/política | Análisis A2-07 y validez | M1, R6 |
| VIII. Cierre del avance y siguiente fase | Balance acotado y continuidad; no afirmar mantenimiento/despliegue realizados | Resultados y roadmap | R6 |
| Referencias | IEEE, fuentes realmente citadas y verificadas | Bibliografía vigente y nuevas fuentes pertinentes | R5 |
| Anexos | Fichas completas, matrices, detalles reproducibles y revisión de rúbrica | Productos propios y evidencia depurada | R3–R5 |

La numeración se ajustará en el documento acumulativo. Se conserva la instantánea del Word presentado y se documentan los cambios de su continuación. La entrega acumulativa es una instrucción explícita, no una condición pendiente. Los bloques III-V desarrollan la rúbrica apoyándose en la arquitectura y los principios ya escritos; no duplican el marco teórico. Los anexos A-C se conservan y actualizan con verificaciones, límites y llamadas a la evidencia nueva.

Tablas recomendadas: línea base, prácticas de codificación, alcance por herramienta, clasificación de pruebas, resumen de resultados y catálogo de hallazgos. Figuras solo cuando aclaren arquitectura o flujo de evidencia. El cuerpo del PDF debe explicar los resultados principales sin depender de abrir enlaces de GitHub.

Defensa prevista: explicar la diferencia entre autenticación y autorización; un contrato y una caracterización; unidad e integración; CI y navegador; un hallazgo sustentado y una hipótesis; y por qué una política provisional no prueba una vulnerabilidad oficial.
