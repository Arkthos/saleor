# A2-07 Análisis de resultados y recomendaciones

El estudio reúne tres capas de evidencia: código/arquitectura revisados, ejecución GraphQL histórica recuperada y unidades locales nuevas. La primera explica decisiones; la segunda muestra comportamiento integrado en un entorno identificado; la tercera mide propiedades aisladas con expectativas independientes. Ninguna capa sustituye las restantes o demuestra seguridad total.

Los 23 ASVS tienen disposición explícita. Dieciséis aparecen literalmente en el CSV histórico; las nuevas relaciones se identifican como análisis y no se añaden retrospectivamente a un resultado. Los 13 riesgos conservan NO_DETERMINADO. El catálogo siguiente contiene catorce observaciones sustantivas con recomendaciones; incluye controles positivos, caracterizaciones y brechas, sin una cuota artificial de vulnerabilidades.

## A2-H01 Vías de extracción de credenciales

**Condición y evidencia.** La cabecera específica tiene precedencia; Authorization admite JWT/Bearer y rechaza prefijos incompletos o ajenos en los casos seleccionados. Referencias: CM-T17;CM-U09; saleor/core/auth.py:8-16.

**Interpretación y límites.** La extracción no autentica por sí sola y no demuestra consistencia con un proxy. Las unidades nuevas verifican bordes de formato, no tráfico HTTP externo.

**Recomendación.** Documentar cabeceras admitidas y normalización del borde; conservar casos de cabecera ausente, incompleta y precedencia.

**Verificación propuesta.** Reproducir la matriz en el cliente y proxy reales y comprobar que solo la credencial prevista llega al backend. Vínculo: H01 / R01. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H02 Backoff y procedencia de IP

**Condición y evidencia.** Existe retraso creciente con contadores IP/usuario y bordes deterministas; la función IP toma la primera cadena válida del encabezado antes del fallback remoto. Referencias: CM-T18;CM-T19;CM-U08;CM-U10; saleor/account/throttling.py:21-71,95-129; saleor/core/utils/__init__.py:57-71.

**Interpretación y límites.** La sintaxis de IP no prueba confianza del origen; ni los bordes de una función ni una caché simulada prueban resistencia distribuida o bloqueo malicioso de cuentas.

**Recomendación.** Fijar la política de proxy/caché, documentar umbrales y aislar el origen confiable; conservar regresión de los bordes y probar concurrencia acotada cuando exista entorno.

**Verificación propuesta.** Registrar cabecera recibida tras el borde y contadores efectivos con identidades sintéticas; no usar volumen de fuerza bruta. Vínculo: H02;H14 / R02. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H03 Respuesta ante credenciales inválidas

**Condición y evidencia.** Las dos variantes históricas de cuenta conocida con contraseña errónea y cuenta inexistente producen el mismo código de error y no emiten credenciales. Referencias: CM-T09; saleor/graphql/tests/test_cybermarket_security_extended.py:90-114.

**Interpretación y límites.** No se midieron distribución de tiempos, códigos HTTP comparados, recuperación de contraseña o registro. Igual código no demuestra ausencia completa de enumeración.

**Recomendación.** Mantener respuestas externas uniformes y revisar los demás canales; medir tiempos con un protocolo pequeño y controlado si se adopta el requisito completo.

**Verificación propuesta.** Comparar contenido y estado sin datos de cuenta y registrar tiempos bajo condiciones equivalentes, sin extrapolar una muestra mínima a equivalencia estadística. Vínculo: H03 / R03. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H04 Validación de tipo firma y vigencia JWT

**Condición y evidencia.** La integración histórica rechaza access usado como refresh y alg none. Las unidades nuevas rechazan una firma HS256 alterada, exp pasado y nbf futuro con reloj fijo, tras comprobar el control de firma válida. Referencias: CM-T10;CM-T21;CM-U01;CM-U02;CM-U03; saleor/core/jwt_manager.py:183-200; saleor/graphql/account/mutations/authentication/refresh_token.py:76-90.

**Interpretación y límites.** Las unidades no cubren todas las ramas RS256, rotación de claves o receptores. No se transforma su PASS en certificación de gestión criptográfica.

**Recomendación.** Conservar controles negativos por propiedad y añadir RS256/rotación cuando se amplíe el alcance, manteniendo separación entre autenticidad, tipo y receptor.

**Verificación propuesta.** Ejecutar contratos equivalentes en cada receptor previsto con claves efímeras y expectativas independientes; no registrar JWT completos. Vínculo: H05;H09 / R05;R08. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H05 Revocación de credenciales por usuario

**Condición y evidencia.** La revocación cambia jwt_token_key; el caso histórico establece acceso válido antes y comprueba que access y refresh anteriores dejan de servir en las rutas seleccionadas. Referencias: CM-T02; saleor/graphql/account/mutations/authentication/deactivate_all_user_tokens.py:13-27; saleor/core/auth_backend.py:124-156.

**Interpretación y límites.** No se probó cada consumidor, proveedor de identidad o cierre de interfaz. La cadena de datos y consumidores importa más que encontrar un método llamado logout.

**Recomendación.** Mantener una regresión de la secuencia válida-revocación-reuso y un inventario de consumidores que comprueban la clave.

**Verificación propuesta.** Reutilizar credenciales anteriores por las rutas identificadas y registrar ausencia de datos o de nueva emisión; incorporar un consumidor adicional solo si entra en alcance. Vínculo: H08 / R07. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H06 CSRF según transporte del refresh

**Condición y evidencia.** La cookie requiere csrfToken; la ruta por argumento explícito tiene un contrato distinto. La matriz histórica comprueba presencia/ausencia/error y la unidad nueva compara secretos iguales o distintos bajo máscaras válidas. Referencias: CM-T03;CM-U04; saleor/graphql/account/mutations/authentication/refresh_token.py:60-145; saleor/graphql/account/mutations/authentication/utils.py:55-65.

**Interpretación y límites.** No se probó origen en navegador, preflight CORS, almacenamiento del frontend ni todos los formatos malformados. El resultado es de la condición implementada.

**Recomendación.** Documentar el modelo de cliente y mantener casos por transporte, sin presentar el argumento explícito como un bypass automático o el CSRF como defensa universal.

**Verificación propuesta.** En C10, comparar peticiones del navegador con origen permitido/no permitido y preservar tokens solo en memoria. Vínculo: H05;H06;H07 / R06. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H07 Cookies condicionadas por configuración

**Condición y evidencia.** El middleware fija HttpOnly y usa Secure/SameSite según DEBUG. La caracterización histórica distingue ambos modos. El nombre refreshToken carece de los prefijos examinados en ASVS 3.3.1. Referencias: CM-T14; saleor/core/middleware.py:18-40; saleor/core/jwt.py:23.

**Interpretación y límites.** El efecto de navegador/TLS no se evaluó. La nomenclatura y el canal del mismo valor requieren interpretación de cliente/aplicabilidad; no constituyen por sí solos un exploit.

**Recomendación.** Fijar DEBUG=False en el despliegue objetivo, documentar TLS y política de cookies y evaluar compatibilidad de prefijos dentro del contrato de cliente.

**Verificación propuesta.** Inspeccionar Set-Cookie sobre HTTPS y almacenamiento/flujo real antes de adjudicar la condición completa. Vínculo: H07 / R06. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H08 Separación de acceso a usuarios y personal

**Condición y evidencia.** Las pruebas históricas comparan me anónimo/autenticado y user con actor ajeno, anónimo y personal con permisos diferenciados sobre clientes o staff. Referencias: CM-T01;CM-T12;CM-T13; saleor/graphql/account/resolvers.py:76-119.

**Interpretación y límites.** La muestra no representa todos los campos y combinaciones de permisos. Un error de autorización aislado no prueba ausencia de efectos o datos en otras rutas.

**Recomendación.** Mantener una matriz de rol-recurso-campo y extenderla solo para los campos pertinentes; verificar datos además de códigos de error.

**Verificación propuesta.** Afirmar exactamente qué entidad/campo se devuelve o queda ausente para cada consumidor y permiso. Vínculo: H11 / R10. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H09 Intersección de permisos delegados

**Condición y evidencia.** Los tokens de acción delegada restringen permisos mediante intersección de usuario y aplicación; dos variantes históricas cubren solapamiento y conjuntos disjuntos. Referencias: CM-T20; saleor/core/jwt.py:172-199.

**Interpretación y límites.** No se evaluó una app real, todo el ciclo de revocación o la política de cada servicio receptor. Intersección local no demuestra corrección de toda delegación.

**Recomendación.** Documentar scopes y consumidores y conservar controles de intersección vacía/parcial; revisar cambios de permisos durante la vida del token.

**Verificación propuesta.** Emitir credenciales sintéticas para permisos conocidos y comparar el conjunto exacto, además del efecto al ejecutar una operación autorizada o denegada. Vínculo: H15 / R13. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H10 Semántica de pedidos UUID y legacy

**Condición y evidencia.** Con UUID conocido, actores ajenos/anónimos obtienen campos sintéticos originales; la ruta legacy aplica ofuscación. Controles de propietario e ID ausente y comparación exacta caracterizan el resultado. Las unidades nuevas muestran dominio/primer carácter/longitud residuales y la precondición de formato del helper. Referencias: CM-T05;CM-T06;CM-T07;CM-T22;CM-T23;CM-T24;CM-T25;CM-T26;CM-T27;CM-U05;CM-U06;CM-U07; saleor/graphql/order/types.py:2161-2222,2636-2665; saleor/core/anonymize.py:1-18.

**Interpretación y límites.** No se demuestra enumeración de UUID, obtención desde storefront o fuga real. P-ORDER-01 sigue provisional; sus dos XFAIL de correo no son dos vulnerabilidades ni cubren por separado las calles.

**Recomendación.** Definir si el UUID es una capacidad compartible, quién puede recibirlo y qué campos corresponden a cada audiencia; acordar información residual permitida y validar entradas del helper.

**Verificación propuesta.** Trazar el flujo legítimo de entrega del ID y repetir la matriz por actor/campo en un despliegue controlado con una política explícita, sin parchear el producto para aprobar una propuesta tácita. Vínculo: H12 / R11. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H11 Límites configurables de consultas

**Condición y evidencia.** Se registran validadores de costo, alias y mutaciones; los casos históricos rechazan dos elementos cuando el umbral se configura en uno. Referencias: CM-T15;CM-T16; saleor/graphql/core/validators/__init__.py:26-49.

**Interpretación y límites.** No se midió costo máximo general, profundidad exhaustiva, carga, estrés o capacidad distribuida. Un rechazo de dos operaciones no acredita disponibilidad global.

**Recomendación.** Documentar límites efectivos y agregar valores bajo/en/sobre umbral para consultas pertinentes; separar ensayos funcionales de rendimiento.

**Verificación propuesta.** Comprobar el rechazo antes de ejecutar operaciones y la ausencia de efectos laterales; medir rendimiento solo bajo un protocolo autorizado distinto. Vínculo: H13 / R12. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H12 Captura amplia y diagnóstico de errores

**Condición y evidencia.** get_payload transforma excepciones JWT específicas; get_user captura Exception y convierte cualquier causa en ausencia de usuario. Referencias: S06; saleor/graphql/account/mutations/authentication/utils.py:19-58.

**Interpretación y límites.** La inspección identifica una captura amplia, pero no demuestra una explotación. Puede reducir la precisión diagnóstica y ocultar una dependencia averiada.

**Recomendación.** Acotar excepciones esperadas y diferenciar errores recuperables/internos en registros depurados, manteniendo respuestas externas prudentes.

**Verificación propuesta.** Introducir en una prueba aislada una excepción prevista y una inesperada y verificar respuesta/registro sin revelar datos ni credenciales. Vínculo: H09 / R08. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H13 Audiencia conservada frente a receptor validado

**Condición y evidencia.** El claim aud se conserva en emisión/renovación. El decoder permite verify_aud opcional y lo desactiva por defecto al tratar tokens propios. Referencias: CM-T08;CM-T11; saleor/core/jwt_manager.py:183-200; saleor/graphql/account/mutations/authentication/refresh_token.py:138-145.

**Interpretación y límites.** Conservar el claim no valida una allowlist del receptor. La aplicabilidad depende de servicios, emisores y modelo de audiencia; no se demuestra aceptación indebida de un token de otro servicio.

**Recomendación.** Definir receptores y públicos previstos y documentar cómo se valida o limita el uso del token; diseñar un negativo de audiencia ajena si corresponde.

**Verificación propuesta.** Presentar un token sintético válido para otro receptor y observar rechazo bajo un contrato de servicio explícito, sin asumirlo por un claim presente. Vínculo: H09;H15 / R08. No se asigna CVSS ni se declara mitigación de producto aplicada.

## A2-H14 Vida absoluta e inactividad de sesión

**Condición y evidencia.** Se comprueban TTL de emisión de access/refresh, pero no se dispone de una política del caso que fije inactividad, vida absoluta y reautenticación ni de una prueba de esa sesión completa. Referencias: CM-T08;CM-T11; saleor/settings.py:992-1000; saleor/graphql/account/mutations/authentication/refresh_token.py:138-145.

**Interpretación y límites.** Expirar un JWT y renovar otro no prueban que una sesión no pueda prolongarse más allá de un máximo de negocio. No se inventa que la configuración sea incorrecta sin ese criterio.

**Recomendación.** Definir una política temporal justificada por el caso y distinguir caducidad de token, revocación e interacción del usuario; seleccionar una prueba con reloj controlado.

**Verificación propuesta.** Recorrer una secuencia de renovaciones y comprobar el máximo absoluto/inactividad adoptados antes de afirmar conformidad. Vínculo: H04 / R04. No se asigna CVSS ni se declara mitigación de producto aplicada.

## Síntesis por objetivo

La caracterización de arquitectura, actores y amenazas del primer avance se conserva y se precisa con módulos y dependencias. El examen técnico incorpora controles positivos/negativos y nuevos resultados de firma, vigencia, CSRF y bordes, delimitados por fuente y entorno. El objetivo de diez observaciones técnicas con recomendaciones dispone de catorce entradas diferenciadas. No se afirma haber aplicado mitigaciones del producto: se mejoró el harness y el control documental; las políticas y cambios funcionales siguen siendo propuestas sujetas a criterio y retest.

## Propuesta de tratamiento

Primero deben resolverse las decisiones que cambian la interpretación: audiencia de pedidos/UUID, política de tiempos, servicios receptores y configuración confiable de proxy/cookies. Después se validan sus condiciones con casos específicos. Conviene conservar regresiones de controles positivos, mejorar diagnóstico de capturas amplias y ampliar lo que permanezca dentro de la pregunta. Esta secuencia evita parchear comportamiento deliberado o convertir una alerta de herramienta en un defecto sin fundamento.

La prioridad de investigación de los riesgos del primer avance no se traduce en severidad empírica. Las recomendaciones no llevan ahorros, porcentajes de reducción o probabilidades inventadas. Cada retest propuesto debe registrar condición previa, cambio, esperado y observado; si no se ejecuta, permanece propuesto.

## Validez y límites

El muestreo es intencional sobre seis operaciones y utilidades relacionadas, no una muestra aleatoria de Saleor. Las aserciones de caracterización pueden pasar ante un comportamiento que requiere debate de negocio. El algoritmo esperado y el valor observado deben tener procedencia independiente; por eso las unidades de masking usan literales. Los tests de integración históricos y los nuevos aislados difieren en entorno y no se suman como porcentajes de cobertura.

No se ejecutó un nuevo CI integrado ni un despliegue C10. La configuración de pruebas usa helpers y secretos sintéticos y no representa el coste criptográfico de producción. No se concluye explotación real, enumeración de UUID, fortaleza de HTTPS, consistencia de proxy o cumplimiento global ASVS. Las conclusiones son válidas para los componentes y condiciones realmente examinados y pueden cambiar ante una política o evidencia nueva.
