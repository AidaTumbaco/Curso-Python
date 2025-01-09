"""
Crea un while True que esté siempre iterando y sumando a un contador +1.
"""
# Inicializamos el contador
contador = 0

try:
    # Bucle infinito que incrementa el contador
    while True:
        contador += 1
        print(contador)
        
        # Verificamos si el contador supera 9999
        if contador > 9999:
            raise BufferError("Se ha superado los 9999 registros")
    
except BufferError as e:
    # Capturamos el BufferError y mostramos el mensaje
    print(f"Se ha detectado el error '{e}'")

# Código que sigue ejecutándose después de capturar el error
print("El código continúa")
