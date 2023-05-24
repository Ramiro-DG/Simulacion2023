from Shared import metodo_rechazo as mr
from Shared import kolmogorov_smirnov_test as kst
from scipy.stats import binom

import matplotlib.pyplot as plt
import numpy as np
import math


def mdf_binomial(n, p):
    factorial = lambda x: math.factorial(int(x))
    f1 = lambda x: factorial(n) / (factorial(x) * factorial(n - x))
    f2 = lambda x: (p**x) * ((1 - p)**(n - x))
    return lambda x: f1(x) * f2(x)


def binomial(n, p, size):
    name = "Binomial"
    min = 0
    max = n
    mdf = mdf_binomial(n, p)
    techo = 1

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
    x = range(0, n)
    y = list(map(lambda k: mdf(k), x))
    plt.scatter(x, y, color='red', label=name + ' teorica')

    plt.title('Distribución ' + name+ f" - size={size} n={n} p={p}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()

    kst.ks_test(accepted, binom, "Binomial (rechazo)")