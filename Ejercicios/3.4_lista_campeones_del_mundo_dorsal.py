# -*- coding: utf-8 -*-

futbolistas = ["1 - Casillas", "15 - Ramos", "3 - Pique", "5 - Puyol",
               "11 - Capdevila", "14 - Xabi Alonso", "16 - Busquets",
               "8 - Xavi Hernandez", "18 - Pedrito", "6 - Iniesta",
               "7 - Villa"]

"""
Se pide ordenar la lista de forma descendente por el dosal del futbolista
"""
# Lista inicial
futbolistas = [
    "1 - Casillas", "15 - Ramos", "3 - Pique", 
    "5 - Puyol", "11 - Capdevila", "14 - Xabi Alonso", 
    "16 - Busquets", "8 - Xavi Hernandez", "18 - Pedrito", 
    "6 - Iniesta", "7 - Villa"
]

# Ordenar la lista de forma descendente por el dorsal
futbolistas_ordenados = sorted(
    futbolistas,
    key=lambda x: int(x.split(" - ")[0]),  # Extraer el dorsal y convertirlo a entero
    reverse=True                           # Orden descendente
)

# Imprimir el resultado
print("Lista ordenada por dorsal de forma descendente:")
for futbolista in futbolistas_ordenados:
    print(futbolista)
