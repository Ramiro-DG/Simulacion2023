import random
import matplotlib.pyplot as plt
import numpy as np

iteraciones=1000
numeroEstudio=7
valorEstimado=18

iter=[]
promedios=[]
suma=0
cantidad=0

print('Procesando simulacion...')
for x in range(iteraciones):
    num=random.randint(0,36)
    suma+=num
    cantidad+=1
    iter.append(cantidad)
    promedios.append(suma/cantidad)

fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.plot(iter, [valorEstimado]*iteraciones)
ax.plot(iter, promedios)

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('promedio')
ax.set_title('Promedios')
fig.set_facecolor('white')

plt.show()