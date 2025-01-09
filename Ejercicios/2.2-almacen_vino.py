# Crear las variables que representan los barriles en cada almacén
almacen_barriles_tinto = 123
almacen_barriles_blanco = 87
almacen_barriles_rosado = 65

# Crear las variables que guardan el nombre de cada almacén
str_almacen_tinto = "Almacén tinto"
str_almacen_blanco = "Almacén blanco"
str_almacen_rosado = "Almacén rosado"

# Calcular el total de barriles
total_barriles = almacen_barriles_tinto + almacen_barriles_blanco + almacen_barriles_rosado
print(f"Tenemos un total de {total_barriles} barriles")

# Calcular los litros de vino en cada almacén
litros_tinto = almacen_barriles_tinto * 2
litros_blanco = almacen_barriles_blanco * 47
litros_rosado = almacen_barriles_rosado * 73

# Imprimir la cantidad de litros en cada almacén
print(f"El {str_almacen_tinto} tiene {litros_tinto} litros")
print(f"El {str_almacen_blanco} tiene {litros_blanco} litros")
print(f"El {str_almacen_rosado} tiene {litros_rosado} litros")

# Comparaciones entre almacenes
print(f"{litros_tinto} > {litros_rosado} = {litros_tinto > litros_rosado}")
print(f"{litros_tinto} > {litros_blanco} = {litros_tinto > litros_blanco}")
print(f"{litros_rosado} > {litros_blanco} = {litros_rosado > litros_blanco}")
print(f"{litros_tinto} == {litros_blanco} = {litros_tinto == litros_blanco}")
print(f"{litros_tinto} == {litros_rosado} = {litros_tinto == litros_rosado}")
print(f"{litros_blanco} == {litros_rosado} = {litros_blanco == litros_rosado}")
