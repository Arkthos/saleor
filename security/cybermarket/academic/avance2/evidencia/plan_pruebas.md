# A2-04 — Plan de pruebas y clasificación

**Estado:** diseño completado. Los resultados nuevos se registrarán en A2-05; este documento no afirma ejecución de los casos propuestos.

## Reutilización y clasificación

Se conservan CM-T01–T27, sus 61 variantes y el CSV histórico. clasificacion_pruebas.csv añade nivel, diseño, dependencias, alcance de aserción, estado normativo y referencia de evidencia sin reescribir el historial. Cuatro IDs ejercitan directamente funciones (T17, T18, T19, T21); 23 combinan GraphQL, fixtures y base de datos. El diseño es de caja blanca porque se conoce el código. Las propiedades ensayadas no se convierten en negras por ejecutarse con pytest.

La clasificación por cuerpo no demuestra aislamiento de la ejecución completa: conftest.py carga fixtures globales que pueden requerir DB incluso para un cuerpo pequeño. Se comprobó esa dependencia al intentar una prevalidación del validador. El nuevo estrato unitario usará --noconftest para medir funciones sin esas fixtures y sin conectar a PostgreSQL; se conservará la configuración usada. Esto no habilita sustituir la integración por stubs ni atribuir ese resultado a la suite CI completa.

## Ampliaciones seleccionadas

| ID propuesto | Unidad y propósito | Entradas y control | Criterio esperado |
|---|---|---|---|
| CM-U01 | jwt_decode y firma | JWT HS256 válido, luego primer carácter de firma alterado | Control válido decodifica; alteración produce InvalidSignatureError |
| CM-U02 | jwt_decode y expiración | Reloj fijo y exp anterior | ExpiredSignatureError, sin aceptar payload |
| CM-U03 | jwt_decode y nbf | Reloj fijo y nbf futuro | ImmatureSignatureError |
| CM-U04 | Comparación CSRF | Máscaras válidas de secretos iguales o distintos | Mismo secreto coincide aunque cambie máscara; secreto distinto no coincide |
| CM-U05 | obfuscate_string | Vacío, None, un carácter, varios caracteres y teléfono | Valores literales exactos, incluida información residual |
| CM-U06 | obfuscate_email | Correo normal, local corto/vacío y texto sin arroba | Máscara literal esperada; no se usa el helper para calcular la expectativa |
| CM-U07 | Supuesto de entrada del helper de correo | Varias arrobas | ValueError documentado; no se afirma vulnerabilidad de una API sin trazar su entrada |
| CM-U08 | get_client_ip | IPv4/IPv6, cadena inválida y fallback | Selección sintáctica exacta; no prueba confianza del proxy |
| CM-U09 | get_token_from_request | Ausente, incompleto, prefijo no admitido y formato mixto | Token o ausencia literal según contrato de extracción |
| CM-U10 | get_delay_time | Cero, borde 10/11, borde 99/100 y usuario 9 | Retraso determinista exacto en bordes; sin ensayar fuerza bruta |

Las credenciales y máscaras son sintéticas y no se imprimen en reportes. Los timestamps se fijan con freezegun; las funciones se importan del producto sin copiar su implementación. No se añaden porcentajes de cobertura sin instrumentación. CM-U01–03 amplían propiedades no demostradas por comprobar emisión de exp/iat o rechazar alg none. CM-U05–07 aportan expectativas independientes al comportamiento de ofuscación previamente comparado con el propio helper.

## Ejecución y salida

1. Registrar versión de Python, dependencias/lockfile, fuente y configuración local.
2. Comprobar formato de tests con Ruff y ejecutar el estrato aislado sin fixtures globales; conservar JUnit y salida breve. Guardar fallos iniciales y la razón de cualquier corrección del harness.
3. Ejecutar los dos módulos de validación de evidencia bajo aislamiento justificado; son pruebas del sistema de evidencia y se cuentan separadamente.
4. Descargar y verificar el ZIP focal histórico y su SHA256SUMS, reconciliar XML/JSON/CSV; conservar los archivos depurados propios antes de su caducidad.
5. Intentar solo las revalidaciones integradas que permitan recursos reales. Si no hay PostgreSQL/servicios, registrar BLOCKED y la diferencia de entorno; nunca PASS. No alterar el producto o el oráculo para forzar un resultado.
6. Preparar un cierre que distinga IDs, variantes, nivel, resultado, requerimiento y límite. C10 y las pruebas de carga/estrés quedan sometidas a una decisión de alcance separada.

El criterio de salida del nuevo conjunto unitario es ejecución reconciliada y aserciones significativas. Un fallo real se analiza y se reporta; no se elimina para satisfacer un conteo. Los resultados de contratos o caracterizaciones no adjudican por sí solos una condición normativa. La aceptación académica final requiere la síntesis de A2-07 y la auditoría de A2-09.
