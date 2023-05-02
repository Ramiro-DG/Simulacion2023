import math
import scipy
from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def gamma_pdf(k, theta):
    factor_1 = 1 / (math.factorial(int(k) - 1) * (theta**k))
    factor_2 = lambda x: x**(k - 1)
    factor_3 = lambda x: np.exp(-x / theta)
    return lambda x: factor_1 * factor_2(x) * factor_3(x)


def gamma(k, theta, size):
    min = 0
    max = 10
    pdf = gamma_pdf(k, theta)

    aceptados = mr.metodo_rechazo(pdf_estudio=pdf,
                                  techo=pdf((k - 1) * theta),
                                  min=min,
                                  max=max,
                                  size=size)

    plt.hist(aceptados,
             bins=30,
             density=True,
             label="Exponencial por metodo rechazo")

    # Funcion teorica
    x = np.linspace(min, max, size)
    y = pdf(x)
    plt.plot(x, y, color='red', label='Gamma teorica')

    plt.title('Distribución Gamma')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
