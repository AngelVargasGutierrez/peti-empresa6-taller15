# RG01 — Contexto y criterios de la gestión de riesgos del plan

**Organización:** Distribuidora Andina del Sur S.A.C. (caso simulado, Empresa 6) · **Plan:** PETI Año 1 – Año 3 · **Sección 8**

> El presente Plan Estratégico de Tecnologías de Información se elaboró sobre un caso de estudio simulado con fines académicos, denominado Distribuidora Andina del Sur S.A.C. La organización, sus datos, sistemas y documentos son ficticios.

| Campo | Contenido |
|---|---|
| **Alcance del análisis** | Riesgos que amenazan la **ejecución del PETI Año 1 – Año 3**. Excluye los riesgos operativos de TI (los de `universo-auditable-y-riesgos.md`, RG-01 a RG-09 de Administración, se tratan en el diagnóstico y en proyectos del portafolio) y los riesgos de negocio (del PEI: OE-1 a OE-4) |
| Horizonte | 3 años |
| Escalas de probabilidad e impacto | Las de abajo, con su definición operativa |
| **Criterio de aceptación** | ≤ 6 aceptable con documentación · 7–14 requiere tratamiento con plazo · ≥ 15 requiere decisión de la Gerencia General antes de aprobar el plan |
| Niveles | Bajo 1–6 · Medio 7–11 · Alto 12–14 · Crítico 15–25 |
| Dueños de riesgo | Por **cargo**, según la categoría (tabla abajo). Los riesgos de patrocinio y personal clave se redactan como riesgo estructural del cargo, nunca como conducta de una persona |
| Frecuencia de revisión | Trimestral, y ante cualquier hito de decisión de la hoja de ruta |
| Presupuesto del PETI acordado | S/ 320 000 anuales durante 3 años (Entrevista 3 con la gerencia) |
| **Fecha de acuerdo de los criterios** | **19 de noviembre de 2026**, anterior a la evaluación. Verificable en el historial de Git: este archivo es el primer commit del repositorio |

## Escalas (se fijan antes de evaluar)

| Probabilidad | Definición operativa para un plan a 3 años |
|---|---|
| 1 Muy baja | Requeriría una circunstancia excepcional; sin antecedentes |
| 2 Baja | Ha ocurrido alguna vez en organizaciones comparables |
| 3 Media | Ocurre en aproximadamente la mitad de los planes similares |
| 4 Alta | Ocurre habitualmente; **hay antecedentes en esta organización** |
| 5 Muy alta | Es prácticamente seguro que ocurra en el horizonte del plan |

| Impacto | Efecto sobre el plan |
|---|---|
| 1 Insignificante | Retraso menor a un mes en un proyecto |
| 2 Menor | Retraso de un trimestre en un proyecto |
| 3 Moderado | Un proyecto se posterga un año o se reduce su alcance |
| 4 Mayor | Un objetivo del plan no se alcanza; una ola completa se retrasa |
| 5 Catastrófico | El plan se abandona, o se incurre en incumplimiento normativo sancionable |

**Regla de justificación.** Una probabilidad de 4 o más exige citar un antecedente de la propia organización (acta, presupuesto, incidente, documento del caso). Un impacto de 4 o más exige indicar qué objetivo u ola se afecta.

## Dueños de riesgo por categoría

| Categoría | Dueño (cargo) |
|---|---|
| Presupuestal | Gerencia General y Gerencia de Administración |
| Patrocinio | Gerencia General |
| Capacidad de ejecución | Jefatura de TI |
| Personal clave | Jefatura de TI y RR. HH. |
| Resistencia al cambio | Gerencia Comercial |
| Proveedor | Gerencia de Administración |
| Técnico | Jefatura de TI |
| Normativo | Jefatura de TI y Asesoría Legal |
| De alcance | Comité de TI (a constituir, PR-13) |
| Ejecución del plan | Gerencia General |

## Supuesto de trabajo: cartera del PETI

El taller cita objetivos (OD) y proyectos (PR) de las secciones 5 y 7 del PETI. Para trazar los riesgos se usa esta cartera de trabajo, derivada del caso. **Debe reemplazarse por la numeración definitiva del PETI del equipo si difiere.**

| Objetivo | Descripción | Origen |
|---|---|---|
| OD-01 | Digitalizar el canal de pedido al detalle | OE-2 |
| OD-02 | Un maestro de clientes con dueño y fuente autoritativa | OE-4 |
| OD-03 | Ruteo y despacho digital que baje el costo logístico | OE-3 |
| OD-04 | ERP con soporte vigente y plataforma soportada | OE-1, OE-3 |
| OD-05 | Cumplimiento de la Ley 29733 y su reglamento | Marco normativo |
| OD-06 | Continuidad operativa y gestión del conocimiento | Incidentes, dependencia de personas |

| Proyecto | Descripción |
|---|---|
| PR-01 | Maestro de clientes y gobierno del dato |
| PR-02 | Protección de datos personales (registro de tratamiento, flujo transfronterizo) |
| PR-03 | Capa de integración (ERP, WMS, portal) |
| PR-04 | Relanzamiento del canal digital B2B |
| PR-05 | Ruteo y despacho digital |
| PR-06 | Seguridad de la información (correo, accesos) |
| PR-07 | Respaldo y continuidad (BIA validado, pruebas de restauración) |
| PR-08 | Analítica de datos |
| PR-09 | Migración del ERP |
| PR-10 | Gestión del conocimiento |
| PR-11 | Gestión de datos sensibles de planilla |
| PR-12 | Migración de hojas de cálculo de Gerencia Comercial |
| PR-13 | Comité de TI y tablero de seguimiento del plan |
