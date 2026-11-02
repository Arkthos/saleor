**Actualización de cierre, 2026-11-02:** pruebas actuales finalizadas y verificadas. [Cierre completo](../CIERRE_PRUEBAS_TECNICAS.md); [manifiesto vigente](revalidacion_tecnica/CIERRE_TECNICO.json). El contenido previo conservado abajo describe su fase anterior y será incorporado al reanálisis académico.

# A2-03 — Resultado del análisis estático local

Se ejecutaron herramientas sobre las rutas seleccionadas, conservando código funcional y lockfile. El entorno local se instaló con uv sync --locked. El primer intento no pudo compilar pywatchman por ausencia de clang; repetir con CC=gcc permitió instalar las dependencias sin modificar versiones o archivos del proyecto. Esta adaptación de compilador no convierte el entorno local en réplica exacta de CI.

| Herramienta | Alcance y configuración | Resultado real |
|---|---|---|
| Bandit 1.8.6 | Mismas rutas sensibles del workflow histórico; severidad mínima LOW, confianza mínima MEDIUM; salida JSON | Una alerta B105 LOW/MEDIUM, 4629 líneas analizadas; exit 1 por hallazgo |
| Semgrep 1.153.0 | Reglas locales .semgrep/, cinco reglas Python ejecutadas, 21 archivos escaneados | Cero hallazgos, cero errores; exit 0 |
| Revisión manual | Trece registros de control, datos, fallas e interfaces | Observaciones y recomendaciones acotadas en revision_manual.csv |

Los reportes completos, versión, alcance y hashes están en estatica/. Bandit señala saleor/core/jwt.py:23 por el literal refreshToken. La inspección muestra que es el nombre de una cookie, no una contraseña embebida. Se conserva la alerta y se clasifica como falso positivo respecto a B105; no se la oculta ni se describe el scan como cero hallazgos. La discusión del prefijo de cookie según ASVS es una cuestión distinta y no queda resuelta por descartar B105.

Semgrep no encontró coincidencias con las cinco reglas locales aplicadas. Este resultado no valida toda la semántica de permisos, no reemplaza revisión de arquitectura y no constituye cobertura global del repositorio. No se ejecutó un análisis de composición de dependencias; los rangos o versiones instaladas no se presentan como prueba de ausencia de CVE.

Las herramientas no reportaron automáticamente las diferencias de UUID/legacy ni resuelven la autoridad de P-ORDER-01. La revisión manual y la evidencia dinámica son complementarias. Esta fase concluye el producto estático previsto, no los checks globales ni la revalidación integrada de A2-05.
