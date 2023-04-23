import numpy as np
from scipy.stats import chisquare
import GCL
import mcm
import randu

def chi_squared_test(data, num_bins):
    observed, bins = np.histogram(data, bins=num_bins)
    expected = np.ones(num_bins) * len(data) / num_bins
    _, p_value = chisquare(observed, expected)
    return p_value




# numeros_aleatorios = mcm.mid_square2(9731, 100)



# Test GCL
seq_gcl = GCL.generate_sequence_numbers(1000, 742895)
p_gcl = chi_squared_test(seq_gcl, 10)
print('Valor de p para secuencia generada con GLC: ', p_gcl)

# Test MCM
seq_mcm = mcm.mid_square_no_div(9731, 100)
p_mcm = chi_squared_test(seq_mcm, 10)
print('Valor de p para secuencia generada con MCM: ', p_mcm)

# Test Randu
seq_randu = randu.randu(1253,1000);
p_randu = chi_squared_test(seq_randu, 10)
print('Valor de p para secuencia generada con Randu: ', p_randu)