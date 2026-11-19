# Anexo E — Pre-mortem del PETI · Distribuidora Andina del Sur S.A.C. (caso simulado)

**Técnica.** Klein (2007). Se imagina que el plan ya fracasó y se escribe por qué. No se pregunta «qué podría salir mal», sino «ya salió mal: ¿qué pasó?».

**Cómo se hizo.** Lo realizaron los dos integrantes del equipo (Angel Vargas Gutierrez y Franco Mango Puma), no un comité de la organización, sobre los datos del caso simulado. **Se hizo después de construir el registro RG02, como contraste y no como fuente**: el historial de Git lo muestra. Sirve para comprobar que el registro no omite causas de fracaso que el equipo considera plausibles.

## 1. Escenario

> Es noviembre del año 3. El PETI de Distribuidora Andina del Sur no se ejecutó como estaba escrito: el canal digital sigue por debajo del 10 % de los pedidos, el ERP sigue sin soporte y nadie puede demostrar qué se logró. Escribe, en una frase y por cargo, por qué fracasó.

## 2. Causas de fracaso imaginadas

| # | Causa escrita (por cargo, sin culpar a personas) | Riesgo del registro que la cubre | Dato del caso que la hace plausible |
|---|---|---|---|
| 1 | El presupuesto de TI volvió a recortarse en el año 2 y las olas de crecimiento quedaron sin fondos | R-01 | Presupuesto de 790 000 a 755 000; canal digital −56 %; analítica en 0 |
| 2 | Cambió el cargo de Gerencia de Administración y nadie reclamó el plan | R-03 | Decisiones en un solo cargo; directorio sin tratar tecnología en 11 actas |
| 3 | Se aprobó el plan, pero no se designó responsable y el comité de TI nunca sesionó | R-15 | Nunca existió PETI ni comité de TI |
| 4 | Se fue el único desarrollador del portal y nadie pudo mantenerlo | R-05 | Portal conocido por una sola persona |
| 5 | La fuerza de ventas siguió tomando pedidos por teléfono y papel | R-07 | Portal con 4 % de adopción tras años de uso |
| 6 | El ERP sin soporte falló durante la migración y no había proveedor al cual llamar | R-09 | Contrato de soporte vencido; sistema operativo fuera de soporte |
| 7 | La integración con el ERP nunca funcionó más allá del archivo nocturno | R-11 | WMS integrado solo por archivo plano |
| 8 | En la siguiente caída real, la restauración falló porque nunca se había probado y el BIA estaba mal | R-12 | Caída de ERP de 9 h; restauración nunca probada; BIA sin validar |
| 9 | Cada área siguió usando su propia hoja de clientes y el maestro nunca fue «el» maestro | R-08 | Tres fuentes de clientes (8 400 / 340 / 8 900) y supuesto «la información es poder» |
| 10 | El área de TI, con 5 personas, no pudo con los proyectos y la operación a la vez | R-04 | Gasto en soporte y personal operativo; 87 usuarios de ERP |
| 11 | Llegaron pedidos de las gerencias sin caso de negocio y absorbieron la capacidad | R-14 | Inversiones previas aprobadas sin caso formal |
| 12 | La autoridad de protección de datos fiscalizó antes de que el proyecto terminara | R-13 | Planilla con datos de salud en región no verificada; flujo transfronterizo |
| 13 | Nadie pudo demostrar los beneficios y se perdió el argumento para sostener el presupuesto | R-16 | Dos de cuatro objetivos sin meta; tres inversiones sin medición |
| 14 | Licencias y nube crecieron y consumieron el presupuesto del PETI | R-02 | Licencias +17 %, nube +21 %, mantenimiento +20 % en un año |
| 15 | Se fue la analista que lleva márgenes y comisiones y se perdió la lógica comercial | R-06 | Una sola analista, sin control de versiones |
| 16 | Un proveedor único de nube o planilla subió el precio o incumplió | R-10 | RG-08 de Administración: dependencia de proveedor único |

## 3. Qué muestra el contraste

- **Las 16 causas están cubiertas** por los 16 riesgos del registro; no apareció ningún riesgo nuevo.
- **Una observación que refuerza R-04, no la reemplaza:** durante la escritura surgió la causa «un incidente operativo mayor (como el fraude por correo de S/ 12 400 o una caída de ERP) absorbió al equipo y el plan se postergó». Es un riesgo operativo que dispara un riesgo del plan, por eso queda dentro de R-04 y se añade a su señal de seguimiento: **incidentes mayores abiertos al mismo tiempo que proyectos sin hito cerrado**.
- **El orden de gravedad coincide:** las causas 1 a 8 son las de valor ≥ 15 del registro (R-15, R-01, R-03, R-05, R-07, R-09, R-12, R-11), y las personas y el gobierno aparecen primero, como en la evaluación.
- **Limitación.** Al hacerlo los mismos autores del registro, el contraste no es independiente. Una dinámica con la gerencia de la organización podría hacer emerger causas que el equipo no ve.
