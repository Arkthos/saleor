# Revisión de continuidad del primer avance

**Revisado:** 2026-11-03. **Decisión:** mantener un único trabajo acumulativo. La segunda entrega amplía el contenido del primer avance y actualiza los pasajes que quedaron superados. Esta revisión propone cambios; el Word adjunto permanece sin modificar.

## Identidad de la base

Archivo recibido: Proyecto final - primer avance(5).docx. SHA-256: `c8f98d51b40ef7571f0cefaa092ae7c9504b3d5e4cd89db0f5d28c885c014d65`. Coincide byte a byte con el hash registrado para el primer avance presentado como (4).docx. Se recuperaron 505 párrafos con texto en el documento OOXML, incluidos los de tablas. El formato es OOXML Strict; la lectura se hizo directamente sobre sus XML para preservar el original. Se exportó una revisión de 23 páginas y se inspeccionaron páginas clave, sin guardar esa exportación como entregable.

La base ya incluye planteamiento, justificación, pregunta, un objetivo general y tres específicos, fundamentos, marco metodológico, instrumentos I01-I07, arquitectura conceptual, riesgos R01-R13, observaciones H01-H15, referencias IEEE y anexos A-C. Es una base suficiente para continuar. El manuscrito independiente previo de trece páginas constituye material auxiliar y no debe sustituir este contenido.

## Conservar

El problema y la pregunta siguen siendo pertinentes. Los objetivos ya abarcan la revisión, las pruebas y al menos diez observaciones con recomendaciones; no se reformulan para acomodar resultados. Se mantienen el foco en seis operaciones, CyberMarket CR como escenario ficticio, la base funcional 4cb1609a y las distinciones entre mecanismo observado, riesgo, hallazgo y conformidad. Los criterios ASVS/WSTG y las limitaciones correctamente formuladas conservan su función.

## Cambios propuestos para la versión acumulativa

| ID | Apartado existente | Acción | Motivo y cambio concreto |
|---|---|---|---|
| RC-01 | Resumen | actualizar | Se presenta solo como primer avance y declara que no incluye dinámica. Reescribir el resumen de la versión acumulativa para cubrir diseño, método aplicado y resultados de la segunda etapa. Conservar la ausencia de una certificación global. |
| RC-02 | Problema e introducción | ajustar marco temporal | Actualmente y varios futuros describen una etapa sin pruebas. Expresar esa carencia como situación inicial; conservar la pregunta y explicar que la segunda etapa aporta verificación controlada. |
| RC-03 | Objetivos | conservar y precisar evidencia | Objetivo general y tres específicos ya contemplan revisión, pruebas y diez observaciones con recomendaciones. Mantener los objetivos. Al evaluar el tercero distinguir recomendaciones y tratamiento propuesto de mitigaciones de producto realmente aplicadas y retesteadas. |
| RC-04 | Marco metodológico y procedimiento | desarrollar seccion existente | Enfoque, instrumentos I01-I07 y seis etapas están formulados principalmente como protocolo futuro. Consolidar el marco metodológico ya escrito con selección real, niveles de prueba, herramientas/versiones, configuración, oráculos, ejecuciones y análisis. |
| RC-05 | Muestra y actores | actualizar | Se prevén dieciséis escenarios y apps solo si el laboratorio incorpora ese mecanismo. Conciliar el inventario real por IDs y variantes, incluyendo apps/delegación, pruebas focales, unidades, C10 y E2E en conjuntos separados. |
| RC-06 | Arquitectura y límites del entorno | ampliar sin sustituir modelo | TLS, navegador, base/caché y otros elementos figuran como desconocidos o pendientes. Conservar figuras conceptuales y añadir el entorno ejecutado: CI privado, PostgreSQL/Valkey efímeros, ASGI loopback, HTTPS/CA/Chromium y configuraciones registradas. |
| RC-07 | Principios fundamentales identificados y Tabla III | actualizar estado de evidencia | La tabla clasifica varios mecanismos como pendientes de pruebas. Vincular mínimo privilegio, revocación y controles de cookie/CSRF con las evidencias actuales. Mantener sin adjudicar las propiedades no cubiertas. |
| RC-08 | Riesgos R01-R13 y Tabla IV | conservar registro y actualizar | Se justifica incertidumbre porque todavía no existen resultados experimentales. Mantener IDs y distinguir prioridad inicial de investigación del estado actual de evidencia. Actualizar esa justificación: sí hay resultados, pero no estimación de probabilidad operativa o riesgo residual. |
| RC-09 | Observaciones H01-H15 y Tabla V | preservar y trazar | Quince observaciones documentales sirven como punto de partida de una validación futura. Conservar los identificadores originales y enlazarlos al catálogo A2-Hxx y las recomendaciones actualizadas; explicar agrupaciones y nuevas observaciones. |
| RC-10 | Anexos A-C | actualizar con verificaciones | La revocación, pruebas cruzadas y HTTPS/navegador se declaran no ejecutados. Añadir verificación realizada, evidencia y límites restantes. Mantener los listados como inspección de la base y las figuras conceptuales como tales. |
| RC-11 | Listados C.2 y C.3 | corregir ubicacion de codigo | El bloque if need_csrf / clean_csrf_token aparece bajo el listado C.3 atribuido al middleware. Asociar ese bloque a C.2, de refresh_token.py; dejar HttpOnly/Secure/SameSite bajo C.3, del middleware. |
| RC-12 | Referencias y llamadas internas | mantener ieee continuo | Hay doce referencias del documento original y anexos ya citados. Mantener una sola bibliografía y numeración coherente de tablas, figuras, listados y anexos en el documento acumulado. Verificar las fuentes al integrar afirmaciones nuevas. |
| RC-13 | Jerarquía y maquetación | revisar antes del pdf | El archivo contiene secciones de tres, cuatro y dos columnas; la revisión renderizada muestra tabla IV muy estrecha y Fig. C.1 recortada. Revisar saltos de sección, tablas y anchura de figuras al ensamblar la continuación; comprobar el PDF final completo. |

## Dos ajustes de redacción que muestran la continuidad

En Planteamiento del problema, la frase que comienza por Actualmente, la investigación cuenta... debe situarse en la etapa inicial. Redacción propuesta: «En la etapa inicial se disponía de documentación técnica y revisión estática preliminar. La segunda etapa incorpora pruebas controladas para contrastar esos mecanismos, conservando la distinción entre comportamientos observados y requisitos cuya conformidad permanece sin determinar».

En las limitaciones del anexo C no debe seguir afirmándose que no se ejecutó HTTPS/navegador. Redacción propuesta: «La segunda etapa verificó las condiciones seleccionadas de cookie, CSRF y CORS en HTTPS privado y Chromium, con datos sintéticos y una CA desechable. El resultado se limita al laboratorio y a dos orígenes del mismo host; no acredita un storefront público, cookies de terceros entre sitios distintos o la eficacia universal de la política de sesiones».

Son propuestas de edición, no correcciones ya aplicadas ni observaciones recibidas del docente. No se hace un reemplazo global de todos los tiempos futuros: los objetivos, beneficios potenciales y verificaciones todavía no realizadas conservan su sentido.

## Puntos que requieren cuidado al ampliar

- El objetivo tercero menciona mitigaciones técnicamente viables. Se debe declarar qué tratamiento se propone y cuál se aplicó y comprobó. Las correcciones del harness, los oráculos, CI o los metadatos de licencias no equivalen a corregir una vulnerabilidad funcional de Saleor.
- La probabilidad operativa puede seguir sin estimarse aunque existan pruebas. Debe actualizarse la razón de la incertidumbre, no asignar severidades o porcentajes sin fundamento.
- La fórmula de cobertura de requisitos exige un denominador de requisitos aplicables y un criterio de evidencia suficiente. Los 23 candidatos o las 61 variantes focales no producen por sí solos ese porcentaje.
- Los trece riesgos y quince observaciones iniciales conservan sus IDs. El catálogo posterior debe explicar sus enlaces, agrupaciones y límites. P-ORDER-01 sigue provisional; dos XFAIL no son dos vulnerabilidades confirmadas.
- El código funcional conserva su baseline; los SHAs de pruebas y de checkout se añaden como procedencia de ejecución, sin sustituirlos por el HEAD documental.

## Cómo se continuará el mismo trabajo

Se desarrolla la metodología existente y se integran los tres apartados obligatorios —codificación segura, análisis estático/dinámico y pruebas de seguridad—, los hallazgos y la discusión en la misma línea argumental. Se conserva el contenido fundacional útil, se eliminan duplicaciones y se mantiene una bibliografía IEEE única. No se construye un segundo artículo que haga desaparecer el planteamiento, los objetivos o los anexos del primero.

La consigna específica del segundo avance mantiene sus seis criterios y el mínimo de diez hallazgos con recomendaciones. El cierre técnico fuente eb5d3ecb / checkout 90455ca8 aporta la ejecución; el Word original aporta el problema y la estructura acumulativa. La fase técnica no se reabre por esta revisión documental. El siguiente trabajo es aplicar los ajustes a la continuación e incorporar el análisis A2-07. No se ha emitido otra versión académica ni un PDF final.
