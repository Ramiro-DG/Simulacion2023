import random
import matplotlib.pyplot as plt
import numpy as np

iteracion = 10000
iter = range(1, iteracion+1)
numeroEstudio = 7


def calcularPromedio():
    valores = []
    promedios = []
    for x in range(iteracion):
        num = random.randint(0, 36)
        valores.append(num)
        promedios.append(np.average(valores))
    return promedios

promRun = [calcularPromedio(), calcularPromedio(), calcularPromedio(), calcularPromedio()]


# Impresión de resultados
fig, ax = plt.subplots(figsize = (7, 4), constrained_layout = True)
ax.plot(iter, promRun[0], label="Run 1")
ax.plot(iter, promRun[1], label="Run 2")
ax.plot(iter, promRun[2], label="Run 3")
ax.plot(iter, promRun[3], label="Run 4")
ax.plot(iter, [18]*iteracion, label="Valor Esperado: 18")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Promedio')
ax.set_title('Promedios')
ax.legend()
fig.set_facecolor('white')

plt.show()


# Realizo gráfica del promedio de los promedios
promFromPromRun = []
for iteracion in iter:
    suma = 0
    for run in promRun:
        suma += run[iteracion-1]
    promFromPromRun.append(suma/len(promRun))

fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
ax.plot(iter, promFromPromRun, label="Promedio de los promedios obtenidos de las cuatro corridas")
ax.plot(iter, [18]*iteracion, label="Valor Esperado: 18")

ax.set_xlabel('N° (Número de tiradas)')
ax.set_ylabel('Promedio')
ax.set_title('Promedios')
ax.legend()
fig.set_facecolor('white')

plt.show()