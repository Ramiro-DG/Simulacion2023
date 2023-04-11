import sys
from Ruleta import Ruleta, Color


def assert_condition(condition, desc):
    try:
        assert condition, desc
        print('\033[32m', 'Passed: ', desc, '✅', '\033[0m')  # texto verde
    except AssertionError as e:
        print('\033[31m', 'FAILED: ', e, '❌', '\033[0m')  # texto rojo
        sys.exit()
# ----------------------------------------------------------------


test_desc = 'apuesta $10 al 2 y sale el 2, deberia ganar $360'
r = Ruleta(lambda: 2)
r.apostar_numero(2, 10)
assert_condition(r.tirar() == 360, test_desc)

test_desc = 'apuesta $10 al 2 y sale el 10, no deberia ganar nada'
r = Ruleta(lambda: 14)
r.apostar_numero(2, 10)
assert_condition(r.tirar() == 0, test_desc)

test_desc = 'apuesta $100 al 3 y $200 al 5, sale el 3, deberia ganar $3600'
r = Ruleta(lambda: 3)
r.apostar_numero(3, 100)
r.apostar_numero(5, 200)
assert_condition(r.tirar() == 3600, test_desc)

test_desc = 'apuesta $20 al 7 y $30 al 7 devuelta, sale el 7, deberia ganar $1800'
r = Ruleta(lambda: 7)
r.apostar_numero(7, 20)
r.apostar_numero(7, 30)
assert_condition(r.tirar() == 1800, test_desc)


test_desc = 'apuesta $50 al negro y  $50 al rojo, gana $100'
r = Ruleta(lambda: 3)
r.apostar_color(Color.ROJO, 50)
r.apostar_color(Color.NEGRO, 50)
assert_condition(r.tirar() == 100, test_desc)

test_desc = 'apuesta $10 al rojo y sale el 3(rojo), deberia ganar $20'
r = Ruleta(lambda: 3)
r.apostar_color(Color.ROJO, 10)
assert_condition(r.tirar() == 20, test_desc)

test_desc = 'apuesta $10 al negro y sale el 3(rojo), no deberia ganar nada'
r = Ruleta(lambda: 3)
r.apostar_color(Color.NEGRO, 10)
assert_condition(r.tirar() == 0, test_desc)

test_desc = 'apuesto $10 a docena 2, deberia ganar $30'
r = Ruleta(lambda: 3)
r.apostar_docena(1, 10)
assert_condition(r.tirar() == 30, test_desc)

test_desc = 'apuesto $10 a docena 2 y $10 al rojo, deberia ganar $50'
r = Ruleta(lambda: 3)
r.apostar_docena(1, 10)
r.apostar_color(Color.ROJO, 10)
assert_condition(r.tirar() == 50, test_desc)

test_desc = 'apuesto $10 a columna 1, deberia ganar $30'
r = Ruleta(lambda: 1)
r.apostar_columna(1, 10)
assert_condition(r.tirar() == 30, test_desc)


test_desc = 'apuesto $10 a columna 2 y $20 al rojo, sale el 5(rojo), deberia ganar $70'
r = Ruleta(lambda: 5)
r.apostar_columna(2, 10)
r.apostar_color(Color.ROJO, 20)
assert_condition(r.tirar() == 70, test_desc)


test_desc = 'si en la segunda tirada no apuesta no deberia ganar nada'
r = Ruleta(lambda: 15)
r.apostar_numero(15, 5000000)
r.apostar_color(Color.NEGRO, 50000)
primera = r.tirar()
segunda = r.tirar()
assert_condition(segunda == 0, test_desc)
print("\033[1;32mEverything passed 👏\033[0m")
