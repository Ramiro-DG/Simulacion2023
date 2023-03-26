import random
import matplotlib.pyplot as plt
import numpy as np

iteracion=10000
iter=range(1,iteracion+1)
numeroEstudio=7

suma=0
cantidad=0

def calcularPromedio():
    valores=[]
    promedios=[]
    for x in range(iteracion):
        num=random.randint(0,36)
        valores.append(num)
        promedios.append(np.average(valores))
    return promedios

fig, ax = plt.subplots(figsize=(5,4), constrained_layout=True)
ax.plot(iter, calcularPromedio(),label="Run 1")
ax.plot(iter, calcularPromedio(),label="Run 2")
ax.plot(iter, calcularPromedio(),label="Run 3")
ax.plot(iter, calcularPromedio(),label="Run 4")
ax.plot(iter, [18]*iteracion, label="Valor Esperado: 18")

ax.set_xlabel('tiradas')
ax.set_ylabel('promedio')
ax.set_title('promedios')
ax.legend()
fig.set_facecolor('white')

plt.show()