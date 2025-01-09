# Crear variable formato
formato = "{ropa} cuesta {numero} euros"

# Crear dos variables con prendas de ropa
ropa1 = "Camisa"
ropa2 = "Pantalón"

# Crear dos variables con un número escrito
numero1 = "20"
numero2 = "40"

# Crear variables formato_aplicado aplicando el formato
formato_aplicado1 = formato.format(ropa=ropa1, numero=numero1)
formato_aplicado2 = formato.format(ropa=ropa2, numero=numero2)

# Crear una última variable que junte las otras dos
carro_compra = f"Su carro de la compra tiene: {formato_aplicado1} y {formato_aplicado2}"

# Imprimir la última variable
print(carro_compra)
