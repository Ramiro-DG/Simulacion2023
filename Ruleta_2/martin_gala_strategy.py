from Ruleta import Ruleta, Color
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import norm


def run_martingala(n, capital_incial=None):

    MONTO_INICIAL = 5
    monto = MONTO_INICIAL
    r = Ruleta(lambda: random.randint(0, 36))

    flujo_caja_acumulado = 0
    flujos_en_caja = {}
    frs_veces_para_ganar = {}
    contador_veces_perdidas = 0

    for i in range(1, n+1):
        # Estrategia
        if (capital_incial is not None and capital_incial+flujo_caja_acumulado <= 0):
            iteraciones = range(1, len(flujos_en_caja)+1)
            break  # sin plata
        flujo_caja_en_tirada = 0
        flujo_caja_en_tirada -= monto
        r.apostar_color(Color.NEGRO, monto)
        flujo_caja_en_tirada += r.tirar()
        if (flujo_caja_en_tirada < 0):
            monto *= 2
            if (capital_incial is not None and capital_incial+flujo_caja_acumulado < monto):
                monto = capital_incial+flujo_caja_acumulado
        else:
            monto = MONTO_INICIAL
        if (monto > Ruleta.MAX_MONTO):
            monto = Ruleta.MAX_MONTO

        # Actualizacion de estadisticos
        flujo_caja_acumulado += flujo_caja_en_tirada
        flujos_en_caja[i] = flujo_caja_acumulado
        if (flujo_caja_en_tirada < 0):
            contador_veces_perdidas += 1
        else:
            frs_veces_para_ganar[contador_veces_perdidas +
                                 1] = frs_veces_para_ganar.get(contador_veces_perdidas+1, 0)+1
            contador_veces_perdidas = 0

    suma = sum(frs_veces_para_ganar.values())
    if suma == 0:
        suma = -1
    for key, value in frs_veces_para_ganar.items():
        frs_veces_para_ganar[key] = value/suma

    return frs_veces_para_ganar, flujos_en_caja
