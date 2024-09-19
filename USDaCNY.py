def usd_to_cny(usd):
    # Conversión de USD a CNY usando la tasa de conversión 6.75
    cny = usd * 6.75

    # Formateamos el resultado a 2 decimales y lo retornamos como string
    return f"{cny:.2f} Chinese Yuan"


# Ejemplos de uso
print(usd_to_cny(15))  # '101.25 Chinese Yuan'
print(usd_to_cny(465))  # '3138.75 Chinese Yuan'
