from Ruleta import Ruleta, Color
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import norm


def run_martingala(n, capital_incial=None):

    MONTO_INICIAL = 5
    monto = MONTO_INICIAL
    error = 0.01
    z_objetivo = 1.96  # para el 95% de confianza
    r = Ruleta(lambda: random.randint(0, 36))
    numeroElegido = 0

    flujo_caja_acumulado = 0
    fa = 0
    iteraciones = range(1, n+1)
    frecuencias_relativas_apuestas_favorables = []
    flujos_en_caja = []

    for i in range(n):
        if (capital_incial is not None and capital_incial+flujo_caja_acumulado == 0):
            flujos_en_caja.append(flujo_caja_acumulado)
            frecuencias_relativas_apuestas_favorables.append(fa/(i+1))
            continue  # sin plata

        flujo_caja_en_tirada = 0

        flujo_caja_en_tirada -= monto
        r.apostar_color(Color.NEGRO, monto)
        flujo_caja_en_tirada += r.tirar()

        if (flujo_caja_en_tirada < 0):
            monto *= 2
        else:
            monto = MONTO_INICIAL

        if (monto > Ruleta.MAX_MONTO):
            monto = Ruleta.MAX_MONTO

        flujo_caja_acumulado += flujo_caja_en_tirada
        if (flujo_caja_en_tirada > 0):
            fa += 1
        frecuencias_relativas_apuestas_favorables.append(fa/n)
        flujos_en_caja.append(flujo_caja_acumulado)

    pn = frecuencias_relativas_apuestas_favorables[-1]  # ultimo elemento
    if (pn != 0):
        z = error*math.sqrt(n/pn*(1-pn))
        conf_level_fr = 1 - 2*norm.cdf(-z)
    else:
        conf_level_fr = -1
    return iteraciones, frecuencias_relativas_apuestas_favorables, flujos_en_caja, conf_level_fr
