import math
import random

amount = 0
bigs = 0
initial_inv_level = 0
inv_level = 0
next_event_type = 0
num_events = 0
num_months = 0
num_values_demand = 0
smalls = 0
area_holding = 0.0
area_shortage = 0.0
holding_cost = 0.0
incremental_cost = 0.0
maxlag = 0.0
mean_interdemand = 0.0
minlag = 0.0
prob_distrib_demand = []
setup_cost = 0.0
shortage_cost = 0.0
sim_time = 0.0
time_last_event = 0.0
time_next_event = [0.0] * 5
total_ordering_cost = 0.0

def initialize():
    global sim_time, inv_level, time_last_event, total_ordering_cost, area_holding, area_shortage, time_next_event

    # Inicializa el reloj de simulación
    sim_time = 0.0

    # Inicializa las variables de estado
    inv_level = initial_inv_level
    time_last_event = 0.0

    # Inicializa los contadores estadísticos
    total_ordering_cost = 0.0
    area_holding = 0.0
    area_shortage = 0.0

    # Inicializa la lista de eventos. Como no hay pedidos pendientes, el evento de llegada 
    # del pedido se elimina de la consideración
    time_next_event[1] = 1.0e+30
    time_next_event[2] = sim_time + expon(mean_interdemand)
    time_next_event[3] = num_months
    time_next_event[4] = 0.0


def order_arrival():
    global inv_level, time_next_event

    # Aumenta el nivel del inventario por la cantidad ordenada
    inv_level += amount

    # Como no hay pedidos pendientes, elimina el evento de llegada del pedido de la consideración
    time_next_event[1] = 1.0e+30


def demand():
    global inv_level, time_next_event

    # Reduce el nivel del inventario por el tamaño de una demanda generada
    inv_level -= random_integer(prob_distrib_demand)

    # Programa la hora de la siguiente demanda
    time_next_event[2] = sim_time + expon(mean_interdemand)


def evaluate():
    global inv_level, amount, total_ordering_cost, time_next_event

    # Comprueba si el nivel del inventario es menor que "smalls"
    if inv_level < smalls:

        # Como el nivel del inventario es menor a "smalls", se hace un pedido por la cantidad adecuada
        amount = bigs - inv_level
        total_ordering_cost += setup_cost + incremental_cost * amount

        # Programa la llegada del pedido
        time_next_event[1] = sim_time + uniform(minlag, maxlag)

    # Sin importar la decisión de realizar el pedido, se programa la próxima evaluación de inventario
    time_next_event[4] = sim_time + 1.0


def report():
    global area_holding, area_shortage, total_ordering_cost, num_months, smalls, bigs, holding_cost, shortage_cost

    
    # Calcula y devuelve estimaciones de medidas deseadas de rendimiento.
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    avg_ordering_cost = total_ordering_cost / num_months

    print("\n\n({}, {}){:>15.2f}{:>15.2f}{:>15.2f}{:>15.2f}".format(
        smalls, bigs, avg_ordering_cost + avg_holding_cost + avg_shortage_cost,
        avg_ordering_cost, avg_holding_cost, avg_shortage_cost))


def update_time_avg_stats():
    global sim_time, time_last_event, inv_level, area_shortage, area_holding

    # Calcula el tiempo desde el último evento y actualiza el tiempo del último evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Determina el estado del nivel del inventario durante el intervalo anterior
    # Si el nivel del inventario durante el intervalo anterior era negativo, se actualiza area_shortage
    # Si era positivo, se actualiza area_holding
    # Si era cero no se actualiza nada
    if inv_level < 0:
        area_shortage -= inv_level * time_since_last_event
    elif inv_level > 0:
        area_holding += inv_level * time_since_last_event


def expon(mean):
    # Devuelve una variable aleatoria exponencial con media "mean"
    return -mean * math.log(random.random())


def random_integer(prob_distrib):
    u = random.random()

    # Retorna un entero aleatorio de acuerdo con la función de distribución acumulativa "prob_distrib"
    i = 1
    while u >= prob_distrib[i]:
        i += 1
    return i


def uniform(a, b):
    # Función de generación de una variable uniforme. Devuelve una variable aleatoria U(a, b)
    return a + random.random() * (b - a)


def timing():
    global sim_time, next_event_type, time_next_event, num_events

    # Determina el siguiente tipo de evento y avanza el reloj de simulación
    min_time_next_event = 1.0e+30
    next_event_type = 0

    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    if next_event_type == 0:
        print("Event list empty at time {}".format(sim_time))
        exit(1)

    sim_time = min_time_next_event


def main():
    global k, prob_distrib_demand, num_events, num_policies, smalls, bigs, num_months, num_values_demand, mean_interdemand, setup_cost, incremental_cost, holding_cost, shortage_cost, minlag, maxlag

    num_events = 4
    k = 0

    # Ingreso de los parámetros de entrada
    # initial_inv_level = float(input("Ingrese el valor de initial_inv_level: "))
    # num_months = float(input("Ingrese el valor de num_months: "))
    # num_policies = float(input("Ingrese el valor de num_policies: "))
    # num_values_demand = float(input("Ingrese el valor de num_values_demand: "))
    # mean_interdemand = float(input("Ingrese el valor de mean_interdemand: "))
    # setup_cost = float(input("Ingrese el valor de setup_cost: "))
    # incremental_cost = float(input("Ingrese el valor de incremental_cost: "))
    # holding_cost = float(input("Ingrese el valor de holding_cost: "))
    # shortage_cost = float(input("Ingrese el valor de shortage_cost: "))
    # minlag = float(input("Ingrese el valor de minlag: "))
    # maxlag = float(input("Ingrese el valor de maxlag: "))
    
    # Valores de ejemplo del libro:
    initial_inv_level, num_months, num_policies, num_values_demand, mean_interdemand, setup_cost, incremental_cost, holding_cost, shortage_cost, minlag, maxlag = 60, 120, 9, 4, 0.10, 32, 3, 1, 5, 0.5, 1

    prob_distrib_demand = [0.0] * (int(num_values_demand) + 1)
    for i in range(1, int(num_values_demand) + 1):
        prob_distrib_demand[i] = float(input("Ingrese el valor de prob_distrib_demand en {}: ".format(i)))

    # Imprime los parámetros de entrada
    print("\n\n\n\n" + "\033[4m" + "Single-product inventory system" + "\033[0m")
    print("\nInitial inventory level{:>24} items".format(int(initial_inv_level)))
    print("Number of demand sizes{:>25}".format(int(num_values_demand)))
    print("Distribution function of demand sizes \t  ", end=" ")
    numbers = []
    for i in range(1, int(num_values_demand) + 1):
        numbers.append(str(prob_distrib_demand[i]))
    print("   ".join(numbers))
    print("Mean interdemand time{:>26.2f} months".format(mean_interdemand))
    print("Delivery lag range{:>29.2f} to {:.2f} months".format(minlag, maxlag))
    print("Length of the simulation{:>23} months".format(int(num_months)))
    print("K = {:.1f}    i = {:.1f}    h = {:.1f}    pi = {:.1f}".format(setup_cost, incremental_cost, holding_cost, shortage_cost))
    print("Number of policies{:>29}\n".format(int(num_policies)))
    print("              Average         Average         Average        Average")
    print("Policy       total cost    ordering cost   holding cost   shortage cost")

    # Parámetros de "smalls" y "bigs" del libro
    smallsArray = [20, 20, 20, 20, 40, 40, 40, 60, 60]
    bigsArray = [40, 60, 80, 100, 60, 80, 100, 80, 100]

    # Corre la simulación variando la política de inventario
    for i in range(1, int(num_policies) + 1):
        # Lee la política de inventario e inicializa la simulación
        smalls = smallsArray[k]
        bigs = bigsArray[k]
        initialize()

        
        # Corre la simulación hasta que ocurre un evento de fin de simulación (tipo 3)
        while True:
            timing()    # Determina el siguiente evento
            update_time_avg_stats() # Actualiza los acumuladores estadísticos del promedio de tiempo

            if next_event_type == 1:
                order_arrival()
            elif next_event_type == 2:
                demand()
            elif next_event_type == 3:
                report()
            elif next_event_type == 4:
                evaluate()
            
            if next_event_type == 3:
                break
        
        k += 1
main()