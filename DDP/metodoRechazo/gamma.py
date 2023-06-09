import math
from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def gamma_pdf(k, theta):
    factor_1 = 1 / (math.factorial(int(k) - 1) * (theta**k))
    factor_2 = lambda x: x**(k - 1)
    factor_3 = lambda x: np.exp(-x / theta)
    return lambda x: factor_1 * factor_2(x) * factor_3(x)


def gamma(k, theta, size):
    name = "Gamma"
    min = 0
    max = k * theta + 2 * k * theta**2  #aprox con la regla empirica
    pdf = gamma_pdf(k, theta)
    techo = pdf((k - 1) * theta)

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
    y = pdf(x)
    plt.plot(x, y, color='red', label=name + ' teorica')

    plt.title('Distribución ' + name + f" - size={size} theta={theta} k={k}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
