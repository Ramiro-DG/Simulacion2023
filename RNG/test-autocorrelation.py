import numpy as np
import matplotlib.pyplot as plt
import random
import GCL
import mcm
import randu

def autocorrelation_test(seq, nombre):
    acf = np.correlate(seq, seq, mode='full')
    acf = acf[len(acf)//2:]
    acf = acf / float(acf[0])
    
    # Plot
    fig, ax = plt.subplots()
    ax.stem(acf, use_line_collection=True)
    ax.set_xlabel('Retraso')
    ax.set_ylabel('Autocorrelación')
    ax.set_title('Test de autocorrelación para el generador {}'.format(nombre))
    plt.show()


# Test GCL
seq_gcl = GCL.generate_sequence_numbers(1000, 742895)
autocorrelation_test(seq_gcl, "GCL")

# Test MCM
seq_mcm = mcm.mid_square(6568, 1200)
autocorrelation_test(seq_mcm, "MCM")

# Test Randu
seq_randu = randu.randu(1253,1000)
autocorrelation_test(seq_randu, "Randu")

# Test Python
seq_python = []
for _ in range(1000):
    seq_python.append(random.random())
autocorrelation_test(seq_python, "Python3")