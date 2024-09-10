def calcular_temperatura_promedio_por_semana(datos_temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un período de 4 semanas,
    mostrando el promedio de cada semana y el promedio total.

    Parámetros:
    datos_temperaturas (dict): Diccionario con las ciudades como claves y una lista de 4 temperaturas semanales como valores.

    Retorna:
    dict: Diccionario con las ciudades como claves y sus temperaturas promedio por semana y el promedio total.
    """
    #  DICCIONARIO PARA ALMACENAR LOS RESULTADOS
    resultados = {}

    # UTILIZAMOS SOBRE CADA CIUDAD Y SUS TEMPERATURAS
    for ciudad, temperaturas in datos_temperaturas.items():
        # VERIFICAMOS QUE LA LISTA TENGA 4 VALORES, UNA POR CADA SEMANA
        if len(temperaturas) == 4:
            # INICIALIZAMOS UN DICCIONARIO PARA LA TEMPERATURA DE LA CIUDAD
            promedios_por_ciudad = {}

            # CALCULAREMOS EL PROMEDIO DE CADA SEMANA
            for i, temp in enumerate(temperaturas):
                promedios_por_ciudad[f'Semana {i + 1}'] = temp

            # CALCULAMOS SU PROMEDIO TOTAL
            promedio_total = sum(temperaturas) / len(temperaturas)
            promedios_por_ciudad['Promedio Total'] = promedio_total

            # AÑADIMOS LOS RESULTADOS DE LA CIUDADES AL DICCIONARIO PRINCIPAL
            resultados[ciudad] = promedios_por_ciudad
        else:
            print(f"Error: La ciudad {ciudad} no tiene 4 semanas de datos.")

    #  RETORNAMONEL DICCIONARIO CON LOS PROMEDIOS POR SEMANA Y PROMEDIO TOTAL
    return resultados


# EJEMPLO DE SU USO:
if __name__ == "__main__":
    datos = {
        'Quevedo': [25, 26, 27, 24],
        'Puyo': [22, 21, 23, 20],
        'Guayaquil': [30, 31, 32, 29]
    }

    # LLAMAMOS A LA FUNCION MOSTRANDO LOS RESULTADOS
    promedios = calcular_temperatura_promedio_por_semana(datos)
    for ciudad, resultados in promedios.items():
        print(f"Resultados para {ciudad}:")
        for semana, promedio in resultados.items():
            print(f"  {semana}: {promedio}°C")
        print()  # Línea en blanco para separar los resultados por ciudad


