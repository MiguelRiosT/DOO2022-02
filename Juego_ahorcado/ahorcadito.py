import random
import time

#HOLA PANA MIGUEL Y MELANIE <3

# Listas de Palabras
dificil = ['construccion', 'polimorfismo']
medio = ['panadero', 'artesano']
facil = ['oro', 'pan', 'pie', 'casa']

print("-------BIENVENIDO AL AHORCADITO-------")

while True:
    juego = input(" J -- JUGAR\n A -- ADMINISTRAR\n E -- SALIR\n ")
    
    
    #EN CASO DE A - ADMINISTRAR
    if juego.lower() == "a":
        print("-------BIENVENIDO ADMINISTRADOR-------")
        choise_admin = input(" 1 -- Modificar VIDAS\n 2 -- Modificar PUNTOS\n 3 -- Modificar BONUS\n 4 -- Modificar PALABRAS\n 5 -- SALIR\n")
        
        # 1 - MODIFICAR VIDAS
        if choise_admin == 1:
            print("Seleccione el modo al que desea cambiar las VIDAS")
            modo = input(" D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
            
            if modo.lower() == "d":
                cambio_vida=input("¿Cuantas vidas desea poner en DIFICIL?")
                VIDASD=cambio_vida
                break
            if modo.lower() == "m":
                cambio_vida=input("¿Cuantas vidas desea poner en MEDIO?")
                VIDASM=cambio_vida
                break
            if modo.lower() == "f":
                cambio_vida=input("¿Cuantas vidas desea poner en FACIL?")
                VIDASF=cambio_vida
                break

        # 2 - MODIFICAR PUNTOS
        if choise_admin == 2:
            print("Seleccione el modo al que desea cambiar las PUNTOS")
            modo = input(" D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
            if modo.lower() == "d":
                print("")
                break
            if modo.lower() == "m":
                print("")
                break
            if modo.lower() == "f":
                print("")
                break

        # 3 - MODIFICAR BONUS
        if choise_admin == 3:
            print("Seleccione el modo al que desea cambiar las BONUS")
            modo = input(" D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
            if modo.lower() == "d":
                print("")
                break
            if modo.lower() == "m":
                print("")
                break
            if modo.lower() == "f":
                print("")
                break

        # 4 - MODIFICAR PALABRAS
        if choise_admin == 4:
            print("Seleccione el modo al que desea cambiar las PALABRAS")
            if modo.lower() == "d":
                print("1 -- CAMBIAR PALABRA EN DIFICIL \n 2 -- PALABRAS DEFAULT") 
                break
            if modo.lower() == "m":
                print("CAMBIAR PALABRA EN MEDIO \n 2 -- PALABRAS DEFAULT") 
                break
            if modo.lower() == "f":
                print("CAMBIAR PALABRA EN FACIL \n 2 -- PALABRAS DEFAULT") 
                break
        # 5 - SALIR
        elif choise_admin == 5:
            print("Fin del juego")
            break
            
    else:
        print("INGRESE OPCION VALIDA")
        juego = input(" J -- JUGAR\n A -- ADMINISTRAR\n E -- SALIR\n ")



    #EN CASO DE J - JUEGO
    if juego.lower() == "j":
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
        puntosFacil = 1
        puntosDificil = 3
        puntosMedio = 2

        puntos = 3

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

            #SISTEMA DE BONOS
            if letras_faltantes == 0:
                print("Felicidades has ganado")
                if VIDASD == vidas:
                    puntos = 5
                    print("Su puntaje fue: " + str(puntos))
                    break
                elif VIDASM == vidas:
                    puntos = 3
                    print("Su puntaje fue: " + str(puntos))
                    break
                elif VIDASF == vidas:
                    puntos = 2
                    print("Su puntaje fue: " + str(puntos))
                    break

                print("La palabra secreta es: " + palabra_secreta)
                break

    elif juego.lower() == "e":
        print("Fin del juego")
        break
    else:
        print("INGRESE MODO CORRECTO")
        juego = input(" J -- JUGAR\n A -- ADMINISTRAR\n E -- SALIR\n ")
