from martin_gala_strategy import run_martingala
import matplotlib.pyplot as plt

n = 2000
runs = 30
dinero_inicial = 1000

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

for _ in range(runs):
    _, fl = run_martingala(n, dinero_inicial)
    desplazado = list(map(lambda x: x+dinero_inicial, fl.values()))
    ax.plot(list(fl.keys()), desplazado, label="Flujo de caja")

ax.axhline(y=dinero_inicial, color='b', linestyle='dotted')
ax.set_ybound(0)
ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Cantidad de capital')
ax.set_title('Flujo de capital finito - Martingala')
fig.set_facecolor('white')
plt.show()
