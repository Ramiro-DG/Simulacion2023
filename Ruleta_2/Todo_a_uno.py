from Ruleta import Ruleta
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

'''
En cada tirada apostamos $100 al 0, simple y facil
'''

graficar_fr = True
graficar_flujo = True

n = 5000
runs = 10
monto = 1
error = 0.01
z_objetivo = 1.96  # para el 95% de confianza

r = Ruleta(lambda: random.randint(0, 36))
numeroElegido = 0

iteraciones = range(1, n+1)
frecuencias_relativas_apuestas_favorables = []
flujos_en_caja = []
flujo_caja_acumulado = 0
fa = 0

for r in runs:
    for i in range(n):
        flujo_caja_en_tirada = 0
        flujo_caja_en_tirada -= monto
        r.apostar_numero(numeroElegido, monto)
        flujo_caja_en_tirada += r.tirar()
        flujo_caja_acumulado += flujo_caja_en_tirada
        if (flujo_caja_en_tirada > 0):
            fa += 1
        frecuencias_relativas_apuestas_favorables.append(fa/n)
        flujos_en_caja.append(flujo_caja_acumulado)


print('creando graficos...')
if (graficar_flujo):
    fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
    ax.plot(iteraciones, flujos_en_caja, label="Flujo de caja")
    ax.plot(iteraciones, [0]*n, label="capital inicial")
    ax.set_xlabel('N° (Número de tiradas)')
    ax.set_ylabel('Cantidad de capital')
    ax.set_title('Flujo de capital')
    ax.legend()
    fig.set_facecolor('white')
    plt.show()


if (graficar_fr):
    pn = frecuencias_relativas_apuestas_favorables[-1]  # ultimo elemento
    z = error*math.sqrt(n/pn*(1-pn))
    conf_level = 1 - 2*norm.cdf(-z)
    print('nivel de confianza: ', conf_level)
    if (z > z_objetivo):
        fig, ax = plt.subplots()
        bar_labels = ['blue']*n
        bar_colors = ['tab:blue']*n
        ax.bar(iteraciones, frecuencias_relativas_apuestas_favorables,
               label=bar_labels, color=bar_colors)
        ax.set_ylabel('Frecuencia relativa')
        ax.set_title(
            'Frecuencia relativa de obtener la apuesta favorable segun n')
        plt.show()
    else:
        print('nivel de confianza insuficente, aumentar n')
