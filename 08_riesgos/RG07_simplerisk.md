# RG07 — Registro en SimpleRisk

Despliegue (local, solo 127.0.0.1):

```bash
docker run -d --name peti_srdb -e MARIADB_ROOT_PASSWORD=<clave> -e MARIADB_DATABASE=simplerisk mariadb:11
docker run -d --name peti_simplerisk --link peti_srdb:db -p 127.0.0.1:8084:80 -p 127.0.0.1:443:443 \
  simplerisk/simplerisk:20261105-001-noble     # la variante jammy trae PHP 8.1 y no arranca
```

Configuración aplicada: modelo clásico Likelihood x Impact (normalizado 0-10: puntaje = P x I x 0,4); niveles Bajo >= 0, Medio >= 2,8, Alto >= 4,8, Critico >= 6,0 (equivalen a los cortes 7, 12 y 15 de RG01); apetito 2,4 (valor 6); escalas con definición operativa; 10 categorías. Se cargaron los 14 riesgos de valor >= 12 de RG02, con tratamiento, responsable, señal y umbral de RG04. Resultado: 8 Crítico y 6 Alto, igual que RG03.

Capturas: `evidencias/S15/S15_simplerisk_*.png`. La contraseña del administrador local no se versiona.
