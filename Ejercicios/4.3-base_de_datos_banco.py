"""
Crear una base de datos para guardar dinero de nuestros usuarios.
"""

# Generar la tabla de verdad para AND y OR
def tabla_verdad():
    a = True
    b = True
    ultima_iteracion = False

    print("Tabla de la verdad AND")
    print("A\tB\tA AND B")
    while not ultima_iteracion:
        # Imprimir resultado de AND
        print(f"{a}\t{b}\t{a and b}")

        # Actualizar valores de a y b
        if a and b:
            b = False
        elif a and not b:
            a = False
            b = True
        else:
            ultima_iteracion = True

    # Reiniciar variables para la tabla OR
    a = True
    b = True
    ultima_iteracion = False

    print("\nTabla de la verdad OR")
    print("A\tB\tA OR B")
    while not ultima_iteracion:
        # Imprimir resultado de OR
        print(f"{a}\t{b}\t{a or b}")

        # Actualizar valores de a y b
        if a and b:
            b = False
        elif a and not b:
            a = False
            b = True
        else:
            ultima_iteracion = True

# Programa para gestionar la base de datos de dinero de los usuarios
def gestionar_dinero():
    base_datos = {}

    while True:
        nombre = input("Introduce el nombre del usuario (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            print("Saliendo del programa...")
            break

        try:
            dinero = float(input("Introduce el dinero (positivo o negativo): "))
        except ValueError:
            print("Por favor, introduce un valor numérico válido.")
            continue

        if nombre in base_datos:
            base_datos[nombre] += dinero
        else:
            base_datos[nombre] = dinero

        print("Estado actual de la base de datos:")
        for usuario, saldo in base_datos.items():
            print(f"{usuario}: {saldo:.2f}")

# Llamar a las funciones principales
tabla_verdad()
gestionar_dinero()
