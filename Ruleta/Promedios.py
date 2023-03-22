import random
import matplotlib.pyplot as plt
import numpy as np

iteracion=1000000
numeroEstudio=7
iter=[]
promedios=[]
suma=0
cantidad=0
for x in range(iteracion):
    num=random.randint(0,36)
    suma+=num
    cantidad+=1
    iter.append(cantidad)
    promedios.append(suma/cantidad)

fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.plot(iter, promedios)
ax.plot(iter, [18]*iteracion)

ax.set_xlabel('tiradas')
ax.set_ylabel('promedio')
ax.set_title('promedios')
fig.set_facecolor('white')

plt.show()