# CyberMarket CR — revisión de ingeniería de software y aseguramiento de pruebas C2–C9

**Fecha:** 2026-10-18. **Estado:** revisión técnica documentada; cierre de ejecución experimental verificado sobre SHA `63cadee4e9a1b43bfc07103aecbfeb61fbc33112`. **No equivale a certificación de seguridad ni a cierre de requisitos de negocio.**

## 1. Dictamen ejecutivo

La implementación experimental cuenta con resultados reproducibles, instrumentación JUnit y un mecanismo de reconciliación de cobertura por caso. La evidencia respalda **27 IDs / 61 invocaciones: 59 PASS y 2 XFAIL previstos**, sin FAIL/ERROR/SKIP en la ejecución focalizada [39144885995](https://github.com/Arkthos/saleor/actions/runs/39144885995). La suite general [39144885841](https://github.com/Arkthos/saleor/actions/runs/39144885841) reportó **17.613 PASS y 2 XFAIL**, sin fallos inesperados; las invocaciones focalizadas forman parte del total general. Linters, E2E y changelog finalizaron SUCCESS sobre el mismo SHA.

**Juicio de aseguramiento:** ejecución y trazabilidad **verificadas para el conjunto ensayado**; **conformidad normativa, cobertura de amenazas completa, privacidad contractual y riesgo residual: no determinados**. El número de pruebas aprobadas no equivale a porcentaje de cobertura funcional o de ASVS. La evidencia no demuestra un ataque real ni una vulnerabilidad explotable.

## 2. Método, fuentes y límites de la revisión

Se contrastaron: `test_matrix.csv` (27 filas), `build_coverage.py`, `summarize_junit.py`, workflow `cybermarket-security.yaml`, `test_cybermarket_security_contracts.py`, `test_cybermarket_security_c9.py`, `C9_closure_matrix.md`, `POLICY_ORDER_P01_PROVISIONAL.md`, el expediente C9 y las referencias a artefactos CI. Esta revisión **no supone inspección línea a línea de todos los archivos de pruebas adicionales C4–C8**, ni una nueva ejecución local, ni inspección de infraestructura desplegada. Por ello, los veredictos por caso se limitan a los oráculos y resultados descritos en la matriz y expedientes; las garantías sobre lógica no inspeccionada requieren auditoría específica. La revisión no cambia la versión base Saleor `4cb1609a90eade14b6275a407bc7a00c35698090`.

**Procedencia:** tested branch SHA `63cadee4e9a1b43bfc07103aecbfeb61fbc33112`, checkout/merge SHA `98645a24a56e9764e48fdefeea6b2e9a4095ad4a`. Artefactos focal JUnit ID `12142029921` SHA256 ZIP `b8c38641cab220debac6c0d806b74141016f1baa0ad109caeb02647f0ac5412e`; Bandit ID `12143311107` SHA256 ZIP `de680b13d3b1fc5ddd35970d8e999f97c4d65fffea4fda802515ede9c4b8e37f`; general JUnit ID `12143532461` SHA256 ZIP `809f7933869efe42bd1114e6a44d1d55f1c6df66b3d0560c31f55f8d17aae54a`. Los artefactos originales son de retención limitada; el reporte preserva sus identificadores/hashes, no los bytes.

## 3. Calidad de la ingeniería de pruebas

### Fortalezas verificadas

1. **Aislamiento y reproducibilidad:** fixtures sintéticas, dependencias bloqueadas mediante `uv sync --locked`, servicios PostgreSQL/Valkey y workflows con acciones fijadas a SHA. No se ensayan usuarios de producción.
2. **Oráculos diferenciados:** contratos `security_contract`, caracterizaciones `characterization_only` y política provisional `proposed_policy_expected_fail`; XFAIL estricto permite detectar XPASS como evento inesperado.
3. **Comparación de actores:** los casos de orden distinguen propietario, cliente no relacionado y anónimo. C9 parametriza independientemente tres campos por actor y evita ocultar diferencias bajo una sola aserción.
4. **Trazabilidad:** cada caso registra metadatos no sensibles en propiedades JUnit; `summarize_junit.py` normaliza PASS/FAIL/ERROR/SKIP/XFAIL; `build_coverage.py` detecta IDs ausentes, duplicados y deriva de tipo de evidencia.
5. **Integridad:** JUnit, resumen, cobertura y SAST cuentan con SHA256SUMS; la cadena de procedencia incluye SHA de código, ejecución y artefactos.
6. **Separación de hallazgo y juicio:** no se convierte automáticamente un PASS de caracterización en conformidad, ni un XFAIL provisional en vulnerabilidad.

### Riesgos de diseño y mejoras justificadas

| ID | Observación del harness | Consecuencia | Acción recomendada |
| --- | --- | --- | --- |
| QA-01 | `build_coverage.py` clasifica todo contrato con PASS como `CONTRACT_PASSED_REVIEW_PENDING` y todos los riesgos como `NO_DETERMINADO` | La matriz conserva REVIEW_PENDING aunque la ejecución esté completa; no existe capa de evaluación normativa aprobada | Separar ejecución, adecuación del oráculo, aplicabilidad normativa y decisión del riesgo en registro de revisión humana; no convertir automáticamente en CONFORMANT |
| QA-02 | La validación ASVS/WSTG usa allowlists de identificadores, no el texto normativo ni una justificación de aplicabilidad por cada control | Identificador válido no garantiza correspondencia material con el comportamiento probado | Añadir registro por caso con texto/versión del requisito, precondiciones, parte ensayada, parte no ensayada, decisión y revisor |
| QA-03 | La reconciliación de `build_coverage.py` comprueba presencia de IDs, no multiplicidad esperada de variantes ni unicidad de `(case_id,variant)` | Una variante ausente o duplicada podría pasar si el ID aparece al menos una vez | Manifest de variantes esperadas y validación de conteo/identidad, preservando los oráculos existentes |
| QA-04 | `summarize_junit.py` acepta `UNMAPPED` y `unclassified` como valores de respaldo; `build_coverage.py` los rechaza indirectamente si hay deriva | Errores de instrumentación se detectan tarde y el mensaje puede ser poco diagnóstico | Validación explícita de propiedades obligatorias, resultados y esquema antes de publicar |
| QA-05 | `summarize_junit.py` incluye `variant` del nombre pytest sin sanitización adicional | Parámetros futuros con secretos/datos personales podrían filtrarse al resumen, pese al comentario de seguridad | Validar allowlist de caracteres/longitud para IDs de variante o generar variantes exclusivamente desde identificadores estáticos |
| QA-06 | El workflow usa `if: always()` para generar resumen y publicar artefactos, pero no exige explícitamente que la generación de resumen/cobertura finalice antes de considerar éxito del job cuando no existe JUnit | Un fallo temprano puede dejar evidencia incompleta; el job de pytest sí falla, pero la ausencia de manifiesto requiere control explícito | Añadir gate de integridad de evidencia y manifiesto de artefactos sin debilitar el criterio de éxito |
| QA-07 | `cancel-in-progress: true` y múltiples commits documentales disparan CI de repositorio | Cancelaciones de runs históricos y confusión sobre el SHA realmente validado | Congelar commits durante la última corrida; registrar run cancelado por separado; publicar informe después y verificar checks de HEAD |
| QA-08 | `CM-T25` solo comprueba valor distinto del original, mientras `CM-T27` verifica coincidencia exacta con la función de ofuscación | Coincidencia con función de ofuscación no prueba suficiencia de anonimización ni cumplimiento de política | Mantener ambos oráculos, medir información residual y solicitar criterio de minimización aprobado |
| QA-09 | `CM-T26` prueba un UUID ausente, no múltiples entradas malformadas ni formatos incompatibles | No permite concluir robustez general de errores o enumeración | Incluir LIVE-04 y, si se requiere, parametrizar entradas inválidas en fase posterior |
| QA-10 | `CM-T22` aplica dos XFAIL a email, pero P-ORDER-01 describe también direcciones | Existe asimetría entre alcance de política propuesta y aserción normativa implementada | Mantener XFAIL actuales y registrar que los campos de dirección solo están caracterizados; no inventar cuatro XFAIL |
| QA-11 | Bandit es un barrido acotado de módulos y umbrales, no SAST completo | Ausencia de otros avisos no implica ausencia de defectos | Preservar scope/versiones, revisión humana y complementar en C10 con configuración y dependencias según autorización |

Estas observaciones son **mejoras de ingeniería del harness**, no defectos demostrados de Saleor. QA-03/04/05/06 requieren cambios y pruebas de regresión propios antes de considerarse corregidos; el presente informe no afirma haberlos implementado.

## 4. Revisión de cada contrato y caracterización

Convenciones: **EJECUTADO** significa que el oráculo pasó; **CONTRATO LOCAL VERIFICADO** significa solo que el escenario probado satisfizo su aserción; **NORMATIVA NO DETERMINADA** significa que el texto y aplicabilidad del control ASVS/WSTG no fueron formalmente adjudicados; **CARACTERIZADO** significa comportamiento observado sin conformidad. Los ID ASVS/WSTG de la matriz son **mapeos preliminares**, no certificación.

| Caso | Evidencia | Resultado | Alcance defendible / límite |
| --- | --- | --- | --- |
| CM-T01 | Contrato | 1 PASS | `me` nulo anónimo y datos propios autenticado; no prueba todas las consultas de identidad |
| CM-T02 | Contrato | 1 PASS | Revocación invalida acceso y refresh en fixture; no prueba replicación o ventanas distribuidas |
| CM-T03 | Contrato | 4 PASS | Refresh por argumento/cookie y CSRF válido/ausente/inválido; no prueba cookies de navegador real |
| CM-T04 | Contrato | 1 PASS | `order(externalReference:)` deniega a cliente sin `MANAGE_ORDERS`; no generaliza a `order(id:)` |
| CM-T05 | Caracterización | 1 PASS | UUID conocido muestra campos sintéticos a anónimo; no determina autorización correcta |
| CM-T06 | Caracterización | 1 PASS | Propietario, tercero y anónimo ven campos sintéticos con UUID; no implica enumeración |
| CM-T07 | Contrato local | 1 PASS | Número legado preserva datos al propietario y altera los de no propietarios; no demuestra anonimización suficiente |
| CM-T08 | Contrato | 1 PASS | Tipos/TTL/audiencia de tokens en fixture; no cubre todo el ciclo de vida |
| CM-T09 | Contrato | 2 PASS | Respuesta a credenciales inválidas en dos condiciones; no cubre canales laterales/tiempos |
| CM-T10 | Contrato | 1 PASS | JWT de acceso rechazado como refresh; no cubre todas las confusiones de token |
| CM-T11 | Contrato | 1 PASS | Audiencia personalizada preservada al refrescar; no prueba validación de todos los consumidores |
| CM-T12 | Contrato | 1 PASS | `user` restringido a tercero/anónimo en escenario ensayado; no generaliza a todos los campos |
| CM-T13 | Contrato | 1 PASS | Diferencias entre permisos de staff en `user`; no constituye matriz exhaustiva de roles |
| CM-T14 | Caracterización | 2 PASS | Flags cookie con DEBUG verdadero/falso; no verifica terminación TLS o navegador |
| CM-T15 | Contrato | 1 PASS | Rechazo de aliases por límite configurado; no prueba carga/DoS |
| CM-T16 | Contrato | 1 PASS | Rechazo por límite de mutaciones; no prueba abuso distribuido |
| CM-T17 | Caracterización | 3 PASS | Precedencia de cabeceras de autenticación; política de gateway aún no validada |
| CM-T18 | Caracterización | 3 PASS | Parseo de forwarded IP/fallback; confianza en proxies reales no validada |
| CM-T19 | Contrato | 6 PASS | Algoritmo determinista de demoras por IP/usuario; no prueba rate limiting real bajo concurrencia |
| CM-T20 | Contrato | 2 PASS | Intersección de permisos de token delegado y usuario; no prueba todos los scopes de apps |
| CM-T21 | Contrato | 1 PASS | Rechazo de JWT con algoritmo `none`; no prueba todos los ataques criptográficos |
| CM-T22 | Política provisional | 2 XFAIL | Dos actores reciben email contrario a P-ORDER-01 propuesto; no hay requisito oficial incumplido |
| CM-T23 | Caracterización | 6 PASS | 2 actores × 3 campos raw por UUID conocido; evidencia fuerte del comportamiento en fixture |
| CM-T24 | Caracterización | 3 PASS | Control positivo del propietario para los mismos campos |
| CM-T25 | Caracterización | 6 PASS | 2 actores × 3 campos no idénticos al raw en ruta legada |
| CM-T26 | Caracterización | 2 PASS | UUID ausente devuelve orden nula para dos actores |
| CM-T27 | Caracterización | 6 PASS | 2 actores × 3 campos coinciden exactamente con funciones de ofuscación |

**Resultado de adjudicación:** los 16 casos de tipo `security_contract` pueden marcarse **REVIEWED_LOCAL_ORACLE_PASS / NORMATIVE_NOT_ADJUDICATED**, no `ASVS_CONFORMANT`. Los 10 casos de caracterización permanecen **REVIEWED_OBSERVED / NO_SECURITY_VERDICT**. CM-T22 queda **REVIEWED_PROVISIONAL_POLICY_MISMATCH / POLICY_NOT_APPROVED**. Esto cierra la *revisión técnica de interpretación*, pero no falsifica una decisión normativa que necesita autoridad de requisitos.

## 5. Análisis de riesgos R01–R13

| Riesgo | Casos | Interpretación técnica y reserva |
| --- | --- | --- |
| R01 | T17, T18 | Cabeceras e IP origen caracterizadas; riesgo de confianza en proxies requiere topología real |
| R02 | T18, T19 | Algoritmo de demora probado, procedencia IP caracterizada; resistencia operacional no verificada |
| R03 | T09 | Escenarios de credenciales inválidas probados; no inferir ausencia de enumeración temporal |
| R04 | T08 | Propiedades de token probadas en fixture; no concluir gestión integral de sesiones |
| R05 | T10 | Rechazo de access-as-refresh demostrado; no exhaustivo |
| R06 | T03, T14 | CSRF de refresh y flags cookie caracterizados/probados; falta HTTPS/browser |
| R07 | T02 | Revocación de credenciales probada en entorno aislado |
| R08 | T08, T11, T21 | Audiencia/tipo/algoritmo `none` en rutas específicas; no certificación JWT |
| R09 | T04 | `externalReference` deniega a usuario sin permiso; ruta UUID es distinta |
| R10 | T01, T12, T13 | Controles puntuales de identidad/visibilidad; matriz de roles incompleta |
| R11 | T05, T06, T07, T22–T27 | Distinción UUID vs número legado y P-ORDER-01; mayor incertidumbre de autorización y privacidad |
| R12 | T15, T16 | Límites configurados de aliases/mutaciones funcionan en casos puntuales; no carga |
| R13 | T20 | Intersección de permisos delegados probada; falta cobertura exhaustiva de apps |

**Los 13 riesgos mantienen `security_verdict=NO_DETERMINADO`.** El dictamen no equivale a 13 riesgos activos, 13 vulnerabilidades o 13 controles conformes.

## 6. Hallazgo central de órdenes: hipótesis rivales y evidencia discriminante

- **Observación O1:** el UUID conocido de una orden permite a dos actores no propietarios recuperar tres campos personales sintéticos sin ofuscar (CM-T23).
- **Observación O2:** el identificador legado ofrece una representación ofuscada a esos actores (CM-T25/T27), que conserva información parcial.
- **Observación O3:** el propietario obtiene los valores completos (CM-T24) y un UUID inexistente no devuelve orden (CM-T26).
- **Hipótesis H-A:** el UUID es una capacidad de acceso intencional para un flujo de compra invitada/compartición. Requiere evidencia de contrato de producto, distribución y ciclo de vida del identificador.
- **Hipótesis H-B:** el negocio CyberMarket exige titularidad o capacidad adicional para revelar esos campos. Requiere adopción explícita de P-ORDER-01, definición de excepciones y prueba desplegada.
- **Hipótesis H-C:** un frontend, registro, enlace o intermediario revela UUIDs a terceros. No hay evidencia en C2–C9; debe ensayarse en LIVE-07.

**No demostrado:** adivinación factible de UUID, exposición de PII real, incumplimiento de Saleor, explotación, mitigación por simple ofuscación, ni garantía de anonimato.

## 7. Evaluación de la instrumentación y cadena de custodia

El workflow genera JUnit y resumen determinista, registra SHA de `github.sha` y manifiesto SHA256, pero el SHA de evento PR puede corresponder al commit de merge y no al head: ambos deben conservarse. `summarize_junit.py` extrae solo metadatos de caso, aunque el JUnit original puede incluir propiedades o trazas y **no debe presumirse libre de datos sensibles sin inspección**. La verificación de ZIP SHA256 y hashes por archivo está documentada en [cierre auditado previo](INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md); se recomienda almacenamiento de largo plazo para evitar expiración de artefactos Actions.

El barrido Bandit 1.8.6 fue limitado a módulos de autenticación/orden. Su B105 LOW/MEDIUM sobre `JWT_REFRESH_TOKEN_COOKIE_NAME = "refreshToken"` fue clasificado como falso positivo razonado: es un nombre de cookie, no un secreto incrustado. No se deben suprimir silenciosamente avisos ni confundir exit 0 con ausencia de hallazgos.

## 8. Registro de decisiones y criterios de aceptación

| Decisión | Estado | Autoridad / evidencia necesaria |
| --- | --- | --- |
| Integridad de ejecución C2–C9 | VERIFIED | JUnit, CI, SHA, matriz |
| Interpretación de 27 casos | REVIEWED_WITH_LIMITS | Esta revisión, oráculos inspeccionados, expedientes |
| Conformidad formal ASVS/WSTG | NOT_ADJUDICATED | Requisito exacto, aplicabilidad, cobertura y revisión autorizada |
| Aprobación de P-ORDER-01 | NOT_APPROVED | Responsable de producto / hipótesis empresarial aprobada |
| Vulnerabilidad explotable Saleor | NOT_ESTABLISHED | Requisito aplicable, impacto, vector y evidencia reproducible |
| Seguridad en entorno desplegado | NOT_TESTED | C10 con autorización y entorno aislado |
| Completitud de auditoría línea por línea de todo C4–C8 | NOT_CLAIMED | Inspección integral de cada módulo restante |

## 9. Recomendaciones de ingeniería y prioridad

**P0 — antes de cualquier declaración normativa:** aprobar o rechazar P-ORDER-01; validar el significado de UUID como bearer capability; separar campos, actores y excepciones. **P1 — endurecimiento del harness:** manifest de variantes y validación estricta de metadatos JUnit, evaluación humana por requisito, protección de variantes contra fuga y gate de integridad de artefactos. **P2 — extensión C10:** ejecutar matriz de roles, HTTP/HTTPS/browser/proxy, errores de IDs y flujo real de obtención de UUID; controlar teardown, retención y sanitización. **P3 — después de C10:** evaluar si nuevos datos modifican riesgos y recomendaciones; no modificar código Saleor sin aprobación independiente.

## 10. Conclusión

La suite **cumplió sus objetivos de ejecución y caracterización C2–C9**, y el expediente permite rastrear cada resultado al escenario probado. La ingeniería de pruebas tiene buenas bases, pero requiere controles adicionales para garantizar cardinalidad de variantes, higiene de metadatos y una capa formal de adjudicación de requisitos. La incertidumbre principal es **normativa y de contexto de despliegue**, no un FAIL de pytest. El paso siguiente es C10, con roadmap operativo separado. **No se autoriza llamar a los resultados “ASVS compliant” ni “vulnerabilidad confirmada”.**

No se modificó código funcional de Saleor, Avance 1 ni se fusionó el PR.
