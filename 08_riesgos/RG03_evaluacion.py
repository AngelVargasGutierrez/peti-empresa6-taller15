# 08_riesgos/RG03_evaluacion.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt

r = pd.read_csv("RG02_registro.csv")
r["valor"] = r.P * r.I
r["nivel"] = pd.cut(r.valor, [0,6,11,14,25],
                    labels=["Bajo","Medio","Alto","Crítico"])
r = r.sort_values("valor", ascending=False)
r.to_csv("RG03_evaluado.csv", index=False)

print("=== REGISTRO DE RIESGOS DEL PLAN ===")
print(r[["id","Categoría","P","I","valor","nivel"]].to_string(index=False))
print(f"\nRiesgos evaluados : {len(r)}")
print(r.nivel.value_counts().reindex(["Crítico","Alto","Medio","Bajo"]).fillna(0).astype(int).to_string())

CATS = ["Presupuestal","Patrocinio","Capacidad de ejecución","Personal clave",
        "Resistencia al cambio","Proveedor","Técnico","Normativo","De alcance"]
faltan = [c for c in CATS if c not in set(r["Categoría"])]
print(f"\nCategorías SIN riesgo identificado: {faltan or 'ninguna ✔'}")
if faltan:
    print("→ Cada categoría omitida debe justificarse explícitamente en sección 8.")

criticos = r[r.valor >= 15]
print(f"\n=== RIESGOS ≥ 15 — requieren decisión de la gerencia general ===")
print(criticos[["id","Categoría","valor"]].to_string(index=False))

# Mapa de calor (editado: el color depende de la severidad P x I, el numero es la cantidad de riesgos)
from matplotlib.colors import ListedColormap, BoundaryNorm
sev = np.array([[ (5-i)*(j+1) for j in range(5)] for i in range(5)])   # fila i -> impacto 5-i
m = np.zeros((5,5), dtype=int)
for _, x in r.iterrows(): m[5-x.I, x.P-1] += 1
cmap = ListedColormap(["#2e9e5b","#f2d04a","#f08a3c","#c8102e"])      # Bajo, Medio, Alto, Critico
norm = BoundaryNorm([0,6.5,11.5,14.5,26], cmap.N)
fig, ax = plt.subplots(figsize=(8,7))
ax.imshow(sev, cmap=cmap, norm=norm)
for i in range(5):
    for j in range(5):
        v = int(m[i,j])
        ax.text(j, i, v if v else "", ha="center", va="center", fontsize=15, fontweight="bold", color="white")
        ax.text(j+0.42, i+0.42, int(sev[i,j]), ha="right", va="bottom", fontsize=7, color="white", alpha=.8)
ax.set_xticks(range(5)); ax.set_xticklabels(["1 Muy baja","2 Baja","3 Media","4 Alta","5 Muy alta"], fontsize=8)
ax.set_yticks(range(5)); ax.set_yticklabels(["5 Catastrófico","4 Mayor","3 Moderado","2 Menor","1 Insignif."], fontsize=8)
ax.set_xlabel("Probabilidad"); ax.set_ylabel("Impacto")
ax.set_title("Mapa de calor — riesgos de ejecución del PETI (n = %d)" % len(r))
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=c,label=l) for c,l in zip(cmap.colors,["Bajo ≤6","Medio 7–11","Alto 12–14","Crítico ≥15"])],
          loc="upper left", bbox_to_anchor=(1.01,1), fontsize=8, title="Nivel")
plt.tight_layout()
plt.savefig("../graficos/RG_mapa_calor.png", dpi=140, bbox_inches="tight")
