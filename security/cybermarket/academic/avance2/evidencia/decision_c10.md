# A2-06 — Validación C10 reabierta y ejecutada

La decisión anterior de exclusión, conservada abajo como antecedente, quedó superada al reactivar Actions y preparar servicios efímeros. **C10 reducido completado: 26 PASS**, run 41517858406, fuente f1f883d5 / checkout daf9178a. Se usaron sockets ASGI reales, PostgreSQL/Valkey aislados, HTTPS y Chromium con CA desechable; [resultados y procedencia](revalidacion_tecnica/retest_04_summary.json).

La política P-ORDER-01 sigue provisional. LIVE-07 recorre la API legítima del propietario y la revocación, sin desplegar un storefront externo. No se declara confianza de un proxy de producción, replicación física, resistencia a carga o seguridad de una tienda pública. El gate global permanece abierto por regresión/calidad y revisión del control heredado de licencias. No se genera otro entregable.

## Antecedente reemplazado: decisión previa con recursos insuficientes

# A2-06 — Decisión sobre validación desplegada

**Decisión:** no ejecutar C10 en este segundo avance bajo los recursos comprobados de la sesión. Se completa la decisión de alcance y se mantienen LIVE-01–LIVE-07 como NOT_EXECUTED. No se marca ninguna prueba de despliegue como PASS o no aplicable por carecer del entorno.

## Fundamento

La consigna específica exige codificación segura, análisis estático/dinámico, pruebas de seguridad y al menos diez hallazgos con recomendaciones. No prescribe que toda dinámica sea DAST externo ni exige un despliegue público. El estudio dispone de integración GraphQL histórica verificada y de ejecución nueva de unidades de producto, además de análisis estático y revisión manual. Son evidencias válidas dentro de sus condiciones; no sustituyen las propiedades que solo pueden observarse en transporte o navegador.

Esta sesión no dispone de Docker ni PostgreSQL activo. Se intentó la preparación local de pruebas y se observaron errores de fixtures por ausencia de DB. Aunque se instalaron dependencias Python mediante el lockfile, el proceso no puede cambiar a un usuario no privilegiado para un servidor PostgreSQL nativo. No se conecta a otra base de datos, no se modifica un sistema ajeno ni se intenta sortear esa restricción con un servidor como root. Tampoco existe un endpoint de prueba proporcionado por el grupo en esta fase.

El acceso del conector permite conservar el trabajo en GitHub y leer/reintentar ciertos runs, pero no se obtuvo una ejecución nueva del HEAD durante esta fase. Reejecutar un job viejo no demostraría los cambios actuales. El plan evita gastar el tiempo de análisis y manuscrito en una sustitución experimental de PostgreSQL o un despliegue público sin necesidad académica demostrada.

## Estado por caso

| Caso | Estado | Qué queda sin determinar |
|---|---|---|
| LIVE-01 | NOT_EXECUTED | Salud y comportamiento de un servidor HTTP real con build identificado |
| LIVE-02 | NOT_EXECUTED | Reproducción de visibilidad UUID por transporte y actores del despliegue |
| LIVE-03 | NOT_EXECUTED | Representación de ofuscación legacy en ese despliegue |
| LIVE-04 | NOT_EXECUTED | Respuesta HTTP a IDs ausentes/malformados en configuración real |
| LIVE-05 | NOT_EXECUTED | Matriz efectiva de personal/apps y campos sobre HTTP |
| LIVE-06 | NOT_EXECUTED | Cookies en navegador, CORS, origen, proxy y HTTPS/TLS |
| LIVE-07 | NOT_EXECUTED | Ciclo legítimo de entrega/compartición de UUID en storefront |

## Efecto sobre el informe

Se describen resultados de código y fixtures como tales. No se afirma que una cookie Secure haya sido validada por navegador, que exista fuga en una tienda pública, que un UUID pueda adivinarse, que el proxy sea confiable o que el servicio resista carga. Las conclusiones relativas a audiencia/entitlements y transporte se mantienen condicionales o NO_DETERMINADO. P-ORDER-01 no se aprueba por omitir C10.

La propuesta de solución incluye un laboratorio aislado reproducible con versiones y datos sintéticos, ejecución acotada de los siete casos, trazas depuradas y teardown según el plan C10 existente. Su ejecución futura debe registrar resultados reales y cambios de configuración; no se presenta como una mitigación ya verificada.

## Condición para reabrir

Disponer de un laboratorio controlado con PostgreSQL/caché, credenciales efímeras y responsables; fijar build/configuración; definir política de campos y, para LIVE-06, cliente/navegador y terminación HTTPS apropiados. Si aparece un entorno viable antes del cierre final, se puede reabrir esta decisión con nuevas evidencias. Hasta entonces, la etapa está cerrada como decisión explícita, no como despliegue realizado.
