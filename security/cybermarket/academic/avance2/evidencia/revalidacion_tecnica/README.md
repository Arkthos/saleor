# Revalidación técnica actual

Esta carpeta conserva resultados y errores de la fase técnica reabierta el 2 de noviembre de 2026. El estado vigente está en `../../estado.json`; los documentos con nombres de intento/preflight conservan su fecha y no reemplazan al último retest. Los PDF/Word anteriores siguen pausados y no incorporan todavía estos resultados.

## Fuente y procedencia

Fuente del retest: `f1f883d545b44cdd8699a33b3162b7d2486c080b`; checkout PR: `daf9178add04f18c148b84953a32159413e43ea5`. Los commits posteriores solo de evidencia no adquieren el CI del origen probado. PostgreSQL y Valkey tienen sus digests en el ZIP. Python/dependencias/lockfile quedan en environment.json.

## Resultados revisados

| Evidencia | Resultado | Localizador |
|---|---|---|
| Integración focal | 59 PASS, 2 XFAIL previstos | retest_04_summary.json |
| Unidades y validadores independientes | 42 PASS: 30 unidades, 12 validadores | retest_04_summary.json |
| C10 real HTTP/HTTPS/Chromium | 26 PASS, sin errores de cierre | retest_04_summary.json |
| E2E original | 211 PASS | e2e_41517858406_summary.json |
| Estática | Semgrep 2.607 archivos, 0 hallazgos/errores; Bandit B105 cookie-name revisado | estatica_retest_04.json |
| Linters | Diez hooks PASS; job SUCCESS | linters_retest_04.json |
| Regresión general | PENDIENTE de conciliación | run 41517858482 |
| Control heredado de licencias | FAILED_REVIEW_REQUIRED, mismo rechazo en base/HEAD y error stdin | licencias_resultado.json |

La suite focal es subconjunto de la general; no sumar ambos conteos. PASS de caracterización no es cumplimiento normativo ni aprobación de P-ORDER-01.

## Intentos preservados

1. Intento 01: Playwright no soportaba Ubuntu 26.04; no se ejecutó C10. Se fijó Ubuntu 24.04.
2. Intento 02: 1 PASS / 24 FAIL; alias DB de los hilos ASGI apuntaba a la base sin esquema. Semgrep encontró 48 ejemplos deliberados de `.semgrep`. Se preservan y corrigen ambos alcances.
3. Intento 03: 23 PASS / 2 FAIL; se completó el contrato de coste GraphQL y se comparó el perfil middleware normal frente al diagnóstico exclusivo de pruebas.
4. Retest 04: 26 PASS, incluido diagnóstico explícito del writer estricto. Ningún cambio funcional al producto ni relajación de política para obtener PASS.

## Límites relevantes

- Datos sintéticos, servicios efímeros, integraciones desactivadas, sockets loopback y TLS verificado; no hay escaneo de servicios ajenos.
- Los dos orígenes Chromium difieren en puerto y comparten host: validan CORS entre orígenes, no políticas de cookies de terceros entre sitios distintos. Se comprueban los atributos Secure/HttpOnly/SameSite y los positivos/negativos CSRF del laboratorio.
- LIVE-07 recorre la API del propietario y comparte el UUID obtenido legítimamente; no existe storefront externo probado, adivinación de UUID ni datos reales.
- Ambos alias DB comparten la base desechable: no se prueba replicación física. El forwarded-proto directo caracteriza una frontera de confianza; no certifica un proxy de producción.
- No se prueba carga/estrés distribuido ni se afirma ausencia de vulnerabilidades por resultados de SAST. Los dictámenes formales y P-ORDER-01 permanecen sin adjudicar.
- Los archivos ZIP originales archivados contienen evidencia ya depurada por CI. Sus bytes y SHA-256 se conservan; no se normaliza su whitespace.
