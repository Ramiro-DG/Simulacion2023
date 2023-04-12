from tau_strategy import run_todo_a_uno
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

n = 500
runs = 30000


fls = []
for _ in range(runs):
    _, fl = run_todo_a_uno(n)
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
plt.axvline(x=mu, color='r')
plt.axvline(x=mu+sigma, color='y')
plt.axvline(x=mu-sigma, color='y')
plt.axvline(x=mu+2*sigma, color='g')
plt.axvline(x=mu-2*sigma, color='g')


plt.show()
