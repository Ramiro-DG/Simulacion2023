import math
from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def mdf_binomial(n, p):
    f1 = lambda x: math.factorial(n)
    f2 = lambda x: 1 / (math.factorial(int(x)) * math.factorial(int(n - x)))
    f3 = lambda x: (p**x) * ((1 - p)**(n - x))
    return lambda x: f1(x) * f2(x) * f3(x)


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
    print(y)
    plt.scatter(x, y, color='red', label=name + ' teorica')

    plt.title('Distribución ' + name)
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
