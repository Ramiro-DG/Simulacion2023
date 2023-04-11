from tau_strategy import run_todo_a_uno
import matplotlib.pyplot as plt

n = 1_500

i, fr, _, conf = run_todo_a_uno(n)

print('nivel de confianza :', conf)
print('aproximacion final :', fr[-1])

fig, ax = plt.subplots()
bar_labels = ['blue']*n
bar_colors = ['tab:blue']*n
ax.bar(i, fr, label=bar_labels, color=bar_colors)
ax.set_ylabel('Frecuencia relativa')
ax.set_title(
    'Frecuencia relativa de obtener la apuesta favorable segun n - Todo a uno')
plt.show()
