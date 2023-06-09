import numpy as np


def metodo_rechazo(pdf_estudio, techo, min, max, size):
    accepted = []
    for _ in range(size):
        x = np.random.uniform(min, max)
        prob_pass = pdf_estudio(x) / techo
        if (np.random.uniform(0, 1) <= prob_pass):
            accepted.append(x)
    return accepted


def metodo_rechazo_dicreto(mpf_estudio, techo, min, max, size):
    accepted = []
    for _ in range(size):
        x = np.random.uniform(min, max)
        x = round(x)
        prob_pass = mpf_estudio(x) / techo
        if (np.random.uniform(0, 1) <= prob_pass):
            accepted.append(x)
    return accepted
