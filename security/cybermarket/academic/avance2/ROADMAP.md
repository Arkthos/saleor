# Roadmap del segundo avance — CyberMarket CR / Saleor

**Versión:** 1.24. **Actualizado:** 2026-11-02. **Curso:** CY-703 Seguridad de Software. **Entrega:** segundo avance, valor 15 %. **Estado:** validación técnica en ejecución; Actions reactivado y entregable pausado. **Siguiente etapa:** conciliación técnica final.

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
| A2-03 | Revisión de codificación segura y análisis estático | A2-02 | COMPLETADA |
| A2-04 | Plan de pruebas clasificado y selección de ampliaciones | A2-02 | COMPLETADA |
| A2-05 | Ejecución/revalidación CI y conservación de evidencia | A2-03, A2-04 | REABIERTA |
| A2-06 | Validación HTTP seleccionada o exclusión motivada del despliegue | A2-04, A2-05 | REABIERTA |
| A2-07 | Interpretación, mínimo diez hallazgos y recomendaciones | A2-03, A2-05, resolución A2-06 | PENDIENTE_REANALISIS |
| A2-08 | Borrador completo, tablas, figuras y referencias | A2-07 | PAUSADA_HASTA_CIERRE_TECNICO |
| A2-09 | Auditoría de rúbrica/evidencia y PDF revisado | A2-08 | PAUSADA_HASTA_CIERRE_TECNICO |
| A2-10 | Versión congelada y entrega registrada | A2-09 y revisión final del grupo | PAUSADA_HASTA_CIERRE_TECNICO |

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

**Última ejecución validada:** [run 41517858406](https://github.com/Arkthos/saleor/actions/runs/41517858406), fuente `f1f883d545b44cdd8699a33b3162b7d2486c080b`, checkout `daf9178add04f18c148b84953a32159413e43ea5`. C10 26 PASS, focal 59 PASS/2 XFAIL, unidades/validadores 42 PASS. Regresión general, E2E y linters por conciliar; alerta heredada de licencias en revisión. Gate global abierto; entregable pausado.

Por instrucción del usuario, completar todas las pruebas técnicas necesarias antes de generar otra versión del entregable. Se reabren A2-05/A2-06 y queda pendiente el reanálisis de A2-07. A2-08/A2-09/A2-10 quedan pausadas. Los PDF anteriores se conservan como fotografías del alcance anterior; no son una entrega técnicamente definitiva.

| Bloque | Objetivo | Criterio de cierre |
|---|---|---|
| VT-01 | Entorno y nueva integración | SHA actual, PostgreSQL/caché identificados, focal y unidades ejecutadas y resultados archivados |
| VT-02 | Estática y calidad | Bandit/Semgrep/revisión y linters ejecutados; alertas interpretadas |
| VT-03 | Servicio HTTP real | LIVE-01 a LIVE-05 con identidades sintéticas, resultados por actor/campo y oráculos explícitos |
| VT-04 | Transporte y navegador | LIVE-06 sobre HTTPS privado; cookies, CSRF, CORS y proxy con positivos y negativos |
| VT-05 | Ciclo de identificadores y estado | LIVE-07 por flujo legítimo; renovación/revocación y requisitos de audiencia/sesión acotados |
| VT-06 | Regresión y cierre | General/E2E sobre fuente nueva, conteos reconciliados, hashes, redacción de trazas y teardown comprobado |
| VT-07 | Control heredado de licencias | Alternativa declarada trazable y limitada al hash/versionado; reglas originales, stdin explícito y negativo GPL verificados en CI |

Cada bloque debe conservar fallos e intentos iniciales, correcciones y retest. Una caracterización que aprueba no adjudica P-ORDER-01. El cierre técnico exige ejecución real o un bloqueo explícito; no se sustituye por redacción académica. Mantener la fecha límite acordada sin adelantar la generación del informe.

**Referencias de continuidad:** [rúbrica original](https://chatgpt.com/library?file_id=libfile_a78770eba870819187a82a9dd430bbe6&account_id=personal), [primer avance presentado](https://chatgpt.com/library?file_id=libfile_df58994acdec819181215cec7155ca14&account_id=personal), [matriz histórica de pruebas](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/test_matrix.csv), [cierre experimental](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/INFORME_CIERRE_C2_C9_AUDITADO_2026-10-18.md), [plan de semana 7](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/CHECKPOINT_SEMANA7_PRUEBAS_MULTINIVEL_2026-10-20.md), [plan C10](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/C10_live_validation_roadmap_team_handoff.md), [contexto curricular](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/antecedentes/Contexto_Curricular_CY703_2026-11-02.md) y [revisión del checkpoint](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/antecedentes/Revision_Checkpoint_CyberMarket_2026-11-02.md). Los dos últimos informes preceden a la recepción de la rúbrica específica: su antigua ausencia queda resuelta en esta planificación.

## 11. Cierres del desarrollo autónomo

**A2-02, 2026-11-02 — COMPLETADA:** Conciliados los 23 ASVS y la unión de doce WSTG; se separan mappings históricos de relaciones nuevas, siete instrumentos y oráculos por familia. P-ORDER-01 permanece provisional y todos los dictámenes normativos NO_DETERMINADO. No hay pruebas nuevas en esta fase documental. Productos: [trazabilidad_avance2.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/trazabilidad_avance2.csv); [tecnicas_avance2.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/tecnicas_avance2.csv); [criterios_y_oraculos.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/criterios_y_oraculos.md).

**A2-03, 2026-11-02 — COMPLETADA:** Revisión aplicada de trece puntos en control/datos/fallas/interfaces; Bandit 1.8.6 produjo una alerta B105 revisada como falso positivo y Semgrep 1.153.0 cero hallazgos en cinco reglas/21 archivos. Se conservan reportes y hashes; no se afirma seguridad global, SCA o CI completo. Productos: [revision_codificacion.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/revision_codificacion.md); [revision_manual.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/revision_manual.csv); [analisis_estatico.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/analisis_estatico.md); [run_manifest.json](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/estatica/run_manifest.json).

**A2-04, 2026-11-02 — COMPLETADA:** Clasificados los 27 casos históricos por cuerpo/dependencias y documentada la dependencia de fixtures globales. Diseñadas diez unidades CM-U para firma, exp, nbf, CSRF, ofuscación y bordes; oráculos independientes y resultados todavía no ejecutados en este cierre de diseño. Productos: [plan_pruebas.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/plan_pruebas.md); [clasificacion_pruebas.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/clasificacion_pruebas.csv).

**A2-05, 2026-11-02 — COMPLETADA:** Ejecutadas 30 variantes de diez unidades y doce invocaciones de validadores: 42 PASS sin warnings en la corrida final. Recuperados/verificados tres ZIP históricos y checksums internos disponibles; XML focal 59 PASS/2 XFAIL y general 17613 PASS/2 XFAIL reconciliados. Se preservan intentos iniciales y límites; no hay revalidación integrada nueva ni despliegue. Productos: [resultados_ejecucion.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/resultados_ejecucion.md); [resultados_ci_manifest.json](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/resultados_ci_manifest.json); [isolated.xml](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/ejecucion_local/isolated.xml); [archivo_verificado_manifest.json](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/historica_2026-10-20/archivo_verificado_manifest.json).

**A2-06, 2026-11-02 — COMPLETADA:** C10 excluido de la ejecución de este avance por recursos comprobados; LIVE-01–07 permanecen NOT_EXECUTED. La dinámica existente se limita a CI histórico verificado y unidades locales; no se afirman propiedades de HTTP/HTTPS, navegador, proxy o frontend. Se cierra la decisión de alcance, no una validación desplegada. Productos: [decision_c10.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/decision_c10.md).

**A2-07, 2026-11-02 — COMPLETADA:** Analizadas tres capas de evidencia y elaborados catorce hallazgos sustantivos con recomendación y verificación propuesta, vinculados a H/R y casos. Se distinguen controles positivos, caracterización y brechas; no se inventan CVSS, correcciones de producto o aprobación de P-ORDER-01. Límites de CI integrado y C10 conservados. Productos: [hallazgos_avance2.csv](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/hallazgos_avance2.csv); [hallazgos_avance2.json](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/hallazgos_avance2.json); [analisis_resultados.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/evidencia/analisis_resultados.md).

**A2-08, 2026-11-02 — COMPLETADA:** Manuscrito integrado con metodología, tres apartados obligatorios, catorce hallazgos, doce referencias IEEE y anexos de instrumentos, 27 casos históricos, diez unidades nuevas y 23 requisitos. Se corrigieron dos localizadores de código sin alterar evidencia bruta. Productos: [INFORME_AVANCE2.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/INFORME_AVANCE2.md); [REFERENCIAS_IEEE.json](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/REFERENCIAS_IEEE.json); [generar_docx.py](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/generar_docx.py).

**A2-09, 2026-11-02 — COMPLETADA:** Auditoría documental, técnica y visual completada. PDF de trece páginas y Word de revisión guardados; versión pública sin nombres personales en GitHub. Se conciliaron doce citas, catorce hallazgos, 23 requisitos, nueve checksums y los XML. Guía de defensa disponible. Revalidación integrada nueva y C10 siguen sin ejecutarse; revisión grupal y campus pendientes. Productos: [auditoria_final.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/auditoria_final.md); [auditoria_final.json](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/auditoria_final.json); [GUIA_DEFENSA.md](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/GUIA_DEFENSA.md); [CyberMarket_Segundo_Avance_publico.pdf](https://github.com/Arkthos/saleor/blob/research/cybermarket-security-tests-v1/security/cybermarket/academic/avance2/manuscrito/entrega/CyberMarket_Segundo_Avance_publico.pdf).

**A2-10, 2026-11-02 — PREPARACIÓN TERMINADA, etapa EN_CURSO:** PDF y Word de revisión guardados, PDF público preservado en GitHub, manifest con SHA-256 y guía de carga. La revisión grupal y el comprobante del campus siguen pendientes. No se cierra una entrega no realizada.

## 12. Reapertura técnica solicitada por el usuario

**2026-11-02 — VT-00 completada:** entregable pausado; A2-05/A2-06 reabiertas. Se comprobó el HEAD 34891bfd y se preparó un checkout limpio. El entorno sigue sin Docker/PostgreSQL y no admite cambio de UID; se prioriza un laboratorio efímero en CI con servicios reales. El workflow focal no seleccionaba las unidades nuevas de tests/; se corrige su cobertura y sus rutas de activación. No hay nueva ejecución integrada declarada todavía.

**2026-11-02 — VT-01 preparación completada, ejecución BLOQUEADA:** implementadas 25 variantes C10 y workflow integral manual en e2e.yml. Ruff, formato, AST, YAML, lockfile y colección verificados. Smoke local HTTP/HTTPS con CA válida y teardown aprobado tras corregir un fallo inicial de cierre. No son resultados de casos GraphQL con DB ni del navegador. GitHub muestra workflows deshabilitados por escala de uso; requiere reactivación del mantenedor. Consultar [preflight](evidencia/revalidacion_tecnica/preflight.json) y [laboratorio](../../live/README.md). No se genera otro entregable hasta cerrar el gate técnico.

**2026-11-02 — Bloqueo CI resuelto, validación en curso:** comprobados los guards de tareas programadas heredadas en el fork; Actions reactivado en sesión autenticada. Despachado manualmente e2e.yml sobre rama de investigación. Run 41512875410, fuente 1c87cf5. No hay resultados finales todavía y no se genera otro entregable.

**2026-11-02 — Intento técnico 01 conservado:** job 125508906856 falló instalando Playwright 1.56.0 sobre ubuntu-latest, que resolvió a Ubuntu 26.04. Ningún C10 se ejecutó. Se fija Ubuntu 24.04 y se conserva evidencia incluso si el setup falla; la suite E2E del mismo run es independiente. Próximo: nueva ejecución del laboratorio, sin repetir E2E si ya aprobó sin cambios en su código.

**2026-11-02 — Activación automática del laboratorio:** C10 corre también para pull_request en el fork, con runner Ubuntu 24.04. La regresión general y linters se obtienen de los workflows existentes; el job de laboratorio solo los repite si se solicita include_regression en una ejecución manual. Esto evita repetir la suite completa por cada corrección del harness. Nuevos resultados pendientes de revisión.

**2026-11-02 — Intento 02 conservado y harness corregido:** focal 59 PASS/2 XFAIL, unidades/validadores 42 PASS; C10 1 PASS/24 FAIL. Los hilos ASGI abrían el alias replica sobre la base sin esquema, porque el fake de pytest solo aplica al hilo principal. Se enlazan ambos alias reales a la base test antes de servir y se restaura configuración al cerrar. No se debilitan aserciones de autorización. Semgrep ampliado detectó 48 ejemplos deliberados en .semgrep; se conserva su salida y se excluyen los archivos de prueba de reglas en el retest, como hace pre-commit. E2E independiente 211 PASS verificado desde XML y hashes.

**2026-11-02 — Intento 03 conservado; retest preparado:** focal 59 PASS/2 XFAIL y unidades/validadores 42 PASS. HTTP/HTTPS/navegador 23 PASS/2 FAIL: se completa el contrato exacto de coste GraphQL y se distingue middleware normal del producto frente al guard de routing exclusivo de pruebas. Se añade un diagnóstico independiente que conserva ese error exacto; quedan 26 variantes para retest. Cliente HTTP acotado compatible con Semgrep, sin exclusión del código; evidencia estática inmutable excluida solo de reescrituras whitespace/EOF. E2E del mismo run terminó SUCCESS. Ruff, formato y Semgrep sobre seis archivos del harness aprobados localmente. Regresión general y linters siguen por comprobar. No cambia código funcional ni se genera entregable.

**2026-11-02 — Control heredado de licencias:** ambos análisis fallaron antes de emitir veredicto: Python 3.15 frente a PyO3/pydantic-core antiguo. Se revisó la comparación upstream y se fija el workflow reutilizable v1.13.1 por SHA 692d3282, que incorpora soporte compatible. Reglas LGPL/GPL/proprietary y uv.lock de Saleor permanecen iguales. Retest pendiente; no se declara revisión de licencias aprobada.

**2026-11-02 — VT-01/03/04/05 completadas en laboratorio privado:** run 41517858406, fuente f1f883d5, checkout daf9178a: focal 59 PASS/2 XFAIL, independientes 42 PASS y C10 26 PASS/0 FAIL/0 ERROR. Verificados ZIP y hashes internos. HTTPS y Chromium con CA válida, CSRF/cookies/CORS y cierre de sockets/CA comprobados. No cubre storefront externo, proxy de producción ni replicación física. P-ORDER-01 sigue provisional. VT-02/06 continúan por linters/regresión/E2E. Licencias: instalación corregida, dos rechazos heredados idénticos en base/HEAD más error de stdin; revisión requerida, sin aprobación automática. Entregable pausado.

**2026-11-02 — VT-02 completada:** SAST actual revisado y pre-commit completo SUCCESS en run 41517858278/job 125526067035: whitespace, EOF, Ruff, formato, mypy, deptry, Semgrep, uv-lock, migraciones y esquema GraphQL. E2E actual 211 PASS verificado desde XML y hashes, run 41517858406. Se conserva procedencia Playwright 1.56.0/Chromium 141.0.7390.37 build 1194. Queda VT-06 esperando regresión general y conciliación; control heredado de licencias en revisión, sin cambiar reglas ni adjudicar infracción. Entregable pausado.

**2026-11-02 — VT-06 completada; VT-07 en preparación de retest:** regresión actual 17.613 PASS/2 XFAIL, 0 fallos/errores en 1.050,22 s, reconciliada desde XML. Suite focal es subconjunto. Archivo público depura 85 correos de etiquetas de fixtures conservando huellas/identidad de casos y resultados; original queda separado. Para el último control heredado se selecciona la alternativa Artistic que ofrece el autor de text-unidecode 1.3, solo con hash de wheel del lockfile y declaración presente; no se modifica la política GPL. Seis pruebas verifican rechazo de metadatos no confirmados y conservación de GPL ajeno. Grant recibirá una única entrada stdin y un control negativo GPL real. CI pendiente; entregable pausado.

**2026-11-02 — VT-07 intento inicial conservado:** la colección aislada con uvx y config /dev/null no incorporaba la raíz del repositorio al sys.path. ModuleNotFoundError: security; aún no se analizó el SBOM. Se fija PYTHONPATH al workspace, sin instalar el producto ni sus servicios. La misma invocación se reproduce localmente antes del nuevo CI. No cambia la selección Artistic ni la política de licencias.

**2026-11-02 — VT-07 completada:** run 41521562337, selección Artistic-1.0-Perl del autor limitada a text-unidecode 1.3 y hash del wheel del lockfile. Base y HEAD: 502 entradas aprobadas, cero rechazadas; seis pruebas de límites aprobadas en cada fuente y control GPL ajeno denegado por la regla original. Stdin único eliminó el error espurio. Archivos originales y derivadas públicas con procedencia/hashes verificados; reglas LGPL/GPL/proprietary iguales. Se conserva el fallo de colección inicial. No se inventa aprobación grupal ni conformidad jurídica global. Conciliación final de calidad en curso; no se genera PDF/Word.
