from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def mdf_empirica():

    def mdf(x):
        if x == 1:
            return 0.3
        elif x == 2:
            return 0.4
        elif x == 4:
            return 0.3
        else:
            return 0

    return mdf


def empirica_discreta(size):
    name = "Empirica discreta"
    min = 0
    max = 5
    mdf = mdf_empirica()
    techo = 0.4

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
    x = range(0, max)
    y = list(map(lambda k: mdf(k), x))
    plt.scatter(x, y, color='red', label=name + ' teorica')

    plt.title('Distribución ' + name + f" - size={size}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
