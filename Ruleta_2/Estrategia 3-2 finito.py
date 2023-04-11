from Ruleta import Ruleta, Color
import random
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

for n in range(30):
    iteraciones = 2000
    capital = 1000
    flujoCaja = []
    while(capital>50 and iteraciones>0):
        r = Ruleta(lambda: random.randint(0, 36))
        r.apostar_columna(2, 20)
        r.apostar_color(Color.ROJO, 30)
        ganancia = r.tirar()

        capital = capital-50+ganancia
        flujoCaja.append(capital)
        iteraciones-=1
        
    ax.plot(range(1,len(flujoCaja)+1), flujoCaja, label="Flujo de caja")

ax.plot(range(1,2001), [1000]*2000, label="Capital inicial")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Cantidad de capital')
ax.set_title('Flujo de capital con dinero finito')

fig.set_facecolor('white')

plt.show()