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
    f1 = lambda x: scipy.special.comb(K, x)
    f2 = lambda x: scipy.special.comb(N - K, n - x)
    f3 = lambda x: scipy.special.comb(K, x)
    return lambda x: (f1(x) * f2(x) / f3(x))


def hipergeometrica(N, K, n, size):
    name = "Hipergeometrica"
    min = -20
    max = 20
    mdf = mdf_hiper_geometrica(N, K, n)
    techo = mdf(0)
    print('den ', scipy.special.comb(K, 0))

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

    plt.title('Distribución ' + name)
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
