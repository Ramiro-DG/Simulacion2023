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

frRun = [calcularFr(), calcularFr(), calcularFr(), calcularFr()]


# Impresión de resultados
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.plot(iter, calcularFr(), label="Run 1")
ax.plot(iter, calcularFr(), label="Run 2")
ax.plot(iter, calcularFr(), label="Run 3")
ax.plot(iter, calcularFr(), label="Run 4")
ax.plot(iter, [1/37]*iteracion, label="Valor esperado: 1/37")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('fr (frecuencia relativa)')
ax.set_title('Frecuencia relativa del número 7')
ax.legend()
fig.set_facecolor('white')

plt.show()


# Realizo gráfica del promedio de las frecuencias relativas
promFromFrRun = []
for iteracion in iter:
    suma = 0
    for run in frRun:
        suma += run[iteracion-1]
    promFromFrRun.append(suma/len(frRun))

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
ax.plot(iter, promFromFrRun, label="Promedio de las frecuencias relativas obtenidos de las cuatro corridas")
ax.plot(iter, [1/37]*iteracion, label="Valor esperado: 1/37")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('fr (Frecuencia relativa)')
ax.set_title('Promedios de frecuencias relativas')
ax.legend()
fig.set_facecolor('white')

plt.show()