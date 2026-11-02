# Segundo avance — archivo de trabajo académico

**Estado:** VALIDACIÓN TÉCNICA EN EJECUCIÓN. Generación de entregable pausada hasta cerrar VT-01–VT-06. Los informes previos son fotografías del alcance anterior. Consultar [ROADMAP.md](ROADMAP.md) y [estado.json](estado.json).

## Accesos principales

- [Roadmap detallado](ROADMAP.md): fases, actividades, dependencias, productos y criterios de cierre.
- [Matriz de rúbrica](MATRIZ_RUBRICA.csv): seis criterios evaluados y obligaciones adicionales.
- [Ajustes respecto del primer avance](AJUSTES_AVANCE1.md).
- [Bitácora](BITACORA.md): avances y reanudación.
- [Fuentes, permisos y evidencia](FUENTES_Y_EVIDENCIAS.md).
- [Estructura del manuscrito](manuscrito/ESTRUCTURA.md).
- [Guía de conservación de resultados](evidencia/README.md).
- [Ficha de prueba](plantillas/FICHA_PRUEBA.md) y [registro vacío de hallazgos](plantillas/HALLAZGOS.csv).
- [Contexto del curso](antecedentes/Contexto_Curricular_CY703_2026-11-02.md) y [revisión histórica](antecedentes/Revision_Checkpoint_CyberMarket_2026-11-02.md).

El proyecto usa IEEE. La primera entrega permanece intacta. Los informes del 2 de noviembre en antecedentes fueron cerrados antes de recibir la consigna específica; sus referencias a la ausencia de esa consigna son históricas.

## Qué guardar aquí durante el desarrollo

Guardar versiones de borradores propios, tablas, diagramas editables, decisiones metodológicas, localizadores bibliográficos, revisiones, matrices de resultados, recomendaciones, anexos y auditorías. Cada producto llevará etapa, estado y evidencia de revisión. GitHub conserva los cambios; el chat puede contener la conversación de elaboración.

No publicar por defecto los PDF docentes/libros originales ni Word con datos personales. No subir tokens, cookies, contraseñas, datos reales o trazas sin depurar. Para originales externos bastan inventario, referencia, enlace autorizado y hash, conforme a FUENTES_Y_EVIDENCIAS.md.

## Cierre de una etapa

Guardar productos, comprobar criterios, actualizar roadmap/estado/matriz/bitácora, publicar el commit y actualizar la copia del roadmap en el proyecto. Si se interrumpe, registrar estado parcial. Las reglas persistentes están en [AGENTS.md](../../../../AGENTS.md) y en [la decisión documental](../../../../docs/adr/0011-cybermarket-academic-evidence-and-roadmap.md).

No se usa un issue tracker para estas actividades. Este archivo es el índice de productos académicos, no una nueva cola de incidencias.

## Productos para revisión

- [Informe completo en Markdown](manuscrito/INFORME_AVANCE2.md).
- [PDF público de revisión](manuscrito/entrega/CyberMarket_Segundo_Avance_publico.pdf).
- [Auditoría de rúbrica y evidencia](manuscrito/auditoria_final.md).
- [Guía de defensa](manuscrito/GUIA_DEFENSA.md).
- [Archivos privados e instrucciones de entrega](manuscrito/entrega/INSTRUCCIONES_ENTREGA.md).
- [Versión y hashes](manuscrito/entrega/manifest.json).

## Revalidación técnica en curso

[Laboratorio C10 y ejecución](../../live/README.md), [preflight real](evidencia/revalidacion_tecnica/preflight.json). Actions reactivado. Último laboratorio revisado: run 41515853470, 23 PASS/2 FAIL; [intento 03](evidencia/revalidacion_tecnica/intento_03_summary.json) y ZIP conservados. Correcciones y diagnóstico adicional preparados; 26 variantes pendientes de retest. E2E de ese run SUCCESS; regresión y linters por comprobar.

[Control heredado de licencias](evidencia/revalidacion_tecnica/licencias_setup.json): corrección de compatibilidad upstream fijada por SHA; resultado pendiente.

**C10 revisado:** [26 PASS](evidencia/revalidacion_tecnica/retest_04_summary.json), run 41517858406; [SAST actual](evidencia/revalidacion_tecnica/estatica_retest_04.json). VT-02/06 pendientes. [Licencias heredadas](evidencia/revalidacion_tecnica/licencias_resultado.json) requieren revisión.
