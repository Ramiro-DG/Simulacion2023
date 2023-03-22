import random
import matplotlib.pyplot as plt
import numpy as np

iteracion=1000000
numeroEstudio=7
iter=[]
frecuenciasAbsolutas=[0]*iteracion
frecuenciasRelativas=[]

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
ax.plot(iter, frecuenciasRelativas)
ax.plot(iter, [1/37]*iteracion)

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('fr (frecuencia relativa)')
ax.set_title('frecuencia absoluta del numero 7')
fig.set_facecolor('white')

plt.show()