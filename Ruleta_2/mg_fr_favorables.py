from martin_gala_strategy import run_martingala
import matplotlib.pyplot as plt

n = 100000

fr, _ = run_martingala(n)

fig, ax = plt.subplots()
ax.set_xlim(0, 20)
plt.xticks(range(1, 20, 1))  # Set the step size to 1

ax.stem(list(fr.keys()), list(fr.values()))
ax.set_ylabel('Frecuencia relativa')
ax.set_title('Fr de ganar con dinero infinito segun n - Martingala')
plt.show()
