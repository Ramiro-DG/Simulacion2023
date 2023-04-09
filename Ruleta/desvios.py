import random
import matplotlib.pyplot as plt
import numpy as np

# Constantes
iteracion=10000
iter=range(1,iteracion+1)

# Ploteo de Valores del desvio
def calcularDesvios():
    muestras=[]
    desvios=[]
    for x in range(iteracion):
        num=random.randint(0,36)
        muestras.append(num)
        desvios.append(np.std(muestras,dtype=np.float64))
    return desvios

desvioRun = [calcularDesvios(), calcularDesvios(), calcularDesvios(), calcularDesvios()]


# Impresión de resultados
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.plot(iter,desvioRun[0], label="Run 1")
ax.plot(iter,desvioRun[1], label="Run 2")
ax.plot(iter,desvioRun[2], label="Run 3")
ax.plot(iter,desvioRun[3], label="Run 4")
ax.plot(iter, [np.sqrt(114)]*iteracion, label="Valor esperado: 10,6771")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('s (Desvío estándar)')
ax.set_title('Desvío estándar de la muestra')
ax.legend()
fig.set_facecolor('white')

plt.show()


# Realizo gráfica del promedio de los desvíos
promFromDesvioRun = []
for iteracion in iter:
    suma = 0
    for run in desvioRun:
        suma += run[iteracion-1]
    promFromDesvioRun.append(suma/len(desvioRun))

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
ax.plot(iter, promFromDesvioRun, label="Promedio de los desvíos obtenidos de las cuatro corridas")
ax.plot(iter, [np.sqrt(114)]*iteracion, label="Valor esperado: 10,6771")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('s (Desvío estándar)')
ax.set_title('Promedios de desvíos')
ax.legend()
fig.set_facecolor('white')

plt.show()