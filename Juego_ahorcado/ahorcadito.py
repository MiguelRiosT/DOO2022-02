import random
import time

# HOLA PANA MIGUEL Y MELANIE <3

# Listas de Palabras
dificil = ['construccion', 'polimorfismo']
medio = ['panadero', 'artesano']
facil = ['oro', 'pan', 'pie', 'casa']

print("-------BIENVENIDO AL AHORCADITO-------")

while True:
    juego = input(" J -- JUGAR\n A -- ADMINISTRAR\n E -- SALIR\n ")

    # EN CASO DE A - ADMINISTRAR
    if juego.lower() == "a":
        print("-------BIENVENIDO ADMINISTRADOR-------")
        time.sleep(1)
        #choise_admin = int(input(" 1 -- Modificar VIDAS\n 2 -- Modificar PUNTOS\n 3 -- Modificar BONUS\n 4 -- Modificar PALABRAS\n 5 -- SALIR\n"))
        while True:
            choise_admin = int(input(
                " 1 -- Modificar VIDAS\n 2 -- Modificar PUNTOS\n 3 -- Modificar BONUS\n 4 -- Modificar PALABRAS\n 5 -- SALIR\n"))
            # 1 - MODIFICAR VIDAS
            if choise_admin == 1:
                print("Seleccione el modo al que desea cambiar las VIDAS")
                cat_seleccionada = input(
                    " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")

                if cat_seleccionada.lower() == "d":
                    cambio_vida = input(
                        "¿Cuantas vidas desea poner en DIFICIL?")
                    VIDASD = cambio_vida
                    break
                elif cat_seleccionada.lower() == "m":
                    cambio_vida = input("¿Cuantas vidas desea poner en MEDIO?")
                    VIDASM = cambio_vida
                    break
                elif cat_seleccionada.lower() == "f":
                    cambio_vida = input("¿Cuantas vidas desea poner en FACIL?")
                    VIDASF = cambio_vida
                    break
                else:
                    print("Por favor no sea manco seleccione un modo correcto")
                    cat_seleccionada = input(
                        "Ingrese D para el modo DIFICIL, M para el modo MEDIO, F para el modo FACIL: ")

            # 2 - MODIFICAR PUNTOS
            elif choise_admin == 2:
                print("Seleccione el modo al que desea cambiar las PUNTOS")
                cat_seleccionada = input(
                    " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
                if cat_seleccionada.lower() == "d":
                    print("")
                    break
                elif cat_seleccionada.lower() == "m":
                    print("")
                    break
                elif cat_seleccionada.lower() == "f":
                    print("")
                    break

            # 3 - MODIFICAR BONUS
            elif choise_admin == 3:
                print("Seleccione el modo al que desea cambiar las BONUS")
                cat_seleccionada = input(
                    " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
                if cat_seleccionada.lower() == "d":
                    print("")
                    break
                if cat_seleccionada.lower() == "m":
                    print("")
                    break
                if cat_seleccionada.lower() == "f":
                    print("")
                    break

            # 4 - MODIFICAR PALABRAS
            elif choise_admin == 4:
                print("Seleccione el modo al que desea cambiar las PALABRAS")
                if cat_seleccionada.lower() == "d":
                    print("1 -- CAMBIAR PALABRA EN DIFICIL \n 2 -- PALABRAS DEFAULT")
                    break
                elif cat_seleccionada.lower() == "m":
                    print("CAMBIAR PALABRA EN MEDIO \n 2 -- PALABRAS DEFAULT")
                    break
                elif cat_seleccionada.lower() == "f":
                    print("CAMBIAR PALABRA EN FACIL \n 2 -- PALABRAS DEFAULT")
                    break
            # 5 - SALIR
            elif choise_admin == 5:
                print("Fin del juego")
                break
            else:
                print("ojo modo incorrecttttt")
                exit()

    # EN CASO DE J - JUEGO
    elif juego.lower() == "j":
        print("-------AHORCADITO-------\n")
        time.sleep(1)

        print("Tienes 6 vidas, pierdes una vida cada que te equivocas, si te quedas sin vidas PIERDES ")
        time.sleep(1)

        print("Modalidad de juego")
        time.sleep(1)

        cat_seleccionada = input(
            " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")

        while True:
            if cat_seleccionada.lower() == "d":
                print("Genial has seleccionado el modo DIFICIL")
                palabra_secreta = random.choice(dificil)
                vidas = 8
                break
            elif cat_seleccionada.lower() == "m":
                print("Genial has seleccionado el modo MEDIO")
                palabra_secreta = random.choice(medio)
                vidas = 6
                break
            elif cat_seleccionada.lower() == "f":
                print("Genial has seleccionado el modo FACIL")
                palabra_secreta = random.choice(facil)
                vidas = 4
                break

            else:
                print("Por favor no sea manco seleccione un modo correcto")
                cat_seleccionada = input(
                    "Ingrese D para el modo DIFICIL, M para el modo MEDIO, F para el modo FACIL: ")

        VIDASD = 8
        VIDASM = 6
        VIDASF = 4
        puntosb = 0
        puntosn = 0

        lista_letras_adivinadas = []

        # Imprimimos la palabra sin letras
        print('_' * len(palabra_secreta))

        while True:

            while True:
                letra_adivinada = input("Adivina una letra: ")
                if(len(letra_adivinada) != 1 and letra_adivinada.isnumeric()):
                    print("Eso no es una letra intenta con una sola letra")
                else:
                    if letra_adivinada.lower() in lista_letras_adivinadas:
                        vidas = vidas-1
                        print(
                            "Ya habias intentado con esa letra intenta con otra por favor")
                    else:
                        lista_letras_adivinadas.append(letra_adivinada)

                        if letra_adivinada.lower() in palabra_secreta:
                            print("Felicidades adivinaste una letra")
                            break
                        else:
                            vidas = vidas-1
                            print("Te has equivocado PIERDES una VIDA")
                            print("Te quedan " + str(vidas) + " VIDAS")
                            break

            if vidas == 0:
                print("Has perdido la palabra secreta era: " + palabra_secreta)
                break

            estatus_actual = ""

            letras_faltantes = 0
            for letra in palabra_secreta:

                if letra in lista_letras_adivinadas:
                    estatus_actual = estatus_actual + letra

                else:
                    estatus_actual = estatus_actual + "_"
                    letras_faltantes = letras_faltantes + 1

            # Imprimir palabra con algunas letras
            print(estatus_actual)

            # SISTEMA DE BONOS Y PUNTOS
            if letras_faltantes == 0:
                print("Felicidades has ganado")
                print("Las vidas que te quedaron fueron: "+str(vidas))
                if vidas < VIDASD and vidas>VIDASM:
                    puntosn = 3
                    print("Su puntaje final fue: "+str(puntosn))
                    if vidas == 0:
                        puntosn = 0
                        print("Su puntaje final fue: "+str(puntosn))
                        break
                if vidas < VIDASM and vidas>VIDASF:
                    puntosn = 2
                    print("Su puntaje final fue: "+str(puntosn))
                    if vidas == 0:
                        puntosn = 0
                        print("Su puntaje final fue: "+str(puntosn))
                        break
                if vidas < VIDASF and vidas <= 4:
                    puntosn = 1
                    print("Su puntaje final fue: "+str(puntosn))
                    if vidas == 0:
                        puntosn = 0
                        print("Su puntaje final fue: "+str(puntosn))
                        break
                if VIDASD == vidas:
                    puntosb = 5
                    print("Su puntaje con bono fue de: " + str(puntosb))
                    break
                elif VIDASM == vidas:
                    puntosb = 3
                    print("Su puntaje con bono fue de: " + str(puntosb))
                    break
                elif VIDASF == vidas:
                    puntosb = 2
                    print("Su puntaje con bono fue de: " + str(puntosb))
                    break

                print("La palabra secreta es: " + palabra_secreta)
                break
    # EN CASO DE SALIR
    elif juego.lower() == "e":
        print("Fin del juego")
        break
    else:
        print("INGRESE MODO CORRECTO")
        juego = input(" J -- JUGAR\n A -- ADMINISTRAR\n E -- SALIR\n ")
