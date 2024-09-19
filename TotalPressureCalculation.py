def total_pressure(M1, M2, m1, m2, V, T):
    # Constante de los gases ideales (en J/(mol·K))
    R = 8.314

    # Convertimos la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Aplicamos la fórmula para la presión total
    P_total = ((m1 / M1) + (m2 / M2)) * (R * T_kelvin) / V

    return P_total


# Ejemplo de uso
M1 = 28.0  # Masa molar del primer gas en g/mol (ejemplo)
M2 = 32.0  # Masa molar del segundo gas en g/mol (ejemplo)
m1 = 2.0  # Masa del primer gas en gramos (ejemplo)
m2 = 3.0  # Masa del segundo gas en gramos (ejemplo)
V = 10.0  # Volumen del recipiente en dm^3 (ejemplo)
T = 25.0  # Temperatura en grados Celsius (ejemplo)

# Llamada a la función
print(total_pressure(M1, M2, m1, m2, V, T))  # Salida: presión total
