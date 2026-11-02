# Roadmap del segundo avance — CyberMarket CR / Saleor

**Versión:** 1.3. **Actualizado:** 2026-11-02. **Curso:** CY-703 Seguridad de Software. **Entrega:** segundo avance, valor 15 %. **Estado:** desarrollo autónomo autorizado en curso. **Etapas cerradas:** A2-00, A2-01, A2-02. **Siguiente etapa:** A2-03.

**Fecha límite fijada por el usuario:** domingo **8 de noviembre de 2026, 18:00**, zona America/Costa_Rica (UTC−06:00). Equivalente UTC: 9 de noviembre, 00:00. Es la fecha acordada para este plan; no se atribuye a una verificación del campus.

## 1. Propósito y fuentes de control

Desarrollar un informe grupal PDF que documente las fases de desarrollo y pruebas del software seleccionado, con los apartados obligatorios de codificación segura, análisis estático y dinámico, y pruebas de seguridad. Debe incluir al menos diez hallazgos con recomendaciones, resultados trazables, bibliografía y una explicación suficiente para defender las decisiones del grupo.

Este roadmap integra lo ya presentado y probado; no convierte los planes existentes en resultados ni inicia por sí mismo todas las ejecuciones previstas. Esta versión incorpora el cierre de A2-01 y mantiene la continuidad documental. La ejecución y la redacción de las fases posteriores se realizarán al avanzar el proyecto.

**Orden de autoridad:** consigna específica del segundo avance recibida el 2 de noviembre → programa y manual → materiales docentes pertinentes → primer avance presentado → código/evidencia versionados → notas y planes históricos. Una diferencia entre fuentes debe registrarse y resolverse para el punto concreto; no se elimina silenciosamente.

La consigna específica tiene tres páginas: descripción y requisitos en p. 1, instrucciones en p. 2 y rúbrica en p. 3. Su rúbrica usa seis criterios de dos puntos, total doce. El mínimo de diez hallazgos y la autorización del software son obligaciones de la consigna aunque no tengan fila independiente en la tabla de puntuación. El manual aporta metodología y análisis de resultados como contenido de soporte. No se han indicado en esta consigna un máximo de páginas, fecha/hora límite, pentest externo obligatorio o cantidad mínima de pruebas nuevas.

Original: [Segundo avance (evaluable)](https://chatgpt.com/library?file_id=libfile_a78770eba870819187a82a9dd430bbe6&account_id=personal). SHA-256: 82719d0216f9088a4a5e922295450aa8ad4603e3b80a98f1dc0a812596273d1e.

## 2. Dónde se conserva el trabajo

**Fuente operativa de estado:** esta carpeta en [GitHub, rama de investigación](https://github.com/Arkthos/saleor/tree/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2). El PR #1 permanece en borrador. La copia de este roadmap disponible en el proyecto debe reemplazarse conservando su identidad al cerrar cada etapa; GitHub conserva el historial de todos los cambios.

| Archivo o carpeta | Función |
|---|---|
| ROADMAP.md | Objetivo, ruta, actividades, dependencias y criterios de cierre |
| estado.json | Estados de etapas, siguiente acción, bloqueos, versión y referencia a la copia del proyecto |
| MATRIZ_RUBRICA.csv | Obligación → producto → evidencia → etapa → revisión |
| AJUSTES_AVANCE1.md | Qué se conserva, qué se actualiza y por qué, sin alterar el original |
| BITACORA.md | Qué se completó, comprobaciones, decisiones y punto de reanudación |
| FUENTES_Y_EVIDENCIAS.md | Fuentes, permisos de uso, procedencia y política de conservación |
| antecedentes/ | Lectura curricular y revisión del checkpoint, como fotografías históricas |
| evidencia/ | Manifiestos, resultados depurados, fichas y análisis futuros; hoy contiene guía de conservación |
| manuscrito/ | Estructura inicial y futuros borradores, tablas, figuras y referencias editables |
| plantillas/ | Fichas de pruebas y registro de hallazgos; las plantillas no son resultados |

Se guardarán también el razonamiento, decisiones, revisiones, borradores y productos del grupo. El chat es una superficie de trabajo; la última versión aceptada de cada producto debe pasar a GitHub. No redistribuir en el repositorio público libros, presentaciones completas, documentos con datos personales o archivos de terceros sin comprobar su permiso de publicación. Conservar para esos originales referencias, localizadores, enlaces y hashes; archivar los productos propios y la evidencia sintética depurada.

## 3. Punto de partida verificado

| Elemento | Estado al iniciar esta planificación |
|---|---|
| Primer avance | Presentado según el usuario; no se han recibido correcciones del profesor |
| Documento base | Proyecto final - primer avance(4).docx; texto extraído de 505 párrafos igual al Word del checkpoint, distinto hash y estructura interna |
| Alcance | Autenticación, tokens y autorización en tokenCreate, tokenRefresh, tokensDeactivateAll, me, user y order; utilidades directamente relacionadas como apoyo |
| Software base | Arkthos/saleor, 4cb1609a90eade14b6275a407bc7a00c35698090 |
| Rama al planificar | research/cybermarket-security-tests-v1; HEAD de entrada c442099bc0ebee5194a6e58354944563e92e0d28 |
| Evidencia experimental | C2–C9 sintético: 27 IDs, 61 variantes, 59 PASS y dos XFAIL esperados en registros consultados |
| Otras comprobaciones registradas | General: 17 613 PASS y dos XFAIL, incluyendo los casos CyberMarket; E2E: 211 PASS; validador de evidencia: seis PASS |
| Calidad del HEAD de entrada | Lint falló por espacios finales en documentación de semana 7; no es un fallo de autenticación del producto |
| Riesgos y observaciones | Trece riesgos iniciales y quince observaciones estáticas; todos los dictámenes formales de riesgo siguen NO_DETERMINADO |
| Trazabilidad normativa | CSV actual referencia 16 de los 23 ASVS iniciales; diez WSTG distintos frente a once seleccionados inicialmente |
| Trabajo pendiente | Clasificación completa W7-A, ampliaciones justificadas W7-B–F, C10 desplegado, juicio normativo y manuscrito del avance 2 |

Los resultados anteriores pertenecen a sus SHAs y runs. Un commit documental de este roadmap cambia HEAD, pero no constituye una nueva ejecución ni transfiere automáticamente un resultado histórico al SHA nuevo.

## 4. Ajustes con respecto al primer avance

| Se conserva | Se actualiza en una versión nueva | Cómo se comprobará |
|---|---|---|
| Título, problema, un objetivo general y tres específicos | Desarrollo operativo de los objetivos en método, resultados y recomendaciones | Tabla objetivo → sección → evidencia |
| Contexto CyberMarket ficticio y software real | Condiciones efectivas del laboratorio y límites de generalización | Inventario de entorno y manifiesto por ejecución |
| Seis operaciones y baseline del producto | Rama de pruebas y SHAs de ejecución, sin confundirlos con el producto base | Commit, checkout de Actions, run y hashes |
| Trece riesgos y quince observaciones iniciales | Estado actual, evidencia de seguimiento y recomendaciones del avance 2 | Cruce Hxx/Rxx → caso/evidencia → A2-Hxx |
| Instrumentos I01–I07 y selección intencional | Cuáles se aplicaron y cómo se recogieron y analizaron los datos | Instrumentos cumplimentados o equivalentes explícitos |
| Arquitectura conceptual | Diferencias entre arquitectura del código, entorno CI y despliegue si se hace | Figuras con versión, fuente y límites |
| Bibliografía IEEE de la entrega | Nuevas fuentes pertinentes y numeración por primera aparición | Auditoría afirmación–fuente–pasaje–cita |
| Primera entrega original | Ajustes de continuidad y estado técnico; no se inventan correcciones docentes | Registro de cambios con motivo y ubicación |

La frase histórica de que no hubo pruebas deja de describir el estado global actual; permanece válida como fotografía de la primera etapa. El segundo avance narrará las ejecuciones posteriores con precisión temporal. Las mejoras internas detectadas no deben presentarse como observaciones del profesor.

## 5. Productos exigidos y criterio de aceptación

| ID | Obligación | Producto de la entrega | Criterio para considerarla cubierta |
|---|---|---|---|
| R1 | Atender retroalimentación del avance 1 | Nota de continuidad y registro de ajustes | Se indica que no hay retroalimentación recibida; si llega, se procesa cada observación sin inventarla |
| R2 | Buenas prácticas de codificación segura | Revisión aplicada de componentes relevantes | Cada práctica incluye fundamento, implementación observada, evidencia, limitación y recomendación |
| R3 | Análisis estático y dinámico con herramientas | Métodos, alcance y resultados diferenciados | Herramienta/versión, configuración, rutas/casos, ejecución, triage y límites identificados |
| R4 | Casos de seguridad rigurosos | Plan y reporte detallado de pruebas | ID, actor, recurso, entrada, precondiciones, expectativa, observado, evidencia y dictamen; positivos y negativos pertinentes |
| R5 | Citas y bibliografía APA/IEEE | IEEE consistente en todo el manuscrito | Toda afirmación material rastreable; citas y lista corresponden y no contienen metadatos inventados |
| R6 | Ortografía y redacción | Informe revisado y defendible | Claridad, consistencia, ausencia de contradicciones y revisión del grupo |
| O1 | Autorización para usar software | Delimitación y respaldo documental | Licencia del commit y control del entorno documentados; no se infiere permiso para sistemas de terceros |
| O2 | Mínimo diez hallazgos y recomendaciones | Catálogo A2-Hxx y síntesis en el cuerpo | Al menos diez entradas sustantivas, diferenciadas y sustentadas, cada una con recomendación; sin fabricar vulnerabilidades ni dividir artificialmente una observación |
| O3 | Tres apartados obligatorios | Secciones identificables | Codificación segura; análisis estático/dinámico; pruebas de seguridad |
| O4 | Informe grupal PDF y autoría del grupo | PDF final y revisión del equipo | El grupo verifica, adapta y puede explicar su contenido; fuentes citadas y contribuciones reconocidas cuando corresponda |
| M1 | Método y análisis de resultados del manual | Metodología operativa y discusión | Se explica selección de unidades, instrumentos, recolección, resultados y propuesta aplicable |

No se asigna una nota anticipada. La columna de revisión de MATRIZ_RUBRICA.csv permanecerá pendiente hasta auditar el producto real.

## 6. Etapas y dependencias

Estados permitidos: PENDIENTE, EN_CURSO, BLOQUEADA, COMPLETADA y EXCLUIDA_JUSTIFICADA. Solo una etapa con productos y comprobaciones verificadas puede cerrarse. Una exclusión no satisface automáticamente un requisito obligatorio. El calendario de la sección 7 usa la fecha límite fijada por el usuario: 8 de noviembre, 18:00, hora de Costa Rica.

| Etapa | Producto principal | Dependencia | Estado inicial |
|---|---|---|---|
| A2-00 | Rúbrica interpretada, roadmap y archivo documental publicados | Ninguna | COMPLETADA al publicar este paquete |
| A2-01 | Línea base, condiciones de uso, recursos y calendario | A2-00 | COMPLETADA |
| A2-02 | Conciliación de requisitos, instrumentos y oráculos | A2-01 | COMPLETADA |
| A2-03 | Revisión de codificación segura y análisis estático | A2-02 | PENDIENTE |
| A2-04 | Plan de pruebas clasificado y selección de ampliaciones | A2-02 | PENDIENTE |
| A2-05 | Ejecución/revalidación CI y conservación de evidencia | A2-03, A2-04 | PENDIENTE |
| A2-06 | Validación HTTP seleccionada o exclusión motivada del despliegue | A2-04, A2-05 | PENDIENTE |
| A2-07 | Interpretación, mínimo diez hallazgos y recomendaciones | A2-03, A2-05, resolución A2-06 | PENDIENTE |
| A2-08 | Borrador completo, tablas, figuras y referencias | A2-07 | PENDIENTE |
| A2-09 | Auditoría de rúbrica/evidencia y PDF revisado | A2-08 | PENDIENTE |
| A2-10 | Versión congelada y entrega registrada | A2-09 y revisión final del grupo | PENDIENTE |

### A2-00 — Planificación y continuidad documental

**Hecho en esta versión:** lectura de las tres páginas de la consigna y verificación visual de la rúbrica; contraste con el primer avance, revisión del checkpoint y materiales; matriz de obligaciones; decisiones de continuidad; fases y criterios; estructura para guardar trabajo académico; instrucciones de actualización incorporadas en AGENTS.md y enlaces desde los índices existentes.

**Cierre:** archivos publicados juntos en GitHub y copia del roadmap disponible en el proyecto. Este cierre no acredita desarrollo de las fases posteriores. **Reanudación:** A2-01.

### A2-01 — Congelar la línea base de la entrega y organizar recursos

**Hacer:** registrar hashes del Word presentado, rúbrica, código base y lockfile; comprobar rama/PR/CI al retomar; completar inventario I01 de Python, servicios y settings no secretos; dejar documentado el uso académico del fork bajo su LICENSE y el laboratorio controlado. Aplicar la fecha límite del 8 de noviembre a las 18:00, hora de Costa Rica, y registrar la distribución real de responsabilidades cuando el grupo la confirme. Reservar tiempo para análisis y PDF.

**Resolver:** fallo documental de espacios finales y su revalidación pertinente; localizar artefactos históricos necesarios antes de depender de su disponibilidad. No volver a ejecutar todas las suites solo para corregir un documento si no aporta evidencia; distinguir checks de formato de la posterior revalidación experimental.

**Productos:** evidencia/linea_base.md, manifiesto de fuentes/entorno, calendario y roles en estado.json. **Cierre:** versiones y recursos identificados, autorización del entorno documentada, riesgos de acceso/retención anotados y siguiente fase ejecutable. La fecha del plan está fijada por el usuario; el reparto de responsabilidades aún debe registrar personas y disponibilidad reales.

**Cierre registrado de A2-01 (2026-11-02):** se comprobaron originales/hashes, baseline y diferencias del fork, configuración y versiones de la ejecución histórica, estado de CI y disponibilidad de artefactos. Se retiraron espacios finales de siete líneas del checkpoint de semana 7 y se comprobó localmente que el texto restante se conserva. El HEAD documental de entrada no tiene runs asociados; no hay nueva ejecución del producto ni revalidación completa remota. Esa comprobación y el archivo independiente de artefactos siguen para A2-05. La ausencia de Docker local y los roles grupales todavía sin asignar no bloquean A2-02. [Informe de línea base](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/linea_base.md) y [manifiesto](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/linea_base_manifest.json).

### A2-02 — Conciliar requisitos, riesgos y expectativas

**Hacer:** revisar los 23 ASVS iniciales y once WSTG; clasificar cada uno como pertinente, parcialmente cubierto, pendiente o no aplicable con razón. Conciliar los 16 ASVS/diez WSTG del CSV actual y el nuevo WSTG-IDNT-04. Investigar las siete ausencias ASVS de la columna actual y la falta explícita de H10 sin asumir que todo carece de evidencia. Mantener intacto el CSV histórico y crear una matriz derivada de avance 2.

**Definir:** expectativa por operación/actor/objeto/campo y autoridad de esa expectativa: requisito adoptado para el escenario académico, contrato del producto, observación o política propuesta. Resolver o mantener explícitamente provisional P-ORDER-01; la adopción por el grupo, si ocurre, será una decisión del caso ficticio y nunca una política oficial de Saleor. No requiere inventar aprobación de una empresa o del profesor.

**Productos:** evidencia/trazabilidad_avance2.csv, evidencia/criterios_y_oraculos.md y equivalencias I01–I07. **Cierre:** cada requisito inicial tiene disposición explícita y cada caso seleccionado tiene un criterio de interpretación; H, R, ASVS y WSTG no se confunden con unidades de conteo equivalentes.

### A2-03 — Codificación segura y análisis estático aplicado

**Hacer:** revisar módulos de autenticación, tokens, permisos, pedidos y validadores seleccionados. Documentar control, datos, fallas e interfaces, conforme a semana 7. Para codificación segura cubrir validación/representación, uso de APIs de seguridad, excepciones, secretos/configuración, privilegios, encapsulamiento y SOLID cuando aporte al código observado. No reducir el apartado a definiciones generales.

**Herramientas:** aprovechar Bandit acotado, Semgrep, mypy y demás checks existentes, distinguiendo función y alcance. Registrar versiones, reglas, exclusiones y comandos. Evaluar análisis de dependencias solo si puede ejecutarse y añade una pregunta concreta; no adoptar una herramienta por llenar una lista. Los resultados no ejecutados siguen pendientes. Conservar y justificar la alerta B105 sobre el nombre de cookie, sin convertirla en secreto expuesto.

**Productos:** evidencia/revision_codificacion.md, evidencia/analisis_estatico.md y reportes depurados/manifiestos. **Cierre:** prácticas aplicadas a rutas y decisiones reales, alertas interpretadas y limitaciones explícitas. Un parche al producto exige una desviación suficientemente fundamentada y un experimento separado; no se modifica el comportamiento para lograr tests verdes.

### A2-04 — Diseñar y clasificar las pruebas

**Hacer:** aplicar W7-A como manifiesto derivado: test_level, test_design, dependencias, assertion_scope, normative_status y evidence_ref para CM-T01–T27. Distinguir unidad/integración/sistema de caja negra/blanca/gris y de pruebas estáticas/dinámicas. Reconocer las pruebas directas ya existentes antes de diseñar CM-U.

**Seleccionar ampliaciones:** solo las que resuelvan brechas de rúbrica, requisito u oráculo. Candidatos: límites de utilidades aislables; estados/tipos de token; errores e identificadores; permisos de usuarios y campos de pedidos; negativos que verifiquen ausencia de datos y efectos laterales. Preferir fixtures existentes para comportamiento integrado; usar mocks/stubs solo para aislamiento justificado. No duplicar tests ni medir cobertura de ramas por conteo de casos.

**Productos:** evidencia/plan_pruebas.md, manifiesto derivado y fichas por caso; lista justificada de ampliaciones y de casos reutilizados. **Cierre:** cada caso tiene precondiciones, esperado independiente del observado, dependencias, salida y relevancia. Una prueba puede seleccionarse y quedar aún no ejecutada.

### A2-05 — Ejecutar, revisar y conservar la evidencia CI

**Hacer:** implementar las ampliaciones seleccionadas en A2-04; ejecutar el subconjunto pertinente y checks requeridos por el cambio. Ante defectos reales del harness, corregirlos, añadir regresión cuando corresponda y reejecutar. Cuando se cierre el paquete experimental, registrar suite focal, controles de evidencia y checks generales/E2E pertinentes sobre un SHA identificado, sin sumar subconjuntos.

**Capturar:** timestamp, SHA de rama y checkout, versiones, configuración, IDs/variantes, esperado/observado, PASS/FAIL/ERROR/SKIP/XFAIL/XPASS, JUnit/JSON y hashes. Separar pruebas del producto de las del validador. Una ejecución cancelada o un artefacto ausente no se convierte en éxito.

**Conservar:** resultados sintéticos depurados y un resumen por caso bajo evidencia/, más un manifiesto del archivo externo si contiene bytes no aptos para Git. Verificar hashes antes de interpretar. No depender únicamente de artefactos Actions que caducan. **Cierre:** inventario esperado concuerda con ejecutado, resultados explicados y evidencia recuperable. Un fallo de seguridad observado puede formar parte del resultado; no se exige ocultarlo ni cambiar el oráculo.

### A2-06 — Decidir y ejecutar la validación desplegada pertinente

**Decisión al entrar:** evaluar si la pregunta del estudio necesita transporte real para afirmar algo sobre cookies, origen, proxy o configuración. La rúbrica exige análisis dinámico y casos rigurosos, pero no dice que todas las pruebas deban ser DAST externo. El CI ejecutado cuenta como dinámica dentro de sus límites.

**Ruta recomendada si hay recursos:** C10 reducido y controlado, empezando por LIVE-01–04 sobre HTTP aislado para contraste UUID/legacy y errores; añadir LIVE-05–07 cuando existan políticas y componentes verificables. HTTPS/navegador son necesarios para concluir sobre sus propiedades específicas. Mantener cuentas/datos sintéticos, integraciones externas desactivadas, versiones fijadas y teardown.

**Ruta si no se dispone del entorno:** registrar no ejecución, razón, alcance que queda sin determinar y efecto sobre conclusiones. No afirmar cookies seguras en navegador, confianza de proxy, fuga en storefront o despliegue verificado. Si faltase evidencia para un requisito obligatorio, la exclusión no lo resuelve y debe volver al plan.

**Productos:** evidencia/decision_c10.md y, si se ejecuta, manifiesto/HTTP/JUnit depurados y cierre del entorno. **Cierre:** resultados reales revisados o una exclusión de alcance justificada. El despliegue completo del curso no se adelanta automáticamente al segundo avance.

### A2-07 — Analizar resultados y producir hallazgos

**Hacer:** sintetizar por objetivo y tema, contrastando estática, ejecución y criterio adoptado. Actualizar I03, I04 e I06 y construir al menos diez entradas A2-Hxx sustentadas. Cada una debe explicar condición, evidencia, relevancia, alcance, recomendación y modo de comprobarla. Mantener vínculo con Hxx/Rxx históricos y evitar contar variantes de un mismo hecho como hallazgos distintos sin justificación.

**Interpretación:** separar buena práctica observada, caracterización, limitación de entorno, alerta descartada, brecha de trazabilidad, discrepancia de política y vulnerabilidad demostrada. Una limitación debe aportar análisis y recomendación concreta; no usar diez frases genéricas para cumplir el mínimo. No hay cuota de diez vulnerabilidades.

**Productos:** evidencia/hallazgos_avance2.csv y evidencia/analisis_resultados.md, con matriz de tratamiento y retest posible. **Cierre:** diez o más hallazgos sustantivos revisados, recomendaciones proporcionadas, estados normativos con razón y discusión de amenazas a la validez. Si la evidencia solo sustenta NO_DETERMINADO, se conserva y se explica.

### A2-08 — Construir el manuscrito y sus anexos

**Hacer:** redactar sobre una copia nueva, conservando objetivos y primera entrega. Usar la estructura acordada en manuscrito/ESTRUCTURA.md. Integrar prácticas, métodos, resultados y discusión; el cuerpo debe ser comprensible sin abrir GitHub. Llevar tablas extensas, fichas y trazas a anexos con llamadas explícitas desde el texto.

**Fuentes y estilo:** EvidenceSynth MAP/GAP/AUDIT para afirmaciones materiales; IEEE continuo; redacción técnica accesible y revisión de naturalidad sin borrar matices. Verificar versión y pasaje antes de incorporar nuevas fuentes. Los informes anteriores son productos del proyecto y apuntan a evidencia primaria; no sustituyen por sí solos las fuentes científicas o normativas.

**Productos:** manuscrito editable, referencias completas, tablas, diagramas con fuente y borrador de PDF. **Cierre:** los tres apartados obligatorios están desarrollados, mínimo diez hallazgos aparecen de forma localizable y cada objetivo tiene respuesta acotada. Esta etapa no está ejecutada al publicar el roadmap.

### A2-09 — Auditar rúbrica, evidencia y PDF

**Hacer:** revisar fila por fila R1–R6/O1–O4/M1 y completar ubicación concreta, fuerza de la evidencia y brechas. Reconciliar conteos, referencias, figuras, anexos, SHAs, términos y resultados. Buscar activamente inferencias indebidas: PASS=seguridad, XFAIL=corregido, mapping=cumplimiento, CI=navegador y ficticio=datos reales.

**Formato:** exportar PDF, renderizar todas sus páginas y comprobar legibilidad a tamaño de lectura, tablas, diagramas, cortes, encabezados y referencias. Confirmar con el grupo su aportación y autoría; revisar paráfrasis y citas, sin prometer unicidad basada en un detector. Preparar preguntas breves de defensa sobre método, evidencia, hallazgo principal y limitaciones.

**Productos:** manuscrito corregido, auditoría final de rúbrica, PDF revisado y defensa. **Cierre:** todas las obligaciones localizadas, sin contradicciones materiales o afirmaciones sin respaldo; pendientes residuales descritos con impacto en alcance. Ninguna nota se considera evaluación oficial.

### A2-10 — Congelar, entregar y cerrar

**Hacer:** producir versión numerada y hash del PDF final, registrar revisión final del grupo y guardar editable, PDF propio, referencias, anexos y manifiesto bajo una carpeta de entrega versionada. La constancia del campus se conserva en el proyecto o almacenamiento privado si muestra datos personales; en GitHub basta un registro depurado.

**Distinción de estado:** LISTO_PARA_ENTREGAR no significa ENTREGADO. La carga al campus solo se marca cuando el usuario o un comprobante verificable confirme que ocurrió. Una nueva corrección posterior genera nueva versión; no sobrescribe silenciosamente la versión entregada.

**Cierre:** confirmación verificable de la entrega, versión/hora registradas y último checkpoint actualizado. Si el grupo aún no ha revisado o no ha cargado, la etapa permanece abierta en ese punto.

## 7. Secuencia de trabajo y prioridad

**Calendario de trabajo acordado:** del lunes 2 al domingo 8 de noviembre de 2026. Todas las horas indicadas corresponden a Costa Rica. Son metas de planificación; las etapas siguen pendientes hasta cumplir sus criterios y registrar evidencia.

| Fecha objetivo | Etapas | Resultado esperado al cierre de la jornada |
|---|---|---|
| Lunes 2 de noviembre | A2-00; A2-01–02 | Plan publicado; preparar baseline, recursos, requisitos y oráculos. A2-00 y A2-01 cerradas; A2-02 permanece pendiente al actualizar este calendario. |
| Martes 3 de noviembre | A2-03–04 | Revisión de codificación/estática y plan de pruebas clasificado, con ampliaciones justificadas |
| Miércoles 4 de noviembre | A2-05 | Ejecución/revalidación pertinente, resultados reconciliados y evidencia conservada |
| Jueves 5 de noviembre | A2-06–07 | Resolver C10 con alcance viable o exclusión motivada; catálogo de diez o más hallazgos y recomendaciones sustentados |
| Viernes 6 de noviembre | A2-08 | Borrador completo, referencias, tablas y anexos |
| Sábado 7 de noviembre | A2-09 | Auditoría de rúbrica/evidencia, correcciones y PDF revisado visualmente |
| Domingo 8, 09:00–12:00 | A2-10 | Revisión final del grupo y resolución de observaciones |
| Domingo 8, 12:00–15:00 | A2-10 | Congelar PDF/versión/hash y preparar entrega |
| Domingo 8, 15:00–18:00 | A2-10 | Margen para carga y comprobación; fecha límite 18:00. Solo marcar ENTREGADO con confirmación verificable. |

**Puntos de control:** al terminar el miércoles revisar brechas de evidencia; al terminar el jueves resolver qué entra en el manuscrito; el viernes priorizar la redacción completa; reservar el sábado para auditoría y el domingo para revisión/carga. Si una meta se retrasa, actualizar fechas de las tareas y alcance de ampliaciones sin mover la fecha límite por cuenta propia.

**Si el plazo se acorta:** proteger primero las obligaciones de la consigna, la calidad del análisis de evidencia ya disponible y el tiempo de revisión del PDF. Reducir ampliaciones exploratorias y justificar C10 parcial/excluido antes de eliminar un apartado obligatorio. No fabricar ejecución ni reciclar resultados de otro SHA para ahorrar tiempo. A2-03 y A2-04 pueden avanzar en paralelo como actividades si hay personas disponibles; las dependencias de interpretación y cierre siguen vigentes.

**Roles por asignar:** coordinación/autoría del informe; análisis de código y requisitos; pruebas/entorno; revisión de evidencia y forma. Una persona puede cubrir varios roles. No se inventan nombres, aprobaciones ni participación; registrar contribuciones reales. La revisión distinta del ejecutor es recomendable cuando el equipo pueda organizarla.

## 8. Regla de actualización al cerrar cada etapa

Toda persona o agente que trabaje en CyberMarket debe leer esta versión y AGENTS.md antes de continuar. Una etapa se cierra con este procedimiento:

1. Guardar sus productos reales: texto, matrices, fuentes/localizadores, análisis, código si lo hubo y evidencia depurada.
2. Comprobar los criterios de salida y documentar qué respalda la conclusión; registrar exclusiones o bloqueos.
3. Actualizar ROADMAP.md (versión, estado, siguiente etapa), estado.json (estado y evidencia), MATRIZ_RUBRICA.csv (productos/ubicación/revisión) y BITACORA.md (qué cambió y cómo se validó).
4. Registrar decisiones nuevas; las de arquitectura o negocio de alto nivel usan docs/adr/ según las reglas del repositorio. No reemplazar una política de producto por una preferencia académica tácita.
5. Publicar los archivos relacionados en un mismo commit cuando sea posible. Conservar SHA de prueba separado de SHA documental; no reescribir el historial.
6. Reemplazar la copia del roadmap de este proyecto manteniendo el mismo archivo y su historial. Registrar en estado.json la referencia de esa copia. Si una réplica falla, indicar cuál está al día y cuál pendiente antes de anunciar cierre documental completo.
7. Informar al usuario: etapa cerrada, productos, comprobaciones, limitaciones y próxima acción. No afirmar que se actualizó un lugar donde no se pudo guardar.

Esta es una regla operativa persistida, no una sincronización automática en segundo plano. El estado de GitHub se consulta al reanudar para evitar divergencias. Si se interrumpe una tarea, registrar el estado parcial y la siguiente acción antes de salir; no marcar COMPLETADA por haber preparado un borrador.

## 9. Riesgos del desarrollo de esta entrega

| Riesgo | Respuesta prevista |
|---|---|
| Mezclar fases históricas | Etiquetar fecha, baseline, run y condición de cada resultado; conservar antecedentes como fotografías |
| Volumen grande sin análisis | Ordenar por pregunta y evidencia; seleccionar pruebas por brecha y no por cantidad |
| Artefactos que caducan | Guardar resultados depurados y manifiestos verificados al cerrar A2-05 |
| Política de pedidos indefinida | Separar caracterización de juicio normativo y resolver/adoptar supuestos explícitos en A2-02 |
| Exigir todo el curso en avance 2 | Usar la consigna específica; reservar despliegue integral, mantenimiento e incidentes para el alcance que corresponda |
| Reescritura silenciosa del avance 1 | Original preservado, registro de ajustes y versión nueva |
| Retrasos o disponibilidad insuficiente | Fecha límite fijada al 8 de noviembre, 18:00; proteger auditoría/carga y reducir ampliaciones justificadamente, registrando recursos reales |
| GitHub contiene solo código o resúmenes | Versionar también matrices, razonamiento, borradores, anexos y auditorías propias |
| Publicar material ajeno o datos innecesarios | Conservar originales donde ya están; publicar referencias, hashes y productos propios depurados |

## 10. Próxima acción concreta

Continuar A2-03 conforme a sus criterios de salida. El usuario autorizó avanzar autónomamente todas las etapas preparatorias, guardando productos y reportando cada cierre. La revisión final del grupo y una carga real al campus no se simulan.

**Referencias de continuidad:** [rúbrica original](https://chatgpt.com/library?file_id=libfile_a78770eba870819187a82a9dd430bbe6&account_id=personal), [primer avance presentado](https://chatgpt.com/library?file_id=libfile_df58994acdec819181215cec7155ca14&account_id=personal), [matriz histórica de pruebas](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/test_matrix.csv), [cierre experimental](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md), [plan de semana 7](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md), [plan C10](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/C10_live_validation_roadmap_team_handoff.md), [contexto curricular](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/antecedentes/Contexto_Curricular_CY703_2026-11-02.md) y [revisión del checkpoint](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/antecedentes/Revision_Checkpoint_CyberMarket_2026-11-02.md). Los dos últimos informes preceden a la recepción de la rúbrica específica: su antigua ausencia queda resuelta en esta planificación.

## 11. Cierres del desarrollo autónomo

**A2-02, 2026-11-02 — COMPLETADA:** Conciliados los 23 ASVS y la unión de doce WSTG; se separan mappings históricos de relaciones nuevas, siete instrumentos y oráculos por familia. P-ORDER-01 permanece provisional y todos los dictámenes normativos NO_DETERMINADO. No hay pruebas nuevas en esta fase documental. Productos: [trazabilidad_avance2.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/trazabilidad_avance2.csv); [tecnicas_avance2.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/tecnicas_avance2.csv); [criterios_y_oraculos.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/criterios_y_oraculos.md).
