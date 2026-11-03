# Textos de actualización del primer avance — continuación acumulativa

**Estado:** redacción preparada para inserción manual, 2026-11-03. No aplicada al Word. La instantánea presentada permanece intacta. Este documento es una guía de edición del mismo trabajo, no un segundo artículo ni un entregable final.

**Fuente:** Proyecto final - primer avance(5).docx; SHA-256 c8f98d51b40ef7571f0cefaa092ae7c9504b3d5e4cd89db0f5d28c885c014d65. Las frases de búsqueda permiten localizar los cambios con Ctrl+F, aunque cambie la paginación. Los códigos Pxxx son localizadores de la extracción técnica, no números visibles de Word.

**Conservar:** título, autores, pregunta de investigación, objetivo general, tres objetivos específicos, fundamentos y antecedentes que siguen vigentes, I01-I07, R01-R13, H01-H15, fuentes y listados pertinentes. Los textos nuevos no se presentan como retroalimentación del profesor. No se ha informado retroalimentación docente.

**Regla de citas:** [3]-[12] mantienen los números ya existentes en la bibliografía original. [4] fundamenta el código base y no debe usarse como si identificara el checkout posterior de pruebas. Los resultados se sustentan en el manifiesto y la tabla de procedencia que deberán acompañar la sección de pruebas. No se inventan referencias numeradas nuevas ni mappings oficiales ASVS/WSTG.

**Alcance de esta edición:** actualizar el contenido heredado que quedó desfasado. No da por terminado A2-07, el catálogo mínimo de diez hallazgos con recomendaciones, la adjudicación de los 13 riesgos/23 candidatos ASVS o la auditoría del manuscrito acumulativo. Los textos sobre resultados se pueden insertar porque la fase técnica está cerrada; las conclusiones finales se redactarán al completar el análisis.

## Mapa de modificaciones

| Código | Sección | Operación |
|---|---|---|
| ED01 | Resumen y palabras clave | Reemplazar el resumen completo y conservar las palabras clave. |
| ED02 | Introducción: versión, alcance y continuidad | Reemplazar esos tres párrafos; conservar los tres párrafos introductorios anteriores. |
| ED03 | Planteamiento del problema: situación inicial y evidencia actual | Reemplazar solo ese párrafo. Conservar inmediatamente después la pregunta de investigación sin cambios. |
| ED04 | Antecedentes: alcance efectivo de SQUARE | Reemplazar ese párrafo para actualizar su aplicación; conservar su cita. |
| ED05 | Marco metodológico: tipo y enfoque | Reemplazar los cinco párrafos de esta subsección. |
| ED06 | Muestra, actores y unidades de análisis | Cambiar «Se empleará» por «Se empleó» en el muestreo; en las tres viñetas usar «permiten examinar», «sirven para estudiar» y «permite analizar». Reemplazar desde «La unidad de análisis no será» hasta el final de esta subsección por el texto siguiente. |
| ED07 | Instrumentos: arquitectura y entorno observado | Reemplazar ese párrafo y el siguiente. Mantener la Fig. 1 como modelo conceptual. |
| ED08 | Instrumentos de recolección y medición | En los párrafos que presentan la Tabla II utilizar presente: «se apoya», «presenta», «permiten», «sirve», «convierte», «documenta», «debe incluir», «registra», «relacionan», «permite». Conservar I01-I07 y sus funciones. Reemplazar el último párrafo por el siguiente. |
| ED09 | Procedimiento de investigación y verificación | Sustituir la introducción y los seis apartados por esta versión; mantener los seis títulos como subtítulos del mismo nivel. |
| ED10 | Criterios de análisis: cobertura y alcance | Conservar la fórmula y los cuatro estados del análisis. Insertar este párrafo después de «no demostrará cumplimiento de todas las disposiciones de ASVS». |
| ED11 | Principios: permisos delegados y revocación | Reemplazar el párrafo «La misma orientación puede observarse» y el párrafo «El Apéndice A documenta», respectivamente, por estos textos; no cambiar los títulos. |
| ED12 | Principios: síntesis de evidencia | Actualizar la tercera columna de la Tabla III con la tabla de la guía y reemplazar el párrafo final por el siguiente. |
| ED13 | Riesgos: activos y priorización | En el párrafo de activos, sustituir la frase condicional sobre aplicaciones por la primera oración siguiente. Reemplazar el párrafo completo de priorización por el segundo. |
| ED14 | Riesgos: tokens y sesiones | Reemplazar los tres párrafos explicativos conservando el párrafo introductorio de R04–R08. |
| ED15 | Riesgos: objetos, disponibilidad y delegación | Reemplazar «El riesgo R11 consiste» por el primer párrafo. Reemplazar los dos párrafos de R12/R13 por los dos siguientes. Reemplazar el último párrafo de Análisis de riesgos por el cuarto. |
| ED16 | Arquitectura: datos y actualización del modelo | Reemplazar «El tercer límite, T3» por el primer párrafo; reemplazar «En consecuencia, el diseño documentado» por el segundo. |
| ED17 | Quince observaciones iniciales: continuidad y recomendaciones | Reemplazar el párrafo anterior a la tabla por el primero y los tres posteriores por el segundo. Conservar H01–H15; aplicar los ajustes de recomendaciones indicados en la guía. |
| ED18 | Apéndice A: revocación | Reemplazar los dos párrafos de alcance y verificación pendiente. Conservar código, fuente base e identificador EV-H08. |
| ED19 | Apéndice B: permisos y pedidos | Sustituir ambos párrafos. Conservar EV-H10, EV-H11 y EV-H12 y los listados existentes. |
| ED20 | Apéndice C: HTTPS, cookies y CSRF | Reemplazar los dos párrafos. Conservar EV-H05–EV-H07 y el análisis estático que los precede. |

## ED01. Resumen y palabras clave

**Dónde:** Antes de PLANTEAMIENTO DE LA INVESTIGACIÓN. Buscar «Este primer avance prepara».

**Qué hacer:** Reemplazar el resumen completo y conservar las palabras clave.

**Texto para insertar:**

Resumen— Este trabajo evalúa los mecanismos de autenticación, gestión de tokens y autorización del backend de Saleor mediante un fork versionado y un escenario empresarial ficticio denominado CyberMarket CR. El alcance comprende seis operaciones GraphQL y sus dependencias de código. A partir de la arquitectura lógica, los límites de confianza, trece escenarios de riesgo y quince observaciones estáticas identificados en la etapa inicial, se desarrolla una evaluación que adapta SQUARE, OWASP ASVS 5.0.0 y WSTG 4.2 para organizar requisitos, casos y evidencias. La metodología combina revisión de prácticas de codificación segura, análisis estático con Bandit y Semgrep, y pruebas dinámicas positivas y negativas en un laboratorio aislado con datos sintéticos. La batería focal registra 59 pruebas aprobadas y dos fallos esperados vinculados a una política de acceso provisional; adicionalmente, se completan 26 verificaciones mediante HTTP, HTTPS y Chromium. Las ejecuciones permiten caracterizar la revocación de tokens, los permisos por actor y los controles de cookies, CSRF y CORS, conservando evidencia de resultados y limitaciones. Los comportamientos observados sustentan la revisión de riesgos y recomendaciones, pero no equivalen por sí solos a vulnerabilidades confirmadas ni a una declaración de cumplimiento. Las conclusiones se restringen a los componentes, configuraciones y condiciones efectivamente examinados.

Palabras clave— Autenticación, autorización, desarrollo seguro, GraphQL, gestión de tokens, modelado de amenazas, Saleor.

## ED02. Introducción: versión, alcance y continuidad

**Dónde:** INTRODUCCIÓN. Desde «Se seleccionó Saleor como objeto de estudio» hasta el final del párrafo «La investigación parte de una revisión documental».

**Qué hacer:** Reemplazar esos tres párrafos; conservar los tres párrafos introductorios anteriores.

**Texto para insertar:**

Se seleccionó Saleor como objeto de estudio por tratarse de una plataforma de comercio electrónico de código abierto que expone sus funcionalidades mediante una API GraphQL. Su documentación distingue entre clientes, personal administrativo y aplicaciones externas, así como entre autenticación y autorización [3]. El estudio utiliza el fork Arkthos/saleor y conserva como línea base del producto el commit 4cb1609a90eade14b6275a407bc7a00c35698090 [4]. CyberMarket CR proporciona el escenario empresarial ficticio para representar actores, información protegida y operaciones comerciales. La documentación funcional se contrasta con el código de esta versión y con la configuración registrada del laboratorio.

El alcance comprende tokenCreate, tokenRefresh, tokensDeactivateAll, me, user y order. Estas operaciones permiten examinar el establecimiento de identidad, la renovación y revocación de credenciales y las decisiones de acceso a cuentas y pedidos. OWASP ASVS 5.0.0 [5] orienta la formulación de requisitos y WSTG 4.2 [6] la selección de procedimientos de verificación, sin asumir una equivalencia automática entre ambos referentes.

La etapa inicial reconstruyó la arquitectura y documentó escenarios de riesgo y observaciones estáticas. La segunda etapa incorpora revisión de codificación segura, herramientas de análisis estático y pruebas controladas de autenticación, autorización y sesiones. Se mantiene una distinción entre mecanismos identificados, comportamientos reproducidos y requisitos cuya conformidad todavía no se ha determinado. El propósito es reducir incertidumbre mediante evidencia verificable, con conclusiones limitadas a las condiciones examinadas.

## ED03. Planteamiento del problema: situación inicial y evidencia actual

**Dónde:** PLANTEAMIENTO DEL PROBLEMA. Buscar «Actualmente, la investigación cuenta».

**Qué hacer:** Reemplazar solo ese párrafo. Conservar inmediatamente después la pregunta de investigación sin cambios.

**Texto para insertar:**

En la etapa inicial, la investigación disponía de documentación técnica y una revisión estática preliminar, pero carecía de pruebas controladas que contrastaran los mecanismos identificados. Esta situación originó la necesidad de establecer una correspondencia verificable entre los requisitos del escenario CyberMarket CR, los controles de las operaciones seleccionadas y su comportamiento efectivo. La segunda etapa aporta ejecuciones reproducibles y evidencia de laboratorio para examinar esa correspondencia. El problema de evaluación sigue vigente en las condiciones no cubiertas y en los requisitos cuya aplicabilidad o conformidad todavía no se ha adjudicado; por ello, los riesgos hipotéticos, las caracterizaciones de comportamiento y las desviaciones respecto de una política definida deben mantenerse separados.

## ED04. Antecedentes: alcance efectivo de SQUARE

**Dónde:** Antecedentes del problema → Evolución del diseño seguro y la ingeniería de requisitos. Buscar «SQUARE fue concebida».

**Qué hacer:** Reemplazar ese párrafo para actualizar su aplicación; conservar su cita.

**Texto para insertar:**

SQUARE fue concebida para involucrar a ingenieros de requisitos y partes interesadas del proyecto [8]. En CyberMarket CR no existen representantes de una empresa operativa que puedan validar necesidades comerciales reales. Por ello, se adaptaron los elementos compatibles con el alcance académico: definición de activos y objetivos de protección, artefactos arquitectónicos, escenarios de amenaza y priorización de requisitos. Los supuestos del caso se mantienen explícitos, sin presentarlos como decisiones empresariales aprobadas ni afirmar la ejecución íntegra de los nueve pasos de la metodología.

## ED05. Marco metodológico: tipo y enfoque

**Dónde:** MARCO METODOLÓGICO → Tipo y enfoque de investigación. Desde «La investigación se desarrollará» hasta «procedimientos que puedan repetirse bajo las mismas condiciones».

**Qué hacer:** Reemplazar los cinco párrafos de esta subsección.

**Texto para insertar:**

La investigación adopta un enfoque aplicado, con alcance descriptivo y evaluativo. Examina cómo se establecen y aplican los mecanismos de autenticación, gestión de tokens y autorización en seis operaciones de Saleor. El componente descriptivo reconstruye la arquitectura, las dependencias y los controles; el evaluativo contrasta su comportamiento con expectativas y requisitos definidos para las condiciones seleccionadas.

Se combinaron revisión documental, inspección de código y configuración, análisis estático automatizado y pruebas dinámicas en un laboratorio aislado. Estas fuentes cumplen funciones diferentes: el código permite explicar rutas de implementación; las herramientas detectan patrones según sus reglas; y las ejecuciones aportan evidencia del comportamiento bajo configuraciones concretas. Ninguna de ellas demuestra por sí sola la seguridad global del sistema.

El objeto empírico es un artefacto de software, no una empresa en operación. CyberMarket CR es ficticia y las condiciones de evaluación fueron establecidas en el laboratorio. Se adoptan las recomendaciones de Runeson y Höst [11] sobre delimitación, planificación y cadena de evidencia, sin equiparar este diseño con un estudio empresarial en su contexto natural.

Se adaptaron elementos de SQUARE [8] para organizar activos, objetivos de protección, amenazas y prioridades. ASVS 5.0.0 [5] y WSTG 4.2 [6] sirven como referentes para requisitos y procedimientos, respectivamente. No se simularon consultas con representantes empresariales ni se atribuyó aprobación a las políticas provisionales del caso.

La selección intencional permite estudiar mecanismos concretos, pero no estimar estadísticamente la frecuencia de vulnerabilidades de Saleor. Las conclusiones dependen de la versión, los actores, los recursos, los campos y la configuración examinados.

## ED06. Muestra, actores y unidades de análisis

**Dónde:** Población, muestra y unidades de análisis. Conservar la definición de población.

**Qué hacer:** Cambiar «Se empleará» por «Se empleó» en el muestreo; en las tres viñetas usar «permiten examinar», «sirven para estudiar» y «permite analizar». Reemplazar desde «La unidad de análisis no será» hasta el final de esta subsección por el texto siguiente.

**Texto para insertar:**

La unidad de análisis combina actor, operación, recurso, campo solicitado, estado de autenticación y configuración relevante. Dos consultas sobre una misma operación pueden representar condiciones distintas según la propiedad del objeto y los permisos del solicitante.

Se utilizaron identidades y datos sintéticos para representar solicitudes anónimas, dos clientes independientes, personal con permisos diferenciados, aplicaciones y credenciales delegadas. El inventario efectivo sustituyó la previsión inicial de dieciséis escenarios: la batería focal comprende 27 identificadores y 61 variantes ejecutadas, de las cuales 59 aprobaron y dos quedaron como fallos esperados estrictos. Estos últimos corresponden a la política provisional P-ORDER-01 y no se interpretan como vulnerabilidades oficiales de Saleor.

Las 61 variantes focales forman parte de la regresión general; no se contabilizan como casos adicionales al sumar esa suite. Las verificaciones HTTP, HTTPS y de navegador se registran separadamente, al igual que las pruebas unitarias, los validadores de evidencia y la suite E2E. Esta separación evita confundir identificadores, variantes y conjuntos superpuestos.

No se seleccionaron participantes humanos ni se recopilaron datos de clientes reales. Los resultados se restringen a las condiciones registradas y no se generalizan automáticamente a otros módulos, versiones o despliegues.

## ED07. Instrumentos: arquitectura y entorno observado

**Dónde:** Descripción de los instrumentos → Caracterización arquitectónica del sistema. Buscar «Quedan fuera de la caracterización verificada, por el momento».

**Qué hacer:** Reemplazar ese párrafo y el siguiente. Mantener la Fig. 1 como modelo conceptual.

**Texto para insertar:**

La segunda etapa incorporó un entorno verificable con PostgreSQL 15 y Valkey 8.1 efímeros, solicitudes TCP hacia la aplicación ASGI en loopback y verificaciones HTTPS con una autoridad certificadora desechable. Chromium utilizó confianza temporal en ese certificado, sin desactivar su validación. Se emplearon cuentas y datos sintéticos, integraciones desactivadas y correo en memoria. Las versiones y condiciones efectivas se conservaron en los manifiestos de ejecución.

Este entorno complementa el modelo lógico de la Fig. 1; no convierte sus límites analíticos en segmentos físicos ni sus flechas en un orden universal de ejecución. No se verificaron un storefront público, un proxy de producción o replicación física de la base de datos. Los dos orígenes del navegador se diferenciaron por puerto dentro del mismo host, por lo que no representan una comprobación de cookies de terceros entre sitios distintos.

## ED08. Instrumentos de recolección y medición

**Dónde:** Instrumentos de recolección y medición. Buscar «La recolección se apoyará» y «Durante la fase documental».

**Qué hacer:** En los párrafos que presentan la Tabla II utilizar presente: «se apoya», «presenta», «permiten», «sirve», «convierte», «documenta», «debe incluir», «registra», «relacionan», «permite». Conservar I01-I07 y sus funciones. Reemplazar el último párrafo por el siguiente.

**Texto para insertar:**

Los registros preliminares de amenazas, requisitos y observaciones se complementaron con manifiestos de entorno, resultados JUnit y JSON, registros de herramientas, identificadores de ejecuciones y comprobaciones SHA-256. Los artefactos originales se conservaron junto con los intentos fallidos y las correcciones del entorno de pruebas. Las versiones públicas depuradas se distinguen de sus originales mediante procedencia y hashes propios. La existencia de un resultado automatizado no sustituye la interpretación técnica requerida en el registro de hallazgos ni la adjudicación individual de requisitos.

## ED09. Procedimiento de investigación y verificación

**Dónde:** Procedimiento de investigación y verificación. Desde «El procedimiento se organizará» hasta antes de «Criterios de análisis y validez».

**Qué hacer:** Sustituir la introducción y los seis apartados por esta versión; mantener los seis títulos como subtítulos del mismo nivel.

**Texto para insertar:**

El procedimiento conserva las seis etapas planteadas inicialmente e incorpora las actividades efectivamente realizadas y sus límites.

Fijación de la línea base y reconocimiento técnico. Se mantuvo el commit 4cb1609a90eade14b6275a407bc7a00c35698090 como referencia del producto [4]. La fuente utilizada en el ciclo final de pruebas fue eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7 y el checkout de integración de Actions fue 90455ca8abb7d72f707e0137e3ac80fab7a06dec. Estos identificadores distinguen el código base, la incorporación de pruebas y el entorno de ejecución. No se modificaron archivos funcionales de Saleor respecto de la línea base; los commits documentales posteriores no heredan automáticamente los resultados de ese checkout.

Identificación de activos y modelado de amenazas. Se identificaron cuentas, credenciales, permisos, información personal, pedidos y disponibilidad de la API. STRIDE [12] permitió organizar trece escenarios hipotéticos de riesgo. Sus prioridades expresan el interés de investigación, no frecuencias observadas ni severidades de vulnerabilidades confirmadas.

Derivación de requisitos y diseño de pruebas. Se organizaron veintitrés requisitos candidatos de ASVS 5.0.0 [5] y procedimientos orientados por WSTG 4.2 [6]. Se definieron precondiciones, actores, solicitudes y oráculos para distinguir aceptación, rechazo, datos devueltos y efectos sobre el estado. La relación entre ambos referentes requiere justificación individual; la ejecución de una prueba no adjudica por sí sola el cumplimiento de un requisito.

Ejecución de pruebas controladas. Se combinaron inspección manual, Bandit 1.8.6, Semgrep 1.153.0 y pruebas automatizadas. La evaluación dinámica incluyó escenarios positivos y negativos de autenticación, tokens, usuarios y pedidos, además de solicitudes HTTP y HTTPS y comprobaciones con Chromium. La interpretación examinó datos y errores GraphQL y, según el caso, código, mensaje, ruta, máscaras y ausencia de cambios indebidos, en lugar de limitarse al estado HTTP. Los resultados de regresión, batería focal, laboratorio y E2E se registraron como conjuntos diferenciados.

Análisis de evidencia y formulación de hallazgos. Se conciliaron resultados JUnit y JSON con sus inventarios y hashes. Las alertas estáticas requirieron revisión contextual: el B105 de Bandit corresponde al literal que nombra la cookie de renovación, clasificado como falso positivo de contraseña incrustada. Semgrep no produjo hallazgos con las reglas y exclusiones utilizadas, resultado que no demuestra ausencia universal de vulnerabilidades. Los resultados se incorporan al análisis mediante la distinción entre controles observados, caracterizaciones, brechas de evidencia y posibles desviaciones respecto de requisitos aplicables.

Reevaluación y documentación de limitaciones. Se corrigieron y reejecutaron problemas del entorno, del harness y de CI hasta cerrar la batería planificada sin fallos inesperados. Se conservaron dos XFAIL estrictos vinculados a P-ORDER-01, política provisional del escenario. Estas correcciones no constituyen mitigaciones de vulnerabilidades funcionales de Saleor. Las recomendaciones de producto que permanezcan propuestas deben identificarse como tales; su eventual implementación requerirá una modificación concreta y una comprobación antes y después.

## ED10. Criterios de análisis: cobertura y alcance

**Dónde:** Criterios de análisis y validez. Después de la explicación de la fórmula de cobertura.

**Qué hacer:** Conservar la fórmula y los cuatro estados del análisis. Insertar este párrafo después de «no demostrará cumplimiento de todas las disposiciones de ASVS».

**Texto para insertar:**

En esta etapa no se informa un porcentaje de conformidad o cobertura de requisitos: debe adjudicarse individualmente la aplicabilidad de los candidatos y la suficiencia de su evidencia antes de establecer el denominador y el numerador. Los 27 identificadores focales, sus 61 variantes y los resultados de regresión describen ejecución, no un porcentaje de seguridad. El estado PASS significa que se satisfizo el oráculo de una prueba; no implica automáticamente conformidad con ASVS ni aprobación de una política empresarial.

## ED11. Principios: permisos delegados y revocación

**Dónde:** Principios fundamentales identificados. Dos sustituciones dentro de los apartados existentes.

**Qué hacer:** Reemplazar el párrafo «La misma orientación puede observarse» y el párrafo «El Apéndice A documenta», respectivamente, por estos textos; no cambiar los títulos.

**Texto para insertar:**

La generación de tokens de terceros en saleor/core/jwt.py restringe los permisos mediante la intersección de los asociados con el usuario y los concedidos a la aplicación [4]. La segunda etapa complementó esta inspección con solicitudes de aplicaciones y credenciales delegadas que ejercitan condiciones de autorización. La evidencia respalda únicamente las combinaciones ejecutadas; no demuestra la protección de todos los consumidores posibles ni equivale al principio clásico de autorizaciones independientes.

El Apéndice A conserva las funciones que relacionan el cambio de jwt_token_key con la validación de identidad [4] y se amplía con pruebas de uso de credenciales antes y después de la revocación. La evidencia dinámica complementa el comportamiento previsto en el código, sin extender la conclusión a tipos de token, campos o rutas que no formen parte de los casos registrados.

## ED12. Principios: síntesis de evidencia

**Dónde:** Tabla III y párrafo que comienza «En conjunto, la revisión estática muestra».

**Qué hacer:** Actualizar la tercera columna de la Tabla III con la tabla de la guía y reemplazar el párrafo final por el siguiente.

**Texto para insertar:**

La revisión identifica mecanismos relacionados con los principios de diseño seguro y las pruebas aportan evidencia adicional sobre ciertas rutas de ejecución. La diferenciación de permisos, la revocación y los controles de renovación cuentan ahora con comprobaciones controladas. Sin embargo, esa evidencia no establece una política universal de denegación por defecto, mediación completa en toda la plataforma, independencia de autorizaciones o aislamiento de todos los componentes compartidos. Las correspondencias se interpretan como propiedades localizadas y límites de evaluación, no como una certificación integral.

## ED13. Riesgos: activos y priorización

**Dónde:** Análisis de riesgos. Buscar «Se consideran también las credenciales delegadas» y «Se identificaron trece escenarios hipotéticos».

**Qué hacer:** En el párrafo de activos, sustituir la frase condicional sobre aplicaciones por la primera oración siguiente. Reemplazar el párrafo completo de priorización por el segundo.

**Texto para insertar:**

Se incluyen las credenciales delegadas de aplicaciones externas, incorporadas mediante identidades sintéticas y combinaciones de permisos en el laboratorio.

Se identificaron trece escenarios hipotéticos: nueve con prioridad alta de investigación y cuatro con prioridad media. Esta clasificación inicial considera la sensibilidad de los activos, las consecuencias plausibles y su relación con las seis operaciones seleccionadas. Se conservan los identificadores R01–R13 para mantener la trazabilidad. Las prioridades no representan riesgo residual, frecuencia de ocurrencia ni puntuaciones CVSS. Aunque ya existen resultados experimentales, estos no permiten estimar la probabilidad operativa en una empresa ficticia ni en un despliegue productivo no evaluado. Por ello, no se modifica esa probabilidad a partir del número de pruebas aprobadas.

## ED14. Riesgos: tokens y sesiones

**Dónde:** Gestión de tokens y continuidad de las sesiones. Desde «Por ejemplo, tokensDeactivateAll» hasta antes de «Autorización de operaciones, objetos y campos».

**Qué hacer:** Reemplazar los tres párrafos explicativos conservando el párrafo introductorio de R04–R08.

**Texto para insertar:**

En R07, la inspección de tokensDeactivateAll y de la comparación de jwt_token_key se complementó con uso de credenciales antes y después de la revocación. La conclusión se limita a las rutas y tipos de credencial incluidos en las pruebas. El acceso a un recurso mediante un identificador compartido constituye una cuestión diferente: la comprobación de que el ID de pedido sigue resolviendo después de revocar no se interpreta como aceptación del token revocado ni como verificación de todos los campos del pedido.

Para R06 se ejecutaron verificaciones de renovación con cookies, valores CSRF válidos, ausentes e incorrectos y condiciones HTTPS y de navegador. Se comprobaron atributos de cookies y CORS en el laboratorio. Los dos orígenes utilizados difieren por puerto en el mismo host; por ello, el resultado no demuestra protección de cookies de terceros entre sitios distintos ni la seguridad integral de la sesión en producción.

Las comprobaciones de tipo y propósito de token aportan evidencia para las condiciones seleccionadas de R05. R04 y R08 conservan límites relacionados con una política de vida absoluta e inactividad no adoptada, rotación y ramas criptográficas no cubiertas completamente, y validación del destinatario. Conservar un valor de audiencia en un token no demuestra por sí mismo que todos sus receptores lo validen. Los resultados no autorizan a declarar conformidad general de estos escenarios.

## ED15. Riesgos: objetos, disponibilidad y delegación

**Dónde:** Autorización de operaciones, objetos y campos; Disponibilidad y permisos delegados.

**Qué hacer:** Reemplazar «El riesgo R11 consiste» por el primer párrafo. Reemplazar los dos párrafos de R12/R13 por los dos siguientes. Reemplazar el último párrafo de Análisis de riesgos por el cuarto.

**Texto para insertar:**

La evaluación de R10 y R11 compara actores con permisos diferentes y solicitudes sobre recursos propios y ajenos, distinguiendo autorización de operación, acceso al objeto y restricciones de campos. Para pedidos se incluyen identificadores UUID y legacy y un flujo de obtención legítima del UUID mediante la API. Las respuestas se interpretan según la ruta y el contrato aplicable. La política P-ORDER-01 continúa provisional; sus dos fallos esperados no se atribuyen a Saleor como vulnerabilidades oficiales ni demuestran enumeración de identificadores.

Para R12 se verificaron condiciones funcionales seleccionadas de complejidad y validación de solicitudes GraphQL con entradas acotadas. Los valores y configuraciones del laboratorio se registraron como parte de la evidencia. Estas verificaciones no constituyen pruebas de carga o estrés ni permiten demostrar resistencia frente a agotamiento distribuido de recursos.

R13 dejó de depender de una incorporación futura de aplicaciones: se ejecutaron combinaciones de cliente, personal, aplicación y delegación con permisos diferenciados. La evidencia permite estudiar el consumo de permisos en esas rutas, sin extenderse a todos los mecanismos de integración o destinatarios de tokens.

La trazabilidad mantiene la secuencia amenaza, requisito, componente, procedimiento y resultado. Los trece escenarios conservan su función de registro de riesgos, con evidencia de ejecución y límites explícitos. Su dictamen formal requiere analizar individualmente el requisito aplicable y las consecuencias del comportamiento observado; no se convierten en un inventario de vulnerabilidades por haber completado la batería de pruebas.

## ED16. Arquitectura: datos y actualización del modelo

**Dónde:** Arquitectura → Límites de confianza y párrafo de cierre anterior a «Síntesis de observaciones».

**Qué hacer:** Reemplazar «El tercer límite, T3» por el primer párrafo; reemplazar «En consecuencia, el diseño documentado» por el segundo.

**Texto para insertar:**

El tercer límite, T3, separa la lógica de aplicación de los datos y servicios que utiliza. En el laboratorio se identificaron PostgreSQL 15 y Valkey 8.1 efímeros. Los alias de base de datos utilizados por los hilos ASGI apuntaron a la misma base de pytest; esta configuración permite interpretar los casos ejecutados, pero no reproduce replicación física ni acredita aislamiento equivalente al de una infraestructura productiva. La evidencia describe el acceso y el estado de los recursos dentro del entorno controlado.

El diseño documentado se complementa con la configuración y las ejecuciones del laboratorio. Las Figs. 1 y 2 permanecen como modelos lógicos; no representan un storefront público ni la topología de producción. La aplicación directa de cabeceras reenviadas se estudió en condiciones controladas y no certifica la política de confianza de un proxy real. Las conclusiones arquitectónicas se restringen a los componentes y relaciones observados.

## ED17. Quince observaciones iniciales: continuidad y recomendaciones

**Dónde:** Síntesis de observaciones documentales y recomendaciones. Antes y después de la Tabla V.

**Qué hacer:** Reemplazar el párrafo anterior a la tabla por el primero y los tres posteriores por el segundo. Conservar H01–H15; aplicar los ajustes de recomendaciones indicados en la guía.

**Texto para insertar:**

La inspección inicial registró quince observaciones sobre autenticación, tokens, autorización, configuración y protección de la API [4]. Se conservan H01–H15 como antecedentes técnicos y no como quince vulnerabilidades confirmadas. La segunda etapa complementa estas observaciones con análisis estático automatizado y ejecuciones controladas. La Tabla V mantiene los mecanismos identificados; sus recomendaciones se interpretan a la luz de la evidencia posterior y de los límites que persisten.

Las pruebas permiten actualizar las recomendaciones inicialmente formuladas como verificaciones futuras. Allí donde existe evidencia, corresponde conservar el caso como regresión y precisar las condiciones que demuestra; donde persisten brechas, la recomendación debe indicar la comprobación o decisión pendiente. El catálogo de hallazgos de la segunda etapa debe explicar los enlaces y agrupaciones respecto de H01–H15, sin sustituir sus identificadores ni asumir una correspondencia uno a uno. Un resultado favorable, una caracterización y una desviación frente a una política provisional requieren interpretaciones diferentes.

## ED18. Apéndice A: revocación

**Dónde:** Apéndice A. Desde «Alcance de la evidencia» hasta antes de «Trazabilidad».

**Qué hacer:** Reemplazar los dos párrafos de alcance y verificación pendiente. Conservar código, fuente base e identificador EV-H08.

**Texto para insertar:**

Verificación realizada: La inspección de las funciones de revocación se complementó con pruebas controladas que ejercitan credenciales antes y después de tokensDeactivateAll. Se conservaron los resultados y las precondiciones de las rutas seleccionadas en la batería focal y en el laboratorio HTTP.

Alcance y limitaciones: La evidencia se refiere a las credenciales y operaciones efectivamente verificadas. Revocar una credencial no implica necesariamente invalidar un identificador de pedido que el diseño permita compartir. En el flujo LIVE-07, la aserción posterior a revocación comprueba que el ID del pedido sigue resolviendo; no demuestra por sí sola el comportamiento de todos sus campos. No se generaliza la conclusión a modalidades o rutas no ensayadas.

## ED19. Apéndice B: permisos y pedidos

**Dónde:** Apéndice B. Buscar «Limitaciones: No se han ejecutado pruebas cruzadas» y «Verificación pendiente: Preparar consultas equivalentes».

**Qué hacer:** Sustituir ambos párrafos. Conservar EV-H10, EV-H11 y EV-H12 y los listados existentes.

**Texto para insertar:**

Verificación realizada: Se ejecutaron consultas con actores y permisos diferenciados, incluidas cuentas propietarias y ajenas, solicitudes anónimas, personal, aplicaciones y delegación. Los casos examinan acceso a usuarios y pedidos, rutas UUID y legacy, restricciones de campos y un flujo de obtención legítima del UUID por la API. La interpretación considera los datos y errores GraphQL, no únicamente el estado HTTP.

Limitaciones: No se verificaron todos los campos de Order ni todos los recorridos de autorización de la plataforma. Las dos XFAIL de CM-T22 expresan la diferencia respecto de P-ORDER-01, política provisional del escenario. No constituyen dos vulnerabilidades oficiales, no establecen facilidad de adivinar UUID y no acreditan explotación de datos de clientes reales. Las conclusiones se restringen a las combinaciones documentadas.

## ED20. Apéndice C: HTTPS, cookies y CSRF

**Dónde:** Apéndice C. Desde «Limitaciones: No se ha verificado el comportamiento del middleware» hasta antes de «Trazabilidad».

**Qué hacer:** Reemplazar los dos párrafos. Conservar EV-H05–EV-H07 y el análisis estático que los precede.

**Texto para insertar:**

Verificación realizada: Se ejecutaron solicitudes HTTP y HTTPS y comprobaciones con Chromium en un laboratorio con datos sintéticos. Los casos de renovación incluyeron CSRF válido, ausente e incorrecto y la inspección de Secure, HttpOnly y SameSite. El navegador utilizó una autoridad certificadora desechable instalada temporalmente, sin ignorar errores TLS. Se comprobaron también condiciones CORS y se verificó el cierre del entorno y el retiro de la confianza temporal.

Limitaciones: Los dos orígenes del navegador difieren por puerto dentro del mismo host. La evidencia no equivale a una prueba de cookies de terceros entre sitios distintos, un storefront público o una política integral de sesiones en producción. Las condiciones de confianza de un proxy productivo, la vida absoluta y los tiempos de inactividad de negocio permanecen fuera de esta demostración.

## Tabla III: reemplazo de la columna de alcance

Conservar las otras dos columnas.

| Principio | Nuevo alcance de la observación |
|---|---|
| Mínimo privilegio | Rutas seleccionadas contrastadas con actores, apps y delegación; sin extrapolación a todos los consumidores. |
| Mediación completa | Comprobaciones localizadas y pruebas de acceso; cobertura de toda la plataforma no determinada. |
| Valores seguros por defecto | Rechazos seleccionados verificados; sin demostración de una política universal de denegación. |
| Separación de privilegios | Permisos diferenciados; independencia de autorizaciones no comprobada. |
| Reducción de confianza | Revocación, cookies y CSRF contrastados en laboratorio; límites de navegador, proxy y sesión explícitos. |
| Economía de mecanismo | Reutilización identificada; simplicidad no evaluada mediante una medición específica. |
| Minimización de mecanismos comunes | Servicios de laboratorio identificados; aislamiento productivo y replicación física no evaluados. |

## Tabla V: recomendaciones que deben actualizarse

Conservar los identificadores y la columna de observación estática. Las recomendaciones H01-H03, H05 y H10 pueden mantenerse como líneas de verificación, pero deben interpretarse junto al resultado concreto de cada caso; no describirlas todas como tareas todavía no iniciadas.

| ID original | Recomendación actualizada |
|---|---|
| H04 | Contrastar la configuración registrada con una política de vigencia, vida absoluta e inactividad que deberá definirse para el caso. |
| H06 | Conservar los casos CSRF válido/ausente/incorrecto como regresión y ampliar a clientes y contextos de origen no cubiertos. |
| H07 | Mantener las comprobaciones HTTPS y Chromium de atributos de cookie; verificar por separado el despliegue y los contextos entre sitios distintos. |
| H08 | Conservar la regresión antes/después de revocación y ampliar solo a rutas o modalidades de credencial aún no verificadas. |
| H09 | Completar la evidencia de rotación y ramas criptográficas no cubiertas y explicitar la política de destinatario; conservar aud no equivale a validarlo. |
| H11 | Mantener pruebas por actor, recurso y campos; extenderlas cuando se incorporen rutas o permisos no cubiertos. |
| H12 | Documentar diferencias entre UUID y legacy y su política de compartición; resolver la política provisional antes de adjudicar no conformidad. |
| H13 | Conservar las verificaciones funcionales de umbrales; planificar carga/estrés como evaluación distinta si el alcance posterior la requiere. |
| H14 | Definir y verificar por separado la política de confianza de un proxy de producción; no extrapolar pruebas directas de cabeceras. |
| H15 | Conservar las pruebas de intersección y consumo de permisos delegados y ampliar únicamente a consumidores o audiencias no cubiertos. |

## Ajustes puntuales adicionales para evitar contradicciones

- En el párrafo que comienza «La caracterización se contrastará» usar «La caracterización se contrastó»; no afirmar que se siguieron rutas no registradas.
- En «La Tabla II presenta los instrumentos previstos» eliminar «previstos». Conservar sus siete códigos.
- En «La Tabla III sintetiza las correspondencias establecidas durante la inspección» precisar «durante la inspección y las verificaciones seleccionadas».
- En la Tabla IV conservar título histórico, IDs, escenarios y prioridades. Cambiar la cabecera «Verificación propuesta» por «Verificación de referencia». Añadir al pie: «Registro inicial de hipótesis; la ejecución de comprobaciones no adjudica automáticamente el riesgo. El estado actual se determina mediante la evidencia y los límites expuestos en el análisis». No declarar los trece riesgos cerrados.
- En R03, sustituir «todavía falta determinar qué información recibe efectivamente el solicitante» por «la evaluación compara respuestas bajo condiciones seleccionadas; no demuestra por sí sola uniformidad temporal ni viabilidad de enumeración». Mantenerlo como hipótesis hasta su adjudicación.
- En Arquitectura, al final de «La ruta /graphql/ aparece decorada con csrf_exempt», sustituir el futuro «la evaluación deberá distinguir» por «la evaluación distingue».
- En «Además, el middleware encargado de determinadas cookies» conservar la explicación estática y sustituir su última oración por: «La segunda etapa contrastó estos atributos en el laboratorio HTTPS y Chromium; la evidencia sigue sin certificar todas las configuraciones de producción».
- No cambiar globalmente todos los futuros: objetivos, beneficios potenciales, recomendaciones y comprobaciones fuera de alcance conservan ese sentido.

## Corrección del código CSRF y de leyendas

En el Apéndice C, mover las dos líneas `if need_csrf:` y `cls.clean_csrf_token(csrf_token, payload)` que actualmente aparecen debajo de «Listado C.3. Atributos de la cookie de renovación» al final del **Listado C.2**, inmediatamente después de `payload = cls.clean_refresh_token(refresh_token)`. Mantener la indentación:

```python
need_csrf = refresh_token is None
refresh_token = cls.get_refresh_token(info, refresh_token)
payload = cls.clean_refresh_token(refresh_token)

if need_csrf:
    cls.clean_csrf_token(csrf_token, payload)
```

El Listado C.3 conserva solo sus atributos `httponly`, `secure` y `samesite` y la fuente middleware.py. No atribuir el bloque CSRF al middleware.

Mantener las figuras como modelos de código, aunque ya existan pruebas. Para la Fig. 3 usar: «Flujo lógico derivado de las funciones de revocación y validación. La figura representa el mecanismo inspeccionado; las pruebas que lo complementan se describen en este apéndice». Para la Fig. C.1 usar: «Flujo lógico simplificado de emisión y renovación según create_token.py, refresh_token.py y middleware.py [4]. Modelo derivado del código; su verificación dinámica se describe por separado».

## Procedencia de resultados para la sección de pruebas

Esta tabla se incorpora al desarrollar los nuevos apartados, antes de Referencias, en el mismo documento. No debe quedar únicamente como enlace externo.

| Conjunto | Resultado final | Interpretación |
|---|---|---|
| Regresión general | 17.613 PASS y 2 XFAIL | Incluye la batería focal; sin fallos inesperados |
| Batería focal | 59 PASS y 2 XFAIL; 27 IDs, 61 variantes | Subconjunto de la general; P-ORDER-01 provisional |
| Unidades y validadores independientes | 42 PASS | 30 unidades de producto y 12 validadores; no todo es prueba de producto |
| HTTP/HTTPS/Chromium C10 | 26 PASS | 25 variantes de perfil normal y un diagnóstico de guard writer exclusivo de pruebas |
| E2E original | 211 PASS | Suite diferenciada |
| Semgrep 1.153.0 | 2.608 archivos; 0 hallazgos y 0 errores | Reglas e ignores del repositorio; no demuestra ausencia de vulnerabilidades |
| Bandit 1.8.6 | 4.629 líneas; una alerta B105 LOW/MEDIUM | Literal refreshToken revisado como falso positivo de contraseña incrustada |

No sumar estos resultados como total de pruebas únicas: existen subconjuntos. En particular, los 36 casos unitarios del artefacto focal están incluidos en los 42 del laboratorio.

Fuente de pruebas: eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7. Checkout de Actions: 90455ca8abb7d72f707e0137e3ac80fab7a06dec. Regresión run 41522626061; focal 41522626285; laboratorio/E2E 41522626093; linters 41522626126. La procedencia completa, límites y hashes están en [CIERRE_PRUEBAS_TECNICAS.md](../CIERRE_PRUEBAS_TECNICAS.md) y [CIERRE_TECNICO.json](../evidencia/revalidacion_tecnica/CIERRE_TECNICO.json).

## Orden para continuar el manuscrito

Tras actualizar el contenido anterior, desarrollar antes de Referencias los apartados **Codificación segura**, **Análisis estático y dinámico**, **Pruebas de seguridad**, **Hallazgos y recomendaciones**, y **Discusión y límites**. Integrarlos con la arquitectura y metodología ya presentes, sin comenzar otro artículo. La redacción de estos bloques debe incluir el reanálisis A2-07, no copiar como definitivas las catorce observaciones del borrador auxiliar.

Conservar una única bibliografía IEEE y ajustar llamadas a tablas, figuras y anexos tras ensamblar el documento. Los resultados nuevos deben citar su propia procedencia. Antes de exportar, revisar secciones de tres/cuatro/dos columnas, anchura de la Tabla IV y la Fig. C.1 recortada en el render de revisión. Esta observación de maquetación es del control técnico, no del profesor.
