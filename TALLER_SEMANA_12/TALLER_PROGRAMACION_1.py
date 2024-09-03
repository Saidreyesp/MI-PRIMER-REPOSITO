# Crear una matriz 3D para almacenar las temperaturas
temperaturas = [
    [  # Quevedo
        [15, 17, 16, 18, 20, 19, 21],  # Semana 1: Lunes a Domingo
        [16, 18, 19, 21, 22, 20, 23],  # Semana 2: Lunes a Domingo
    ],
    [  # Guayaquil
        [10, 12, 14, 13, 15, 16, 14],  # Semana 1: Lunes a Domingo
        [11, 13, 15, 14, 16, 17, 15],  # Semana 2: Lunes a Domingo
    ]
]

# Lista de nombres de las ciudades
nombres_ciudades = ["Quevedo", "Guayaquil"]

# Iterar sobre cada ciudad
for ciudad_index, ciudad in enumerate(temperaturas):
    nombre_ciudad = nombres_ciudades[ciudad_index]
    print(f"{nombre_ciudad}:")

    # Iterar sobre cada semana de la ciudad
    for semana_index, semana in enumerate(ciudad):
        suma_temperaturas = 0
        num_dias = len(semana)

        # Calcular suma de temperaturas de la semana
        for temperatura in semana:
            suma_temperaturas += temperatura

        # Calcular promedio
        promedio = suma_temperaturas / num_dias
        print(f"  Semana {semana_index + 1}: Promedio de temperatura = {promedio:.2f}°C")
