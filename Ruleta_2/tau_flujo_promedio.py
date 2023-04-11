from tau_strategy import run_todo_a_uno
import matplotlib.pyplot as plt
import numpy as np

n = 40
runs = 400

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

fl_prom = []
for i in range(n):
    arr = []
    for i in range(runs):
        i, _, fl, _ = run_todo_a_uno(n)
        arr.append(fl)
    fl_prom.append(np.average(arr))

ax.plot(i, fl_prom, label="Flujo de caja promedio")
ax.plot(i, [0]*n, label="capital inicial")
ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Cantidad de capital')
ax.set_title('Flujo de capital promedio')
fig.set_facecolor('white')
plt.show()
