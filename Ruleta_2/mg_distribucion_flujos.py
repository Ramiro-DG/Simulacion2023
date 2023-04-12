from martin_gala_strategy import run_martingala
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

n = 200
runs = 1000


fls = []
for _ in range(runs):
    _, fl = run_martingala(n)
    fls.append(fl[n])


fig, ax = plt.subplots(1, 1)

fl_no_repetidos = sorted(list(set(fls)))
fa = {}
for value in fl_no_repetidos:
    fa[value] = 0

for value in fls:
    fa[value] += 1


ax.stem(list(fa.keys()), list(fa.values()))

mu = np.average(fls)
sigma = np.std(fls)

print('media: ', mu)
print('desvio: ', sigma)
ax.set_ylabel('frecuencia absoluta (corridas)')
ax.set_xlabel('ganancia final')
ax.set_xlim(-13000, 1000)
plt.title(
    "Frecuencias absolutas la ganacia final luego de %d tiradas - Martingala" % (n))
plt.axvline(x=mu, color='r', label="promedio")

plt.legend()
plt.show()
