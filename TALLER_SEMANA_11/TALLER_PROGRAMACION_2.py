def merge_sort(fila):
    if len(fila) > 1:
        mid = len(fila) // 2
        izquierda = fila[:mid]
        derecha = fila[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                fila[k] = izquierda[i]
                i += 1
            else:
                fila[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            fila[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            fila[k] = derecha[j]
            j += 1
            k += 1

matriz = [
    [34, 7, 23],
    [11, 56, 8],
    [1, 2, 45]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 1 (segunda fila) usando Merge Sort
fila_a_ordenar = 1
merge_sort(matriz[fila_a_ordenar])

print("Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)
