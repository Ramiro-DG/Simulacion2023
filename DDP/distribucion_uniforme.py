import random
import matplotlib.pyplot as plt
import numpy as np

def uniforme(a, b, size):
    datos = np.random.uniform(a, b, size)
    
    # Valores de la función de densidad en un rango de valores de x
    x = np.linspace(a, b, 1000)
    y = np.full_like(x, 1/(b-a))
    
    plt.plot(x, y, color='blue', label='Distribución Uniforme')
    plt.hist(datos, bins=10, density=True)
    plt.legend(["Función de densidad de probabilidad"], loc='upper right')
    plt.title('Distribución Uniforme')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.show()