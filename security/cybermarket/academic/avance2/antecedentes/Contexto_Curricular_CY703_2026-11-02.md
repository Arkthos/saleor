# Contexto curricular de Seguridad de Software — CY-703

**Fecha de revisión:** 2 de noviembre de 2026. **Proyecto:** CyberMarket CR, escenario ficticio, sobre el fork Arkthos/saleor. Documento de contexto para continuar el trabajo; no es el segundo avance ni una evaluación del profesor.

## 1. Resultado de la lectura y alcance real

El curso pide aplicar seguridad durante el ciclo de vida del software y justificar las decisiones mediante evidencias. Para este proyecto, la relación que debe mantenerse es: problema y objetivos → arquitectura y actores → amenazas y requisitos → decisiones de implementación → casos de prueba → resultados e interpretación → recomendaciones y verificación posterior.

Se inventariaron 143 archivos asociados al curso. Se leyeron los materiales docentes disponibles: programa, manual, consigna del primer avance, 17 presentaciones de las semanas 1 y 4–9 (538 páginas PDF), consignas de los talleres 1–2, foro 2 y transcripción de una sesión identificada como semana 4. También se procesaron 30 capturas mediante OCR, tres extractos de libros y bibliografía complementaria. El número de páginas incluye diapositivas con poco texto; no representa 538 páginas de prosa.

Se extrajo el texto completo de las presentaciones y se inspeccionaron visualmente ejemplos de código que no aparecían bien en la extracción. El OCR de lecturas y capturas puede contener errores; no debe utilizarse para citas literales sin comprobar la imagen original. No se dispone de los libros completos citados por el programa.

Las referencias extensas ASVS 5.0.0, WSTG 4.2 y SQUARE se consultaron de forma selectiva para contextualizar el proyecto. No se presenta esa consulta como lectura íntegra de todas sus páginas ni como auditoría normativa. Los archivos ZIP de código, copias de entregas y auditorías históricas se distinguen del material docente; el inventario no implica lectura semántica de todos sus contenidos.

**Faltantes:** no se localizaron presentaciones independientes de las semanas 2–3, materiales docentes de las semanas 10–14 ni una consigna específica del segundo avance. Sus temas y expectativas generales sí aparecen en el programa. No se han verificado fechas de entrega en el campus.

## 2. Fuentes y autoridad

| Fuente | Uso en el trabajo |
|---|---|
| Consigna específica de cada actividad | Define producto, alcance y rúbrica de esa entrega. La del segundo avance sigue sin localizarse. |
| Programa oficial y manual del proyecto | Definen objetivos, secuencia, evaluación y expectativas generales. Hay diferencias que deben conservarse explícitas. |
| Presentaciones y sesión docente | Explican contenidos y ejemplos; no convierten automáticamente cada técnica mencionada en un entregable obligatorio. |
| Libros y estándares | Sustentan conceptos o criterios concretos, con versión y alcance identificados. |
| Primer avance presentado | Base vigente del proyecto y sus objetivos. El usuario indica que no ha recibido correcciones del profesor. |
| Repositorio y registros CI | Evidencia de implementación y ejecución, vinculada al SHA y al entorno correspondiente. |
| Borradores, notas de otros estudiantes y respuestas anteriores | Contexto histórico; no son instrucciones del docente ni fuentes académicas verificadas por sí mismas. |

Fuentes principales: [Programa del curso](https://chatgpt.com/library?file_id=libfile_6ae14bfb50d081919083c7c1f1cb8e32&account_id=personal), [Manual del proyecto](https://chatgpt.com/library?file_id=libfile_98f903ab6a98819186ef3ec81b7608b4&account_id=personal), [Consigna del primer avance](https://chatgpt.com/library?file_id=libfile_0a28b5be04bc81918962f01ba7b06e8a&account_id=personal) y [primer avance presentado](https://chatgpt.com/library?file_id=libfile_df58994acdec819181215cec7155ca14&account_id=personal).

## 3. Mapa de las 14 semanas

Esta tabla sintetiza el programa. Las aplicaciones a CyberMarket son interpretaciones para orientar trabajo futuro, no actividades nuevas ya realizadas.

| Semana | Contenido y actividad del programa | Aplicación al alcance de CyberMarket | Material disponible |
|---|---|---|---|
| 1 | Privilegios mínimos, valores predeterminados, mediación completa, separación, confianza, economía y mecanismos comunes | Distinguir autenticación de autorización; revisar permisos por operación, objeto y campo, y límites de confianza | S1V1–V3 |
| 2 | Reducir sorpresas, diseño abierto, estratificación, abstracción, modularidad, vinculación completa e iteración | Explicar arquitectura y contratos de comportamiento; evitar atribuir seguridad a una sola capa | Programa y capturas; sin presentación independiente |
| 3 | Derivación y especificación de requisitos, SDLC/SSDLC, lenguajes seguros; foro 1 | Formular expectativas verificables antes de interpretar resultados; justificar selección de ASVS | Programa y lecturas/capturas parciales; sin presentación independiente |
| 4 | Validación, representación, APIs, funciones de seguridad, tiempo y estado; taller 1 | Validar entradas y secuencias de token, expiración, revocación y permisos | S4, transcripción y taller 1 |
| 5 | Excepciones, errores y programación robusta; avance 1 | Examinar respuestas externas, diagnósticos internos, fallos controlados, dependencias y buenas prácticas | S5V1–V3 y consigna de avance 1 |
| 6 | Encapsulamiento, módulos y medio ambiente; foro 2 | Identificar invariantes, responsabilidades y dependencia del entorno; diferenciar sostenibilidad de configuración operativa | S6, lectura de objetos y foro 2 |
| 7 | Análisis estático, dinámico y pruebas unitarias | Clasificar la evidencia por tipo y nivel; revisar control, datos, fallas e interfaces | S7V1–V3 |
| 8 | Integración y pruebas de software; taller 2 | Explicar componentes, DB/caché, contratos, regresión y límites de la suite GraphQL | S8V1–V3 y taller 2 |
| 9 | Configuración, parches, ciclo de vulnerabilidad y entorno; avance 2 | Registrar condiciones de ejecución, versiones, criterios de aceptación y resultados reproducibles | S9V1–V3; falta consigna específica del avance 2 |
| 10 | DevOps y retirada del sistema; taller 3 | Continuidad de CI, cambios, recuperación y cierre del laboratorio | Solo programa |
| 11 | Documentación de instalación, usuario, control y seguridad; foro 3 | Preparar guías y evidencia suficiente para repetir y mantener el trabajo | Solo programa |
| 12 | Ética, aspectos sociales y legales | Delimitar datos sintéticos, autorización y legislación realmente aplicable | Programa; documento jurídico de alcance institucional limitado |
| 13 | Divulgación de vulnerabilidades y qué/cuándo/por qué probar; taller 4 | Justificar límites, priorización y comunicación de hallazgos | Solo programa |
| 14 | Continuación de divulgación y entrega final/presentación | Integrar resultados, propuesta, despliegue, mantenimiento y defensa | Solo programa y manual general |

El programa establece tres créditos, modalidad virtual y nueve horas semanales: dos de recuperación de información, una de trabajo grupal y seis individuales. La secuencia de semanas no permite inferir una fecha de calendario sin consultar el campus.

## 4. Qué aporta cada bloque leído

### Principios y requisitos

Las presentaciones S1 permiten discutir privilegios mínimos, comprobaciones de acceso y separación de componentes y responsabilidades. Su aplicación exige rastrear la cadena completa de autorización. Un resolver aislado o la presencia de un decorador no demuestra protección de todos los campos.

SQUARE aporta una secuencia para definir términos y metas, construir artefactos, evaluar riesgos, seleccionar técnicas de elicitación, identificar, clasificar, priorizar e inspeccionar requisitos. En CyberMarket puede usarse una adaptación documental; no se celebraron entrevistas ni talleres con una empresa real y no deben inventarse.

ASVS expresa requisitos; WSTG orienta procedimientos de evaluación. La correspondencia local entre sus identificadores es una decisión metodológica que debe justificarse. Ninguna selección parcial permite afirmar un nivel ASVS global o una certificación.

### Implementación: semanas 4–6

S4 relaciona validación del lado servidor, tipos, rangos y representación con el uso correcto de APIs y estados. Para el proyecto importa comprobar identidad, permisos, entradas y transiciones de token. La validación de entrada, la parametrización de consultas y la codificación de salida resuelven problemas diferentes.

S5V1 desarrolla excepciones específicas, tratamiento controlado de errores y recuperación. S5V2 presenta SOLID, cohesión, acoplamiento y testabilidad. S5V3 amplía dependencias, datos, autenticación, privilegios, criptografía y revisión de cambios. SOLID o una herramienta de estilo no sustituyen controles de autorización.

S6 diferencia encapsulamiento y ocultamiento de información. Conviene analizar invariantes y responsabilidades, no limitarse a buscar getters y setters. La parte de medio ambiente incluye sostenibilidad, energía y ciclo de hardware. El foro 2 pregunta por condiciones del entorno al diseñar con encapsulamiento y SOLID: ambos sentidos deben explicarse sin mezclarlos automáticamente con proxy/TLS o con sostenibilidad exclusivamente.

### Análisis y pruebas: semanas 7–8

| Distinción | Consecuencia para el proyecto |
|---|---|
| Estático: sin ejecutar el programa | Revisión manual y herramientas, con alcance y triage de alertas. Las cuatro dimensiones docentes son control, datos, fallas e interfaces. |
| Dinámico: observar ejecución | Los tests Django ejecutados son evidencia dinámica dentro de su entorno. Esto no equivale a pruebas externas sobre HTTP/HTTPS. |
| Nivel: unidad, integración, sistema, aceptación | Lo determina qué se combina y qué dependencias participan. Usar pytest no vuelve unitaria una prueba GraphQL con fixtures y DB. |
| Diseño: caja negra, blanca o gris | Describe el conocimiento usado para diseñar la prueba; es independiente del nivel anterior. |
| Regresión | Reejecución para comprobar conservación de comportamiento o de una corrección identificada, vinculada a caso y versión. |
| Seguridad, rendimiento, carga y estrés | Tienen objetivos y criterios distintos. Un test funcional exitoso no demuestra tolerancia a carga. |
| Aceptación por usuarios | Requiere participación y criterios reales. No se puede presentar UAT, aprobación o capacitación como ejecutadas en una empresa ficticia. |

S7V3 destaca límites, entradas inválidas, excepciones, estado, aislamiento, mocks y stubs. S8 añade integración ascendente/descendente, contratos e interfaces, pruebas del sistema y aceptación. No se deduce que el proyecto deba implementar exhaustivamente todas las estrategias expuestas.

### Implementación operativa: semana 9

S9V1 pide planificar recursos, responsabilidades, riesgos, casos, expectativas y criterios de aceptación antes de ejecutar, y documentar desviaciones después. S9V2 aborda instalación, separación de entornos, configuración, versiones, migración y ciclo de vulnerabilidades. S9V3 incorpora capacitación, aprobación y control de cambios. Para CyberMarket esto se traduce en documentación reproducible y un plan delimitado; no acredita un despliegue, aprobación de negocio o capacitación realizados.

## 5. Evaluación y entregas

| Componente | Peso del curso |
|---|---:|
| Tres foros | 15 %: 5 % cada uno |
| Cuatro talleres investigativos | 35 %: 8,75 % cada uno |
| Primer avance | 10 % |
| Segundo avance | 15 % |
| Entrega final y exposición | 20 % |
| Coevaluación | 5 % |
| Total | 100 % |

El proyecto suma 50 %. El segundo avance aparece en la semana 9 y la entrega final en la 14 del programa. El manual menciona semanas 14–15 para actividades finales: conservar la diferencia hasta contar con instrucciones del campus.

### Segundo avance: expectativas combinadas

El manual, páginas PDF 4–5, pide marco metodológico y análisis de resultados, además de correcciones previas. Su rúbrica tiene cinco criterios y diez puntos. El programa, página PDF 13, usa seis criterios y doce puntos; explicita buenas prácticas de codificación, análisis estático/dinámico y casos de seguridad. Las rúbricas son distintas y no deben fundirse en una puntuación inventada.

| Exigencia | Fuente | Base existente | Qué debe quedar explicado o comprobado al preparar la entrega |
|---|---|---|---|
| Correcciones del primer avance | Ambas | Usuario indica que no recibió observaciones del profesor | Registrar esa situación; no inventar retroalimentación ni tratar notas históricas como correcciones docentes |
| Método, instrumentos, recolección y selección de unidades | Manual | I01–I07, seis operaciones y protocolo del avance 1; matrices y CI posteriores | Precisar qué instrumentos se aplicaron, qué datos se recogieron y bajo qué condiciones |
| Resultados, contraste y propuesta de solución | Manual | C2–C9 y sus límites documentados | Relacionar resultados con objetivos y criterios adoptados; separar propuesta de corrección de mejora ya verificada |
| Buenas prácticas de codificación segura | Programa | Código seleccionado, revisión estática y herramientas | Explicar prácticas concretas aplicables con evidencia y límites, sin requerir automáticamente un parche al producto |
| Análisis estático y dinámico con herramientas | Programa | Revisión, Bandit/Semgrep y suite automatizada | Identificar alcance de cada herramienta y ejecución; tratar falsos positivos y distinguir CI de entorno desplegado |
| Casos de seguridad suficientemente rigurosos | Programa | CM-T01–CM-T27, variantes, oráculos y controles | Justificar actores, recursos, positivos/negativos, bordes, esperado/observado y cobertura delimitada |
| Citas, referencias y redacción | Ambas | Primer avance en IEEE | Mantener IEEE y verificar correspondencia con afirmaciones; la APA del foro no cambia el manuscrito |

Esta matriz prepara la lectura de la futura consigna específica; no sustituye ese documento ni declara que el segundo avance ya esté completo.

### Diferencia con la entrega final

Además de integrar resultados, conclusiones, recomendaciones y referencias, el programa incorpora despliegue seguro, pasos y calendario de gestión de vulnerabilidades, respuesta a incidentes, legislación y ética. El manual incluye resumen de máximo 150 palabras, tres a cinco palabras clave, exposición y retroalimentación entre grupos. Hay diferencias sobre el medio de entrega del video; se resolverán con la consigna vigente. No adelantar todos estos productos como si fueran requisitos ya confirmados del avance 2.

### Actividades independientes

El taller 1 pide elegir una herramienta para comprobar APIs, evaluar autenticación/autorización y presentar resultados, recomendaciones y conclusiones en informe individual PDF. El taller 2 pide investigar Big Bang, integración incremental y continua, además de casos de éxito y fracaso, también en informe individual PDF. Esas exigencias no trasladan automáticamente todos sus casos al proyecto grupal.

El foro 2 requiere aporte de al menos 15 líneas, réplicas a por lo menos dos compañeros, netiqueta y APA vigente. No se deduce que APA reemplace IEEE en el proyecto.

## 6. Conexión con lo que ya existe

El primer avance presentado fija autenticación, tokens y autorización en seis operaciones: tokenCreate, tokenRefresh, tokensDeactivateAll, me, user y order. Conserva un objetivo general y tres específicos, siete instrumentos, 13 riesgos de investigación y 15 observaciones estáticas. No debe reinterpretarse como una auditoría de todo Saleor.

El repositorio ya contiene evidencia posterior C2–C9 en CI sintético: 27 identificadores y 61 variantes, con 59 PASS y dos XFAIL esperados. Los PASS de caracterización describen comportamiento; los contratos evalúan expectativas locales; los XFAIL se relacionan con una política provisional. Los 13 riesgos mantienen dictamen NO_DETERMINADO. Estos datos provienen de registros existentes, no de ejecución nueva en esta revisión.

El curso ayuda a organizar esa evidencia en niveles y a explicar sus condiciones. Los planes W7-A–W7-F y C10 siguen siendo planes en los archivos revisados. No se puede convertirlos en resultados ni afirmar que no existe ninguna prueba unitaria en el repositorio: hay pruebas directas de funciones, pero falta completar la clasificación del conjunto y el estrato CM-U propuesto.

## 7. Material complementario y precauciones de interpretación

| Fuente o problema detectado | Tratamiento al continuar |
|---|---|
| Costas Santos, Seguridad y alta disponibilidad (2015), extracto 07163754.pdf | Lectura de acceso lógico y credenciales. Ejemplos de versiones antiguas, MD5 o rotación mensual no se adoptan como recomendaciones actuales. |
| Blasco, Programación orientada a objetos en Java (2019), extracto 05150241.pdf | Excepciones, catch específico y flujo de control. Adaptar al lenguaje y arquitectura reales. |
| Oviedo Regino, Lógica de programación orientada a objetos (2015), extracto 16150248.pdf | Abstracción, objetos, encapsulación y acceso. No generalizar reglas de un lenguaje a Python. |
| S1V1: rótulo de valores predeterminados para prueba de fallos | Parte de los ejemplos trata credenciales o puertos por defecto. Contrastar el concepto de diseño antes de usarlo como definición de fail-safe defaults. |
| Afirmaciones absolutas en diapositivas S1 | No trasladar garantías como evitar todos los ataques o hacer un mecanismo infalible. |
| Ejemplos SOLID y regex | Son ilustrativos. Verificar contratos y precondiciones al usar LSP, y no convertir regex de ejemplo en una política exhaustiva. |
| Tabla de herramientas en S7V2, página 16 | Contiene descripciones repetidas de excepciones bajo herramientas de pruebas; no reutilizar ese error de plantilla. |
| file5.pdf, artículo de 2024 sobre desarrollo seguro | Se leyó; hay discordancias internas entre citas y bibliografía. No adoptar sus porcentajes como hechos verificados. |
| 2311.11021v1.pdf | Consulta selectiva de introducción/contexto; falta lectura integral y verificación bibliográfica antes de incorporarlo como sustento nuevo. |
| Reglamento de protección de datos del Poder Judicial adjunto | Su alcance institucional es judicial. No usarlo como reglamento general aplicable automáticamente a CyberMarket ni como verificación de vigencia legal. |
| Pasted text/markdown y comentarios de estudiantes | Son contexto, prompts o candidatos bibliográficos; verificar fuentes primarias antes de citarlos. |
| Auditorías y borradores antiguos | Sus diagnósticos se refieren a versiones identificadas; no transferirlos a la entrega presentada. |

## 8. Estado para la próxima tarea

Ya existe contexto suficiente para contrastar una consigna concreta del segundo avance con los resultados construidos. Antes de redactar o ampliar pruebas, deberá usarse la versión presentada del avance 1, la consigna vigente cuando esté disponible y el estado real del repositorio. Mantener identificados el SHA del producto, el SHA de la rama experimental y el SHA de checkout de Actions.

No se modificó el manuscrito ni el repositorio, y no se ejecutaron pruebas nuevas del producto durante esta lectura. Tampoco se atribuye aprobación docente, validez de una política ficticia, conformidad global ASVS o vulnerabilidad explotable a partir de los materiales.

## 9. Referencias docentes disponibles

Los enlaces siguientes identifican originales; no son una nueva bibliografía numerada del manuscrito.

| Material | Original |
|---|---|
| S1V1 | [Privilegios y valores predeterminados](https://chatgpt.com/library?file_id=libfile_1cc62b4cf3d081918d79b3ca70432be1&account_id=personal) |
| S1V2 | [Mediación y separación](https://chatgpt.com/library?file_id=libfile_7b0cc4f853548191b3fd4c43dbaea2b7&account_id=personal) |
| S1V3 | [Economía y confianza](https://chatgpt.com/library?file_id=libfile_378ea4f50c5881919dfe8a3237600e5b&account_id=personal) |
| S4 | [Validación y APIs](https://chatgpt.com/library?file_id=libfile_507ede8706e4819195038d1f655a20a2&account_id=personal) |
| S5V1 | [Excepciones y errores](https://chatgpt.com/library?file_id=libfile_88b06cba9bd081918683d4a49a2e11f8&account_id=personal) |
| S5V2 | [Programación robusta](https://chatgpt.com/library?file_id=libfile_7a958203746881918bafb0009038b151&account_id=personal) |
| S5V3 | [Buenas prácticas](https://chatgpt.com/library?file_id=libfile_f115565917388191b75c4a2ddd87ceff&account_id=personal) |
| S6 | [Encapsulado y medio ambiente](https://chatgpt.com/library?file_id=libfile_3f6bbfb6c0b48191a7d5245f11649da6&account_id=personal) |
| S7V1 | [Análisis estático](https://chatgpt.com/library?file_id=libfile_88eed10e70288191976cfc8755edcc8c&account_id=personal) |
| S7V2 | [Análisis dinámico](https://chatgpt.com/library?file_id=libfile_24c18b5bcdac8191b711973cef903158&account_id=personal) |
| S7V3 | [Pruebas unitarias](https://chatgpt.com/library?file_id=libfile_f916aea198a48191a19e2933d75ce1ef&account_id=personal) |
| S8V1 | [Pruebas de software](https://chatgpt.com/library?file_id=libfile_1b5664c7fde081918ad4dd490619d06a&account_id=personal) |
| S8V2 | [Pruebas de integración](https://chatgpt.com/library?file_id=libfile_7e4998a145d081919b2e8a235186dc24&account_id=personal) |
| S8V3 | [Pruebas avanzadas](https://chatgpt.com/library?file_id=libfile_76b35ff6a1508191a346495e47140f31&account_id=personal) |
| S9V1 | [Plan de implementación](https://chatgpt.com/library?file_id=libfile_0546b6fbafa881919914f488d5316903&account_id=personal) |
| S9V2 | [Implantación](https://chatgpt.com/library?file_id=libfile_755e8a477ac08191b38c8dd730797230&account_id=personal) |
| S9V3 | [Capacitación y aprobación](https://chatgpt.com/library?file_id=libfile_121905effd888191b3dbc8819c9e0992&account_id=personal) |
| Taller 1 | [Consigna](https://chatgpt.com/library?file_id=libfile_c26d9d8bc4e48191b5d5355ca5139804&account_id=personal) |
| Taller 2 | [Consigna](https://chatgpt.com/library?file_id=libfile_a23c73041f008191a859180f51654de9&account_id=personal) |
| Foro 2 | [Consigna](https://chatgpt.com/library?file_id=libfile_5c7cea129664819182ffbf2c75f9ddad&account_id=personal) y [rúbrica](https://chatgpt.com/library?file_id=libfile_eba49af7e1008191b04c6b09524fa1f0&account_id=personal) |
| Sesión semana 4 | [Transcripción](https://chatgpt.com/library?file_id=libfile_3ca90b02c3908191a92ea2e9a6954be9&account_id=personal) |
