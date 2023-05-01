import random
import matplotlib.pyplot as plt
import numpy as np
import math


fig, ax = plt.subplots()

aceptados=[]
lam=0.3
c=1/lam
a=0
b=20

def fg(x)->float:
    return math.exp(-lam*x)

def fx(r)->float:
    return a+(b-a)*r

def metodo():
    for ran in range(6000):
        x=fx(np.random.uniform(0,1))
        g=fg(x)
        rand=np.random.uniform(0,1)
        if(rand<=g):
            aceptados.append(x)
            # print(x)
            # print(rand)


metodo()
print(len(aceptados))

plt.hist(aceptados,
        bins=30,
        density=True,
        label="Exponencial por metodo rechazo")

# Funcion teorica
x = np.linspace(a,b, 1000)
y = lam * np.exp(-lam * x)
ax.plot(x, y, 'r-', linewidth=2)
plt.plot(x, y, color='red', label='Exponencial teorica')
plt.title('Distribución Exponencial')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.legend()
plt.show()