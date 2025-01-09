"""
Pregunta al usuario por pantalla el índice del listado de frutas y capturar excepciones.
"""
# Listado de frutas
frutas = ["Manzana", "Plátano", "Cereza", "Naranja", "Uva"]

# Pedir al usuario el índice
try:
    indice = int(input("Introduce el índice de la fruta que deseas ver (0-4): "))
    
    # Comprobar si el índice está dentro del rango
    if 0 <= indice < len(frutas):
        print(f"La fruta en el índice {indice} es: {frutas[indice]}")
    else:
        print("El índice está fuera del rango. Debes elegir un valor entre 0 y 4.")
        
except ValueError:
    print("Error: Debes introducir un número entero válido.")
except IndexError:
    print("Error: El índice proporcionado no es válido.")
