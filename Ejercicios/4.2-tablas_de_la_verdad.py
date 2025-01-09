"""
Crea un programa que cree las tablas de la verdad AND y OR.
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

# Llamar a la función principal
tabla_verdad()
