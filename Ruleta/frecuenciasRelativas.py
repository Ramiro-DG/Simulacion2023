import random
import matplotlib.pyplot as plt
import numpy as np

# Constantes
iteracion=10000
iter=range(1,iteracion+1)
numeroEstudio=7

def calcularFa():
    frecuenciasAbsolutas=[0]*iteracion
    for x in range(iteracion):
        num=random.randint(0,36)
        if(num==numeroEstudio):
            frecuenciasAbsolutas[x]+=1
        if(x<iteracion-1):
            frecuenciasAbsolutas[x+1]=frecuenciasAbsolutas[x]
    return frecuenciasAbsolutas

def calcularFr():
    frecuenciasRelativas=[]
    frecuenciasAbsolutas=calcularFa()
    for y in range(iteracion):
        frecuenciasRelativas.append(frecuenciasAbsolutas[y]/iter[y])
    return frecuenciasRelativas



fig, ax = plt.subplots(figsize=(5,4), constrained_layout=True)
ax.plot(iter, calcularFr(), label="Run 1")
ax.plot(iter, calcularFr(), label="Run 2")
ax.plot(iter, calcularFr(), label="Run 3")
ax.plot(iter, calcularFr(), label="Run 4")
ax.plot(iter, [1/37]*iteracion, label="Valor esperado: 1/37")

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('fr (frecuencia relativa)')
ax.set_title('frecuencia relativa del numero 7')
ax.legend()
fig.set_facecolor('white')

plt.show()