def calculate_pet_ages(humanYears):
    # Inicializamos las variables para los años de gatos y perros
    catYears = 0
    dogYears = 0

    # Calculamos los años para el primer año
    if humanYears >= 1:
        catYears += 15
        dogYears += 15

    # Calculamos los años para el segundo año
    if humanYears >= 2:
        catYears += 9
        dogYears += 9

    # Calculamos los años para los años restantes (si humanYears > 2)
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    # Devolvemos el resultado en forma de diccionario
    return {
        "humanYears": humanYears,
        "catYears": catYears,
        "dogYears": dogYears
    }


# Ejemplo de uso:
humanYears = 5  # Cambia este valor para probar con diferentes años humanos
result = calculate_pet_ages(humanYears)
print(result)  # Salida: {'humanYears': 5, 'catYears': 36, 'dogYears': 39}
 