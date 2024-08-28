# busqueda_matriz.py

def buscar_valor(matriz, valor):
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si el valor no se encuentra

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    valor_buscado = int(input("Introduce el valor a buscar: "))
    resultado = buscar_valor(matriz, valor_buscado)

    if resultado:
        print(f"Valor encontrado en la posición: {resultado}")
    else:
        print("Valor no encontrado")

if __name__ == "__main__":
    main()
