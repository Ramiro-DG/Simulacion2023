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

# Impresion de resultados
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.plot(iter,calcularDesvios(), label="Run 1" )
ax.plot(iter,calcularDesvios(), label="Run 2" )
ax.plot(iter,calcularDesvios(), label="Run 3" )
ax.plot(iter,calcularDesvios(), label="Run 4" )
ax.plot(iter, [np.sqrt(114)]*iteracion, label="Valor esperado: 10,6771")

ax.set_xlabel('n (numero de tiradas)')
ax.set_ylabel('s (desvio estandar)')
ax.set_title('Desvio estandar de la muestra')
ax.legend()
fig.set_facecolor('white')

plt.show()