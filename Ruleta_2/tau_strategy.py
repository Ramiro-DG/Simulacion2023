from Ruleta import Ruleta
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

'''
En cada tirada apostamos $100 al 0, simple y facil
'''

monto = 5
error = 0.01
z_objetivo = 1.96  # para el 95% de confianza

r = Ruleta(lambda: random.randint(0, 36))
numeroElegido = 0


def run_todo_a_uno(n, capital_incial=None):
    flujo_caja_acumulado = 0
    fa = 0
    iteraciones = range(1, n+1)
    frecuencias_relativas_apuestas_favorables = []
    flujos_en_caja = []
    for i in range(n):
        if (capital_incial is not None and capital_incial+flujo_caja_acumulado < 0):
            iteraciones = range(1, len(flujos_en_caja)+1)
            break  # sin plata
        flujo_caja_en_tirada = 0
        flujo_caja_en_tirada -= monto
        r.apostar_numero(numeroElegido, monto)
        flujo_caja_en_tirada += r.tirar()
        flujo_caja_acumulado += flujo_caja_en_tirada
        if (flujo_caja_en_tirada > 0):
            fa += 1
        frecuencias_relativas_apuestas_favorables.append(fa/(i+1))
        flujos_en_caja.append(flujo_caja_acumulado)

    pn = frecuencias_relativas_apuestas_favorables[-1]  # ultimo elemento
    if (pn != 0):
        z = error*math.sqrt(n/pn*(1-pn))
        conf_level_fr = 1 - 2*norm.cdf(-z)
    else:
        conf_level_fr = -1
    return iteraciones, frecuencias_relativas_apuestas_favorables, flujos_en_caja, conf_level_fr
