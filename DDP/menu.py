import os
import metodoTransfInversa.distribucion_uniforme as ti_du
import metodoTransfInversa.distribucion_exponencial as ti_de
import metodoTransfInversa.distribucion_normal as ti_dn
import metodoRechazo.exponencial as r_de
import metodoRechazo.poisson as r_dp
import metodoRechazo.normal as r_dn
import metodoRechazo.binomial as r_db
import metodoRechazo.uniforme as r_du
import metodoRechazo.gamma as r_dg
import metodoRechazo.pascal as r_pas
import metodoRechazo.hipergeometrica as r_dh
import metodoRechazo.empiricaDiscreta as r_ded

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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Métodos:")
        print("1. Transformada Inversa")
        print("2. Rechazo y aceptación")
        method = int(input("Ingrese método a aplicar: "))
        if method == 1:
            ti_du.uniforme(a, b, size)
        elif method == 2:
            r_du.uniforme()

    elif opcion == 2:
        lam = float(input("Ingrese valor de lamda: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Métodos:")
        print("1. Transformada Inversa")
        print("2. Rechazo y aceptación")
        method = int(input("Ingrese método a aplicar: "))
        if method == 1:
            ti_de.exponencial(lam, size)
        if method == 2:
            r_de.exponencial(lam, size)

    elif opcion == 3:
        k = float(input("Ingrese valor de k: "))
        theta = float(input("Ingrese valor de theta: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        print("Métodos:")
        print("1. Transformada Inversa")
        print("2. Rechazo y aceptación")
        method = int(input("Ingrese método a aplicar: "))
        if method == 1:
            print('mmmmmmm mepa que no impementaron esto')
        if method == 2:
            r_dg.gamma(k, theta, size)

    elif opcion == 4:
        media = float(input("Ingrese el valor de la media: "))
        sigma = float(input("Ingrese el valor de sigma: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Métodos:")
        print("1. Transformada Inversa")
        print("2. Rechazo y aceptación")
        method = int(input("Ingrese método a aplicar: "))
        if method == 1:
            ti_dn.normal(media, sigma, size)
        if method == 2:
            r_dn.normal(media, sigma, size)

    elif opcion == 5:
        r_pas.pascal()

    elif opcion == 6:
        n = int(input("Ingrese el valor de la n: "))
        p = float(input("Ingrese el valor de p: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Métodos:")
        print("1. Transformada Inversa")
        print("2. Rechazo y aceptación")
        method = int(input("Ingrese método a aplicar: "))
        if method == 1:
            print('nop')
            #ti_db.biomial(n, p, size)
        if method == 2:
            r_db.binomial(n, p, size)
        r_db.binomial()

    elif opcion == 7:
        r_dh.hipergeometrica()

    elif opcion == 8:
        lam = float(input("Ingrese valor de lamda: "))
        size = int(input("Ingrese la cantidad de valores a generar: "))
        r_dp.poisson(lam, size)

    elif opcion == 9:
        r_ded.empirica_discreta()

    elif opcion == 10:
        break

    else:
        print(
            "----------------------------- Opción inválida -----------------------------"
        )
        print("")
        input("Presione la tecla Enter para continuar...")