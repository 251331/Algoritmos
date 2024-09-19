import math


def convert_to_16_9(x, y):
    # Calculamos el nuevo ancho ajustado a la relación 16:9
    new_x = math.ceil((16 / 9) * y)

    # Devolvemos la nueva resolución (X ajustado, Y original)
    return new_x, y


# Ejemplo de uso
x, y = 1024, 901  # Resolución original (4:3)
new_resolution = convert_to_16_9(x, y)
print(f"Resolución ajustada: {new_resolution}")  # Salida: (1920, 1080)
