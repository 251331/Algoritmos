def round_to_two_decimals(number):
    """
    Redondea un número a dos lugares decimales.
    """
    return round(number, 2)


def process_numbers(numbers):
    """
    Procesa una lista de números, redondeándolos a dos lugares decimales.
    """
    return [round_to_two_decimals(num) for num in numbers]


def main():
    # Lista de números de ejemplo
    numbers = [5.5589, 3.3424, 7.8765, 2.3456]

    # Procesar y redondear los números
    rounded_numbers = process_numbers(numbers)

    # Imprimir los resultados
    print("Números originales:", numbers)
    print("Números redondeados a dos decimales:", rounded_numbers)


if __name__ == "__main__":
    main()


