"""
Sistema de registros de un cajero automático.
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

# Programa para clasificar futbolistas según dorsal
futbolistas = [
    "1 - Casillas", "15 - Ramos", "3 - Pique", 
    "5 - Puyol", "11 - Capdevila", "14 - Xabi Alonso", 
    "16 - Busquets", "8 - Xavi Hernandez", "18 - Pedrito", 
    "6 - Iniesta", "7 - Villa"
]

a, b, pares, impares = {}, [], [], []

for jugador in futbolistas:
    dorsal, nombre = jugador.split(" - ")
    dorsal = int(dorsal)
    if dorsal % 2 == 0:
        pares.append({dorsal: nombre})
    else:
        impares.append(nombre)

# Ordenar impares por nombre
impares.sort()

# Generar pares_al_reves
pares_al_reves = {nombre: dorsal for jugador in pares for dorsal, nombre in jugador.items()}

print("Pares:", pares)
print("Impares ordenados:", impares)
print("Pares al reves:", pares_al_reves)

# Método para registrar movimientos en el cajero automático
def registrar_movimiento(fecha, concepto, cantidad=0, movimiento="Domiciliación"):
    if cantidad < 0:
        print(f"{fecha} - {concepto} - {cantidad} - {movimiento} - Déficit")
    else:
        print(f"{fecha} - {concepto} - {cantidad} - {movimiento}")

# Ejemplo de uso del método
registrar_movimiento("2025-01-09", "Pago de factura", -50)
registrar_movimiento("2025-01-10", "Ingreso mensual", 1000, "Transferencia")
registrar_movimiento("2025-01-11", "Compra supermercado")
registrar_movimiento("2025-01-12", "Recibo luz", -75, "Domiciliación")

# Llamar a las funciones principales
tabla_verdad()
gestionar_dinero()
