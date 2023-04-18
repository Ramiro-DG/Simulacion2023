
def generate_number(module, multiplicator, increment, initial_seed):
    fraccion=(increment*(multiplicator-1))/(multiplicator-1)
    return (multiplicator*initial_seed+fraccion)% module

print(generate_number(2**32, 33, 20, 6666))

def generate_sequence_numbers(m, a, c, x0, n):
    secuencia=[]
    xi=generate_number(m,a,c,x0)
    secuencia.append(xi)
    for num in range(n-1):
        xi=generate_number(m,a,c,xi)
        secuencia.append(xi)
    return secuencia

print(generate_sequence_numbers(2**32, 30, 20, 6666, 5))