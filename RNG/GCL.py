def generate_number_base(module, multiplicator, increment, initial_seed):
    return (multiplicator * initial_seed + increment) % module

def generate_sequence_numbers_base(m, a, c, x0, n):
    secuencia=[]
    xi=generate_number_base(m,a,c,x0)
    secuencia.append(xi)
    for num in range(n-1):
        xi=generate_number_base(m,a,c,xi)
        secuencia.append(xi)
    return secuencia

def generate_number(initial_seed):
    return generate_number_base(2**32, 134775813 , 1, initial_seed)

def generate_sequence_numbers(n, initial_seed):
    return generate_sequence_numbers_base(2**32, 134775813 , 1, initial_seed, n)

print(generate_sequence_numbers(10, 1337))