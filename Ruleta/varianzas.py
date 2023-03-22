import random
import matplotlib.pyplot as plt
import numpy as np

iteraciones=1000
valorEstimado=108

iter=[]
muestras=[]
varianzas=[]

print('Procesando simulacion...')
for x in range(iteraciones):
    num=random.randint(1,36)
    iter.append(x+1)
    muestras.append(num)
    varianzas.append(np.var(muestras,dtype=np.float64))


fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.plot(iter, [valorEstimado]*iteraciones)
ax.plot(iter, varianzas)

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('s2 (varianza muestral)')
ax.set_title('Varianza de la muestra')
fig.set_facecolor('white')

plt.show()