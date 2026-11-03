# Segundo avance — archivo de trabajo académico

**Estado:** PRUEBAS FINALIZADAS EN ALCANCE PLANIFICADO. [Cierre técnico](CIERRE_PRUEBAS_TECNICAS.md) y [evidencia final](evidencia/revalidacion_tecnica/CIERRE_TECNICO.json). Siguiente: reanálisis A2-07 e incorporación al texto académico. Los PDF/Word previos conservan el alcance anterior; no se generó otro entregable.

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

- [Borrador auxiliar previo en Markdown](manuscrito/INFORME_AVANCE2.md).
- [PDF auxiliar previo de revisión](manuscrito/entrega/CyberMarket_Segundo_Avance_publico.pdf).
- [Auditoría de rúbrica y evidencia](manuscrito/auditoria_final.md).
- [Guía de defensa](manuscrito/GUIA_DEFENSA.md).
- [Archivos privados e instrucciones de entrega](manuscrito/entrega/INSTRUCCIONES_ENTREGA.md).
- [Versión y hashes](manuscrito/entrega/manifest.json).

## Revalidación técnica en curso

[Laboratorio C10 y ejecución](../../live/README.md), [preflight real](evidencia/revalidacion_tecnica/preflight.json). Actions reactivado. Último laboratorio revisado: run 41515853470, 23 PASS/2 FAIL; [intento 03](evidencia/revalidacion_tecnica/intento_03_summary.json) y ZIP conservados. Correcciones y diagnóstico adicional preparados; 26 variantes pendientes de retest. E2E de ese run SUCCESS; regresión y linters por comprobar.

[Control heredado de licencias](evidencia/revalidacion_tecnica/licencias_setup.json): corrección de compatibilidad upstream fijada por SHA; resultado pendiente.

**C10 revisado:** [26 PASS](evidencia/revalidacion_tecnica/retest_04_summary.json), run 41517858406; [SAST actual](evidencia/revalidacion_tecnica/estatica_retest_04.json). VT-02/06 pendientes. [Licencias heredadas](evidencia/revalidacion_tecnica/licencias_resultado.json) requieren revisión.

**VT-02 completada:** [Linters y diez hooks aprobados](evidencia/revalidacion_tecnica/linters_retest_04.json); [E2E actual 211 PASS](evidencia/revalidacion_tecnica/e2e_41517858406_summary.json). VT-06 espera regresión general.

**VT-06 completada:** [Regresión general 17.613 PASS/2 XFAIL](evidencia/revalidacion_tecnica/general_41517858482_summary.json), sin fallos inesperados. VT-07 prueba selección declarada Artistic acotada al wheel fijado y conserva la denegación GPL.

VT-07 corrigió sys.path de la colección aislada; el primer run 41521406564 se conserva como intento sin análisis del SBOM.

**VT-07 completada:** [Licencias y negativo GPL verificados](evidencia/revalidacion_tecnica/licencias_retest_02_summary.json). Todos los bloques previstos tienen evidencia; resta conciliación final de calidad actual.

El control de revisión de licencias de contribuciones externas se conserva; la identidad del repositorio distingue las ramas internas de este fork, sin añadir etiquetas ni aprobar en nombre de otra persona.

## Cierre técnico vigente

**2026-11-02 — CIERRE TÉCNICO COMPLETADO:** última fuente eb5d3ecb, checkout 90455ca8; todos los workflows de pruebas/calidad seleccionados SUCCESS. XML, JSON y SHA-256 reconciliados: general 17.613 PASS/2 XFAIL; focal 59 PASS/2 XFAIL; independientes 42 PASS; C10 26 PASS; E2E 211 PASS; seis fronteras de licencias y 502 entradas aprobadas por fuente, negativo GPL vigente; diez hooks PASS. Cero fallos inesperados o bloqueos de pruebas. Artefactos completos conservados y derivadas públicas depuradas; fallos iniciales visibles. Los dos XFAIL de política provisional y límites ASVS permanecen explícitos. Roadmap, estado, matriz, bitácora y copia del proyecto conciliados. Siguiente: A2-07. Sin nuevo PDF/Word ni merge/campus.

## Documento acumulativo

Por aclaración del usuario del 2026-11-03, la segunda entrega continúa el Word del primer avance. [Revisión del contenido y cambios propuestos](REVISION_CONTINUIDAD_AVANCE1.md). Pregunta y objetivos se conservan; se actualizan los estados de evidencia y se desarrolla el método existente. Los borradores independientes previos y sus auditorías son material auxiliar, no la continuación definitiva. El original no se ha modificado.
