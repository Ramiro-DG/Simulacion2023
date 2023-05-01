import os
import distribucion_uniforme as du
import distribucion_exponencial as de
# import distribucion_gamma as dg
import distribucion_normal as dn
# import distribucion_pascal as dpa
# import distribucion_binomial as db
# import distribucion_hipergeometrica as dhg
# import distribucion_poisson as dpo
# import distribucion_empirica_discreta as ded

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Menú:")
    print("1. UNIFORME")
    print("2. EXPONENCIAL")
    print("3. GAMMA")
    print("4. NORMAL")
    print("5. PASCAL")
    print("6. BINOMIAL")
    print("7. HIPERGEOMÉTRICA")
    print("8. POISSON")
    print("9. EMPÍRICA DISCRETA")
    print("10. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    if opcion == 1:
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))

        du.uniforme(a, b, size)

    elif opcion == 2:
        lam = float(input("Ingrese valor de lamda: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        de.exponencial(lam, size)

    elif opcion == 3:
        dg.gamma()

    elif opcion == 4:
        media = float(input("Ingrese el valor de la media: "))
        sigma = float(input("Ingrese el valor de sigma: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        dn.normal(media, sigma, size)

    elif opcion == 5:
        dpa.pascal()

    elif opcion == 6:
        db.binomial()

    elif opcion == 7:
        dhg.hipergeometrica()

    elif opcion == 8:
        dpo.distribucion_poisson()

    elif opcion == 9:
        ded.empirica_discreta()

    elif opcion == 10:
        break

    else:
        print(
            "----------------------------- Opción inválida -----------------------------"
        )
        print("")
        input("Presione la tecla Enter para continuar...")