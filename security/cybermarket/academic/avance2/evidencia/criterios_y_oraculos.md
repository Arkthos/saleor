# A2-02 — Criterios, autoridad y reglas de interpretación

**Estado:** conciliación documental completada; no se adjudica conformidad global ni se ejecutan pruebas en esta fase.

## Selección y autoridad

Se conservan los 23 ASVS y once WSTG iniciales. La matriz derivada asigna una disposición explícita a cada requisito y separa los casos citados literalmente por el CSV histórico de las relaciones analíticas nuevas. Se documenta también WSTG-IDNT-04, incorporado al CSV posterior. Ninguna ausencia de ID en una columna demuestra por sí sola ausencia de toda evidencia.

ASVS 5.0.0 se usa como referente analítico escogido para el estudio. WSTG 4.2 orienta procedimientos adaptados; la relación entre ambos no es un mapping oficial. Los niveles se transcriben como atributos del requisito de referencia, no como nivel alcanzado por Saleor. Todo dictamen formal permanece NO_DETERMINADO hasta contar con aplicabilidad y evidencia suficientes.

## Clases de oráculo

| Clase | Qué espera la prueba | Qué significa PASS |
|---|---|---|
| Contrato local | Comportamiento esperado de una función/ruta según código, API y criterio declarado | Se cumple la aserción acotada; no se adjudica todo ASVS |
| Caracterización | Describir fielmente un comportamiento versionado, incluso si merece debate de seguridad | Coincidencia con el comportamiento observado/esperado de la implementación |
| Requisito de referencia | Condición de seguridad seleccionada y aplicable, con alcance explícito | Solo puede juzgarse sobre la propiedad y condiciones realmente comprobadas |
| Política propuesta | Preferencia aún no aprobada para el caso ficticio | No produce conformidad oficial del producto ni aprobación del grupo |

CM-T01–04, T07–13, T15–16 y T19–21 son contratos locales en el inventario histórico. T05–06, T14, T17–18 y T23–27 son caracterizaciones. T22 aplica una política provisional y tiene dos XFAIL estrictas de correo para actores no propietarios. Las direcciones observadas en T23 no añaden XFAIL normativas nuevas.

## Expectativas por familia

| Familia/casos | Criterio de comparación | Límite que debe conservarse |
|---|---|---|
| T01, T12–13: me/user | Actor autenticado/anon y personal con permisos; datos exactos o ausencia | No revisar solo error: comprobar ausencia de datos seleccionados; otros campos siguen fuera de muestra |
| T02: revocación | Token previamente válido deja de servir para me y refresh tras rotación | No equivale a probar cada servicio consumidor o logout de navegador |
| T03, T10: refresh | Tipo correcto; cookie requiere CSRF; argumento explícito tiene otra condición | No es una validación general de origen, CORS o almacenamiento del frontend |
| T08–11: emisión, error, audiencia | Tipo/exp/iat y conservación de aud; código común de error | TTL emitido no es vida absoluta; aud conservada no es audiencia validada; código común no prueba tiempo uniforme |
| T04/T20: permisos | Función externalReference exige privilegio; delegación es intersección | No se valida toda BaseMutation ni cada app/operación |
| T14: cookies | HttpOnly y valores Secure/SameSite por DEBUG | Transporte HTTPS, política de cliente y entrega del mismo valor requieren análisis separado |
| T15–16: límites GraphQL | Dos elementos exceden umbral configurado en uno | No es carga, estrés, profundidad completa o disponibilidad distribuida |
| T17–19: cabeceras/IP/backoff | Precedencia y casos deterministas de función | No prueba que un proxy elimine cabeceras controladas por cliente |
| T21: JWT none | Excepción criptográfica al token sin firma | Falta prueba de firma alterada, expiración y nbf para otras propiedades |
| T23–27: UUID/legacy | Raw/masked/null por actor y campo, comparados con fixture sintético y controles | UUID conocido no demuestra enumeración, obtención desde frontend o explotación de datos reales |

Las ampliaciones se diseñarán a partir de las brechas anteriores, manteniendo el valor esperado independiente de la implementación bajo prueba. En particular, para probar ofuscación se usarán valores esperados literales y no llamar al mismo helper para calcular la aserción.

## P-ORDER-01

Se mantiene PROVISIONAL/NO_APROBADA. La instrucción de continuar autónomamente permite desarrollar y analizar el estudio; no equivale a aprobar una política empresarial o la intención funcional de Saleor. El informe puede describir discrepancia frente a la propuesta, recomendar su definición y contrastar semántica de capacidad por UUID. No atribuye una vulnerabilidad oficial o aprobación humana inexistente. No se cambia el código del producto para satisfacerla.

## H10 y trazabilidad

H10 trataba el chequeo base de permisos de mutaciones. El CSV posterior no lo cita en observation_ids, aunque CM-T04 relaciona R09 con H12 y hay permisos backend observables. Se documenta la brecha de enlace y se revisará BaseMutation y sus llamadas en A2-03; no se inventa una prueba ejecutada ni se modifica retroactivamente la matriz histórica.

## Equivalencia de instrumentos I01–I07

| Instrumento inicial | Producto actual o previsto | Estado al cerrar A2-02 |
|---|---|---|
| I01 configuración | linea_base.md y linea_base_manifest.json | Aplicado a fuentes y ejecución histórica; configuración de nuevo laboratorio todavía no aplicada |
| I02 arquitectura/DFD | Diagramas del primer avance y lectura de rutas | Base documental existente; revisión aplicada A2-03 |
| I03 riesgos | R01–R13 y relación de casos | Registro preliminar conservado; no cerrado por tener casos |
| I04 requisitos | trazabilidad_avance2.csv | 23 requisitos conciliados; dictámenes no adjudicados |
| I05 pruebas | CSV histórico y fichas/oráculos derivados | Inventario y criterios disponibles; ampliaciones/ejecución nuevas en fases siguientes |
| I06 observaciones | H01–H15 y futuro catálogo A2-Hxx | Se conserva procedencia; catálogo de resultados pendiente |
| I07 evidencia/citas | Fuentes versionadas, runs, manifiestos y auditoría de afirmaciones | Mecanismo aplicado; ampliar al manuscrito sin convertir auditorías antiguas en evidencia nueva |

## Criterio de cierre

Cada uno de los 23 requisitos tiene disposición, relaciones y límite; las doce técnicas de la unión histórica tienen procedencia/uso; las expectativas por familia y su autoridad están diferenciadas y los siete instrumentos tienen correspondencia. La resolución documental no acredita ejecución ni cumplimiento normativo. Próximo paso: revisión de codificación segura y análisis estático A2-03.
