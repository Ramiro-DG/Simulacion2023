from Shared import kolmogorov_smirnov_test as kst
from scipy.stats import poisson

import random
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy

fig, ax = plt.subplots()

accepted=[]
a=0
b=30

def fg(x, lam)->float:
    return (math.exp(-lam)*pow(lam, x))/(scipy.special.factorial(x))

def fx(r)->float:
    return a+(b-a)*r

def poisson_rechazo(lam, size):
    for ran in range(10000):
        x=fx(np.random.uniform(0,1))
        g=fg(x, lam)
        rand=np.random.uniform(0,1)
        if(rand<=g):
            accepted.append(x)

    plt.hist(accepted,
            bins=30,
            density=True,
            label="Poisson por metodo rechazo")

    # Funcion teorica
    x = np.linspace(a, b, size)
    y = (math.exp(-lam)*pow(lam, x))/(scipy.special.factorial(x))
    ax.plot(x, y, 'r-', linewidth=2)
    plt.plot(x, y, color='red', label='Poisson teórica')
    plt.title('Distribución Poisson' + f" - size={size} lamda={lam}")
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()

    kst.ks_test(accepted, poisson, "Poisson (rechazo)")