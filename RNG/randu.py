
import numpy as np

def randu(seed,n):
  values = np.empty(n)
  final_values = np.empty(n)
  values[0] = seed
  final_values[0] = values[0] / (2 ** 31 - 1)
  for i in range(1, n):
      values[i] = ((2 ** 16 + 3) * values[i - 1]) % (2 ** 31)
      final_values[i] = values[i] / (2 ** 31 )
  return final_values

