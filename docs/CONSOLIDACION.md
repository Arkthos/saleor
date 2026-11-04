# Respaldo y consolidación del repositorio

Fecha: 4 de noviembre de 2026, America/Costa_Rica.
Solicitud: conservar el estado completo y preparar el repositorio actual
como sustento de pruebas, evidencias y reproducibilidad del trabajo.

## Respaldo previo, verificado antes de cambiar GitHub

Se creó un clon espejo y un bundle Git autónomo del estado remoto: **93
ramas, 1.658 etiquetas y dos referencias de PR**. `git fsck --full` y
`git bundle verify` concluyeron sin errores. Se restauró el bundle en otro
clon espejo y se compararon sus 1.753 referencias con el original: igualdad
exacta. Se guardaron el inventario y la instantánea del PR #1 antes de su cierre.

| Archivo de respaldo descargable | SHA-256 |
|---|---|
| `saleor-pre-cleanup-2026-11-04.bundle` (254.373.118 bytes) | `0c5788dbc18980a6309d54dc530a5dc245412d32ad94007a3c3170f045c67d71` |

El respaldo contiene todo lo versionado, incluidas las evidencias técnicas,
borradores y código previo. No pretende incluir secretos, configuración de
cuenta ni artefactos de Actions nunca versionados. La copia y sus metadatos
se entregan por separado; no se añaden 243 MiB al repositorio de presentación.

```bash
git clone --mirror saleor-pre-cleanup-2026-11-04.bundle saleor-restaurado.git
git -C saleor-restaurado.git fsck --full
git clone saleor-restaurado.git saleor-restaurado
git -C saleor-restaurado checkout research/cybermarket-security-tests-v1
```

## Criterios de conservación

Se conservan los archivos de prueba y validación sin alterar su contenido,
matrices, oráculos, análisis técnico, política provisional, evidencia final
y fallos históricos relevantes. Las rutas citadas en el trabajo se mantienen.
El [inventario](INVENTARIO_CONSOLIDACION.json) registra los archivos
conservados y los retirados del árbol respecto de
`c66c34d0c4d639c2e4dc09b9ef7e86ff1cfb29e7`.

Se retiran del árbol los módulos funcionales de Saleor, la infraestructura
de publicación y despliegue, documentación general ajena al estudio,
borradores académicos, generadores de Word y planes de redacción sustituidos.
Las configuraciones de las ejecuciones históricas se guardan en
`reproduction/reference/`, fuera de los workflows activos.

Se consolida la rama de investigación en `main` y se retiran las ramas de
trabajo heredadas después del respaldo. Las etiquetas históricas de versión
se conservan como referencias de procedencia. **No se reescribe ni purga el
historial Git**: los archivos retirados siguen en sus commits anteriores.
Esta limpieza cambia el contenido visible y las ramas activas; no reduce
por sí sola el tamaño del historial de un clon completo.

## Reproducibilidad y límites de la consolidación

`reproduction/prepare_source.py` recupera exactamente la fuente evaluada y
verifica el árbol Git, el lock y los bytes de las pruebas. Se puede usar
el remoto o el espejo restaurado como origen. Así se conserva la posibilidad
de ejecutar las pruebas sin presentar el código completo de Saleor en el
árbol principal.

La consolidación no cambia expectativas, política P-ORDER-01 ni producto.
El único control automático activo al publicar es la integridad del
paquete. Los resultados históricos no se transfieren al nuevo HEAD.
No se publica el Word acumulativo como parte de esta operación.
