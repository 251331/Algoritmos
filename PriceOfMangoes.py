def mango(quantity, price):
    # Dividir en grupos de 3 mangos. Solo pagamos por 2 de cada grupo.
    groups_of_three = quantity // 3
    remaining_mangoes = quantity % 3

    # El costo es por los mangos que se pagan, que son 2 mangos por cada grupo de 3 + los mangos restantes.
    total_cost = (groups_of_three * 2 + remaining_mangoes) * price

    return total_cost


# Ejemplos de uso
print(mango(2, 3))  # Salida: 6
print(mango(3, 3))  # Salida: 6
print(mango(5, 3))  # Salida: 12
print(mango(9, 5))  # Salida: 30
