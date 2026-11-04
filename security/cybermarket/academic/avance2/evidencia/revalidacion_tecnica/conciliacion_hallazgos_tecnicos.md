# Conciliación técnica de observaciones

**Estado:** insumo de trabajo para A2-07. El manuscrito y el PDF/Word siguen pausados. Este registro vincula las pruebas nuevas con las catorce observaciones previas, conservando cada límite. [Matriz completa](conciliacion_hallazgos_tecnicos.csv).

La evidencia nueva cambia especialmente A2-H05/H06/H07/H09/H10: ya existen revocación por HTTP, HTTPS y Chromium, permisos delegados ejercitados y flujo legítimo de UUID por la API. Las afirmaciones anteriores de ausencia de estas pruebas necesitan actualizarse en el posterior reanálisis académico. El control de cookies cubre dos orígenes en un mismo host; la variante posterior a revocación comprueba que el ID del pedido resuelve, sin extender esa aserción automáticamente a todos sus campos.

A2-H03/H11/H12/H13/H14 conservan límites sustantivos: código de error no equivale a tiempo uniforme; límites funcionales no son carga/estrés; un diagnóstico writer no es una prueba de la captura get_user; aud conservada no demuestra validación de receptor; caducidad/revocación no fijan vida absoluta de negocio. Que una recomendación permanezca propuesta no autoriza describirla como mitigación aplicada.

Los 13 riesgos formales y los 23 ASVS mantienen sus dictámenes no adjudicados; la matriz no cambia la autoridad de esos criterios ni atribuye a OWASP un mapping oficial nuevo. Las dos XFAIL siguen vinculadas solo a la política P-ORDER-01 provisional. Las catorce observaciones continúan siendo controles, caracterizaciones y brechas diferenciadas, sin convertirse en catorce vulnerabilidades. El control heredado de licencias se conserva como evidencia de calidad y trazabilidad, sin inflar esa cuenta.
