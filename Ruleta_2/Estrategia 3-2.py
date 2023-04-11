from Ruleta import Ruleta, Color
import random
import matplotlib.pyplot as plt

iteraciones = 200
arrayIteraciones=range(0, iteraciones)
capitalInicial = 0.0
flujoCaja=[]
apuestaRojo=3  #3
apuestaColumna=apuestaRojo*2/3   #2

for n in range(iteraciones):
    r = Ruleta(lambda: random.randint(0, 36))
    r.apostar_columna(2, apuestaColumna)
    r.apostar_color(Color.ROJO, apuestaRojo)
    ganancia=r.tirar()
    capitalInicial=capitalInicial-(apuestaRojo+apuestaColumna)+ganancia
    flujoCaja.append(capitalInicial)

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
ax.plot(arrayIteraciones, flujoCaja, label="Flujo de caja")
ax.plot(arrayIteraciones, [0]*iteraciones, label="Capital inicial")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Cantidad de capital')
ax.set_title('Flujo de capital con dinero infinito')
ax.legend()
fig.set_facecolor('white')

plt.show()