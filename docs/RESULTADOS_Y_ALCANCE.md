# Resultados, procedencia y alcance

El cierre técnico del 2 de noviembre está preservado; esta consolidación
organiza su sustento. Los archivos de prueba conservados son idénticos a los
de la fuente `eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7`. Las revisiones
documentales posteriores añadieron análisis y artefactos, sin modificar el
código funcional de Saleor frente a `4cb1609a90eade14b6275a407bc7a00c35698090`.

| Evidencia | Run histórico | Resultado |
|---|---|---|
| General | [41522626061](https://github.com/Arkthos/saleor/actions/runs/41522626061) | 17.613 PASS + 2 XFAIL; sin FAIL/ERROR/SKIP inesperados |
| Focal | [41522626285](https://github.com/Arkthos/saleor/actions/runs/41522626285) | 59 PASS + los mismos 2 XFAIL; 27 IDs / 61 variantes |
| Laboratorio y E2E | [41522626093](https://github.com/Arkthos/saleor/actions/runs/41522626093) | 42 unidades/validadores, 26 C10 y 211 E2E PASS |
| Calidad | [41522626126](https://github.com/Arkthos/saleor/actions/runs/41522626126) | 10 hooks PASS |
| Licencias | [41522626105](https://github.com/Arkthos/saleor/actions/runs/41522626105) | 502 entradas aprobadas por fuente; 6 controles de frontera por fuente |
| Reglas Semgrep | [41522626053](https://github.com/Arkthos/saleor/actions/runs/41522626053) | SUCCESS |
| Changelog | [41522626075](https://github.com/Arkthos/saleor/actions/runs/41522626075) | SUCCESS |

Semgrep 1.153.0 examinó 2.608 archivos, sin hallazgos ni errores bajo sus reglas
y exclusiones. Bandit 1.8.6 examinó 4.629 líneas y emitió **una alerta B105,
LOW/MEDIUM** sobre `refreshToken`: el análisis manual identificó el literal
como nombre de cookie, no contraseña incrustada. Se conserva la alerta y su
interpretación; no se informa como un escaneo sin alertas.

## Qué sustentan los resultados

Los casos ejercitan autenticación, JWT, revocación, CSRF de refresh, consultas
`me`, `user`, `order`, permisos de staff/aplicaciones y límites funcionales de
GraphQL. Incluyen controles positivos y negativos y caracterizaciones
separadas de los contratos. CM-T17/18/19/21 son pruebas directas de funciones;
las 61 variantes focales no son todas integración con base de datos.

Los 42 controles independientes del laboratorio son 30 variantes unitarias
de producto más 12 de validadores. El artefacto focal separado de 36
controles contiene un subconjunto: 30 de producto más seis validadores.
Los seis controles de licencia se repitieron en dos fuentes y no se suman
dos veces. No sumar los resultados focales a los generales.

## Límites que debe explicar la presentación

- C10 usa ASGI y sockets TCP reales sobre `127.0.0.1`, PostgreSQL/Valkey
  desechables, cuentas sintéticas e integraciones desactivadas. No acredita
  un storefront público ni un despliegue productivo.
- HTTPS y Chromium verifican certificados con una CA efímera; no se
  desactiva la validación TLS. Los dos orígenes del navegador difieren por
  puerto en el mismo host: no demuestra cookies de terceros entre sitios.
- Dos alias de base de datos apuntan a la misma base temporal. No prueba
  replicación física ni consistencia de una réplica productiva.
- La confianza en `X-Forwarded-Proto` se caracteriza directamente; no se
  certifica la configuración de un proxy productivo.
- Un UUID conocido de pedido puede actuar como referencia compartida según
  el comportamiento evaluado. No se demostró enumeración de UUID ni acceso
  a datos reales de clientes. Revocar JWT no equivale a revocar ese UUID.
- CM-T22 mantiene dos XFAIL estrictos frente a P-ORDER-01 no aprobada.
  No constituyen una declaración de vulnerabilidad oficial.
- No hay prueba distribuida de carga/estrés, rotación RS256 completa,
  política de audiencia adoptada ni garantía de sesión absoluta/inactiva.
- Los trece dictámenes de riesgo y la conformidad formal ASVS permanecen
  sin adjudicar. Los workflows de publicación/despliegue omitidos no
  acreditan despliegues ni pruebas de carga.

## Dónde están los resultados auditables

La ruta canónica es
`security/cybermarket/academic/avance2/evidencia/revalidacion_tecnica/`.
`raw/final_*` contiene las baterías finales y `raw/licencias_final/` los
derivados públicos de licencias. Las demás carpetas conservan intentos y
correcciones anteriores. `CIERRE_TECNICO.json` diferencia los hashes de los
ZIP originales y de los derivados públicos depurados; no son intercambiables.
Los originales de general/focal/licencias que no se publicaron permanecen
referenciados en el manifiesto de conservación privada.

La verificación actual comprueba la evidencia disponible en el árbol y la
fuente fijada; no descarga ni afirma haber comprobado originales privados
ausentes. Las fechas, estados y URLs de las notas históricas pertenecen a
sus instantáneas. El documento académico y su revisión grupal son una
entrega independiente.
