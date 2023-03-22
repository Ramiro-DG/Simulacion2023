import random
import matplotlib.pyplot as plt
import numpy as np

iteracion=10000
valorEstimado=np.sqrt(108)

iter=[]
muestras=[]
desvios=[]

print('Procesando simulacion...')
for x in range(iteracion):
    num=random.randint(1,36)
    iter.append(x+1)
    muestras.append(num)
    desvios.append(np.std(muestras,dtype=np.float64))

print(muestras)

fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.plot(iter, [valorEstimado]*iteracion)
ax.plot(iter, desvios)

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('s (desvio estandar)')
ax.set_title('Desvio estandar de la muestra')
fig.set_facecolor('white')

plt.show()