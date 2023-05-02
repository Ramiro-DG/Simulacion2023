from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def normal_pdf(mean, sigma):
    coeficient = 1 / (sigma * np.sqrt(2 * np.pi))
    index = lambda x: -0.5 * ((x - mean) / sigma)**2
    return lambda x: coeficient * np.exp(index(x))


def normal(mean, sigma, size):
    min = mean - 3 * sigma
    max = mean + 3 * sigma
    pdf = normal_pdf(mean, sigma)

    aceptados = mr.metodo_rechazo(pdf_estudio=pdf,
                                  techo=pdf(mean),
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
    plt.plot(x, y, color='red', label='Normal teorica')

    plt.title('Distribución Normal')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
