# Cierre de la fase de pruebas — CyberMarket CR / Saleor

**Estado: COMPLETADA EN EL ALCANCE PLANIFICADO. Fecha: 2 de noviembre de 2026.** La última ejecución de todas las suites y controles seleccionados terminó sin fallos inesperados. No hay pruebas pendientes de esa batería ni ejecuciones activas de su ciclo final. No se generó un nuevo PDF/Word académico.

Fuente de pruebas: `eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7`. Checkout de integración de Actions: `90455ca8abb7d72f707e0137e3ac80fab7a06dec`. Producto base: `4cb1609a90eade14b6275a407bc7a00c35698090`. Comparación de 135 archivos modificados en el fork: **ningún archivo funcional de saleor/ modificado**; sus cambios son pruebas. Los commits documentales de cierre posteriores no adquieren el CI de ese SHA.

## Resultados finales comprobados

| Familia | Resultado | Evidencia |
|---|---|---|
| Regresión general | 17.613 PASS, 2 XFAIL; 0 FAIL/ERROR/SKIP inesperado | [Tests 41522626061](https://github.com/Arkthos/saleor/actions/runs/41522626061) |
| Focal CyberMarket | 59 PASS, 2 XFAIL; 27 IDs y 61 variantes | [Contratos 41522626285](https://github.com/Arkthos/saleor/actions/runs/41522626285) |
| Unidades y validadores independientes | 42 PASS: 30 de producto y 12 del sistema de evidencia | [Laboratorio 41522626093](https://github.com/Arkthos/saleor/actions/runs/41522626093) |
| HTTP/HTTPS/Chromium C10 | 26 PASS; positivos, negativos y teardown aprobados | Mismo laboratorio |
| E2E original | 211 PASS, sin fallos ni omisiones | Mismo workflow, job independiente |
| Frontera de selección de licencias | 6 PASS; repetidas en base/HEAD, se cuentan una vez | [Licencias 41522626105](https://github.com/Arkthos/saleor/actions/runs/41522626105) |
| Entradas de licencia analizadas | 502 aprobadas y 0 rechazadas por fuente; negativo GPL ajeno denegado | Mismo workflow |
| Pre-commit / linters | Diez hooks aprobados | [Linters 41522626126](https://github.com/Arkthos/saleor/actions/runs/41522626126) |
| Reglas Semgrep y changelog | SUCCESS | Runs 41522626053 / 41522626075 |

La suite focal es un subconjunto de la general. El archivo unitario del workflow focal tiene 36 resultados: 30 unidades de producto más seis validadores raíz; también es subconjunto de las 42 del laboratorio. No se suman esos conjuntos como pruebas adicionales. El XML general contiene 17.615 casos, incluidos los dos XFAIL; su duración observada en ese runner fue 690,35 s, sin interpretación como rendimiento de producción.

Los dos XFAIL estrictos pertenecen solo a CM-T22: política CyberMarket P-ORDER-01 provisional y no aprobada sobre correo de pedidos con UUID conocido. Se mantienen visibles. No se atribuye a Saleor una vulnerabilidad oficial ni se convierten en PASS por omitirlos. El validador ejecutado sobre la evidencia final confirmó 27 IDs y 61 ejecuciones; JSON, XML y hashes coinciden.

## Análisis estático y calidad

Bandit 1.8.6 revisó 4.629 líneas del alcance de autenticación, JWT, mutaciones y pedidos: un hallazgo B105 de severidad LOW/confianza MEDIUM, en saleor/core/jwt.py:23. El literal refreshToken es el nombre de la cookie; la revisión lo clasifica como falso positivo de contraseña incrustada. La alerta y el exit code original permanecen archivados.

Semgrep 1.153.0 revisó 2.608 archivos: cero hallazgos y cero errores con las reglas del repositorio y sus ignores. Los ejemplos deliberados de .semgrep se excluyen como en pre-commit; el harness y las herramientas también pasaron sus comprobaciones. Este resultado no demuestra ausencia de todas las vulnerabilidades.

Los diez hooks aprobados son whitespace, EOF, Ruff, formato, mypy, deptry, Semgrep, uv-lock, migraciones pendientes y esquema GraphQL. Los workflows de publicación/despliegue quedaron SKIPPED; no se presentan como ensayos ejecutados ni como evidencia de carga.

## Matriz dinámica C10 ejecutada

Las peticiones usan sockets TCP ASGI reales de Saleor. PostgreSQL 15 y Valkey 8.1 son efímeros; los digests, versiones Python/dependencias y hash del lockfile están en el [manifiesto de cierre](evidencia/revalidacion_tecnica/CIERRE_TECNICO.json) y en environment.json del ZIP. Datos sintéticos, plugins desactivados, correo en memoria, HTTP acotado a loopback y verificación TLS activa.

| ID | Variantes aprobadas | Comprobación y límite |
|---|---|---|
| LIVE-01 | 1 | Salud, GraphQL válido con coste exacto y JSON malformado |
| LIVE-02 | 3 | UUID: propietario/ajeno/anónimo, tres campos con valores literales |
| LIVE-03 | 3 | Legacy: mismos actores/campos, máscaras exactas y control de propietario |
| LIVE-04 | 4 | IDs ausentes, tipo equivocado y formato inválido: sin pedido ni cambios |
| LIVE-05 | 8 + 1 diagnóstico | Cliente/staff/app/delegación y permisos; guard writer exclusivo de pruebas conservado aparte |
| LIVE-06 | 3 HTTPS + 1 cabeceras + 1 Chromium | Cookie/CSRF válido-ausente-inválido, CORS, forwarded-proto y navegador con CA confiable |
| LIVE-07 | 1 | UUID obtenido por API legítima, lista de otro usuario, compartición y revocación |

El detalle de las 26 variantes y su clase observada está en el manifiesto. Los errores de autorización se comprueban por código, mensaje, path, ausencia de datos y conteos de entidades según el caso. Las máscaras esperadas son literales independientes. El flujo posterior a revocación prueba que el ID de pedido sigue resolviendo; no se extrapola esa aserción a todos sus campos después de revocar.

HTTPS emplea una CA/certificado desechables con SAN válido. Chromium usa confianza NSS temporal y no ignora errores de certificado. Se verifican Secure/HttpOnly/SameSite, invisibilidad para JavaScript, CSRF y CORS entre dos orígenes por puerto. Startup/shutdown tienen límites; las aserciones de puertos cerrados, retiro de CA y pasos de eliminación de servicios concluyeron sin errores.

## Correcciones y contraevidencia preservadas

1. Setup inicial: Playwright 1.56.0 no soportaba Ubuntu 26.04; C10 no llegó a ejecutarse. Se fijó Ubuntu 24.04.
2. Intento 02: 1 PASS/24 FAIL por alias DB de hilos ASGI apuntando a una base sin esquema. Ambos alias reales se enlazaron a la DB de pytest antes de servir y se restauran al cerrar.
3. Primer Semgrep ampliado: 48 ejemplos de los archivos de prueba de reglas; salida conservada y alcance corregido.
4. Intento 03: 23 PASS/2 FAIL. Se completó el contrato de coste GraphQL y se distinguió middleware normal del producto del guard SQL exclusivo de tests. Se preservó ese diagnóstico en un caso independiente; no se parcheó la autorización funcional.
5. Pre-commit: se corrigieron llamadas HTTP directas con un cliente Session acotado y TLS verificado. Los bytes de evidencia inmutable se excluyen únicamente de reescrituras whitespace/EOF; el código permanece bajo análisis.
6. Licencias: se corrigieron la instalación antigua del analizador, el import path de la colección aislada y la lectura espuria de stdin. El SBOM original y sus rechazos se conservan junto al retest.

## Control de licencias y revisión externa

La selección Artistic-1.0-Perl se aplica solo a text-unidecode 1.3, con el hash exacto del wheel del lockfile y declaración de alternativa presente. Se registra la declaración del autor, el antes/después y los hashes de ambos SBOM. Otra versión, hash incorrecto o metadatos solo GPL fallan y requieren revisión. Los demás componentes permanecen intactos.

Las reglas allow-lgpl, deny-gpl y deny-proprietary siguen activas. Un SBOM sintético GPL ajeno debe ser rechazado y el reporte debe atribuirlo exactamente a deny-gpl; ese negativo aprobó. Grant analiza una sola entrada stdin explícita, sin el error adicional de lectura vacía. Resultado base y HEAD: 502 entradas aprobadas por fuente, seis pruebas de límites aprobadas por fuente.

Se conserva la revisión de mantenedor para contribuciones de otro repositorio. Este PR tiene head y base Arkthos/saleor: el paso de etiqueta externa quedó SKIPPED por identidad interna, aunque repo.fork sea verdadero. No se añadió Licenses Reviewed ni se atribuyó revisión humana inexistente. Es una verificación técnica acotada, sin dictamen jurídico global.

## Conservación, alcance y siguiente paso

[CIERRE_TECNICO.json](evidencia/revalidacion_tecnica/CIERRE_TECNICO.json) conserva resultados, SHA fuente/checkout, runs/jobs, versiones, checksums, variantes y límites. Los ZIP públicos de regresión, evidencia focal y licencias son derivadas depuradas; se verificaron los hashes originales de GitHub y los SHA256SUMS existentes. El artefacto general no trae manifiesto interno: su hash de archivo se verifica y la derivada incorpora uno nuevo. Los originales con etiquetas de correo sintético y metadatos de autores del SBOM se conservan separados, con identidad y versión en [ARCHIVO_ORIGINALES_FINAL.json](evidencia/revalidacion_tecnica/ARCHIVO_ORIGINALES_FINAL.json). No se confunden sus hashes con los de las derivadas.

El laboratorio no cubre un storefront público, cookies de terceros entre sitios distintos, replicación física, confianza de un proxy de producción o carga/estrés distribuido. Las ramas RS256/rotación, contratos de audiencia y políticas de vida absoluta/inactividad mantienen sus límites de alcance; no se inventan requisitos adoptados. Los dictámenes formales de los riesgos y ASVS siguen sin adjudicar. La ejecución aprobada de caracterizaciones no equivale a conformidad normativa general.

**Siguiente etapa: A2-07, incorporar e interpretar la nueva evidencia en los hallazgos y el texto académico.** Los PDF/Word previos son fotografías del alcance anterior. Esta sesión cierra las pruebas y sus registros; el PR permanece en borrador, sin merge, publicación pública o carga al campus.
