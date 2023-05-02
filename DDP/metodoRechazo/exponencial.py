from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def exponencial(lam, size):
    min = 0
    max = 20
    pdf = lambda x: lam * np.exp(-lam * x)

    aceptados = mr.metodo_rechazo(pdf_estudio=pdf,
                                  techo=lam,
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
    plt.plot(x, y, color='red', label='Exponencial teorica')

    plt.title('Distribución Exponencial')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()