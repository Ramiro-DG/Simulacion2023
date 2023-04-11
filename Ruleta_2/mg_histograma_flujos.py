from martin_gala_strategy import run_martingala
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

n = 5000
runs = 2000


fls = []
for i in range(runs):
    i, _, fl, _ = run_martingala(n)
    fls.append(fl[-1])


n_bins = int((max(fls)-min(fls))/10000)
print(n_bins)
fig, ax = plt.subplots(1, 1)

n, bins, _ = ax.hist(fls, bins=n_bins, density=True)

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
