import random
import matplotlib.pyplot as plt
import numpy as np

iteracion=10000
iter=range(1,iteracion+1)

def calcularVarianza():
    muestras=[]
    varianzas=[]
    for x in range(iteracion):
        num=random.randint(0,36)
        muestras.append(num)
        varianzas.append(np.var(muestras,dtype=np.float64))
    return varianzas


fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.plot(iter, calcularVarianza(), label="Run 1")
ax.plot(iter, calcularVarianza(), label="Run 2")
ax.plot(iter, calcularVarianza(), label="Run 3")
ax.plot(iter, calcularVarianza(), label="Run 4")
ax.plot(iter, [114]*iteracion, label="Valor esperado: 114")

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('s2 (varianza muestral)')
ax.set_title('varianza de la muestra')
ax.legend()
fig.set_facecolor('white')

plt.show()