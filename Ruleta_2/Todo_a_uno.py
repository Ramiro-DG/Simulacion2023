from Ruleta import Ruleta
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

'''
En cada tirada apostamos $100 al 0, simple y facil
'''

r = Ruleta(lambda: random.randint(0, 36))
n = 2000
numeroElegido = 0
monto = 100
error = 0.01
z_objetivo = 1.96  # para el 95% de confianza

iteraciones = range(1, n+1)
frecuanciasRelativasApuestasFavorables = []
fa = 0
for i in range(n):
    flujo_caja_en_tirada = 0
    flujo_caja_en_tirada -= monto
    r.apostar_numero(numeroElegido, monto)
    flujo_caja_en_tirada += r.tirar()
    if (flujo_caja_en_tirada > 0):
        fa += 1
    frecuanciasRelativasApuestasFavorables.append(fa/n)


print('creando graficos...')
fig, ax = plt.subplots()

pn = frecuanciasRelativasApuestasFavorables[-1]  # ultimo elemento
z = error*math.sqrt(n/pn*(1-pn))

conf_level = 1 - 2*norm.cdf(-z)
print('nivel de confianza: ', conf_level)
if (z > z_objetivo):
    print('suficente n')
else:
    print('falta n')

bar_labels = ['blue']*n
bar_colors = ['tab:blue']*n

ax.bar(iteraciones, frecuanciasRelativasApuestasFavorables,
       label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('')

plt.show()
