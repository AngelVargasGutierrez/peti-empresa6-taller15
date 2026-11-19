## 8. Gestión de riesgos del plan

> Caso de estudio simulado: Distribuidora Andina del Sur S.A.C. (ficticio). Información **Confidencial**: expone vulnerabilidades de ejecución.

### 8.1 Alcance, contexto y criterios
Esta sección gestiona los riesgos que amenazan la **ejecución del PETI Año 1 – Año 3**. Excluye los riesgos operativos de TI (registro de Administración RG-01 a RG-09, tratados en el diagnóstico) y los de negocio (PEI, OE-1 a OE-4). Escalas de probabilidad e impacto con definición operativa, criterio de aceptación (≤ 6 aceptable con documentación · 7–14 tratamiento con plazo · ≥ 15 decisión de la Gerencia General antes de aprobar el plan) y dueños por cargo están en `08_riesgos/RG01_contexto.md`. **Fecha de acuerdo de los criterios: 19 de noviembre de 2026**, primer commit del repositorio, anterior a la evaluación.

### 8.2 Método
ISO 31000:2018 (contexto, apreciación, tratamiento, residuo, comunicación, seguimiento) con ISO/IEC 27005:2022 como referencia complementaria. Fuentes de identificación: política de respaldo POL-TI-023 contrastada con la práctica declarada, BIA (`bia.csv`), universo auditable y registro de riesgos de Administración, y el caso (ficha, gobierno, sistemas, presupuesto, inversiones cerradas, incidentes). **Se realizó además un pre-mortem de los dos integrantes (Anexo E), posterior al registro, como contraste**: las 16 causas de fracaso imaginadas quedaron cubiertas por los 16 riesgos y no apareció ninguno nuevo. No sustituye una dinámica con la gerencia.

### 8.3 Registro de riesgos
Dieciséis riesgos sobre las **nueve categorías**, más la categoría característica «Ejecución del plan». Ninguna categoría se omitió.

| id | Categoría | Riesgo (evento + causa + consecuencia) | Objetivos o proyectos afectados | P | I | Valor | Nivel |
|---|---|---|---|---|---|---|---|
| R-01 | Presupuestal | Que el presupuesto de TI se recorte o se reasigne a gasto corriente en el año 2, porque el presupuesto ya bajó de S/ 790 000 a S/ 755 000 y el canal digital cayó 56 %, dejando sin fondos las olas de crecimiento y transformación | OD-01, OD-03 · PR-04, PR-05, PR-08 | 4 | 4 | 16 | Crítico |
| R-02 | Presupuestal | Que el gasto operativo acumulado crezca más rápido que el presupuesto (licencias +17 %, nube +21 %, mantenimiento +20 % en un año) y consuma los S/ 320 000 anuales del PETI, obligando a abandonar servicios ya entregados | OD-01, OD-04 | 3 | 4 | 12 | Alto |
| R-03 | Patrocinio | Que el patrocinio del plan recaiga en el cargo de Gerencia de Administración sin comité de TI y que el cambio de ese cargo deje al plan sin autoridad ni quien lo reclame | Todos | 4 | 4 | 16 | Crítico |
| R-04 | Capacidad de ejecución | Que el área de TI, con 5 personas, no sostenga tres proyectos simultáneos mientras mantiene la operación (87 usuarios de ERP, WMS, portal), y ningún proyecto cierre | Toda la hoja de ruta | 4 | 3 | 12 | Alto |
| R-05 | Personal clave | Que el único desarrollador que conoce el portal B2B, o el cargo que custodia el respaldo físico, deje la organización antes de completar la gestión del conocimiento (PR-10), dejando portal y respaldo sin quien los sostenga | OD-01, OD-06 · PR-04, PR-07, PR-10 | 4 | 4 | 16 | Crítico |
| R-06 | Personal clave | Que la única analista de Gerencia Comercial que maneja márgenes, presupuesto y comisiones en hojas sin control de versiones deje el cargo antes de PR-12, perdiendo el conocimiento de la gestión comercial | OD-02, OD-03 · PR-12 | 3 | 3 | 9 | Medio |
| R-07 | Resistencia al cambio | Que la fuerza de ventas (26 personas) no adopte el canal digital porque percibe que reduce su intermediación con el cliente, repitiendo la adopción de 4 % del portal actual | OD-01 · PR-04 | 4 | 4 | 16 | Crítico |
| R-08 | Resistencia al cambio | Que las áreas dueñas de hojas de cálculo (Comercial, RR. HH., Despacho) resistan el maestro de clientes y el dueño del dato por percibir pérdida de control, manteniendo tres fuentes de clientes (8 400 / 340 / 8 900 registros) | OD-02, OD-03 · PR-01, PR-05 | 4 | 3 | 12 | Alto |
| R-09 | Proveedor | Que el proveedor del ERP no brinde soporte a la migración por tener vencido el contrato y el sistema operativo fuera de soporte, bloqueando PR-09 y la integración | OD-04 · PR-03, PR-09 | 4 | 4 | 16 | Crítico |
| R-10 | Proveedor | Que un proveedor único de nube, correo o planilla eleve el precio, incumpla o no brinde garantías del flujo transfronterizo, forzando una migración no prevista | OD-05 · PR-02, PR-11 | 3 | 3 | 9 | Medio |
| R-11 | Técnico | Que la capa de integración no logre exponer los datos del ERP empaquetado (más de diez años, hoy integrado al WMS solo por archivo plano nocturno) por limitaciones no documentadas de la plataforma | OD-01, OD-02, OD-03 · PR-03 y dependientes | 3 | 5 | 15 | Crítico |
| R-12 | Técnico | Que PR-07 se dimensione con un BIA no validado (RTO y RPO propuestos por un practicante, con criticidad incoherente: Tesorería «Baja» con impacto a 24 h «Alto»; Cobranza RTO 72 h con RPO 1 h) y el plan declare continuidad sin capacidad real de restauración | OD-06 · PR-07 | 4 | 4 | 16 | Crítico |
| R-13 | Normativo | Que la autoridad de protección de datos fiscalice antes de que PR-02 concluya, o amplíe obligaciones del D. S. 016-2024-JUS durante la ejecución, con datos sensibles de salud en planilla alojados en una región no verificada | OD-05 · PR-02, PR-11 | 3 | 4 | 12 | Alto |
| R-14 | De alcance | Que aparezcan pedidos de las áreas sin caso de negocio y consuman la capacidad prevista, como las inversiones previas sin caso (servidores sin caso, módulo de comisiones aprobado por correo) | Toda la hoja de ruta | 4 | 3 | 12 | Alto |
| R-15 | Ejecución del plan | Que el plan se apruebe y no se ejecute por ausencia de responsable designado, comité de TI y seguimiento, en una organización que nunca ha tenido PETI ni plan de continuidad | Todos | 4 | 5 | 20 | Crítico |
| R-16 | Ejecución del plan | Que el plan se ejecute pero no se mida su beneficio, porque dos de cuatro objetivos (OE-2 y OE-4) no tienen meta y las tres inversiones cerradas nunca midieron beneficio, impidiendo justificar la continuidad del presupuesto | OD-01, OD-02 · PR-13 | 4 | 3 | 12 | Alto |

La justificación de P e I con el dato que la sostiene está en la columna correspondiente de `RG02_registro.csv`.

### 8.4 Evaluación y mapa de calor
Distribución: Crítico 8 · Alto 6 · Medio 2 · Bajo 0. Mapa de calor en `graficos/RG_mapa_calor.png`. **Requieren decisión de la Gerencia General antes de aprobar el plan (valor ≥ 15):** R-01, R-03, R-05, R-07, R-09, R-11, R-12, R-15. Los de valor más alto no son técnicos: R-15 (el plan no se ejecuta, 20), y los de gobierno, personas y presupuesto.

### 8.5 Tratamiento y riesgo residual
| id | Valor | Decisión | Acciones concretas de tratamiento | Responsable (cargo) | Plazo | Costo | Valor residual |
|---|---|---|---|---|---|---|---|
| R-15 | 20 | Mitigar | Designar por resolución un responsable del plan; constituir el comité de TI (PR-13) como órgano de seguimiento; tablero de indicadores con reporte trimestral obligatorio a Gerencia General y al directorio | Gerencia General | Al aprobar el plan | Bajo | 8 |
| R-01 | 16 | Mitigar + Asumir con contingencia | Aprobación plurianual del presupuesto del PETI (S/ 320 000 por año) por acta de directorio; hitos de decisión por ola; escenario reducido que prioriza PR-03, PR-04 y PR-07 | Gerencia General y Gerencia de Administración | Al aprobar el plan | Bajo | 9 |
| R-03 | 16 | Mitigar | Radicar el patrocinio en el comité de TI y no en un cargo; acta de aprobación firmada por Gerencia General; inducción del plan a todo el comité y al directorio | Gerencia General | Al aprobar el plan | Bajo | 8 |
| R-05 | 16 | Mitigar | Adelantar PR-10 a la ola 1; documentar la arquitectura del portal y el procedimiento de respaldo; formar un segundo responsable; custodia del respaldo fuera de un solo cargo; revisar condiciones de retención. Reduce impacto, no probabilidad de renuncia | Jefatura de TI y RR. HH. | 90 días | Medio | 8 |
| R-07 | 16 | Mitigar | Incorporar a dos vendedores líderes como cocreadores; esquema de comisiones que también pague el pedido digital; piloto con 20 clientes antes del despliegue; medir adopción desde el día 1 | Gerencia Comercial | Antes de PR-04 | Medio | 8 |
| R-09 | 16 | Transferir + Mitigar | Renegociar y firmar el contrato de soporte con niveles de servicio y penalidad antes de iniciar PR-09; documentar el plan de salida de la plataforma | Gerencia de Administración | Antes de la ola 2 | Medio | 8 |
| R-12 | 16 | Mitigar | Validar el BIA con los dueños de proceso antes de dimensionar PR-07; corregir criticidad, RTO y RPO incoherentes; ejecutar la primera prueba de restauración y llevar el registro de restauraciones; revisar la política POL-TI-023 vencida | Jefatura de TI | Primer trimestre | Bajo | 8 |
| R-11 | 15 | Mitigar | Prueba de concepto de integración antes de comprometer el presupuesto de PR-03; si falla, activar integración por archivo con mayor frecuencia | Jefatura de TI | Antes de PR-03 | Bajo | 8 |
| R-02 | 12 | Asumir con contingencia | Techo de OPEX por año dentro del presupuesto del PETI; revisión de licencias y nube al cierre de cada ola; baja de servicios de menor uso | Gerencia de Administración | Cierre de cada ola | Bajo | 9 |
| R-08 | 12 | Mitigar | Nombrar dueño del dato de cliente por cargo; mostrar a las áreas el beneficio propio de PR-01; talleres de gestión del cambio con 10 % del presupuesto de PR-01 | Gerencia General y Gerencia Comercial | Antes de PR-01 | Medio | 9 |
| R-04 | 12 | Mitigar | Máximo dos proyectos simultáneos; tercerizar el soporte de nivel 1; reasignar mantenimiento correctivo; secuenciar por olas | Jefatura de TI | Al aprobar el plan | Medio | 6 |
| R-13 | 12 | Mitigar | PR-02 en el primer semestre; registro de tratamiento y garantías del flujo transfronterizo como primeros entregables; vigilancia normativa trimestral | Jefatura de TI y Asesoría Legal | Primer semestre | Bajo | 6 |
| R-14 | 12 | Mitigar | Aplicar la regla de admisión de la sección 7.1: todo pedido nuevo requiere caso de negocio y aprobación del comité; control de cambios del plan | Comité de TI | Continuo | Bajo | 6 |
| R-16 | 12 | Mitigar | Proponer la meta cuantificada de OE-2 y OE-4; línea base y medición de beneficio por proyecto; revisión de beneficios en el tablero trimestral | Jefatura de TI y Gerencia General | Primer trimestre | Bajo | 6 |
| R-06 | 9 | Mitigar | Documentar las hojas, control de versiones y segundo responsable antes de PR-12 | Gerencia Comercial | Antes de PR-12 | Bajo | 6 |
| R-10 | 9 | Mitigar | Cláusulas de nivel de servicio y garantías transfronterizas en la renovación; plan de salida documentado | Gerencia de Administración | Renovación anual | Bajo | 6 |

Reducción total lograda: **102 puntos (46%)**. En R-05 el tratamiento reduce el impacto, no la probabilidad de renuncia; bajar la probabilidad sería maquillar el registro.

### 8.6 Señales tempranas y umbrales de alerta
| id | Señal temprana | Umbral de alerta |
|---|---|---|
| R-15 | Comité sin sesionar | 1 trimestre sin acta |
| R-01 | Presupuesto de TI no aprobado en la fecha habitual | 30 días de retraso |
| R-03 | Ausencia del patrocinador en el comité | 2 sesiones consecutivas |
| R-05 | Una sola persona figura en todos los proyectos activos | Cualquier proyecto con factor bus = 1 |
| R-07 | Participación en el piloto por debajo del 50 % | 2 semanas con adopción < 10 % |
| R-09 | Contrato sin firmar a 60 días del inicio de PR-09 | 60 días |
| R-12 | Prueba de restauración no ejecutada en el trimestre | 1 trimestre sin acta de prueba |
| R-11 | Prueba de concepto pospuesta | 2 postergaciones |
| R-02 | OPEX proyectado supera el 70 % del presupuesto anual de TI | Superar el 70 % en cualquier trimestre |
| R-08 | Hoja paralela se sigue actualizando tras el cierre de PR-01 | Una hoja activa 30 días después del cierre |
| R-04 | Proyectos que avanzan pero ninguno cierra; incidentes mayores abiertos a la vez | 3 proyectos activos sin hito cerrado en un trimestre |
| R-13 | Prepublicación de proyecto normativo o notificación de la autoridad | Publicación en consulta |
| R-14 | Proyectos activos sin caso de negocio | 1 caso |
| R-16 | Proyecto cerrado sin medición de beneficio | 1 proyecto |
| R-06 | Única analista sin respaldo asignado | Cualquier trimestre sin segundo responsable |
| R-10 | Aviso de alza de precio o incidente de proveedor | Alza > 10 % o 2 incidentes |

Cero riesgos sin señal temprana. Sin señal observable no hay seguimiento.

### 8.7 Matriz de comunicación del riesgo
| id del riesgo | Qué se comunica | A quién (cargo) | Cuándo / frecuencia | Canal | Quién comunica | Formato | Qué decisión habilita |
|---|---|---|---|---|---|---|---|
| R-15 | Estado de ejecución del plan e indicadores | Gerencia General, comité de TI y directorio | Trimestral | Sesión de comité | Responsable del plan | Tablero + acta | Continuar, ajustar o detener |
| R-01 | Ejecución presupuestal vs. planificado y proyección del año siguiente | Gerencia General y Gerencia de Administración | Trimestral y ante desviación > 10 % | Informe escrito | Jefatura de TI | Reporte de 1 página | Reasignación o escenario reducido |
| R-03 | Asistencia del patrocinador y acuerdos del comité | Gerencia General y directorio | Trimestral | Sesión de comité | Responsable del plan | Acta | Reforzar o sustituir el patrocinio |
| R-05 | Factor bus por proyecto y avance de PR-10 | Gerencia General y RR. HH. | Mensual mientras el residual sea > 6 | Correo con tablero | Jefatura de TI | Indicador | Priorizar contratación o formación |
| R-07 | Adopción del canal digital por vendedor y cliente | Gerencia Comercial y fuerza de ventas | Semanal en el piloto; mensual después | Reunión de equipo | Gerencia Comercial | Tablero visible | Ajustar incentivos o rediseñar |
| R-09 | Estado de la renegociación del soporte del ERP | Gerencia General | Quincenal hasta la firma | Correo | Gerencia de Administración | Estado en una línea | Escalar o activar plan de salida |
| R-12 | Resultado de pruebas de restauración y BIA validado | Gerencia General y dueños de proceso | Trimestral | Sesión de comité | Jefatura de TI | Informe de prueba | Aprobar dimensionamiento de PR-07 |
| R-11 | Resultado de la prueba de concepto de integración | Comité de TI | Al concluir la prueba | Sesión de comité | Jefatura de TI | Informe técnico | Aprobar PR-03 o activar la alternativa |
| R-02 | OPEX acumulado vs. techo anual | Gerencia de Administración | Trimestral | Informe escrito | Jefatura de TI | Reporte de 1 página | Dar de baja servicios o reasignar |
| R-08 | Estado del maestro de clientes y hojas paralelas | Gerencia General y áreas dueñas de hojas | Mensual durante PR-01 | Reunión de equipo | Jefatura de TI | Indicador | Reforzar gestión del cambio |
| R-04 | Proyectos activos y cierres de hito | Jefatura de TI y comité de TI | Mensual | Reunión de equipo | Jefatura de TI | Tablero | Postergar o tercerizar |
| R-13 | Vigilancia normativa y avance de PR-02 | Jefatura de TI y Asesoría Legal | Trimestral | Correo | Asesoría Legal | Nota de 1 página | Adelantar o reordenar PR-02 |
| R-14 | Pedidos nuevos y casos de negocio | Comité de TI | En cada sesión | Sesión de comité | Jefatura de TI | Lista de admisión | Admitir, diferir o rechazar |
| R-16 | Línea base y beneficio medido por proyecto | Gerencia General y comité de TI | Trimestral | Sesión de comité | Jefatura de TI | Tablero | Continuar financiando o corregir |
| R-06 | Estado de respaldo de la analista comercial | Gerencia Comercial | Trimestral | Correo | Gerencia Comercial | Indicador | Asignar segundo responsable |
| R-10 | Incidentes y precios de proveedores | Gerencia de Administración | Semestral | Informe escrito | Jefatura de TI | Reporte de 1 página | Renegociar o activar salida |
| Todos ≥ 15 | Riesgo, tratamiento, residual y responsable de la aceptación | Gerencia General | Antes de aprobar el plan | Sesión formal | Responsable del plan | Anexo del PETI con firmas | Aprobar el plan con conocimiento del riesgo |

### 8.8 Riesgos residuales que requieren aceptación formal
| id | Valor residual | ¿Quién acepta el residual? |
|---|---|---|
| R-15 | 8 | Gerencia General |
| R-01 | 9 | Gerencia General |
| R-03 | 8 | Gerencia General |
| R-05 | 8 | Gerencia General |
| R-07 | 8 | Gerencia Comercial |
| R-09 | 8 | Gerencia General |
| R-12 | 8 | Gerencia General |
| R-11 | 8 | Gerencia General |
| R-02 | 9 | Gerencia General |
| R-08 | 9 | Gerencia General |

Cada uno exige firma del dueño del riesgo antes de aprobar el plan (anexo de firmas, sección 9). **El equipo formulador no puede aceptarlos en nombre de la gerencia.** Mientras no estén firmados, se reportan como ignorados, no como aceptados.

### 8.9 Seguimiento y revisión
Revisión trimestral por el comité de TI (PR-13), responsable: Responsable del plan. Disparadores de revisión extraordinaria: cualquier señal que alcance su umbral, cambio del cargo de patrocinio o de la Jefatura de TI, recorte presupuestal mayor al 10 %, publicación de normativa de protección de datos y cada hito de decisión de la hoja de ruta.
