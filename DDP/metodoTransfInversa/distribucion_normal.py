from Shared import kolmogorov_smirnov_test as kst
from scipy.stats import norm

import random
import matplotlib.pyplot as plt
import numpy as np
import spicy as norm2


def newton_raphson(p, mu=0, sigma=1, tol=1e-6, max_iter=100):
    x = mu # initial guess
    for i in range(max_iter):
        pdf = norm2.spicy.pdf(x, loc=mu, scale=sigma)
        cdf = norm2.spicy.cdf(x, loc=mu, scale=sigma)
        x_new = x - (cdf - p) / pdf
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x

#f^(-1)(y) = μ ± σ√(-2ln(yσ√(2π)))

def normal(media, sigma, size): 

    fig, ax = plt.subplots()
    #f(x) = (1 / σ√(2π)) * e^(-(x-μ)^2 / (2σ^2))
    #  
    # Distribucion generada a partir de la uniforme
    datos = np.random.uniform(0, 1, size)
    transformZ = np.vectorize(lambda u: (pow(u, 0.1349)-pow(1-u,0.1349))/0.1975)
    datosZ = transformZ(datos);
    transformX = np.vectorize(lambda u: u*sigma+media)
    datosX=transformX(datosZ)
    plt.hist(datosX,
            bins=30,
            density=True,
            label="Normal por transformada inversa")

    #Normal teórica
    x = np.linspace(media-3*sigma, media+3*sigma, size)
    y = (1/(sigma*np.sqrt(2*np.pi)))*(np.exp(-pow(x-media,2)/(2*pow(sigma,2))))
    ax.plot(x, y, 'r-', linewidth=2)
    plt.plot(x, y, color='red', label='Normal teórica')
    
    plt.title('Distribución Normal')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend(["Función de densidad de probabilidad"], loc='upper right')
    plt.show()

    kst.ks_test(datos, norm, "Normal (inversa)")