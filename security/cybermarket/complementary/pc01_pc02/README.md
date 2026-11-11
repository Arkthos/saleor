# PC-01 y PC-02: scripts y evidencia complementaria

Este paquete conserva los dos scripts y los resultados JSON entregados por
el integrante del grupo. Los scripts, el ZIP y los JSON extraídos mantienen
sus bytes originales. La incorporación al repositorio comprende revisión
estática e integridad de archivos; no incluye una nueva ejecución contra Saleor.

## Ruta de revisión

| Archivo | Contenido |
|---|---|
| [PC_01.py](PC_01.py) | Tres solicitudes de registro con distintas contraseñas |
| [PC_02.py](PC_02.py) | Comparación de respuestas de registro para dos correos |
| [Resultados PC-01](evidence/evidencias_PC_01/resultados.json) | Respuestas conservadas de PC-01.1, PC-01.2 y PC-01.3 |
| [Resultados PC-02](evidence/evidencias_PC_02/resultados.json) | Respuestas de ambos escenarios y comparación normalizada |
| [ZIP original](evidence/original.zip) | Copia exacta de `Evidencias PC_01 y PC_02.zip` |
| [SHA256SUMS](SHA256SUMS) | Hashes de todos los archivos de este paquete, salvo el propio manifiesto |

## Resultados que contienen los archivos

| Caso | Entrada o comparación | Resultado registrado |
|---|---|---|
| PC-01.1 | Contraseña numérica de 8 caracteres | `SIN_ERRORES_REPORTADOS` |
| PC-01.2 | Contraseña común de 11 caracteres | `SIN_ERRORES_REPORTADOS` |
| PC-01.3 | Contraseña de control de 12 caracteres | `SIN_ERRORES_REPORTADOS` |
| PC-02.1 / PC-02.2 | Correo declarado existente frente a correo generado | `RESPUESTAS_EQUIVALENTES` en los campos normalizados |

En las cinco respuestas, `accountRegister.errors` es una lista vacía y
`user.id` es una cadena vacía. PC-01 registra la ausencia de errores de la
API. Estos JSON, por sí solos, no acreditan la creación de las cuentas,
la coincidencia de contraseñas en la base de datos ni los validadores activos.
La etiqueta original `Contrasena robusta` de PC-01.3 se conserva como parte
del archivo recibido; corresponde a un ejemplo fijo y no acredita su robustez.

PC-02 compara presencia de `user`, `user.id`, errores de registro y errores
generales de GraphQL. Excluye el correo devuelto y `extensions`; su conclusión
se refiere a esos campos, no a la igualdad completa de las respuestas.
No mide tiempos ni examina mensajes de correo u otros canales.

El script PC-02 supone que `pc01-prueba01@example.com` ya existe, pero no lo
crea ni verifica esa condición. Ejecutar PC-01 tampoco la establece: PC-01
genera correos distintos con UUID. Sin evidencia del estado previo de ambos
correos, el JSON conserva una comparación de respuestas, pero no basta para
confirmar protección contra enumeración de usuarios.

## Procedencia y alcance

Los artefactos recibidos no incluyen fecha verificable de ejecución, SHA
del código de Saleor, versiones del entorno, volcado de
`AUTH_PASSWORD_VALIDATORS` ni resultados de consultas a la base de datos.
La fecha del commit identifica la publicación de este paquete, no la
ejecución original. Los hashes permiten detectar cambios posteriores;
no certifican por sí mismos cómo se obtuvieron las respuestas.

Los scripts usan la biblioteca estándar de Python y envían solicitudes POST
a `http://localhost:8000/graphql/`, con `redirectUrl` fijado en
`http://localhost:3000/`. Contienen correos `example.com` y contraseñas de
prueba literales. No incluyen aserciones de `pytest` ni producen resultados
JUnit. Sus observaciones se mantienen separadas de los 27 casos focales y
de los conteos históricos PASS/XFAIL. No se atribuyen a GitHub Actions.

## Ejecución posterior en un laboratorio aislado

Antes de ejecutarlos, preparar una instancia local desechable de Saleor
en la URL indicada y registrar su SHA, versiones, configuración y estado
previo de la base de datos. Para PC-02, crear y verificar específicamente
`pc01-prueba01@example.com` y registrar la ausencia inicial del correo nuevo.
El script genera ese segundo correo durante su ejecución; una reproducción
con control explícito de ambos correos requiere una copia instrumentada,
con sus cambios y hash propios. Conservar estos originales intactos.

Desde la raíz del repositorio, usar un directorio nuevo para cada ejecución
y pasar rutas absolutas a los scripts:

```bash
repo_root="$PWD"
run_dir="$(mktemp -d)"
cd "$run_dir"
python "$repo_root/security/cybermarket/complementary/pc01_pc02/PC_01.py"
python "$repo_root/security/cybermarket/complementary/pc01_pc02/PC_02.py"
```

Las solicitudes pueden crear cuentas. Los archivos nuevos se escriben en
`evidencias_PC_01/resultados.json` y `evidencias_PC_02/resultados.json` dentro
de `run_dir`. Cada reproducción debe conservar su fecha, código, entorno,
precondiciones, resultados y hashes propios. Los originales recibidos no
se sustituyen con esas salidas.

## Verificación de integridad

Desde esta carpeta, en un entorno con `sha256sum`:

```bash
sha256sum -c SHA256SUMS
```

Desde la raíz del repositorio:

```bash
python scripts/verify_delivery.py
```

El segundo comando comprueba la integridad del paquete completo y la
coherencia de la evidencia histórica. No ejecuta PC-01/PC-02 contra la API.
