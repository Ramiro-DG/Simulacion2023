from Shared import metodo_rechazo as mr
import matplotlib.pyplot as plt
import numpy as np

def normal_pdf(mean, sigma):
    coeficient = 1 / (sigma * np.sqrt(2 * np.pi))
    index = lambda x: -0.5 * ((x - mean) / sigma)**2
    return lambda x: coeficient * np.exp(index(x))


def normal(mean, sigma, size):
    name = "Normal"
    min = mean - 3 * sigma
    max = mean + 3 * sigma
    pdf = normal_pdf(mean, sigma)
    techo = pdf(mean)

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

    plt.title('Distribución ' + name + f" - size={size} promedio={mean} desvio={sigma}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
