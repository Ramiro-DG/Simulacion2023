import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import GCL
import mcm
import randu

def kolmogorov_smirnov_test(seq, gen_name):
    n = len(seq)
    seq.sort()
    dist = stats.uniform(loc=0, scale=1)
    ecdf = np.arange(1, n + 1) / n
    tcdf = dist.cdf(seq)
    d = np.max(np.abs(ecdf - tcdf))
    alpha = 0.05
    critical_value = np.sqrt(-0.5 * np.log(alpha / 2)) / np.sqrt(n)
    
    if d < critical_value:
        print(f"{gen_name} pasó el test de Kolmogorov-Smirnov")
    else:
        print(f"{gen_name} falló el test de Kolmogorov-Smirnov")

    plt.plot(seq, ecdf, label="Función de distribución empírica")
    plt.plot(seq, tcdf, label="Función de distribución teórica")
    plt.xlabel('Valores ordenados de la secuencia')
    plt.ylabel('Probabilidad')
    plt.title('Test de Kolmogorov-Smirnov para el generador {}'.format(gen_name))
    plt.legend()
    plt.show()

# Test GCL
seq_gcl = GCL.generate_sequence_numbers(1000, 742895)
kolmogorov_smirnov_test(seq_gcl, "GCL")

# Test MCM
seq_mcm = mcm.mid_square(6568, 1000)
kolmogorov_smirnov_test(seq_mcm, "MCM")

# Test Randu
seq_randu = randu.randu(1253, 1000)
kolmogorov_smirnov_test(seq_randu, "Randu")

# Test Python
seq_python = []
for _ in range(1000):
    seq_python.append(random.random())
kolmogorov_smirnov_test(seq_python, "Python3")