from Ruleta import Ruleta, Color
import random
import matplotlib.pyplot as plt
import numpy as np

iteraciones = 200
corridas = 3000
arrayIteraciones = range(0, iteraciones)
apuestaRojo = 300  # 3
apuestaColumna = 200  # apuestaRojo*2/3  # 2}
vecesHastaGanar = [0]*iteraciones

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
fig2, ax2 = plt.subplots(figsize=(7, 4), constrained_layout=True)

flujo_caja_finales = []

for num in range(corridas):
    capitalInicial = 0.0
    flujoCaja = []
    frGanancia = []
    cantRondasSinGanar = 0
    for n in range(iteraciones):
        r = Ruleta(lambda: random.randint(0, 36))
        r.apostar_columna(2, apuestaColumna)
        r.apostar_color(Color.ROJO, apuestaRojo)
        ganancia = r.tirar()
        if (ganancia == 0):
            cantRondasSinGanar += 1
        else:
            vecesHastaGanar[cantRondasSinGanar+1] += 1
            cantRondasSinGanar = 0
        capitalInicial = capitalInicial-(apuestaRojo+apuestaColumna)+ganancia
        flujoCaja.append(capitalInicial)

    ax.plot(arrayIteraciones, flujoCaja, label="Flujo de caja")

    result = np.divide(vecesHastaGanar, iteraciones*30)
    ax2.stem(arrayIteraciones, result)
    flujo_caja_finales.append(flujoCaja[-1])
ax.axhline(y=0, color='b', linestyle='dotted')

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Cantidad de capital')
ax.set_title('Flujo de capital con dinero infinito')

# ax.legend()
fig.set_facecolor('white')


ax2.set_xlabel('N° (Número de tiradas)')
ax2.set_ylabel('fr de Ganancia')
ax2.set_title('fr de ganar con dinero infinito según n - Sistema 3/2')
ax2.set_xlim(left=0, right=10)
fig2.set_facecolor('white')


# distribucion de frecuencias absolutas del flujo de capital
fig_dist, ax_dist = plt.subplots(figsize=(7, 4), constrained_layout=True)
fl_no_repetidos = sorted(list(set(flujo_caja_finales)))
fa = {}
for value in fl_no_repetidos:
    fa[value] = 0
for value in flujo_caja_finales:
    fa[value] += 1
ax_dist.stem(list(fa.keys()), list(fa.values()))

mu = np.average(flujo_caja_finales)
sigma = np.std(flujo_caja_finales)
print('media: ', mu)
print('desvio: ', sigma)
plt.axvline(x=mu, color='r', label='promedio')
plt.axvline(x=mu+sigma, color='y', label='un desvio estandar')
plt.axvline(x=mu-sigma, color='y')
plt.axvline(x=mu+2*sigma, color='g', label='dos desvios estandar')
plt.axvline(x=mu-2*sigma, color='g')

ax_dist.set_ylabel('frecuencia absoluta (corridas)')
ax_dist.set_xlabel('ganancia final')
ax_dist.set_xlim(mu-3*sigma, mu+3*sigma)
plt.title(
    "Frecuencias absolutas la ganacia final luego de %d tiradas - Estrategia 3-2" % (iteraciones))

plt.legend()
plt.show()


plt.show()
