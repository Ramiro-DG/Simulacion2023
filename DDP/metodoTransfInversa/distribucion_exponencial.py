from Shared import kolmogorov_smirnov_test as kst
from scipy.stats import expon

import random
import matplotlib.pyplot as plt
import numpy as np


def exponencial(lam, size):

    fig, ax = plt.subplots()

    # Distribucion generada a partir de la uniforme
    datos = np.random.uniform(0, 1, size)
    transform = np.vectorize(lambda u: (-1 / lam) * np.log(1 - u))
    datos = transform(datos)
    plt.hist(datos,
             bins=30,
             density=True,
             label="Exponencial por transformada inversa")

    # Funcion teorica
    x = np.linspace(0, np.amax(datos), 100)
    y = lam * np.exp(-lam * x)
    ax.plot(x, y, 'r-', linewidth=2)
    plt.plot(x, y, color='red', label='Exponencial teorica')

    plt.title('Distribución Exponencial')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()

    kst.ks_test(datos, expon, "Exponencial (inversa)")