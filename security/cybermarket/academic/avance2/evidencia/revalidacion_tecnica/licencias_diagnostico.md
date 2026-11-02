# Control heredado de licencias: diagnóstico técnico

**Estado: FAILED_REVIEW_REQUIRED.** No se declara conformidad ni infracción jurídica. Run 41517859635, fuente f1f883d5. Reglas originales LGPL/GPL/proprietary conservadas; ninguna dependencia funcional nueva ni cambio de uv.lock.

| Comparación | Base | HEAD |
|---|---|---|
| Entradas del reporte Grant | 504 | 504 |
| Entradas aprobadas | 502 | 502 |
| Entradas rechazadas | 2 | 2 |
| Paquete afectado | text-unidecode 1.3 | text-unidecode 1.3 |
| Identificadores rechazados | GPL-1.0-only; GPL-2.0-or-later | GPL-1.0-only; GPL-2.0-or-later |

Son dos entradas de licencia del mismo paquete, no dos dependencias nuevas. El generador SBOM incluye por separado el nombre Artistic License y los identificadores GPL. La [fuente original de la versión 1.3](https://github.com/kmike/text-unidecode/blob/1.3/README.rst) ofrece alternativas de licenciamiento. El reporte no basta para concluir que el proyecto incurre en una incompatibilidad: falta revisar cómo representar y escoger la alternativa aplicable. No se añade una excepción automática ni se convierte una opción del autor en aprobación del grupo.

La instalación inicialmente fallaba antes de analizar por Python 3.15/PyO3. La actualización upstream fijada por SHA resolvió esa fase. El analizador actual también emite un error por entrada estándar: [Grant 0.2.9](https://github.com/anchore/grant/blob/v0.2.9/cmd/grant/cli/command/check.go) añade automáticamente el argumento - cuando detecta pipe/redirección, incluso al haber recibido bom.json. En CI intenta analizar una entrada vacía además del archivo; sí quedan 504 resultados del archivo en grant.json. El job de análisis puede terminar SUCCESS porque comunica el resultado mediante un output; Report Summary falla al comprobarlo. Por eso no se equipara SUCCESS del job intermedio con aprobación de licencias.

## Disposición

Conservar el control fallido y sus dos causas. La revisión de licencias requiere una decisión explícita sobre la alternativa y una corrección acotada de la invocación de Grant. No reemplazar dependencias funcionales, permitir GPL globalmente o deshabilitar el control solo para obtener verde. Los ZIP base/HEAD y sus SHA-256 quedan archivados; el SBOM original con metadatos de autores se conserva para análisis sin publicarlo en Git. La generación del entregable continúa pausada.
