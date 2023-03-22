import random
import matplotlib.pyplot as plt
import numpy as np

iteracion=1000000
numeroEstudio=7
valorEstimado=1/37

iter=[]
frecuenciasAbsolutas=[0]*iteracion
frecuenciasRelativas=[]

print('Procesando simulacion...')
for x in range(iteracion):
    num=random.randint(0,36)
    iter.append(x+1)
    if(num==numeroEstudio):
        frecuenciasAbsolutas[x]+=1
    if(x<iteracion-1):
        frecuenciasAbsolutas[x+1]=frecuenciasAbsolutas[x]

for y in range(iteracion):
    frecuenciasRelativas.append(frecuenciasAbsolutas[y]/iter[y])


fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.plot(iter, [valorEstimado]*iteracion)
ax.plot(iter, frecuenciasRelativas)

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('fr (frecuencia relativa)')
ax.set_title('Frecuencia absoluta del numero 7')
fig.set_facecolor('white')

plt.show()