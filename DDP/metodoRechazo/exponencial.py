import random
import matplotlib.pyplot as plt
import numpy as np
import math


fig, ax = plt.subplots()

aceptados=[]
a=0
b=20

def fg(x, lam)->float:
    return math.exp(-lam*x)

def fx(r)->float:
    return a+(b-a)*r

def exponencial(lam, size):
    for ran in range(6000):
        x=fx(np.random.uniform(0,1))
        g=fg(x, lam)
        rand=np.random.uniform(0,1)
        if(rand<=g):
            aceptados.append(x)
    
    plt.hist(aceptados,
            bins=30,
            density=True,
            label="Exponencial por metodo rechazo")

    # Funcion teorica
    x = np.linspace(a,b, size)
    y = lam * np.exp(-lam * x)
    ax.plot(x, y, 'r-', linewidth=2)
    plt.plot(x, y, color='red', label='Exponencial teorica')
    plt.title('Distribución Exponencial')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()

