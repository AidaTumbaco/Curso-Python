"""
Se da el siguiente listado:
"""
lista_de_inicio = [
    "fruta y verduras",
    "carnes y pescados",
    "lácteos y huevos",
    "dulces y pan",
    "hogar y jardín",
    "cuidado y limpieza"
]

"""
Imprime la longitud del listado
"""


"""
Elimina el elemento "hogar y jardín" (pista: usa la posición)
"""


"""
Inserta en el listado el elemento: "entretenimiento y deportes"
"""


"""
Imprime por pantalla cada uno de los elementos (por posición) 
formateado con: "En el mercado hay <primero> pero no <segundo>". 
Para obtener primero y segundo son cada una de las líneas separadas 
por " y " (pista: crea una lista desde un String con split. 
Ejemplo: "fruta y verduras".split(" y ") ).
"""

# Copiar el listado inicial
lista_de_inicio = [
    "fruta y verduras",
    "carnes y pescados",
    "lácteos y huevos",
    "dulces y pan",
    "hogar y jardín",
    "cuidado y limpieza"
]

# Imprimir la longitud del listado
print(f"La longitud del listado es: {len(lista_de_inicio)}")

# Eliminar el elemento «hogar y jardín» usando la posición
del lista_de_inicio[4]

# Insertar el elemento "entretenimiento y deportes"
lista_de_inicio.append("entretenimiento y deportes")

# Imprimir cada uno de los elementos formateado
for elemento in lista_de_inicio:
    # Dividir el elemento en «primero» y «segundo» usando split
    primero, segundo = elemento.split(" y ")
    print(f"En el mercado hay {primero}, pero no {segundo}")
