# ESCRITURA DE ARCHIVOS DE TEXTO
# ESCRIBIMOS NUESTRAS NOTAS EN MODO ESCRITURA (W)
with open('my_notes.txt', 'w') as file:
    file.write("Hoy fue un día interesante como estudiante de UEA.\n")
    file.write("Estoy aprendiendo a trabajar con archivos en Python.\n")
    file.write("Me siento cada vez más cómodo con la programación.\n")
    # El archivo se cerrará automáticamente al salir del bloque with

# LECTURA DE ARCHIVOS DE TEXTO
# ABRIMOS EL ARCHIVO EN MODO LECTURA (r) PARA PODER LEER EL CONTENIDO
with open('my_notes.txt', 'r') as file:
    # LEEMOS LINEA POR LINEA UTILIZANDO READLINE ()
    line = file.readline()
    while line:
        print(line.strip())  # IMPRIMIMOS CADA LINEA ELIMINANDO LOS SALTOS DE LINEAS ADICIONALES
        line = file.readline()
    # EL ARCHIVO SE CERRARA AUTOMATICAMENTE AL SALIR DEL BLOQUE WITH
