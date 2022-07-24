import random
import time

#HOLA PANA MIGUEL Y MELANIE <3

# Listas de Palabras
dificil = ['construccion', 'polimorfismo']

medio = ['panadero', 'artesano']

facil = ['oro', 'pan', 'pie', 'casa']

juego = input(
    "Ingresa J para jugar, si eres admin preciona A, si no desea jugar preciona E ")

while True:
    if juego.lower() == "j":
        print("--- Ahorcadito ---")
        time.sleep(1)

        print("tienes 6 vidas, pierdes una vida cada que te equivocas si te quedas sin vidas pierdes ")
        time.sleep(1)

        print("Desea jugar en modo dificil, medio o facil ")
        time.sleep(1)

        cat_seleccionada = input(
            "Ingrese D para el modo dificil, M para el modo medio, F para el modo facil: ")

        while True:
            if cat_seleccionada.lower() == "d":
                print("Genial haz seleccionado el modo dificil")
                palabra_secreta = random.choice(dificil)
                vidas = 8
                break
            elif cat_seleccionada.lower() == "m":
                print("Genial haz seleccionado el modo medio")
                palabra_secreta = random.choice(medio)
                vidas = 6
                break
            elif cat_seleccionada.lower() == "f":
                print("Genial haz seleccionado el modo facil")
                palabra_secreta = random.choice(facil)
                vidas = 4
                break

            else:
                print("Por favor no sea manco seleccione un modo correcto")
                cat_seleccionada = input(
                    "Ingrese D para el modo dificil, M para el modo medio, F para el modo facil: ")

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
                            print("Te haz equivocado y perdido una vida")
                            print("Te quedan " + str(vidas) + " vidas")
                            break

            if vidas == 0:
                print("Haz perdido la palabra secreta era: " + palabra_secreta)
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

            if letras_faltantes == 0:
                print("Felicidades haz ganado")
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
        print("Por favor no sea manco seleccione un modo correcto")
        juego = input("Ingresa J para jugar, si eres admin preciona A, si no desea jugar preciona E")
