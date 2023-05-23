import math
import random

Q_LIMIT = 100   # Límite en la longitud de la cola.
BUSY = 1    # Indica si el servidor esté ocupado
IDLE = 0    # Indica si el servidor está inactivo

time_arrival = [0.0] * (Q_LIMIT + 1)
time_next_event = [0.0] * 3

num_in_queue_counts = [0] * (Q_LIMIT + 1)


def initialize():
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    global time_next_event
    global num_in_queue_counts, num_in_system, total_time_in_system

    global area_num_in_system
    
    # Inicializa el reloj de simulación
    sim_time = 0.0
    
    # Inicializa las variables de estado
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    
    # Inicializa los contadores estadísticos
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    # Inicializa la lista de eventos. Como no hay clientes presentes, el fin del servicio se elimina de
    # la consideración.
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30

    # Inicializa las nuevas variables extras
    num_in_queue_counts = [0] * (Q_LIMIT + 1)       # Número de clientes en cola
    num_in_system = 0                               # Número de clientes en el sistema
    area_num_in_system = 0.0                        # Área debajo de la función de clientes en el sistema
    total_time_in_system = 0.0                      # Tiempo total en el sistema


def timing():
    global next_event_type, sim_time
    
    min_time_next_event = 1.0e+29
    next_event_type = 0
    
    # Determina el siguiente tipo de evento a ocurrir
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    
    # Comprueba si la lista de eventos está vacía. Si lo está, termina la simulación
    if next_event_type == 0:
        print("\nEvent list empty at time", sim_time)
        exit(1)
    
    # Si no está vacía, se avanza el reloj de simulación
    sim_time = min_time_next_event


def arrive():
    global num_in_q, server_status, total_of_delays, num_custs_delayed, time_next_event
    global num_in_system
    
    # Programa la siguiente llegada
    time_next_event[1] = sim_time + expon(mean_interarrival)
    
    # Comprueba si el servidor está ocupado
    if server_status == BUSY:

        # Si está ocupado, aumenta el número de clientes en cola
        num_in_q += 1

        # Aumenta el número de clientes en el sistema
        num_in_system += 1
        
        # Comprueba si la cola está desbordada. Si lo está, finaliza la simulación.
        if num_in_q > Q_LIMIT:
            print("\nOverflow of the array time_arrival at time", sim_time)
            exit(2)
        
        # Hay espacio en la cola ya que no está desbordada. Luego, se almacena la hora de
        # llegada del cliente que llega al final de time_arrival
        time_arrival[num_in_q] = sim_time

    else:

        # El servidor está inactivo, el cliente que llega tiene un retraso de cero.
        delay = 0.0
        total_of_delays += delay
        
        # Incrementa el número de clientes retrasados y hace que el servidor esté ocupado.
        num_custs_delayed += 1
        server_status = BUSY
        
        # Programa una salida (fin de servicio)
        time_next_event[2] = sim_time + expon(mean_service)


def depart():
    global num_in_q, server_status, total_of_delays, num_custs_delayed, time_next_event
    global num_in_system, total_time_in_system

    # Comprueba si la cola está vacía
    if num_in_q == 0:

        # La cola está vacía: el servidor está inactivo y se elimina el evento de fin de servicio
        server_status = IDLE
        time_next_event[2] = 1.0e+30

    else:

        # La cola no está vacía: se disminuye el número de clientes en la cola
        num_in_q -= 1

        # Disminuye el número de clientes en el sistema
        if num_in_system > 0:
            num_in_system -= 1
        
        # Se calcula la demora del cliente que está iniciando el servicio y se
        # actualiza el acumulador de demora total
        delay = sim_time - time_arrival[1]
        total_of_delays += delay

        # Aumenta el tiempo total de clientes en el sistema
        total_time_in_system += delay
        
        # Incrementa el número de clientes retrasados y se programa la salida
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        
        # Mueve todos los clientes en cola (si los hay) un lugar hacia arriba
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]


def report():
    global total_of_delays, num_custs_delayed, area_num_in_q, sim_time, area_server_status
    
    # Calcula y devuelve estimaciones de medidas deseadas de rendimiento.
    print("\033[4m" + "Performance measures" + "\033[0m")
    print("verage delay in queue:", total_of_delays / num_custs_delayed, "minutes")
    print("Average number in queue:", area_num_in_q / sim_time)
    print("Server utilization:", area_server_status / sim_time)
    print("Time simulation ended:", sim_time, "minutes")

    # Nuevas variables
    print("Average number of customers in the system:", area_num_in_system / sim_time)
    print("Average time in the system:", total_time_in_system / num_custs_delayed, "minutes")
    print("\nProbability of finding n customers in the queue:")
    for n in range(Q_LIMIT + 1):
        probability = num_in_queue_counts[n] / sim_time
        if (round(probability, 3) != 0.0):
            print(f"* n = {n}: {round(probability*100, 2)}%")


def update_time_avg_stats():
    global time_last_event, area_num_in_q, area_server_status, num_in_q, server_status, sim_time
    global area_num_in_system

    # Calcula el tiempo desde el último evento y actualiza el tiempo del último evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    
    # Actualiza el área bajo la función del número en cola
    area_num_in_q += num_in_q * time_since_last_event

    # Actualiza el área bajo la función de indicador de servidor ocupado
    area_server_status += server_status * time_since_last_event

    # Actualiza el área bajo la función de números de clientes en el sistema y
    # actualiza el número de clientes en cola
    num_in_queue_counts[num_in_q] += time_since_last_event
    area_num_in_system += num_in_system * time_since_last_event


def expon(mean):
    # Devuelve una variable aleatoria exponencial con media "mean"
    return -mean * math.log(random.random())


def main():
    global num_delays_required, mean_interarrival, mean_service, num_events
    
    num_events = 2

    # Ingreso de la media de entre llegadas, la media del servicio y el número de retrasos necesarios
    mean_interarrival = float(input("Ingrese el valor de mean_interarrival: "))
    mean_service = float(input("Ingrese el valor de mean_service: "))
    num_delays_required = int(input("Ingrese el valor de num_delays_required: "))
    
    # Imprime los parámetros de entrada
    print("\n\n\n\n" + "\033[4m" + "Single-server queueing system" + "\033[0m")
    print("Mean interarrival time: {:.3f} minutes".format(mean_interarrival))
    print("Mean service time: {:.3f} minutes".format(mean_service))
    print("Number of customers: {}\n".format(num_delays_required))
    
    # Inicia la simulación
    initialize()
    
    # Ejecuta la simulación hasta que un evento de fin (de tipo 3) ocurra. 
    while num_custs_delayed < num_delays_required:
        timing()    # Determina el siguiente evento
        update_time_avg_stats() # Actualiza los acumuladores estadísticos del promedio de tiempo
        
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()
    
    report()

main()

# Faltaría:
# - Probabilidad de denegación de servicio (cola finita de tamaño: 0, 2, 5, 10, 50).
#  + Variar (al menos) las tasas de arribo: 25%, 50%, 75%, 100%, 125% con respecto a la tasa de servicio.
#  + Mínimo 10 corridas por cada experimento.