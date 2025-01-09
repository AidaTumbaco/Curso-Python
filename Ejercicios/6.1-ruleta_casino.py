"""
Juego de la ruleta de casino.
"""
import random

def jugar_ruleta():
    historial = []  # Lista para almacenar el historial de partidas ganadas y perdidas
    colores = {
        "rojo": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
        "negro": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    }

    while True:
        print("Bienvenido a la ruleta de casino simplificada.")
        print("Apostar a un número del 1 al 36, o escribe 'salir' para terminar.")
        
        apuesta = input("Introduce tu apuesta (número del 1 al 36): ")
        
        if apuesta.lower() == 'salir':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        # Comprobamos que la apuesta es un número entre 1 y 36
        if not apuesta.isdigit() or int(apuesta) < 1 or int(apuesta) > 36:
            print("Por favor, introduce un número válido entre 1 y 36.")
            continue

        apuesta = int(apuesta)
        
        # Simulamos la tirada de la ruleta (0 a 36)
        resultado = random.randint(0, 36)
        if resultado == 0:
            print("La ruleta ha caído en 0. Has perdido.")
            historial.append((apuesta, "Perdido"))
        else:
            # Determinamos si el número es rojo o negro
            color = "rojo" if resultado in colores["rojo"] else "negro"
            
            if resultado == apuesta:
                print(f"¡Felicidades! La ruleta ha caído en {resultado} y has ganado.")
                historial.append((apuesta, "Ganado"))
            elif apuesta in colores[color]:
                print(f"Ha tocado el color {color}, pero no tu número. Has ganado por el color.")
                historial.append((apuesta, "Ganado por color"))
            else:
                print(f"La ruleta ha caído en {resultado} {color}. Has perdido.")
                historial.append((apuesta, "Perdido"))
        
        # Mostramos el historial de partidas
        print("\nHistorial de partidas:")
        for partida in historial:
            print(f"Número apostado: {partida[0]} - Resultado: {partida[1]}")
        print("\n")
        
# Ejecutar el juego
jugar_ruleta()
