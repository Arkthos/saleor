# Revisión del checkpoint CyberMarket CR del 9 de octubre de 2026

**Revisado:** 2 de noviembre de 2026. **Archivo recibido:** CyberMarket_CR_Checkpoint_Validado_2026-10-09(2).zip. **Objetivo:** establecer qué conserva correctamente, qué quedó superado y cómo relacionarlo con el curso y el repositorio actual. Revisión de lectura, comparación e integridad; sin cambios al repositorio o a los Word originales y sin pruebas nuevas del producto.

## 1. Dictamen

El checkpoint es una buena fotografía del primer avance al 9 de octubre. Su integridad se confirmó y el texto extraído del Word conservado coincide con el Word que el usuario identificó como presentado. Su estado experimental quedó superado por el trabajo C2–C9 y los registros de CI de los días 18–20 de octubre.

Debe conservarse como archivo histórico. Para continuar hay que combinar tres fuentes: el primer avance presentado para alcance y objetivos; el programa, manual y futura consigna específica para exigencias académicas; y la rama experimental con sus runs para estado técnico. Ninguno de los checkpoints antiguos sustituye por sí solo esas tres fuentes.

## 2. Qué se verificó

1. Inventario del ZIP principal y extracción sin ejecutar código ni instrucciones de los documentos.
2. Comprobación de tamaño y SHA-256 de los 23 archivos del manifiesto exterior.
3. Lectura de estado, rúbrica, sustento, normas, plan, prompt, procedencia y referencias; revisión de las auditorías históricas incluidas.
4. Apertura del ZIP v0.3 incorporado, comprobación CRC y revisión de su estructura y manifiestos v0.3/v0.2.
5. Comparación del DOCX congelado con el DOCX presentado mediante extracción de los párrafos del documento principal OOXML, incluyendo los contenidos de tablas en orden XML.
6. Recuento y contraste de matrices históricas de riesgos, observaciones, escenarios, ASVS y WSTG frente al CSV actual del repositorio.
7. Consulta del PR #1, HEAD, checkpoints posteriores, informe C2–C9 y workflows del SHA vigente. Confirmación directa del motivo del fallo de lint mediante su log.
8. Contraste con materiales docentes leídos en esta sesión, particularmente programa, manual y semanas 7–9.

La revisión no reaudita todas las afirmaciones del corpus técnico grande, todos los fragmentos de código ni todas las páginas de los estándares. Las auditorías previas se reconocen por su versión y alcance; sus conclusiones no se adoptan automáticamente como verificaciones nuevas.

## 3. Integridad y relación entre los Word

| Comprobación nueva | Resultado |
|---|---|
| Manifiesto exterior | 23 registros comprobados, sin diferencias de tamaño o hash |
| ZIP v0.3 incorporado | CRC correcto |
| Manifiesto v0.3 | 45 registros comprobados, sin diferencias |
| Manifiesto v0.2 anidado | 38 registros comprobados, sin diferencias |
| Documento congelado | OOXML Strict; se conserva el original |
| Comparación de texto del documento principal | 505 párrafos con texto en cada archivo; secuencias idénticas |

Los tres manifiestos se solapan por anidación; no deben sumarse como archivos únicos independientes.

**SHA-256 del Word del checkpoint, Proyecto final - primer avance(3).docx:**

6408e5aa90c2d8d1038070a042180364f97564d0bbae4bdac57c871fd76309b7

**SHA-256 del Word presentado, Proyecto final - primer avance(4).docx:**

c8f98d51b40ef7571f0cefaa092ae7c9504b3d5e4cd89db0f5d28c885c014d65

La diferencia binaria no corresponde a una diferencia en los 505 párrafos extraídos. Sí hay cambios en componentes internos del paquete, entre ellos estilos, configuración, propiedades y XML del documento. Esto no establece equivalencia visual página por página, de comentarios, de todas las revisiones o de cada propiedad de formato. No se regeneró ni exportó ninguno de los Word.

La regla histórica que designaba (3).docx como canónico correspondía a aquella sesión. Ahora el usuario identifica (4).docx como la entrega presentada; esa identificación rige la continuidad del proyecto. La coincidencia textual evita tener que elegir entre dos versiones con contenido sustantivo distinto.

## 4. Qué sigue vigente

| Elemento | Evaluación |
|---|---|
| CyberMarket CR ficticio y software Saleor real | Vigente; no atribuir operación empresarial o incidentes reales |
| Fork Arkthos/saleor y baseline 4cb1609… | Vigente como producto base y referencia estática; distinguirlo de los commits de pruebas |
| Título y foco de autenticación/autorización | Coinciden con el primer avance presentado |
| Seis operaciones seleccionadas | tokenCreate, tokenRefresh, tokensDeactivateAll, me, user y order |
| Un objetivo general y tres específicos | Preservar la formulación del manuscrito presentado |
| Instrumentos I01–I07 | Base metodológica existente; explicar después qué se aplicó y qué quedó propuesto |
| 13 riesgos y 15 observaciones | Consistentes con la fase inicial; prioridades de investigación y observaciones estáticas, no 15 vulnerabilidades |
| ASVS 5.0.0 y WSTG 4.2 | Versiones de referencia del estudio; requisitos y procedimientos con funciones diferentes |
| IEEE en el manuscrito | Convención del avance presentado y del checkpoint exterior |
| Separación entre hecho, inferencia y prueba | Vigente; debe mantenerse al incorporar resultados posteriores |
| Aprobación del usuario | Decisión editorial; no acredita evaluación o aprobación del profesor |

El usuario indica que no hay correcciones del profesor. No deben transformarse las observaciones editoriales archivadas en retroalimentación docente pendiente.

## 5. Qué quedó desactualizado

| Declaración o instrucción histórica | Situación comprobada ahora | Tratamiento |
|---|---|---|
| No existen pruebas dinámicas confirmadas | Hay suite ejecutada en CI sintético y registros posteriores de resultados | Mantener esa frase solo como estado al 9 de octubre |
| Laboratorio completamente futuro | Existen condiciones automatizadas con fixtures y servicios en CI; C10 desplegado sigue sin ejecutarse | Separar entorno de tests de navegador/HTTPS/proxy |
| Derivar todos los casos a partir de los 16 escenarios iniciales | La matriz actual tiene 27 IDs y 61 variantes registradas | Usar el inventario actual y conservar su procedencia |
| Revocación, CSRF y pedidos solo por investigar | Hay pruebas y caracterizaciones acotadas sobre esos flujos | Incorporarlas con sus precondiciones y límites |
| Próxima sección: III. Justificación | Es una instrucción del borrador v0.3; el avance 1 completo ya fue presentado | No reanudar la redacción desde ahí |
| Referencias limitadas a [1]–[6] o a once entradas | Son estados editoriales anteriores; el documento exterior y el avance presentado tienen doce | Utilizar la bibliografía del manuscrito presentado |
| Pendiente completar autores o apartados vacíos | Procede de auditorías de borradores anteriores | Comprobar cada caso en la entrega, sin arrastrar la lista antigua |
| Corpus docente limitado a S1 | Ahora se leyeron materiales de S4–S9, talleres, foro y sesión | Usar el mapa curricular actualizado |

El propio ZIP exterior advierte que v0.3/v0.2 son historia y que no sustituyen al documento completo. Su inclusión no es un error; el riesgo está en darles la misma prioridad al retomar.

## 6. Estado del repositorio al revisar

**PR:** [#1](https://github.com/Arkthos/saleor/pull/1), abierto, en borrador y sin fusionar. Rama: research/cybermarket-security-tests-v1. Se observaron 119 commits y 34 archivos cambiados respecto a main, con 2993 adiciones y cero eliminaciones.

| Identificador | SHA |
|---|---|
| Producto base / main | 4cb1609a90eade14b6275a407bc7a00c35698090 |
| HEAD de la rama consultada | c442099bc0ebee5194a6e58354944563e92e0d28 |
| Checkout de integración del PR | b0604014dab69125a4a535f1ece5828be99ea3c8 |

Los informes del 18 de octubre conservan SHAs anteriores, entre ellos 63cadee… y 6722e120…, con sus propios runs. Esa procedencia sigue siendo útil, pero sus resultados no deben atribuirse sin comprobación al HEAD posterior. El cuerpo del PR también resume una ejecución histórica: la evidencia más reciente del SHA debe consultarse por separado.

### Registros más recientes del HEAD consultado

| Workflow | Resultado registrado | Enlace |
|---|---|---|
| CyberMarket GraphQL | 59 PASS, 2 XFAIL esperados; validación de evidencia con 6 PASS | [39443927080](https://github.com/Arkthos/saleor/actions/runs/39443927080) |
| Suite general | 17 613 PASS, 2 XFAIL esperados | [39443927003](https://github.com/Arkthos/saleor/actions/runs/39443927003) |
| E2E | 211 PASS | [39443926898](https://github.com/Arkthos/saleor/actions/runs/39443926898) |
| Linters | FAILURE por espacios al final de líneas del checkpoint de semana 7 | [39443927026](https://github.com/Arkthos/saleor/actions/runs/39443927026) |
| Changelog | SUCCESS | [39443927138](https://github.com/Arkthos/saleor/actions/runs/39443927138) |
| Despliegue y publicación para carga | SKIPPED | No representan pruebas realizadas |

Los casos CyberMarket están incluidos en la suite general; no sumar esos conteos. Las seis pruebas del validador verifican el sistema de evidencia y deben distinguirse de las pruebas del producto.

En el log del job 118700705681, el hook trailing-whitespace modifica security/cybermarket/CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md y hace fallar el check. Ruff, formato, mypy, deptry, Semgrep, lockfile, migraciones y esquema pasan. Esto no equivale a un fallo de autenticación del producto ni permite decir que todos los checks del HEAD están verdes. Se registró el problema y no se corrigió, porque la tarea actual es comprender y revisar.

## 7. Reconciliación de las matrices

| Unidad | Checkpoint inicial | Evidencia actual |
|---|---:|---|
| Riesgos de investigación | 13: nueve de prioridad alta y cuatro media | Los 13 tienen al menos un caso asociado; dictamen formal NO_DETERMINADO |
| Observaciones estáticas | 15, H01–H15 | El CSV actual referencia explícitamente 14; H10 no aparece en esa columna |
| Escenarios actor–operación–recurso | 16 | 27 identificadores CM-T y 61 variantes registradas; unidades diferentes |
| Requisitos ASVS seleccionados | 23 | 16 IDs distintos referenciados explícitamente en el CSV de pruebas |
| Procedimientos WSTG seleccionados | 11 | 10 IDs distintos en el CSV actual, con una incorporación y dos ausencias respecto a la selección inicial |

La comparación de columnas no demuestra por sí sola que un tema carezca de toda evidencia en documentos o código. Sí demuestra que no puede declararse trazabilidad completa del catálogo inicial a partir del CSV actual únicamente.

**ASVS sin referencia explícita en el CSV actual:** v5.0.0-6.1.1, 7.1.1, 7.2.1, 7.3.2, 8.1.1, 8.3.1 y 9.1.1. Todos los 16 IDs actualmente referenciados pertenecían a la selección original.

**WSTG:** WSTG-IDNT-01 y WSTG-INFO-10 estaban en la selección inicial y no aparecen en el CSV actual; WSTG-IDNT-04 aparece ahora y no estaba en aquella lista. Puede tratarse de evolución razonable de procedimientos, pero hace falta registrar el cambio y justificar qué evidencia documental o experimental se usa para cada elemento.

**H10:** su ausencia de la columna observation_ids no prueba ausencia de toda evaluación de permisos. CM-T04 está asociado a R09 y H12, por ejemplo. La revisión pendiente es de trazabilidad y alcance específico, no un veredicto automático sobre BaseMutation.

### Qué significan los resultados

El inventario actual distingue 16 IDs de contratos de seguridad, diez de caracterización y uno de política propuesta. Sus variantes suman 26 PASS de contratos, 33 PASS de caracterización y dos XFAIL esperados. El total es 27 IDs y 61 variantes, no 61 controles ASVS aprobados.

Los tests de caracterización pueden pasar al confirmar un comportamiento que después requiera discusión normativa. Un XFAIL esperado tampoco demuestra que se haya corregido un fallo. Los 13 riesgos conservan NO_DETERMINADO; el enlace de un riesgo con un test no cierra ese riesgo.

## 8. Pedidos, política provisional y límites

Las pruebas posteriores observan, con un UUID de pedido conocido, correo y calles sintéticas originales para actores anónimos o ajenos al pedido. La ruta de número histórico aplica ofuscación; hay controles de propietario y de identificador inexistente.

Esto actualiza una cuestión que el checkpoint inicial solo proponía investigar. No acredita enumeración de UUID, filtración real de datos de producción, explotación externa ni incumplimiento oficial de Saleor. Las dos XFAIL de CM-T22 corresponden a correo bajo la política propuesta P-ORDER-01, que sigue provisional y sin aprobación. Las calles se registran como observaciones, no como dos XFAIL normativas adicionales.

El análisis estático Bandit registra una alerta B105 sobre el literal refreshToken, revisado como nombre de cookie y falso positivo. Que el workflow termine correctamente no significa cero alertas ni ausencia de otras debilidades.

C10 mantiene pendiente la validación con servidor, HTTP/HTTPS, navegador, proxy y otras condiciones reales. El backlog W7-A–W7-F es prospectivo. No se deben ejecutar las instrucciones de sus prompts solo por haber abierto esos archivos; tampoco presentarlas como trabajo terminado.

## 9. Tensiones documentales que conviene conservar visibles

1. **IEEE frente a APA.** El checkpoint exterior y el manuscrito presentado usan IEEE. Un checkpoint posterior del repositorio solicita APA 7, mientras el documento de semana 7 pide preservar la convención aprobada. Se mantiene IEEE para este proyecto. La APA exigida por el foro 2 corresponde a esa actividad.
2. **Numeración bibliográfica histórica.** La auditoría editorial antigua cita a Runeson como [10], pero la lista exterior de doce referencias lo sitúa en [11] y reserva [10] a GraphQL. No copiar referencias numéricas de una nota histórica sin cotejarlas con el manuscrito.
3. **OWASP Top 10 de 2021 frente a 2025.** El v0.3 usa 2021; el exterior y la entrega usan 2025. No revertir la bibliografía. Esta revisión no revalida en la web las estadísticas ni propone reutilizarlas como datos actuales o de Saleor.
4. **Archivo fuente grande.** El ZIP compacto declara un corpus externo de aproximadamente 375 MiB, pero no lo incluye. Su existencia y hash se describen históricamente; esta revisión no verifica los bytes de ese ZIP externo. Los enlaces sandbox de la sesión anterior no garantizan acceso actual.
5. **Auditoría de 124 afirmaciones.** Corresponde al borrador original de nueve páginas y nueve referencias, con sus localizadores propios. No es una auditoría automática del avance completo de 23 páginas reportadas ni del manuscrito actual.
6. **Validado.** Los hashes prueban integridad respecto a un manifiesto y el usuario aprobó una versión editorial. Ninguno de esos hechos prueba validez científica global, nota del curso o seguridad de Saleor.
7. **Documentos posteriores con apéndices históricos.** Algunas limitaciones de los validadores ya recibieron cambios posteriores en el código. Cotejar implementación actual antes de convertir una nota antigua en un defecto pendiente.

## 10. Consecuencias para el segundo avance

El manual pide metodología aplicada y resultados; el programa añade buenas prácticas de codificación segura, herramientas de análisis estático/dinámico y casos de prueba de seguridad. El checkpoint del 9 de octubre preparaba esa fase, pero no refleja los resultados posteriores que ahora sí pueden analizarse con sus límites.

Para una futura entrega conviene explicar qué se hizo, con qué instrumentos, sobre qué unidades, bajo qué configuración, qué se observó y qué conclusión permite cada dato. La clasificación de pruebas de semanas 7–8 y los criterios de ejecución de semana 9 proporcionan el marco docente para hacerlo.

Sigue faltando la consigna específica del avance 2. No se deduce que sean obligatorios pentest externo, CVSS, un despliegue público o todas las pruebas avanzadas mencionadas en clase. Tampoco se inventan correcciones del profesor, aprobación de P-ORDER-01, UAT o capacitación.

## 11. Base de continuidad recomendada

- Mantener intacto el ZIP del 9 de octubre como preservación del avance 1.
- Tomar el Word presentado (4).docx como referencia de contenido y objetivos.
- Usar el programa, manual y mapa curricular como marco de expectativas, pendiente de la consigna específica.
- Consultar la rama del PR y sus resultados por SHA, separando cierres históricos, reejecuciones y planes.
- Completar la conciliación requisito–caso–evidencia–dictamen antes de afirmar cobertura normativa.
- Cuando el usuario pida preparar el segundo avance, trabajar sobre una versión nueva y preservar la primera entrega.

Estas son orientaciones derivadas de la revisión; no se implementaron cambios, no se amplió el experimento y no se redactó el avance 2.

## 12. Fuentes para comprobar el estado

| Fuente | Localización |
|---|---|
| ZIP revisado | [Checkpoint recibido](https://chatgpt.com/library?file_id=libfile_808d46fcad608191bab8beed096b4bd4&account_id=personal) |
| Word presentado | [Primer avance](https://chatgpt.com/library?file_id=libfile_df58994acdec819181215cec7155ca14&account_id=personal) |
| PR y estado | [Arkthos/saleor #1](https://github.com/Arkthos/saleor/pull/1) |
| Matriz de pruebas | [CSV fijado al HEAD revisado](https://github.com/Arkthos/saleor/blob/c442099bc0ebee5194a6e58354944563e92e0d28/security/cybermarket/test_matrix.csv) |
| Cierre C2–C9 y apéndices | [Informe](https://github.com/Arkthos/saleor/blob/c442099bc0ebee5194a6e58354944563e92e0d28/security/cybermarket/INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md) |
| Checkpoint posterior | [Pre-redacción del 18 de octubre](https://github.com/Arkthos/saleor/blob/c442099bc0ebee5194a6e58354944563e92e0d28/security/cybermarket/CHECKPOINT_PRE_REDACCION_2026-10-18.md) |
| Plan metodológico posterior | [Semana 7, 20 de octubre](https://github.com/Arkthos/saleor/blob/c442099bc0ebee5194a6e58354944563e92e0d28/security/cybermarket/CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md) |
| Programa | [CY-703](https://chatgpt.com/library?file_id=libfile_6ae14bfb50d081919083c7c1f1cb8e32&account_id=personal) |
| Manual | [Proyecto grupal](https://chatgpt.com/library?file_id=libfile_98f903ab6a98819186ef3ec81b7608b4&account_id=personal) |
| Lectura del curso y expectativas | [Mapa curricular revisado](https://chatgpt.com/library?file_id=libfile_a6a6056200a481918a10dd73dcc9845d&account_id=personal) |

## 13. Texto de estado para retomar

> CyberMarket CR sigue el alcance del primer avance presentado: autenticación, tokens y autorización de seis operaciones sobre Arkthos/saleor. El Word del checkpoint del 9 de octubre y el Word presentado tienen el mismo texto extraído, pero distinto hash y componentes internos. El checkpoint es histórico: desde entonces se ejecutó C2–C9 en CI sintético. Al 2 de noviembre el PR #1 permanece abierto y draft, con HEAD c442099bc0ebee5194a6e58354944563e92e0d28; las pruebas registran 59 PASS y dos XFAIL esperados, y el lint actual falla por espacios finales en documentación. Los 13 riesgos siguen NO_DETERMINADO. C10 y W7-A–W7-F están planificados; P-ORDER-01 es provisional. El proyecto conserva IEEE y no tiene correcciones docentes comunicadas. Ya se leyó el material docente disponible hasta semana 9, con faltantes explícitos. La tarea actual fue comprender y conciliar fuentes; no autoriza por sí misma ejecutar backlog, modificar Saleor, fusionar el PR o redactar una entrega.
