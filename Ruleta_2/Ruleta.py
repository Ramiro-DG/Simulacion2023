import random

# gracias chat gpt por genera esto
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16,
                 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15,
                  17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


class Color:
    ROJO = 'rojo'
    NEGRO = 'negro'


class Ruleta:
    def __init__(self, generate_number):
        self.generate_number = generate_number
        self.apuestas = []

    def apostar_numero(self, numero: int, monto: int) -> int:
        self.apuestas.append({'numeros': [numero], 'ganacia': monto*36})

    def apostar_color(self, color, monto):
        if (color == Color.ROJO):
            self.apuestas.append(
                {'numeros': numeros_rojos, 'ganacia': monto*2}
            )
        if (color == Color.NEGRO):
            self.apuestas.append(
                {'numeros': numeros_negros, 'ganacia': monto*2}
            )

    def tirar(self):
        n = self.generate_number()
        ganacia = 0
        for a in self.apuestas:
            if (n in a['numeros']):
                ganacia += a['ganacia']
        self.apuestas = []
        return ganacia


'''
EJEMPLO DE USO:
r = Ruleta(random.randint(0, 36))  # inicializo ruleta
r.apostar_numero(2, 100)  # apuesto $100 al 2
ganacia = r.tirar()  # si salio el 2 , ganacia serai 3600, sino 0

r.apostar_color(Color.ROJO, 50)  # al apostar con colores es parecido
ganacia = r.tirar()
'''
