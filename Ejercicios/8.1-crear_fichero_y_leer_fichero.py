"""
Escribir, añadir y leer de fichero.
"""
import os
import random

# Crear el directorio
directorio = "mi_directorio"
if not os.path.exists(directorio):
    os.mkdir(directorio)

# Crear y escribir el fichero con números aleatorios
ruta_fichero = os.path.join(directorio, "fichero.txt")
with open(ruta_fichero, "w") as f:
    for _ in range(5):
        f.write(f"{random.randint(1, 10)}\n")

# Leer y mostrar el contenido del fichero
print("Contenido inicial del fichero:")
with open(ruta_fichero, "r") as f:
    for linea in f:
        print(linea.strip())
