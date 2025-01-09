"""
Juego de combate contra la máquina .
"""
import random

# Métodos de las acciones
def atacar_jugador(vida_jugador, vida_enemigo, defensa_enemigo):
    if defensa_enemigo:
        print("El enemigo se ha defendido. No ha perdido vida.")
        return vida_jugador, vida_enemigo  # El enemigo no pierde vida si se defiende
    else:
        print("¡El jugador ataca al enemigo!")
        if random.choice([True, False]):  # Si el jugador ataca y el enemigo también
            vida_enemigo -= 2
            vida_jugador -= 2
            print("Ambos atacan. ¡Ambos pierden 2 vidas!")
        else:
            vida_enemigo -= 2
            print("El enemigo recibe 2 de daño por el ataque del jugador.")
        return vida_jugador, vida_enemigo

def defender_jugador(vida_jugador, vida_enemigo):
    print("El jugador se defiende.")
    return vida_jugador, vida_enemigo  # El jugador no pierde vida

def curar_jugador(vida_jugador, vida_enemigo):
    vida_jugador += 1
    print("El jugador se cura y recupera 1 vida.")
    return vida_jugador, vida_enemigo

def atacar_enemigo(vida_jugador, vida_enemigo, defensa_jugador):
    if defensa_jugador:
        print("El jugador se ha defendido. No ha perdido vida.")
        return vida_jugador, vida_enemigo
    else:
        print("¡El enemigo ataca al jugador!")
        if random.choice([True, False]):  # Si el enemigo ataca y el jugador también
            vida_jugador -= 2
            vida_enemigo -= 2
            print("Ambos atacan. ¡Ambos pierden 2 vidas!")
        else:
            vida_jugador -= 2
            print("El jugador recibe 2 de daño por el ataque del enemigo.")
        return vida_jugador, vida_enemigo

def defender_enemigo(vida_jugador, vida_enemigo):
    print("El enemigo se defiende.")
    return vida_jugador, vida_enemigo  # El enemigo no pierde vida

def curar_enemigo(vida_jugador, vida_enemigo):
    vida_enemigo += 1
    print("El enemigo se cura y recupera 1 vida.")
    return vida_jugador, vida_enemigo

# Función adicional: Golpe fuerte
def golpe_fuerte(vida_jugador, vida_enemigo, defensa_enemigo):
    if defensa_enemigo:
        print("El enemigo se ha defendido. No ha perdido vida.")
        return vida_jugador, vida_enemigo
    else:
        print("¡El jugador lanza un golpe fuerte!")
        vida_enemigo -= 4
        return vida_jugador, vida_enemigo

# Función adicional: Robo de vida
def robo_vida(vida_jugador, vida_enemigo):
    print("¡El jugador roba vida al enemigo!")
    vida_jugador += 2
    vida_enemigo -= 2
    return vida_jugador, vida_enemigo

# Función principal de combate
def combate():
    vida_jugador = 20
    vida_enemigo = 20

    while vida_jugador > 0 and vida_enemigo > 0:
        print(f"\nVida del jugador: {vida_jugador} | Vida del enemigo: {vida_enemigo}")
        
        # Entrada del jugador para decidir la acción
        accion_jugador = input("Elige tu acción (atacar, defender, curar, golpe fuerte, robo vida): ").lower()

        # Acciones del jugador
        if accion_jugador == 'atacar':
            defensa_enemigo = random.choice([True, False])  # El enemigo puede defenderse o no
            vida_jugador, vida_enemigo = atacar_jugador(vida_jugador, vida_enemigo, defensa_enemigo)
        elif accion_jugador == 'defender':
            vida_jugador, vida_enemigo = defender_jugador(vida_jugador, vida_enemigo)
        elif accion_jugador == 'curar':
            vida_jugador, vida_enemigo = curar_jugador(vida_jugador, vida_enemigo)
        elif accion_jugador == 'golpe fuerte':
            vida_jugador, vida_enemigo = golpe_fuerte(vida_jugador, vida_enemigo, random.choice([True, False]))
        elif accion_jugador == 'robo vida':
            vida_jugador, vida_enemigo = robo_vida(vida_jugador, vida_enemigo)
        else:
            print("Acción no válida. Intenta de nuevo.")
            continue
        
        # Acción del enemigo (elección aleatoria)
        accion_enemigo = random.choice(['atacar', 'defender', 'curar', 'golpe fuerte', 'robo vida'])
        print(f"El enemigo elige: {accion_enemigo}")
        
        if accion_enemigo == 'atacar':
            vida_jugador, vida_enemigo = atacar_enemigo(vida_jugador, vida_enemigo, random.choice([True, False]))
        elif accion_enemigo == 'defender':
            vida_jugador, vida_enemigo = defender_enemigo(vida_jugador, vida_enemigo)
        elif accion_enemigo == 'curar':
            vida_jugador, vida_enemigo = curar_enemigo(vida_jugador, vida_enemigo)
        elif accion_enemigo == 'golpe fuerte':
            vida_jugador, vida_enemigo = golpe_fuerte(vida_jugador, vida_enemigo, random.choice([True, False]))
        elif accion_enemigo == 'robo vida':
            vida_jugador, vida_enemigo = robo_vida(vida_jugador, vida_enemigo)
        
    # Determinamos el ganador
    if vida_jugador <= 0:
        print("\n¡Has perdido! El enemigo ha derrotado al jugador.")
    elif vida_enemigo <= 0:
        print("\n¡Has ganado! Has derrotado al enemigo.")
    else:
        print("\nEl combate ha terminado de manera inesperada.")

# Ejecutar el combate
combate()
