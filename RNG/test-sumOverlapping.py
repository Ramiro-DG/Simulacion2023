import math
import random
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

import GCL
import mcm
import randu

n=1000

# Test GCL
sumas = []
window= 50
step= 20
inf=0
sup=50
seed=742895
seq = GCL.generate_sequence_numbers(n, seed)
while(sup<=1000):
    acumulador = 0
    for n in range(inf, sup+1):
        acumulador+= seq[n]
    sumas.append(acumulador)
    inf+=step
    sup+=step
sumas.sort()
media = np.average(sumas)
std=np.std(sumas)
z= (max(sumas)-media)/std
plt.plot(sumas, scipy.stats.norm.pdf(sumas, media, std), color='red', linewidth=3 )
plt.title('Test superposicion de la suma - Generador GCL')
plt.show()


# Test MCM
sumas = []
window= 50
step= 20
inf=0
sup=50
seed=1232
seq = mcm.mid_square(seed,1000)
while(sup<=1000):
    acumulador = 0
    for n in range(inf, sup+1):
        acumulador+= seq[n]
    sumas.append(acumulador)
    inf+=step
    sup+=step
sumas.sort()
media = np.average(sumas)
std=np.std(sumas)
z= (max(sumas)-media)/std
plt.plot(sumas, scipy.stats.norm.pdf(sumas, media, std), color='red', linewidth=3 )
plt.title('Test superposicion de la suma - Generador MCM')
plt.show()

# Test Randu
sumas = []
window= 50
step= 20
inf=0
sup=50
seed=1232
seq = randu.randu(1253,1000);
while(sup<=1000):
    acumulador = 0
    for n in range(inf, sup+1):
        acumulador+= seq[n]
    sumas.append(acumulador)
    inf+=step
    sup+=step
sumas.sort()
media = np.average(sumas)
std=np.std(sumas)
z= (max(sumas)-media)/std
plt.plot(sumas, scipy.stats.norm.pdf(sumas, media, std), color='red', linewidth=3 )
plt.title('Test superposicion de la suma - Generador Randu')
plt.show()


## Para concluir que la distrubución es uniforme habrá que comprobar si el valor de Z está entre [-1.95, 1.95]