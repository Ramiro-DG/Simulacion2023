from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np


def exponencial(lam, size):
    name = "Exponencial"
    min = 0
    max = (-1 / lam) * np.log(1 - 0.999)
    pdf = lambda x: lam * np.exp(-lam * x)
    techo = lam

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

    plt.title('Distribución ' + name + f" - size={size} lamba={lam}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
