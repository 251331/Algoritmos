def find_third_angle(angle1, angle2):
    # Paso 1: Sumar los dos ángulos que nos han proporcionado
    sum_of_angles = angle1 + angle2

    # Paso 2: Restar la suma de los dos ángulos a 180 grados para obtener el tercer ángulo
    third_angle = 180 - sum_of_angles

    # Paso 3: Devolver el valor del tercer ángulo
    return third_angle


# Ejemplos de uso
print(find_third_angle(60, 60))  # Salida: 60
print(find_third_angle(45, 90))  # Salida: 45
