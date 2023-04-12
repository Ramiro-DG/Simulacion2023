from tau_strategy import run_todo_a_uno
import matplotlib.pyplot as plt

n = 100000

fr, _ = run_todo_a_uno(n)


fig, ax = plt.subplots()
ax.set_xlim(0, 200)


ax.stem(list(fr.keys()), list(fr.values()))
ax.set_ylabel('Frecuencia relativa')
ax.set_title(
    'Fr de ganar con dinero infinito segun n - Todo a uno')
plt.show()
