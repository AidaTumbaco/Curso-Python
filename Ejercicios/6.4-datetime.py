"""
Se pide crear un script que pida introducir por pantalla una fecha de nacimiento con formato “DD/MM/YYYY” y que
imprima por pantalla los días que ha vivido desde su nacimiento hasta el instante de ejecutar el script y que
también imprima por pantalla la edad en años.
"""
from datetime import datetime

# Pedir la fecha de nacimiento
fecha_nacimiento_str = input("Introduce tu fecha de nacimiento (DD/MM/YYYY): ")

# Convertir la fecha de nacimiento a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia entre las dos fechas
diferencia = fecha_actual - fecha_nacimiento

# Calcular los días vividos
dias_vividos = diferencia.days

# Calcular la edad en años (redondeando hacia abajo)
edad = (fecha_actual - fecha_nacimiento).days // 365

# Mostrar los resultados
print(f"Has vivido {dias_vividos} días.")
print(f"Tu edad es {edad} años.")
