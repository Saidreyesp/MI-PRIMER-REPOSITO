# Creación del diccionario 'informacion_personal' con la información proporcionada, incluyendo la edad correcta
informacion_personal = {
    "nombre": "Said Reyes Pianda",
    "edad": 21,
    "ciudad": "Quevedo",
    "profesion": "Comerciante"
}

# Acceder y modificar el valor de la clave "ciudad" a otra ciudad ficticia
informacion_personal["ciudad"] = "Guayaquil"  # Cambiado a Guayaquil

# Actualizar la profesión de Comerciante a otra (ficticia)
informacion_personal["profesion"] = "Empresario"

# Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0967283141"  # Número proporcionado

# Imprimir el diccionario final con la edad incluida
print(informacion_personal)

