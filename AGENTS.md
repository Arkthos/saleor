# CyberMarket CR: repositorio de pruebas y evidencias

Leer primero README.md, docs/RESULTADOS_Y_ALCANCE.md y docs/CONSOLIDACION.md.
La consolidación fue solicitada por el usuario el 2026-11-04 y sustituye la
antigua restricción de mantener el PR #1 abierto como borrador.

- Este árbol es un paquete de sustento técnico. No añadir el manuscrito,
  fuentes docentes completas ni infraestructura de publicación de Saleor.
- Mantener intactos los resultados y archivos históricos. Toda nueva ejecución
  necesita SHA, entorno, resultados y hashes propios.
- No atribuir CI de 2026-11-02 al HEAD actual. No sumar la suite focal a general.
- P-ORDER-01 sigue provisional; caracterización PASS no implica conformidad.
- No modificar el producto para conseguir que pasen los tests. Preparar una
  copia aislada con reproduction/prepare_source.py y ejecutar allí.
- No hacer pruebas sobre servicios externos, datos reales o despliegues públicos.
- Ejecutar scripts/verify_delivery.py tras cambios al paquete y actualizar
  SHA256SUMS únicamente después de revisar las diferencias esperadas.
- Conservar LICENSE y la atribución de Saleor. No crear un issue tracker.
- El índice actual manda sobre notas históricas que aún mencionen planes,
  ramas o workflows anteriores.
