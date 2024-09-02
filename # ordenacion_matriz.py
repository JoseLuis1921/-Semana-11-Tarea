# ordenacion_matriz.py

def bubble_sort(arr):
    """
    Ordena una lista usando el algoritmo de Bubble Sort.
    
    Args:
        arr (list of int): La lista a ordenar.
    
    Returns:
        list of int: La lista ordenada.
    """
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorre la lista de 0 a n-i-1
            if arr[j] > arr[j+1]:
                # Intercambia si el elemento encontrado es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def imprimir_matriz(matriz):
    """
    Imprime la matriz en formato de tabla.
    
    Args:
        matriz (list of list of int): La matriz a imprimir.
    """
    for fila in matriz:
        print(fila)

def ordenar_fila(matriz, fila_a_ordenar):
    """
    Ordena una fila específica de la matriz.
    
    Args:
        matriz (list of list of int): La matriz que contiene la fila a ordenar.
        fila_a_ordenar (int): El índice de la fila a ordenar.
    
    Returns:
        list of list of int: La matriz con la fila ordenada.
    """
    if 0 <= fila_a_ordenar < len(matriz):
        # Ordena la fila usando Bubble Sort
        matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])
    else:
        print("Índice de fila fuera de rango.")
    return matriz

# Definimos una matriz 3x3
matriz = [
    [9, 2, 5],
    [4, 7, 1],
    [8, 3, 6]
]

# Índice de la fila a ordenar
indice_fila = 1

print("Matriz original:")
imprimir_matriz(matriz)

# Ordenamos la fila especificada
matriz_ordenada = ordenar_fila(matriz, indice_fila)

print("\nMatriz después de ordenar la fila:")
imprimir_matriz(matriz_ordenada)