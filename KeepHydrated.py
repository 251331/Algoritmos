def litres(time):
    # Multiplicar el tiempo por 0.5 para calcular los litros y redondear hacia abajo
    return int(time * 0.5)

# Ejemplos de uso
print(litres(3))    # Salida: 1
print(litres(6.7))  # Salida: 3
print(litres(11.8)) # Salida: 5
