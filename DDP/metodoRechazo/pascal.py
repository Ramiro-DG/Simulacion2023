import math
from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt


def mdf_pascal(r, p):
    return lambda x: math.comb(x + r - 1, x) * (p**r) * ((1 - p)**x)


def pascal(r, p, size):
    name = "Pascal"
    moda = math.floor((r - 1) * (1 - p) / p)
    min = 0
    max = moda * 2
    mdf = mdf_pascal(r, p)
    techo = mdf(moda)

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

    plt.title('Distribución ' + name + f" - size={size} r={r} p={p}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
