from scipy.stats import binom, nbinom
import msvcrt

def ks_test(seq, type, distr_name):
    d_positive = []
    d_negative = []
    seq.sort()

    for i in range(len(seq)):
        d_positive.append(i / len(seq) - seq[i])
        d_negative.append(seq[i] - (i - 1) / len(seq))
    
    d_max = max(max(d_positive), max(d_negative))
    
    if type(type) is type(binom):
        k = binom.ppf(1 - 0.05 / 2, len(seq))
    elif type(type) is type(nbinom):
        k = nbinom.ppf(1 - 0.05 / 2, len(seq))
    else:
        k = type.ppf(1 - 0.05 / 2, len(seq))

    print("\n\n" + "\033[4m" + "Resultado del test:" + "\033[0m")
    if d_max < k:
        print("La distribución", distr_name, "pasó la prueba.")
    else:
        print("La distribución", distr_name, "falló la prueba.")

    print("\n" + "\x1B[3m" + "Presione una tecla para continuar..." + "\x1B[0m")
    msvcrt.getch()