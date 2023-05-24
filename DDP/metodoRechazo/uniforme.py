from Shared import metodo_rechazo as mr
from Shared import kolmogorov_smirnov_test as kst
from scipy.stats import uniform

import matplotlib.pyplot as plt
import numpy as np

def uniforme_pdf(a, b):
    return lambda x: 1 / (b - a)


def uniforme(a, b, size):
    name = "Uniforme"
    min = a
    max = b
    pdf = uniforme_pdf(a, b)
    techo = pdf((a + b) / 2)

    accepted = mr.metodo_rechazo(pdf_estudio=pdf,
                                 techo=techo,
                                 min=min,
                                 max=max,
                                 size=size)

    plt.hist(accepted,
             bins=30,
             density=True,
             label=name + " por método rechazo")

    # Funcion teorica
    x = np.linspace(min, max, size)
    y = [pdf(x)] * len(x)
    plt.plot(x, y, color='red', label=name + ' teorica')

    plt.title('Distribución ' + name + f" - size={size} a={a} b={b}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()

    kst.ks_test(accepted, uniform, "Uniforme (rechazo)")