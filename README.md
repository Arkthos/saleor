# CyberMarket CR — pruebas y evidencias de Seguridad de Software

Repositorio de sustento técnico del trabajo académico sobre autenticación,
JWT y autorización en Saleor. La rama `main` reúne el código de pruebas,
los resultados conservados y un procedimiento para recuperar la versión
evaluada. El documento académico se entrega por separado.

## Ruta de revisión

1. [Resumen verificable y límites](docs/RESULTADOS_Y_ALCANCE.md).
2. [Cierre técnico detallado](security/cybermarket/academic/avance2/CIERRE_PRUEBAS_TECNICAS.md)
   y [manifiesto final](security/cybermarket/academic/avance2/evidencia/revalidacion_tecnica/CIERRE_TECNICO.json).
3. [Matriz de los 27 casos](security/cybermarket/test_matrix.csv),
   [clasificación de pruebas](security/cybermarket/academic/avance2/evidencia/clasificacion_pruebas.csv)
   y [criterios y oráculos](security/cybermarket/academic/avance2/evidencia/criterios_y_oraculos.md).
4. [Revisión de codificación](security/cybermarket/academic/avance2/evidencia/revision_codificacion.md),
   [análisis estático](security/cybermarket/academic/avance2/evidencia/analisis_estatico.md)
   y [conciliación de hallazgos](security/cybermarket/academic/avance2/evidencia/revalidacion_tecnica/conciliacion_hallazgos_tecnicos.md).
5. [Reproducción](reproduction/README.md) y [respaldo y consolidación](docs/CONSOLIDACION.md).

## Resultados conservados del 2 de noviembre de 2026

| Batería | Resultado | Relación entre conteos |
|---|---:|---|
| Regresión general | 17.613 PASS + 2 XFAIL previstos | Incluye la suite focal |
| Focal CyberMarket | 59 PASS + 2 XFAIL previstos | 27 IDs, 61 variantes; subconjunto de general |
| Unidades y validadores independientes | 42 PASS | 30 variantes de producto + 12 de validadores |
| C10 HTTP/HTTPS/Chromium | 26 PASS | Laboratorio privado sobre loopback |
| E2E original | 211 PASS | Suite separada |
| Fronteras de licencias | 6 PASS | Repetidas en base/head; contar una vez |

Fuente de pruebas: `eb5d3ecbac104b32b42145f6c4a3db5c5fd8f2e7`.
Checkout histórico de Actions: `90455ca8abb7d72f707e0137e3ac80fab7a06dec`.
Producto base: `4cb1609a90eade14b6275a407bc7a00c35698090`.
Estos resultados pertenecen a esas ejecuciones; no acreditan nuevas pruebas
de producto sobre el HEAD de consolidación.

Los dos XFAIL son exclusivamente de CM-T22: una expectativa de privacidad
P-ORDER-01 **provisional y no aprobada**. No son dos vulnerabilidades oficiales
confirmadas de Saleor. Los dictámenes formales de riesgo y ASVS siguen sin
adjudicar. El alcance y las limitaciones están en el informe enlazado arriba.

## Organización

| Ruta | Contenido |
|---|---|
| `saleor/graphql/tests/test_cybermarket_security_*.py` | Cuatro archivos de casos focales; requieren recuperar Saleor |
| `tests/test_cybermarket_*.py` | Unidades, validadores y controles de licencias |
| `security/cybermarket/live/tests/` | Pruebas C10, transporte, entorno y depuración de evidencia |
| `security/cybermarket/academic/avance2/evidencia/` | Matrices, análisis, manifiestos, JUnit y ZIP conservados |
| `security/cybermarket/` | Herramientas de validación y evidencia histórica fechada |
| `.semgrep/` | Reglas y fixtures de prueba del análisis estático; algunos fixtures son deliberadamente inseguros |
| `reproduction/` | Fuente fijada, preparación de laboratorio, ejecución y configuraciones históricas |
| `docs/` | Índice de resultados, decisiones de consolidación e inventario de conservación |

Los archivos históricos conservan sus estados y cifras de su fecha. Para el
cierre técnico vigente, usar `CIERRE_TECNICO.json` y `CIERRE_PRUEBAS_TECNICAS.md`.
El árbol actual conserva las rutas de evidencia citadas en el trabajo.

## Verificación sin instalar Saleor

Desde la raíz, con Python 3.12 o posterior:

```bash
python scripts/verify_delivery.py
```

Comprueba los hashes del paquete, el contenido de los ZIP, los manifiestos
internos presentes y los conteos JUnit finales. No usa red, base de datos ni
credenciales. El workflow **Integridad de evidencias** ejecuta esa misma
comprobación; su éxito no equivale a repetir la batería de Saleor.

Para ejecutar pruebas sobre el producto, seguir [reproduction/README.md](reproduction/README.md).
El código funcional completo, los borradores y las ramas anteriores están
en el respaldo previo; también se conserva la historia Git en `main`.
