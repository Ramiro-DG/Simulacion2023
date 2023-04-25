import math
import random
import numpy as np
import matplotlib.pyplot as plt

import GCL
import mcm
import randu


def bitmap_of_array(arr, title):
    matrix = []
    fila_aux = []
    lado = int(math.sqrt(len(arr)))
    for i in range(lado):
        for j in range(lado):
            if arr[lado * i + j] < 0.5:
                fila_aux.append(0)
            else:
                fila_aux.append(1)
        matrix.append(fila_aux)
        fila_aux = []

    fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

    cmap = plt.cm.binary
    plt.imshow(matrix, cmap=cmap)
    plt.axis('off')
    plt.title(title)
    plt.show()


# ----------------------------------------------------------------

lado_bitmap = 1000

bitmap_of_array(GCL.generate_sequence_numbers(lado_bitmap**2, 742895), 'GCL')

bitmap_of_array(randu.randu(1253, lado_bitmap**2), 'Randu')

arr = []
for _ in range(lado_bitmap**2):
    arr.append(random.random())
bitmap_of_array(arr, 'Generador de python3')

bitmap_of_array(mcm.mid_square(6568, lado_bitmap**2), "MCM")
