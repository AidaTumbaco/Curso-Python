# -*- coding: utf-8 -*-

futbolistas = {
    1: "Casillas", 15: "Ramos",
    3: "Pique", 5: "Puyol",
    11: "Capdevila", 14: "Xabi Alonso",
    16: "Busquets", 8: "Xavi Hernandez",
    18: "Pedrito", 6: "Iniesta",
    7: "Villa"
}

"""
1)	Contar el número de jugadores (elementos) en el diccionario.
"""



"""
2)	Modificar el nombre de “Casillas” por “Iker Casillas” en el diccionario.
"""


"""
3)	En el minuto 60’ del partido se realiza un cambio: entra “Navas” con el 
   dorsal 22 por “Pedrito” (dorsal 18). En el minuto 87 se realiza otro cambio: 
   entra “Fabregas” con el dorsal 10 por “Xabi Alonso” (dorsal 14). Hay que 
   eliminar del diccionario a los dos jugadores titulares y añadir a los dos 
   jugadores nuevos.
"""



"""
4)	Crear una lista con los dorsales de los jugadores que hay en el diccionario.
"""


"""
5)	Crear una lista con los nombres de los jugadores que hay en el diccionario.
"""
    
    
"""
6)	Crear una copia del diccionario “futbolistas” llamada “campeones_del_mundo”.
"""


7)	Eliminar el diccionario “futbolistas”.
"""
# Diccionario inicial
futbolistas = {
    1: "Casillas",
    15: "Ramos",
    3: "Pique",
    5: "Puyol",
    11: "Capdevila",
    14: "Xabi Alonso",
    16: "Busquets",
    8: "Xavi Hernandez",
    18: "Pedrito",
    6: "Iniesta",
    7: "Villa"
}

# 1. Contar el número de jugadores en el diccionario
num_jugadores = len(futbolistas)
print(f"El número de jugadores en el diccionario es: {num_jugadores}")

# 2. Modificar el nombre de "Casillas" por "Iker Casillas"
futbolistas[1] = "Iker Casillas"

# 3. Cambios en el minuto 60 y 87 del partido
# Entra "Navas" con dorsal 22 por "Pedrito" (dorsal 18)
del futbolistas[18]
futbolistas[22] = "Navas"

# Entra "Fabregas" con dorsal 10 por "Xabi Alonso" (dorsal 14)
del futbolistas[14]
futbolistas[10] = "Fabregas"

# 4. Crear una lista con los dorsales de los jugadores
dorsales = list(futbolistas.keys())
print(f"Dorsales de los jugadores: {dorsales}")

# 5. Crear una lista con los nombres de los jugadores
nombres = list(futbolistas.values())
print(f"Nombres de los jugadores: {nombres}")

# 6. Crear una copia del diccionario llamada "campeones_del_mundo"
campeones_del_mundo = futbolistas.copy()

# 7. Eliminar el diccionario "futbolistas"
del futbolistas

# Comprobar que el diccionario original ha sido eliminado
try:
    print(futbolistas)
except NameError:
    print("El diccionario 'futbolistas' ha sido eliminado.")

# Imprimir el diccionario "campeones_del_mundo"
print(f"Campeones del mundo: {campeones_del_mundo}")
