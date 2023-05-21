from math import comb
import math
import scipy
from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


# los nombres de los parametros son los que aparcen en la teoria,
# yo soy malo poniendo nombres pero los de estadisitca son peores
def mdf_hiper_geometrica(N, K, n):
    if (N < 0 or K < 0 or n < 0):
        raise ValueError('argumento debe ser mayor que cero')
    if (n > N or K > N):
        raise ValueError('n y K no pueden execer N')

    numerator = lambda x: comb(K, x) * comb(N - K, n - x)
    denominator = comb(N, n)
    return lambda x: numerator(x) / denominator


def hipergeometrica(N, K, n, size):
    name = "Hipergeometrica"
    mean = int(n * (K / N))
    sigma = int(math.sqrt(n * (K / N) * ((N - K) / N) * ((N - n) / (N - 1))))
    min = 0
    max = mean + 4 * sigma
    mdf = mdf_hiper_geometrica(N, K, n)
    techo = mdf(mean)

    accepted = mr.metodo_rechazo_dicreto(mpf_estudio=mdf,
                                         techo=techo,
                                         min=min,
                                         max=max,
                                         size=size)

    fa = {}
    for i in accepted:
        fa[i] = fa.get(i, 0) + 1

    for k in fa.keys():
        fa[k] = fa[k] / len(accepted)

    plt.bar(fa.keys(), fa.values(), label=name + " por método rechazo")

    # Funcion teorica
    x = range(min, max)
    y = list(map(lambda k: mdf(k), x))
    plt.scatter(x, y, color='red', label=name + ' teorica')
    plt.xlim(min, max)

    plt.title('Distribución ' + name + f" - size={size} N={N} k={k} n={n}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
