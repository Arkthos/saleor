# Bitácora del segundo avance

## 2026-11-02 — A2-00: planificación y conservación del trabajo

**Solicitud:** usar la rúbrica recibida y todo el contexto disponible para planear la segunda entrega, documentar ajustes respecto a la primera, establecer un roadmap en el proyecto y en GitHub y conservar también el trabajo académico.

**Fuentes comprobadas:** tres páginas de la consigna específica, incluida verificación visual de la rúbrica; primer avance y revisión del checkpoint ya leídos; contexto curricular; PR #1 y HEAD de entrada; plan maestro, README, C10, instrucciones AGENTS y decisiones pertinentes del repositorio; LICENSE revisada.

**Decisiones:** mantener IEEE y el Word presentado; registrar ausencia de correcciones docentes; conservar seis operaciones y baseline; producir mínimo diez hallazgos con recomendaciones sin fabricar diez vulnerabilidades; separar dinámica CI de transporte real; seleccionar C10 por necesidad de la investigación; preservar borradores, matrices, fuentes/localizadores y razonamiento en GitHub.

**Productos de esta etapa:** ROADMAP.md v1.0, estado.json, MATRIZ_RUBRICA.csv, AJUSTES_AVANCE1.md, guía de fuentes/evidencia, estructura del manuscrito, plantillas y antecedentes propios. Se enlaza desde los índices existentes y se incorpora la regla de cierre en AGENTS.md y ADR-0011. Los documentos se publican en el mismo commit; consultar su SHA en el historial de esta entrada. La copia del roadmap del proyecto queda identificada en estado.json.

**Validación de planificación:** lectura de consigna/rúbrica y hashes de originales; revisión de coherencia de fases/dependencias, suma de doce puntos de los seis criterios, referencias de productos y enlaces del paquete, y ausencia de resultados nuevos presentados como ejecutados. Esta validación documental no es CI ni ejecución del producto.

**Estado al cerrar:** A2-00 COMPLETADA al publicar el paquete. A2-01–A2-10 PENDIENTES. No se ha redactado el manuscrito nuevo, completado el catálogo A2-Hxx, ampliado pruebas, desplegado C10, modificado Saleor funcional ni fusionado el PR. Los resultados C2–C9 citados son históricos y están vinculados a su evidencia.

**Abiertos:** fecha/hora del campus, roles/disponibilidad del grupo, adopción o no de la política provisional de pedidos y necesidad/recursos del despliegue. No se atribuyen aprobaciones o contribuciones que no hayan ocurrido.

**Siguiente acción:** A2-01, confirmar baseline actual, condiciones de ejecución y conservación; incorporar fecha/roles cuando se disponga y preparar A2-02. Si una publicación o réplica falla, registrar el estado parcial y no anunciar cierre documental completo.

## 2026-11-02 — Fecha límite y calendario, versión 1.1

El usuario fijó la fecha límite para el domingo siguiente a las 18:00. Desde la fecha de esta sesión (lunes 2 de noviembre), corresponde al **domingo 8 de noviembre de 2026, 18:00, America/Costa_Rica (UTC−06:00)**; equivalente 9 de noviembre, 00:00 UTC. La fecha se registra por instrucción del usuario, sin presentarla como una verificación del campus.

Se actualizaron ROADMAP.md y estado.json con la fecha y metas diarias hasta la entrega. El sábado se reserva para auditoría y PDF; el domingo para revisión final, congelación y carga, con margen de 15:00 a 18:00. Se mantiene A2-00 cerrada y A2-01–A2-10 pendientes: asignar fechas no acredita ejecución. Se conserva la identidad de la copia del roadmap del proyecto.

Validación: calendario y día de semana comprobados, zona horaria y conversión UTC verificadas; versiones coincidentes y estados preservados. Esta actualización no crea recordatorios ni confirma una carga al campus.

## 2026-11-02 — A2-01: línea base y condiciones de trabajo, roadmap 1.2

Por solicitud de avanzar la siguiente etapa, se comprobó el PR abierto/draft, HEAD de entrada 6af5fbad0101d3261055b2bcb089df3255fc1053 y comparación con el producto base. Se revisaron configuración/workflows, licencia, logs históricos de tests y lint y metadatos de artefactos; se recalcularon hashes de los originales disponibles.

Productos: evidencia/linea_base.md y evidencia/linea_base_manifest.json. Se eliminaron exclusivamente espacios finales de las líneas 3–8 y 86 del checkpoint de semana 7, conservando el texto normalizado. Comprobación local de formato/EOF; no se ejecutaron pre-commit completo o pruebas nuevas del producto. El HEAD de entrada tiene cero runs asociados; la revalidación del nuevo SHA queda explícita para A2-05.

Se registró disponibilidad por API, tamaños, digests y expiraciones de cuatro artefactos históricos, sin declarar descarga/hash independiente. CI histórico: Python 3.12.15, Django 5.2.17 y servicios/digests en manifiesto; entorno local: Python 3.12.14, sin Docker. El reparto entre integrantes permanece sin asignar y no bloquea conciliación documental.

Cierre: A2-01 COMPLETADA como preparación, con límites explícitos. Se actualizan roadmap, estado, matriz de rúbrica, índices y copia del proyecto. Siguiente acción: A2-02, conciliación de requisitos e instrumentos y definición de oráculos. No se aprobó P-ORDER-01 ni se cerraron dictámenes de riesgo; no se modificó código funcional ni se fusionó el PR.

## Formato para las próximas entradas

Cada entrada debe identificar fecha, etapa, solicitud/objetivo, productos, cambios en evidencia o criterios, comprobaciones realmente ejecutadas, resultados y límites, decisiones, referencias al commit/run cuando existan, estado y punto exacto de reanudación. Añadir entradas; no reescribir el pasado para atribuirle conocimiento posterior.

## 2026-11-02 — A2-02, roadmap 1.3

Conciliados los 23 ASVS y la unión de doce WSTG; se separan mappings históricos de relaciones nuevas, siete instrumentos y oráculos por familia. P-ORDER-01 permanece provisional y todos los dictámenes normativos NO_DETERMINADO. No hay pruebas nuevas en esta fase documental.

Productos: evidencia/trazabilidad_avance2.csv, evidencia/tecnicas_avance2.csv, evidencia/criterios_y_oraculos.md. Estado: COMPLETADA. Siguiente etapa: A2-03. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-03, roadmap 1.4

Revisión aplicada de trece puntos en control/datos/fallas/interfaces; Bandit 1.8.6 produjo una alerta B105 revisada como falso positivo y Semgrep 1.153.0 cero hallazgos en cinco reglas/21 archivos. Se conservan reportes y hashes; no se afirma seguridad global, SCA o CI completo.

Productos: evidencia/revision_codificacion.md, evidencia/revision_manual.csv, evidencia/analisis_estatico.md, evidencia/estatica/run_manifest.json. Estado: COMPLETADA. Siguiente etapa: A2-04. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-04, roadmap 1.5

Clasificados los 27 casos históricos por cuerpo/dependencias y documentada la dependencia de fixtures globales. Diseñadas diez unidades CM-U para firma, exp, nbf, CSRF, ofuscación y bordes; oráculos independientes y resultados todavía no ejecutados en este cierre de diseño.

Productos: evidencia/plan_pruebas.md, evidencia/clasificacion_pruebas.csv. Estado: COMPLETADA. Siguiente etapa: A2-05. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-05, roadmap 1.6

Ejecutadas 30 variantes de diez unidades y doce invocaciones de validadores: 42 PASS sin warnings en la corrida final. Recuperados/verificados tres ZIP históricos y checksums internos disponibles; XML focal 59 PASS/2 XFAIL y general 17613 PASS/2 XFAIL reconciliados. Se preservan intentos iniciales y límites; no hay revalidación integrada nueva ni despliegue.

Productos: evidencia/resultados_ejecucion.md, evidencia/resultados_ci_manifest.json, evidencia/ejecucion_local/isolated.xml, evidencia/historica_2026-10-20/archivo_verificado_manifest.json. Estado: COMPLETADA. Siguiente etapa: A2-06. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-06, roadmap 1.7

C10 excluido de la ejecución de este avance por recursos comprobados; LIVE-01–07 permanecen NOT_EXECUTED. La dinámica existente se limita a CI histórico verificado y unidades locales; no se afirman propiedades de HTTP/HTTPS, navegador, proxy o frontend. Se cierra la decisión de alcance, no una validación desplegada.

Productos: evidencia/decision_c10.md. Estado: COMPLETADA. Siguiente etapa: A2-07. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-07, roadmap 1.8

Analizadas tres capas de evidencia y elaborados catorce hallazgos sustantivos con recomendación y verificación propuesta, vinculados a H/R y casos. Se distinguen controles positivos, caracterización y brechas; no se inventan CVSS, correcciones de producto o aprobación de P-ORDER-01. Límites de CI integrado y C10 conservados.

Productos: evidencia/hallazgos_avance2.csv, evidencia/hallazgos_avance2.json, evidencia/analisis_resultados.md. Estado: COMPLETADA. Siguiente etapa: A2-08. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-08, roadmap 1.9

Manuscrito integrado con metodología, tres apartados obligatorios, catorce hallazgos, doce referencias IEEE y anexos de instrumentos, 27 casos históricos, diez unidades nuevas y 23 requisitos. Se corrigieron dos localizadores de código sin alterar evidencia bruta.

Productos: manuscrito/INFORME_AVANCE2.md, manuscrito/REFERENCIAS_IEEE.json, manuscrito/generar_docx.py. Estado: COMPLETADA. Siguiente etapa: A2-09. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-09, roadmap 1.10

Auditoría documental, técnica y visual completada. PDF de trece páginas y Word de revisión guardados; versión pública sin nombres personales en GitHub. Se conciliaron doce citas, catorce hallazgos, 23 requisitos, nueve checksums y los XML. Guía de defensa disponible. Revalidación integrada nueva y C10 siguen sin ejecutarse; revisión grupal y campus pendientes.

Productos: manuscrito/auditoria_final.md, manuscrito/auditoria_final.json, manuscrito/GUIA_DEFENSA.md, manuscrito/entrega/CyberMarket_Segundo_Avance_publico.pdf. Estado: COMPLETADA. Siguiente etapa: A2-10. Publicación conjunta con roadmap, estado y matriz; consultar el commit de esta entrada. No se atribuye aprobación docente o humana inexistente.

## 2026-11-02 — A2-10, roadmap 1.11

Preparación de entrega terminada con PDF de trece páginas, editable, fuente, auditoría, guía de defensa y manifest de hashes. Versión congelada avance2-revision-2026-11-02-v1. PDF privado y Word guardados; PDF público con nombre del equipo en GitHub. A2-10 EN_CURSO: revisión grupal y campus pendientes. No se atribuyen aprobación, reunión, contribuciones individuales o entrega inexistentes.

## 2026-11-02 — VT-00 reapertura, roadmap 1.12

Usuario ordena completar todas las pruebas necesarias antes de generar entregable. Se pausa generación, se reabren integración/C10 y se define VT-01–06. Checkout limpio desde 34891bfd. Capacidades locales: UID 0 sin capacidades, sin Docker/PostgreSQL; unshare no permite mapa UID. No se eluden las restricciones. Se amplía el workflow focal para incluir unidades nuevas. Ningún resultado histórico se transfiere al HEAD nuevo.

## 2026-11-02 — VT-01 preparación, roadmap 1.13

Conjunto C10 implementado; 25 variantes recolectadas sin ejecutarlas, Ruff/formato/AST/YAML/lockfile correctos. Smoke real HTTP y HTTPS contra health sin DB: ambos 200, CA verificada y teardown final aprobado. Intento inicial de teardown HTTPS falló y quedó registrado; se corrigieron tiempos de cierre y conexiones. Se amplió e2e.yml con job integral manual y artefactos depurados. Sin modificaciones funcionales del producto.

Se cerró/reabrió el mismo PR borrador para comprobar activación; no hubo runs nuevos. La UI pública confirmó la causa: workflows deshabilitados en el fork por escala de uso, no un resultado de tests. Navegador sin sesión de mantenedor; conector sin dispatch. Se requiere reactivación y lanzamiento del mantenedor. No se marca ningún LIVE PASS. Entregable sigue pausado.

## 2026-11-02 — CI reactivado, roadmap 1.14

Acceso local autenticado al repositorio permitió confirmar el bloqueo y reactivar Actions. Se revisaron guards del fork en jobs programados para no lanzar despliegues heredados. Despachado workflow e2e.yml sobre research/cybermarket-security-tests-v1; run 41512875410 IN_PROGRESS, fuente 1c87cf5. Se conserva por separado la fuente probada y el commit documental. Ningún LIVE se declara aprobado todavía.

## 2026-11-02 — Corrección del intento 01, roadmap 1.15

Run 41512875410: preparación del laboratorio falló por Ubuntu 26.04 no soportado por Playwright fijado. C10 omitido, no fallos del producto. Se fija runner ubuntu-24.04 y se crea siempre carpeta de evidencia. E2E original sigue independiente. Nuevo input include_e2e evita repetir pruebas ajenas a la corrección del laboratorio. Se conserva intento_01_setup.json.

## 2026-11-02 — C10 automático, roadmap 1.16

Para evitar dependencia del despacho por navegador, se activa el laboratorio también en eventos pull_request. Runner ubuntu-24.04 y artefactos en fallos de setup conservados. General y linters quedan en sus workflows existentes sobre la misma fuente; opción include_regression permite repetirlos manualmente cuando corresponde. No se omiten pruebas requeridas ni se marca éxito de un job pendiente.

## 2026-11-02 — Corrección del intento 02, roadmap 1.17

Fuente de rama 94383be; checkout real 03b3de3e1be39f1c4d796186284cfd5ebeaa86f6. XML verificados: focal 59 PASS/2 XFAIL, unidades/validadores 42 PASS y C10 1 PASS/24 FAIL. Causa de C10: alias replica no apuntaba a test DB en hilos ASGI; se corrige configuración del laboratorio, sin tocar producto o expectativas de acceso. Se añaden mensajes/path exactos a negativos de permisos y revocación. 48 coincidencias de Semgrep pertenecen a ejemplos de .semgrep; se conserva salida original y se excluye esa carpeta de ejemplos. E2E 211 PASS del run 41512875410 archivado y verificado. Nuevo retest pendiente.

## VT: intento 03 y correcciones para retest

**2026-11-02 — Intento 03 conservado; retest preparado:** focal 59 PASS/2 XFAIL y unidades/validadores 42 PASS. HTTP/HTTPS/navegador 23 PASS/2 FAIL: se completa el contrato exacto de coste GraphQL y se distingue middleware normal del producto frente al guard de routing exclusivo de pruebas. Se añade un diagnóstico independiente que conserva ese error exacto; quedan 26 variantes para retest. Cliente HTTP acotado compatible con Semgrep, sin exclusión del código; evidencia estática inmutable excluida solo de reescrituras whitespace/EOF. E2E del mismo run terminó SUCCESS. Ruff, formato y Semgrep sobre seis archivos del harness aprobados localmente. Regresión general y linters siguen por comprobar. No cambia código funcional ni se genera entregable.
