# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el porcentaje.

    :param monto_total: El monto total de la compra en dólares
    :param porcentaje_descuento: El porcentaje de descuento (10% por defecto)
    :return: El monto del descuento en dólares
    """
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


# Llamada a la función y mostrar los resultados
def main():
    # Primer caso: usando el porcentaje de descuento predeterminado (10%)
    monto1 = 900  # Monto total de la compra en dólares
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Monto total: ${monto1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")

    # Segundo caso: usando un porcentaje de descuento personalizado (16%)
    monto2 = 2500  # Monto total de la compra en dólares
    porcentaje_descuento2 = 16  # Porcentaje de descuento personalizado
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    monto_final2 = monto2 - descuento2
    print(f"Monto total: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
