from martin_gala_strategy import run_martingala
import matplotlib.pyplot as plt

n = 40_000

i, fr, _, conf = run_martingala(n)

print('nivel de confianza :', conf)
print('aproximacion final :', fr[-1])

fig, ax = plt.subplots()
bar_labels = ['blue']*n
bar_colors = ['tab:blue']*n
ax.bar(i, fr, label=bar_labels, color=bar_colors)
ax.set_ylabel('Frecuencia relativa')
ax.set_title(
    'Frecuencia relativa de obtener la apuesta favorable segun n - Martingala')
plt.show()
