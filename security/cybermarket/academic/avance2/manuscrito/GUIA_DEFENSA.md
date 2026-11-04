# Guía breve de defensa del segundo avance

## Qué se puede sostener

Se evaluaron seis operaciones y componentes de identidad y acceso de un fork versionado de Saleor. La contribución de esta entrega es la revisión aplicada, la recuperación verificable de evidencia integrada histórica, treinta variantes unitarias nuevas y un catálogo de catorce hallazgos con recomendaciones. Los hallazgos incluyen controles positivos y brechas; no equivalen a catorce vulnerabilidades.

## Preguntas y respuestas para estudiar

1. **¿Por qué ASVS y WSTG?** ASVS aporta requisitos de referencia y WSTG orienta procedimientos. La relación local entre IDs se documentó; no es un mapping oficial ni certificación de cumplimiento.
2. **¿Cuántas pruebas se ejecutaron?** La evidencia histórica focal contiene 59 PASS y dos XFAIL, incluida en la suite general de 17 613 PASS y dos XFAIL. La corrida local nueva contiene treinta variantes de producto y doce invocaciones de validadores. No sumar focal y general ni presentar las doce como controles nuevos.
3. **¿Qué significa XFAIL en pedidos?** Dos expectativas de correo de una política restrictiva propuesta no se cumplen y están marcadas estrictamente. P-ORDER-01 no fue aprobada. La caracterización de calles es evidencia distinta, sin XFAIL normativa añadida.
4. **¿Se encontró una fuga de datos reales?** No. Se observaron campos sintéticos originales al consultar un UUID conocido como actor ajeno o anónimo. No se demostró obtención de UUID, enumeración, explotación real o discrepancia con una política oficial de Saleor.
5. **¿Qué aporta la prueba de firma alterada?** Establece primero un JWT HS256 válido, altera bytes significativos de su firma y exige InvalidSignatureError. Separa autenticidad de exp, nbf, tipo o audiencia; no cubre RS256 o rotación completa.
6. **¿Por qué no basta comparar una máscara con el helper?** La expectativa comparte el posible error del helper. Las unidades nuevas usan resultados literales. La información residual y el acceso legítimo siguen necesitando un criterio de negocio.
7. **¿Qué significa cero en Semgrep?** Cinco reglas locales no coincidieron en 21 archivos y no hubo errores de análisis. No se examinó todo Saleor ni sus dependencias con SCA. Bandit produjo una alerta sobre un nombre de cookie, revisada como falso positivo de B105.
8. **¿Se probó el despliegue?** No. C10 conserva siete casos sin ejecutar y no hay revalidación integrada del HEAD nuevo. Quedan fuera navegador, TLS, proxy real y entrega de UUID. El informe distingue esos límites de las pruebas locales e históricas disponibles.
9. **¿Qué se corregiría primero?** Antes de cambiar acceso a pedidos, audiencia o duración de sesiones, definir el contrato del caso. Luego diseñar el negativo y control positivo correspondientes, aplicar una mitigación justificada y conservar el antes/después. No se modificó código funcional para forzar una propuesta tácita.
10. **¿Cómo se preserva la evidencia?** Commits, comandos, versiones, JUnit, JSON y SHA-256. Los archivos originales se conservan por bytes. Un digest permite comprobar un archivo disponible; no reemplaza al archivo.

## Revisión del grupo antes de entregar

Confirmar lectura y autoría, estudiar las propiedades efectivamente probadas y revisar la política propuesta. Registrar cambios como nueva versión, regenerar PDF y hashes y conservar el comprobante real de campus. No declarar reunión, aprobación, contribuciones individuales o entrega que no hayan ocurrido.
