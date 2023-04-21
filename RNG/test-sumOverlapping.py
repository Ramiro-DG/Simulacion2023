import math
import random
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

import GCL
import mcm

# Test GCL
sumas = []
window= 50
step= 20
inf=0
sup=50
seed=742895
seq = GCL.generate_sequence_numbers(1000, seed)
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
plt.plot(sumas, scipy.stats.norm.pdf(sumas, media, std), color='red', linewidth=3 )
plt.title('Test superposicion de la suma - Generador GCL')
plt.show()


## Test MCM
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
plt.plot(sumas, scipy.stats.norm.pdf(sumas, media, std), color='red', linewidth=3 )
plt.title('Test superposicion de la suma - Generador MCM')
plt.show()
