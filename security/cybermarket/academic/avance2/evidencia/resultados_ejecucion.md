**Actualización de cierre, 2026-11-02:** pruebas actuales finalizadas y verificadas. [Cierre completo](../CIERRE_PRUEBAS_TECNICAS.md); [manifiesto vigente](revalidacion_tecnica/CIERRE_TECNICO.json). El contenido previo conservado abajo describe su fase anterior y será incorporado al reanálisis académico.

# A2-05 — Ejecución local y verificación independiente de evidencia histórica

## Resultado nuevo

Se implementaron diez IDs CM-U01–U10 en tests/test_cybermarket_security_units.py. La ejecución aislada final produjo **30 PASS de unidades de producto y doce PASS de los dos módulos de validación de evidencia**, total 42 ejecuciones, sin fallos, errores, omisiones o warnings en esa corrida. Se registran JUnit, fuente/lockfile SHA-256 y comando en resultados_ci_manifest.json. La propiedad cybermarket_unit_id permite distinguir las 30 variantes de producto de las doce invocaciones del harness; no se presentan como 42 requisitos o 42 controles diferentes.

Las unidades ejercitan firmas HS256 válidas/alteradas, exp y nbf con reloj fijo, comparación CSRF con máscaras válidas, ofuscación con resultados literales y bordes de IP, cabeceras y backoff. Se importan funciones del producto, sin copiar su lógica para obtener un resultado. Los valores de masking se escribieron independientemente del helper. Los tests nuevos se publicaron en el commit 5c7e4233ba24412ed80e3cd9a76a2ee18e4990a9 antes de la corrida final; el manifiesto distingue ese contenido del checkout local base.

El estrato se ejecutó con --noconftest, sin las fixtures globales del repositorio, y un solo worker. No usa PostgreSQL, caché remota ni red. Configurar una clave sintética larga evita que el fixture de tests de nueve bytes contamine con warnings las pruebas de firma. Esto no es una modificación o hallazgo sobre la clave de producción. La ejecución completa normal del repositorio mantiene sus propias fixtures y dependencias.

## Intentos iniciales y correcciones

Un intento inicial de los seis tests del validador bajo las fixtures normales produjo seis errores de setup por ausencia de PostgreSQL, no seis fallos del control de acceso. Se conservaron sus conteos y causa. La ejecución de validadores aislados pasó doce invocaciones de dos módulos; algunas comprobaciones se solapan y no se cuentan como doce controles nuevos. El primer conjunto de 30 unidades ya pasó, pero produjo warnings de longitud de clave del fixture; se ajustó solo el setup sintético del test. Ruff también pidió un match más específico para ValueError; se añadió y se verificaron formato y reglas del archivo nuevo.

La instalación inicial de dependencias falló por clang ausente al compilar pywatchman. CC=gcc uv sync --locked funcionó sin cambiar el lockfile. Estas diferencias de entorno forman parte de la reproducibilidad y no se ocultan como si la primera orden hubiese completado todo.

## Evidencia histórica recuperada

Se descargaron los ZIP focal, estático y general del 20 de octubre. Sus SHA-256 coinciden con los digests informados por GitHub. También se verificaron los SHA256SUMS internos donde están incluidos. El XML focal contiene 61 testcases, cero failures/errors y dos pytest.xfail; el general contiene 17 615 testcases con los mismos dos XFAIL. Los conteos respaldan 59 y 17 613 PASS respectivamente. Los casos focales están incluidos en la suite general y no se suman como evidencia independiente.

El inventario y hashes completos se preservan en historica_2026-10-20/archivo_verificado_manifest.json. Se conservaron los componentes focales y los reportes estáticos; el archivo general se mantiene en el paquete de evidencia con su hash, evitando insertar miles de casos del producto ajenos a la muestra en el cuerpo del informe. El archivo de evidencia del proyecto preserva los ZIP originales verificados.

## Lo que no se ejecutó

No hay nuevos runs remotos asociados al commit documental de entrada ni al commit de unidades al consultar. La revalidación de la integración GraphQL/general/E2E en un HEAD nuevo no se declara realizada. No se dispone de PostgreSQL ni Docker local y el proceso no puede cambiar a un usuario no privilegiado para configurar un servidor nativo de PostgreSQL. Se mantuvo el entorno aislado sin conectar a sistemas externos. No se reejecutó un run viejo para hacerlo pasar por evaluación de código nuevo.

El paquete experimental de esta fase concluye las ampliaciones aisladas seleccionadas y el archivo independiente de evidencia. La revalidación integrada nueva queda como limitación y tarea identificada, sin alterar los resultados históricos. Los dictámenes de riesgo y la autoridad de P-ORDER-01 no cambian por obtener PASS. No se midió cobertura de ramas, resistencia a carga, TLS ni comportamiento de navegador. La decisión de C10 se documenta en A2-06.

## Integridad frente a formateadores

Los XML y JSON archivados se conservan byte a byte para que sus checksums sigan siendo verificables. Algunos XML generados no terminan en salto de línea. Se excluyen únicamente los directorios de evidencia de máquina ejecucion_local/ e historica_2026-10-20/ de los hooks de espacios finales/EOF; siguen comprobándose hashes y estructura. No se excluye código, el manuscrito o el resto de documentación de las reglas de calidad. Los originales verificados también se conservan en el paquete de evidencia del proyecto.
