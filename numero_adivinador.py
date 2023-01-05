import random

def adivina_el_numero():
    print("===================================")
    print("!Bienvenido(a) al juego de adivinar el número!")
    print("===================================")
    print("Tu meta es adivinar el número generado por la computadora en el menor número de intentos posible.")

    numero_aleatorio = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    numero_de_intentos = 0  # Inicializa el contador de intentos en 0

    # Bucle principal del juego
    while True:
        prediccion = int(input("Adivina un número entre 1 y 100: "))  # Pide al usuario que adivine un número
        numero_de_intentos += 1  # Incrementa el contador de intentos en 1

        # Comprueba si la predicción es correcta
        if prediccion == numero_aleatorio:
            print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente en {numero_de_intentos} intentos.")
            break  # Sal del bucle
        elif prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        else:  # prediccion > numero_aleatorio
            print("Intenta otra vez. Este número es muy grande.")

adivina_el_numero()

