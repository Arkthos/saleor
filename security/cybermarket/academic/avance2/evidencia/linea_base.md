# A2-01 — Línea base y condiciones de trabajo

**Fecha:** 2026-11-02. **Estado:** línea base documentada y comprobaciones de esta etapa realizadas. **Siguiente etapa:** A2-02. El [manifiesto](linea_base_manifest.json) conserva los identificadores y límites de esta revisión. No se realizaron nuevas pruebas del producto ni despliegue durante esta etapa.

## 1. Versiones y fuentes preservadas

| Elemento | Identificación |
|---|---|
| Producto base | Arkthos/saleor, 4cb1609a90eade14b6275a407bc7a00c35698090 |
| Rama de trabajo | research/cybermarket-security-tests-v1 |
| HEAD al comenzar A2-01 | 6af5fbad0101d3261055b2bcb089df3255fc1053 |
| Estado del PR #1 | Abierto, draft, sin merge |
| Ejecución histórica focal de referencia | Run 39443927080, branch SHA c442099bc0ebee5194a6e58354944563e92e0d28, checkout b0604014dab69125a4a535f1ece5828be99ea3c8 |
| Dependencias | uv.lock: objeto Git 2f26624141e4893e75ddc0bfccf217bf6aa715fa; pyproject.toml: 42fc13bdcc3d6d5b8b1b69b6111aa4d948b7ca53 |

La comparación del producto base con el HEAD de entrada devolvió 121 commits y 49 archivos distintos. Las diferencias corresponden a pruebas, herramientas de evidencia, workflow de investigación e instrucciones/documentación. No hay modificaciones de código funcional del producto en esa comparación. Un nuevo commit de esta etapa cambia HEAD sin convertirse en una ejecución de pruebas.

Se comprobaron nuevamente tamaños y SHA-256 de los originales disponibles, sin modificarlos:

| Original | Bytes | SHA-256 |
|---|---:|---|
| Primer avance presentado (4).docx | 437232 | c8f98d51b40ef7571f0cefaa092ae7c9504b3d5e4cd89db0f5d28c885c014d65 |
| Segundo avance (evaluable).pdf | 202151 | 82719d0216f9088a4a5e922295450aa8ad4603e3b80a98f1dc0a812596273d1e |
| Manual del proyecto | 321178 | 1c916c8aa1349297afc3709696bcf88ed96268fdafc115cb7a04dbed24c1f849 |
| Programa del curso | 724877 | 504b9ecc527f61c4cbe56c9d258df710f3157c22923601f4cff00423d4d9a324 |

El manifiesto también identifica blobs de workflows, configuración de pruebas, licencia y matriz histórica. Un objeto Git y un SHA-256 de archivo son identificadores distintos y no se presentan como el mismo tipo de hash. No se republican los originales con datos del grupo o material docente.

## 2. Entorno existente: qué está comprobado

El workflow de investigación declara contenedor Python 3.12, PostgreSQL 15-alpine y Valkey 8.1-alpine, con dependencias instaladas mediante uv sync --locked. El log histórico revisado permite concretar las versiones ejecutadas, en lugar de tomar los rangos del proyecto como versiones instaladas:

| Componente | Observado en el job histórico 118701056304 |
|---|---|
| Runner | ubuntu-26.04 |
| Python | CPython 3.12.15 |
| Django | 5.2.17 |
| Graphene / graphql-core | 2.1.9 / 2.3.2 |
| PyJWT / psycopg | 2.14.0 / 3.3.4 |
| pytest / pytest-django | 9.0.3 / 4.12.0 |

Los digests observados de las tres imágenes están en el manifiesto. El workflow utiliza etiquetas, no digests fijados en su definición; las versiones deben registrarse de nuevo cuando haya otra ejecución. No se deduce que una etiqueta siempre resuelva a los mismos bytes.

La configuración de pytest selecciona saleor.tests.settings, desactiva sockets por defecto y permite determinados hosts de servicio. Las settings de pruebas declaran correo en memoria, tareas Celery eager, ausencia de plugins y un hasher de pruebas. Son condiciones de un entorno automatizado; no validan el hasher de producción, TLS, un navegador, confianza de proxy ni un despliegue real. Los valores de credenciales sintéticas no se copian a este informe. Tampoco se acredita bloqueo de egreso a nivel de red solo por usar pytest-socket.

**Entorno disponible en esta sesión:** Python 3.12.14 y uv presentes; Docker, pre-commit y pre_commit_hooks no disponibles. No se levantó Saleor aquí ni se usó una base de datos externa. La vía existente para pruebas integradas es el workflow del repositorio. Se preparará su ejecución y conservación en la fase correspondiente; no se presenta la lectura de logs como una nueva corrida.

## 3. Estado de CI y corrección documental

Se consultaron los runs asociados al HEAD de entrada 6af5fbad…: la API devolvió cero. Por tanto, no se atribuyen al HEAD documental los resultados del 20 de octubre.

El run histórico focal 39443927080 registra 59 PASS y dos XFAIL esperados del producto, además de seis PASS del validador de evidencia. La suite general histórica los incluye; no se suman los conteos. Se mantiene la interpretación anterior: caracterización no equivale a conformidad, las XFAIL corresponden a una política provisional y los dictámenes de riesgo permanecen NO_DETERMINADO.

Se verificó en el log del run 39443927026 que el fallo de lint provenía de trailing-whitespace en el checkpoint de semana 7. En esta etapa se retiraron exclusivamente los espacios finales de sus líneas 3–8 y 86. La comparación del texto normalizado confirma que el resto del contenido se conserva y se comprobó el salto final de archivo.

**Alcance de la comprobación:** validación local de formato, no ejecución completa de pre-commit ni nuevo resultado remoto de Linters. Esa revalidación sigue identificada para A2-05. Reejecutar un job viejo sin cambiar su SHA no comprobaría la corrección publicada en HEAD y no se usó para simular ese resultado.

## 4. Disponibilidad de artefactos y conservación

La API de Actions informa estos artefactos como no expirados al revisar:

| Artefacto | ID | Run | Expiración informada |
|---|---:|---:|---|
| cybermarket-security-junit | 12275735957 | 39443927080 | 2026-11-19 15:05:06 UTC |
| cybermarket-static-review | 12274974418 | 39443927080 | 2026-11-19 14:58:10 UTC |
| pytest-results | 12275832930 | 39443927003 | 2027-01-18 14:57:09 UTC |
| pytest-django-db-queries-results | 12275658303 | 39443927003 | 2027-01-18 14:57:09 UTC |

Se registraron los digests y tamaños comunicados por GitHub en el manifiesto. No se descargaron ni recalcularon sus ZIP en A2-01; disponibilidad por API no equivale a copia duradera o verificación independiente. A2-05 debe conservar los bytes/resultados necesarios y registrar cualquier límite de acceso. La fecha límite académica acordada, 8 de noviembre, precede a las expiraciones informadas, pero eso no sustituye el archivo de evidencia.

## 5. Condiciones de uso y organización

Se comprobó LICENSE en el commit base: BSD-3-Clause. El usuario ha solicitado trabajar en su fork y avanzar esta etapa. La actividad realizada consiste en lectura de código/configuración y evidencia del fork, documentación y corrección de formato. No se atribuye autorización para servicios ajenos, una aprobación empresarial real ni una evaluación docente. Un eventual laboratorio usará activos controlados y datos sintéticos según el plan.

**Fecha límite vigente:** domingo 8 de noviembre de 2026, 18:00, America/Costa_Rica, fijada por el usuario. El calendario diario de ROADMAP.md permanece vigente. No hay feedback docente recibido según lo comunicado.

**Responsabilidades actuales:** el asistente ejecutó la revisión técnica/documental de A2-01 por instrucción del usuario. Los nombres y distribución entre integrantes del grupo siguen sin asignarse en este registro; no se inventan contribuciones. Esa información será necesaria para coordinar revisión grupal y entrega, pero no bloquea la conciliación de fuentes y requisitos.

## 6. Cierre y siguiente acción

La línea base, entorno de referencia, procedencia, estado de CI, disponibilidad de artefactos y condiciones de trabajo quedan documentados. Se corrige el defecto documental conocido y se delimita su comprobación local. No se afirma que todos los checks del nuevo HEAD estén verdes.

**A2-01 se cierra como preparación de la investigación.** A2-02 puede comenzar con los 23 ASVS, once WSTG, H01–H15 y R01–R13 iniciales y la matriz CM-T01–T27 actual, conservando sus diferencias y definiendo oráculos. Permanecen para sus fases: revalidación experimental, archivo independiente, decisión C10, política provisional y asignación de personas.

Fuentes técnicas: [PR #1](https://github.com/Arkthos/saleor/pull/1), [run focal](https://github.com/Arkthos/saleor/actions/runs/39443927080), [run de lint](https://github.com/Arkthos/saleor/actions/runs/39443927026), [workflow fijado](https://github.com/Arkthos/saleor/blob/6af5fbad0101d3261055b2bcb089df3255fc1053/.github/workflows/cybermarket-security.yaml), [settings de pruebas](https://github.com/Arkthos/saleor/blob/6af5fbad0101d3261055b2bcb089df3255fc1053/saleor/tests/settings.py), [pyproject](https://github.com/Arkthos/saleor/blob/6af5fbad0101d3261055b2bcb089df3255fc1053/pyproject.toml) y [licencia base](https://github.com/Arkthos/saleor/blob/4cb1609a90eade14b6275a407bc7a00c35698090/LICENSE).
