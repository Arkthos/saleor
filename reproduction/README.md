# Recuperar la fuente y reproducir las pruebas

## 1. Comprobar primero la evidencia conservada

Desde la raíz del repositorio, con Python 3.12 o posterior:

```bash
python scripts/verify_delivery.py
```

Este paso no necesita red ni Saleor instalado.

## 2. Preparar una copia aislada y exacta

Requisitos: Git, Python 3.12 y `uv`. La instalación del entorno necesita
acceso a los registros de paquetes. No usar una base de datos productiva.

```bash
python reproduction/prepare_source.py /tmp/cybermarket-lab
cd /tmp/cybermarket-lab
uv sync --locked
```

El destino no debe existir. El preparador obtiene
`eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7` y comprueba el ID del árbol,
SHA-256 de `uv.lock` y cada archivo de pruebas conservado. No incorpora
automáticamente cambios nuevos del repositorio limpio ni usa `main` como
versión del producto. El checkout efímero histórico de Actions se registra
como procedencia; no se afirma reproducir su SHA de merge.

Si se trabaja sin acceso al repositorio remoto, primero restaurar el bundle:

```bash
git clone --mirror /ruta/saleor-pre-cleanup-2026-11-04.bundle /tmp/saleor-respaldo.git
python reproduction/prepare_source.py /tmp/cybermarket-lab --from-repository /tmp/saleor-respaldo.git
```

Esto evita depender de la disponibilidad futura de la rama de investigación.
La instalación de dependencias sigue requiriendo paquetes o una caché propia.

## 3. Ejecutar una batería elegida

Para las pruebas con datos se necesitan PostgreSQL 15 y Valkey 8.1
**desechables**, accesibles solo desde el laboratorio. La cuenta PostgreSQL
necesita crear su base de prueba. Las configuraciones exactas del runner
histórico están en [reference/workflows/e2e.yml](reference/workflows/e2e.yml).
No se inicia ningún servicio al preparar la fuente.

Desde el repositorio limpio:

```bash
export DATABASE_URL='postgres://saleor:saleor@127.0.0.1:5432/saleor'
export CACHE_URL='redis://127.0.0.1:6379/0'
export SECRET_KEY='cybermarket-disposable-local-lab-only-key'
export ALLOWED_CLIENT_HOSTS='127.0.0.1,localhost'
export SEND_USAGE_TELEMETRY='False'
python reproduction/run_suite.py /tmp/cybermarket-lab focal
python reproduction/run_suite.py /tmp/cybermarket-lab units
```

| Selector | Ejecución |
|---|---|
| `focal` | Cuatro archivos CM-T01–CM-T27, incluye dos XFAIL estrictos previstos |
| `units` | 30 variantes de producto + 12 de validadores, sin base ni red |
| `licenses` | Seis controles de frontera del normalizador; no repite el análisis de 502 entradas |
| `live` | 26 casos C10; requiere servicios y Chromium/NSS/TLS de laboratorio |
| `e2e` | Suite E2E original, separada |
| `general` | Regresión general no E2E, que ya incluye focal |

Antes de `live`, instalar `libpq-dev` y `libnss3-tools` mediante el gestor de
paquetes del sistema y ejecutar dentro de la fuente preparada:

```bash
uv run --with playwright==1.56.0 python -m playwright install --with-deps chromium
```

Los comandos de Bandit, Semgrep, linters y licencias completos se conservan
en los workflows de referencia. Deben ejecutarse desde la fuente preparada;
escaneo del árbol reducido no equivale a examinar Saleor. Los fixtures de
reglas deliberadamente inseguros deben excluirse del escaneo de producto y
validarse aparte con las pruebas de reglas.

## Evidencia de una reproducción nueva

Cada selector crea una carpeta nueva bajo `technical-results/` en la copia
del laboratorio, registra SHA, versión de Python y comando, conserva JUnit,
depura la salida estructurada y calcula hashes. Se preserva el código de
salida de pytest; una sanitización fallida también falla la ejecución.
No se copian resultados nuevos al archivo histórico automáticamente.
La salida de consola debe revisarse antes de publicarla; no debe contener
JWT, cookies utilizables, secretos ni datos reales.

Cambiar de sistema, versiones resueltas o imágenes puede cambiar resultados.
Una reproducción necesita su propia revisión; el control de integridad
de este repositorio solo valida la evidencia ya conservada.
