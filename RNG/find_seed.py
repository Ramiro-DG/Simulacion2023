import random
# borrable

from GCL import generate_sequence_numbers
import numpy as np

best = 0
seed = 2**32
print(seed)
while True:
    seed -= 1
    arr = generate_sequence_numbers(100, seed)
    std = np.std(arr)
    mean = np.mean(arr)
    if best < std:
        best = std
        print('semilla: ', seed)
        print('desvio: ', std)
        print('media: ', mean)
    if (seed < 0):
        exit()
