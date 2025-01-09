"""
Crea un programa que pregunte por teclado (pista: input) si 
hay "chocolate" primero y si hay "harina" después 
(pista: bool("Cualquier valor") es True o bool("") es False). 
"""



"""
Imprime:
Si ambos son ciertos imprimiremos "Cocinamos una tarta"
Si solo es cierto "chocolate" imprimiremos "Haremos bombones"
Si solo es cierto "harina" imprimiremos "Hornearemos pan"
Si ninguna es cierta imprimiremos "Hoy descanso"
"""
chocolate = input("¿Tienes chocolate? (Escribe algo si sí, deja vacío si no): ")
harina = input("¿Tienes harina? (Escribe algo si sí, deja vacío si no): ")

# Convertimos la entrada en valores booleanos
hay_chocolate = bool(chocolate)
hay_harina = bool(harina)

# Determinamos qué hacer según los valores
if hay_chocolate and hay_harina:
    print("Cocinamos una tarta")
elif hay_chocolate:
    print("Haremos bombones")
elif hay_harina:
    print("Hornearemos pan")
else:
    print("Hoy descanso")


