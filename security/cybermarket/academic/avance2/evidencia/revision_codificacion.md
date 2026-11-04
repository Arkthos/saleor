# A2-03 — Codificación segura aplicada

La revisión utiliza el código funcional conservado en 4cb1609… y el checkout de investigación 5f4d416…; no introduce parches de producto. Trece registros en revision_manual.csv cubren las cuatro dimensiones docentes: control, datos, fallas e interfaces. Los rangos de línea apuntan al código revisado; los IDs CM son evidencia histórica relacionada, no resultados nuevos de esta fase.

## Prácticas y decisiones observadas

**Validación en backend y mediación.** La extracción de cabeceras identifica credenciales, pero autenticar exige seguir la clasificación del token, jwt_decode, tipo de credencial y clave por usuario. is_saleor_token decodifica sin verificar firma para clasificar el propietario; load_user_from_request llama después a jwt_decode antes de confiar en la identidad. Analizar una llamada fuera de esa cadena produciría un falso hallazgo de autenticación sin firma.

**Control de acceso y extensión.** BaseMutation.mutate consulta check_permissions antes de perform_mutation. El método base permite continuar cuando no se declaran permisos, como punto de extensión; por eso H10 requiere inventario de mutaciones concretas y controles adicionales. La recomendación es registrar el contrato de cada ruta y sus casos negativos, no convertir toda operación sin Meta.permissions en una vulnerabilidad. Los resolvers de user distinguen permisos y tipos de cuenta. En pedidos, la bifurcación UUID/legacy exige revisar campos y loaders además del esquema de consulta.

**Estados y credenciales.** Revocación cambia la clave por usuario y los consumidores seleccionados la comparan. Las credenciales de acceso y refresh tienen propósitos distintos; RefreshToken valida su tipo antes de emitir acceso. La audiencia conservada al renovar no constituye una validación del receptor. Se necesitan pruebas específicas de firma alterada, expiración y nbf para ampliar las propiedades ya comprobadas; el TTL de emisión no sustituye una política de vida absoluta o reautenticación.

**Errores y robustez.** get_payload distingue errores JWT para devolver códigos controlados de la API. En cambio, get_user captura Exception y lo convierte en ausencia de usuario. Esta captura amplia puede esconder causas inesperadas y dificultar diagnóstico; es una observación de robustez, no una explotación demostrada. Conviene delimitar excepciones conocidas, mantener errores externos sobrios y registrar fallas internas depuradas, sin introducir tokens en logs.

**Configuración y transporte.** La cookie usa HttpOnly y varía Secure/SameSite con DEBUG. El nombre refreshToken no utiliza los prefijos examinados en ASVS 3.3.1. Deben analizarse por separado la propiedad estática del nombre, la configuración efectiva, el cliente y el riesgo de transporte. Un flag correcto en una respuesta de Django no demuestra funcionamiento seguro en navegador ni HTTPS. El manejo de IP toma valores de encabezado; la confianza depende del borde y no de que la cadena sea una IP válida.

**Límites y representación.** validate_query registra controles de costo, alias y cantidad de mutaciones. Dos consultas sobre el umbral configurado aportan evidencia de una condición, sin medir carga ni todas las formas de complejidad. Las funciones de ofuscación retienen dominio, primer carácter y/o longitud. Esa información residual debe discutirse con un criterio de datos, no llamarse anonimización completa. Una entrada con múltiples arrobas puede producir ValueError en el helper de correo: el helper presupone un formato, por lo que su contexto de uso y validación importan.

## Encapsulamiento y SOLID

El código separa extracción de credenciales, gestión JWT, mutaciones, resolvers y helpers, lo que facilita revisar responsabilidades y probar funciones aisladas. No se atribuye cumplimiento global de SOLID por existir módulos. El punto check_permissions muestra extensión mediante sobreescritura, pero cada implementación debe preservar el contrato de autorización. Las interfaces de cookie/argumento y request.META hacen visibles dependencias del entorno: esconder esos supuestos bajo una etiqueta de encapsulamiento no protege por sí solo un recurso.

La revisión prioriza invariantes y contratos: no aceptar tipo equivocado, no confiar en un payload antes de validarlo, no permitir datos por un mero error de clasificación y no alterar estados si una operación fue denegada. Las ampliaciones de A2-04 se seleccionan para medir estas propiedades con valores esperados independientes. No se ejecutan todos los temas del curso sin una pregunta que lo justifique.

## Tratamiento

Se recomiendan aclaraciones de política/configuración, mejora de diagnóstico y pruebas focales antes que parches especulativos. El estudio mantiene P-ORDER-01 provisional y los dictámenes normativos pendientes. Los resultados de herramientas se registran separadamente en analisis_estatico.md. Las observaciones anteriores alimentan el catálogo A2-Hxx, sin contarlas todavía como trece vulnerabilidades o trece hallazgos finales aprobados.
