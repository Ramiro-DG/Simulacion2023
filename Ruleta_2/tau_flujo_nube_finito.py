from tau_strategy import run_todo_a_uno
import matplotlib.pyplot as plt

n = 2000
runs = 30
dinero_inicial = 1000

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

for i in range(runs):
    i, _, fl, _ = run_todo_a_uno(n, dinero_inicial)
    print('aproximacion final :', fl[-1])
    print('largos: ', len(i), len(fl))
    ax.plot(i, fl, label="Flujo de caja")

ax.axhline(y=0, color='b', linestyle='dotted')
ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Cantidad de capital')
ax.set_title('Flujo de capital')
fig.set_facecolor('white')
plt.show()