def nba_extrap(ppg, mpg):
    # Si mpg es 0, devolvemos 0 directamente (no puede extrapolar si no juega nada)
    if mpg == 0:
        return 0

    # Extrapolamos los puntos por 48 minutos
    extrapolated_ppg = (ppg * 48) / mpg

    # Redondeamos a una cifra decimal
    return round(extrapolated_ppg, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # Salida: 28.8
print(nba_extrap(10, 10))  # Salida: 48.0
print(nba_extrap(5, 17))  # Salida: 14.1
print(nba_extrap(0, 0))  # Salida: 0
