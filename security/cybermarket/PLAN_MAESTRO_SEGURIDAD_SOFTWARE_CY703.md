# CyberMarket CR — Plan maestro de aseguramiento de Seguridad de Software

**Curso:** CY-703 Seguridad de Software, Universidad Fidélitas. **Fecha:** 2026-10-18. **Estado:** plan de cobertura y aceptación; NO sustituye ejecuciones. **Fuente:** currículo y requisitos del proyecto previamente documentados; verificar correspondencia final con rúbrica institucional antes de entregar.

## 1. Enfoque profesional

El trabajo debe evaluar **seguridad durante todo el ciclo de vida del software (SSDLC)**, no limitarse a una batería de GraphQL. Saleor es el sistema objeto de estudio, CyberMarket CR es el contexto empresarial ficticio. Conservar el fork, baseline `4cb1609a90eade14b6275a407bc7a00c35698090`, Avance 1 aprobado, la trazabilidad académica y el PR sin merge. No modificar código funcional del producto para hacer pasar pruebas. Todos los entornos y datos deben ser sintéticos y autorizados.

## 2. Cobertura de currículo y pruebas

| Eje curricular | Evaluación requerida | Evidencia y condición de aceptación | Estado |
| --- | --- | --- | --- |
| SSDLC y análisis de requisitos | Amenazas, activos, fronteras de confianza, abuso, criterios de seguridad, trazabilidad objetivos-requisitos | Matriz requisito-amenaza-prueba-evidencia y aprobación de P-ORDER-01 | PARCIAL; aprobación pendiente |
| Diseño seguro, encapsulamiento y SOLID | Revisión de responsabilidades, acoplamiento, validación de entradas, invariantes y separación de permisos | Revisión documentada de módulos relevantes y tests negativos | PENDIENTE |
| Autenticación y sesiones | JWT, revocación, refresh, CSRF, cookies, identidad | C2–C9 tests + HTTP/browser C10 | PARCIAL, CI fixture completado |
| Autorización y privacidad | GraphQL field/object access, owner/peer/anon/staff/app, UUID/legacy | Matriz de roles y campos, requisito autorizado, C10 HTTP | PARCIAL; mayor incertidumbre R11 |
| API y GraphQL | Límites de consultas, aliases, mutaciones, errores, IDs malformados, exposición de esquema | Casos positivos/negativos y pruebas HTTP con umbrales seguros | PARCIAL |
| Codificación segura | Revisión estática, secretos, manejo de errores, dependencias, configuración | Bandit acotado, dependencias/SCA y revisión de código, triage reproducible | PARCIAL |
| SAST y DAST | Distinguir cobertura estática vs validación dinámica de aplicación desplegada | Reportes separados con herramientas, versiones, alcance y hallazgos | SAST PARCIAL, DAST NO EJECUTADO |
| Comprobación del entorno y despliegue | Config, HTTPS, proxy, cookies, CORS, CSRF, secretos, DEBUG, logging | C10 entorno aislado, inventario y controles comprobados | NO EJECUTADO |
| Vulnerabilidades y remediación | Reproducción, requisito, impacto, severidad, causa, mitigación, retest | Registro con evidencia y decisión; sin inventar CVE o explotación | PENDIENTE DE ADJUDICACIÓN |
| Gestión de incidentes y ética | Registro, alerta, contención, evidencia, límites de autorización, teardown | Simulación documental con datos sintéticos y cadena de custodia | PENDIENTE |

## 3. Plan de trabajo por gates

**G0 — alcance:** objetivos Avance 1, rúbrica, hipótesis, entorno autorizado, políticas de negocio y aceptación. **G1 — diseño:** revisar arquitectura, módulos, dependencias, superficie GraphQL, modelado de amenazas y oráculos. **G2 — estática:** SAST, SCA, revisión manual, configuración, categorización de falsos positivos. **G3 — dinámica en CI:** C2–C9 + validador + pruebas de regresión + suite general + E2E + linters sobre mismo SHA. **G4 — vivo:** ejecutar C10 en contenedores aislados con HTTP y, si procede, HTTPS/browser/proxy; LIVE-01–LIVE-07. **G5 — juicio:** mapear cada evidencia a requisitos aplicables, distinguir comportamiento esperado, defecto de harness, debilidad de producto y política no aprobada. **G6 — cierre:** informe académico con método, resultados, limitaciones, riesgos priorizados, mitigaciones, trazabilidad, APA 7 y anexos reproducibles; revisión de integridad y aprobación final.

## 4. Reglas de ejecución y resultados

Registrar PASS, FAIL, ERROR, SKIP, XFAIL, XPASS, BLOCKED por test y por gate. Los XFAIL de P-ORDER-01 no son PASS de seguridad. Las 13 categorías R01–R13 son **hipótesis de riesgo**, no 13 vulnerabilidades. Un control ASVS no se certifica por citar su ID. Cada conclusión debe distinguir **observación**, **interpretación**, **inferencia** y **requisito autorizado**. Toda nueva corrección obliga a CI sobre nuevo SHA y reporte de delta. Los tests no ejecutados permanecen NOT_EXECUTED.

## 5. Entregables controlados

1. Matriz SSDLC y requisitos de seguridad con autoridad/aplicabilidad.
2. Inventario y revisión de diseño/código de módulos relevantes.
3. Plan y manifest de pruebas de todas las capas; artefactos CI y C10.
4. Registro de vulnerabilidades/debilidades con evidencia, severidad condicionada y acciones.
5. Reporte de calidad del harness y regresiones.
6. Informe final académico, referencias APA 7, limitaciones y anexos verificables.
7. Checkpoint previo a redacción y handoff reproducible de C10.

**Regla de cierre:** ningún informe se llamará «definitivo» mientras haya gates obligatorios sin ejecutar o sin justificación de exclusión, o falten evidencias verificadas. El informe C2–C9 existente es un cierre parcial del experimento, no la entrega integral del curso.
