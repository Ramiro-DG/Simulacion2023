import math
import random
import numpy as np
import matplotlib.pyplot as plt

import GCL


def bitmap_of_array(arr, title):
    matrix = []
    fila_aux = []
    lado = int(math.sqrt(len(arr)))
    for i in range(lado):
        for j in range(lado):
            if arr[lado*i+j] > 0.5:
                fila_aux.append(1)
            else:
                fila_aux.append(0)
        matrix.append(fila_aux)
        fila_aux = []

    fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

    cmap = plt.cm.binary
    plt.imshow(matrix, cmap=cmap)
    plt.axis('off')
    plt.title(title)
    plt.show()

# ----------------------------------------------------------------


lado_bitmap = 2000

bitmap_of_array(GCL.generate_sequence_numbers(lado_bitmap**2, 742895), 'GCL')

arr = []
for _ in range(lado_bitmap**2):
    arr.append(random.random())
bitmap_of_array(arr, 'python rand')
