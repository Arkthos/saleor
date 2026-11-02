# Continuidad y ajustes respecto del primer avance

**Fecha:** 2026-11-02. **Naturaleza:** decisiones de planificación y actualización para una versión nueva, no correcciones ya aplicadas al Word presentado. **Retroalimentación docente comunicada:** ninguna.

| ID | Punto | Decisión para avance 2 | Motivo y comprobación | Etapa |
|---|---|---|---|---|
| AJ-01 | Documento original | Preservar Proyecto final - primer avance(4).docx; trabajar en copia nueva | Entrega identificada por el usuario; hash en inventario | A2-01, A2-08 |
| AJ-02 | Observaciones del profesor | Registrar que no se recibieron; incorporar cada una si llega | No convertir notas propias o auditorías antiguas en feedback docente | A2-01, A2-09 |
| AJ-03 | Problema y objetivos | Mantener un general y tres específicos, con desarrollo operativo | Evitar reformular la investigación solo para acomodar resultados | A2-02, A2-08 |
| AJ-04 | Estado de ejecución | Actualizar la narrativa con C2–C9, fechas y alcance sintético | La ausencia de pruebas corresponde al estado anterior; los resultados posteriores tienen runs y SHAs | A2-05, A2-08 |
| AJ-05 | Arquitectura y entorno | Separar arquitectura conceptual, CI y eventual despliegue | No representar HTTPS/proxy/navegador como verificados por fixtures | A2-01, A2-06 |
| AJ-06 | Instrumentos | Identificar equivalentes aplicados de I01–I07 y completar vacíos | Distinguir instrumentos propuestos, aplicados y resultados recogidos | A2-02, A2-07 |
| AJ-07 | Requisitos ASVS/WSTG | Conciliar selección inicial y matriz de tests actual | CSV referencia 16/23 ASVS; siete ausencias de columna, no prueba automática de ausencia de evidencia | A2-02 |
| AJ-08 | H10 y observaciones | Seguir vínculo de H10 y actualizar H01–H15 con evidencia disponible | No se encuentra H10 en observation_ids del CSV actual; verificar trazabilidad antes de concluir | A2-02, A2-07 |
| AJ-09 | Tipos de pruebas | Clasificar cada caso por nivel, diseño, dependencias y alcance | Pytest no implica aislamiento; ejecución interna no implica DAST externo | A2-04 |
| AJ-10 | Política de pedidos | Mantener provisional o adoptar explícitamente para el caso ficticio; separar intención de Saleor | Dos XFAIL son de correo bajo política propuesta; no vulnerabilidad oficial demostrada | A2-02, A2-07 |
| AJ-11 | Hallazgos | Elaborar al menos diez A2-Hxx sustantivos, con recomendación y trazabilidad | La consigna repite este mínimo; no exige diez vulnerabilidades ni permite rellenar con variantes del mismo hecho | A2-07 |
| AJ-12 | Codificación segura | Aplicar prácticas a módulos, invariantes, permisos y manejo de errores | R2 requiere prácticas pertinentes y rigurosas, no un glosario genérico de SOLID | A2-03 |
| AJ-13 | Referencias | Conservar IEEE y numerar según manuscrito vigente | El primer avance usa IEEE; los planes antiguos con APA 7 quedan superados para esta entrega | A2-08, A2-09 |
| AJ-14 | Bibliografía histórica | No copiar numeración, cifras o diagnósticos sin cotejo | Auditorías de borradores y OWASP 2021 no sustituyen referencias de la entrega posterior | A2-08 |
| AJ-15 | Formato y autoría | Nuevo PDF propio del grupo con revisión visual y de contenido | No hay máximo de páginas indicado en la consigna recibida; verificar futuras instrucciones | A2-09, A2-10 |

No se propone corregir retrospectivamente el avance 1 ni alterar código de producto para satisfacer una expectativa sin autoridad. Si aparece una desviación demostrada, registrar requisito, alcance, corrección propuesta y retest como trabajo identificado.
