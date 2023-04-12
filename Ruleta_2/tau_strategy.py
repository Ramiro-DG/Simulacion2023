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
    iter = range(1, n+1)
    flujos_en_caja = []
    frs_veces_para_ganar = [0]*n
    contador_veces_perdidas=0
    for _ in range(n):
        if (capital_incial is not None and capital_incial+flujo_caja_acumulado < 0):
            iter = range(1, len(flujos_en_caja)+1)
            break  # sin plata
        flujo_caja_en_tirada = 0
        flujo_caja_en_tirada -= monto
        r.apostar_numero(numeroElegido, monto)
        flujo_caja_en_tirada += r.tirar()
        flujo_caja_acumulado += flujo_caja_en_tirada
        if(flujo_caja_en_tirada<0):
            contador_veces_perdidas+=1
        else:
            frs_veces_para_ganar[contador_veces_perdidas+1]+=1
            contador_veces_perdidas=0
    suma=sum(frs_veces_para_ganar)
    frs_veces_para_ganar=list(map(lambda x:x/suma, frs_veces_para_ganar) )
    return iter, frs_veces_para_ganar, flujos_en_caja
