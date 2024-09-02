# busqueda_matriz.py

def buscar_en_matriz(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.
    
    Args:
        matriz (list of list of int): La matriz en la que se realizará la búsqueda.
        valor (int): El valor que se busca en la matriz.
    
    Returns:
        tuple: (encontrado, fila, columna) donde 'encontrado' es un booleano que indica si el valor fue encontrado,
               'fila' y 'columna' son las posiciones del valor en la matriz.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, -1, -1

# Definimos una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 8

# Llamamos a la función de búsqueda
encontrado, fila, columna = buscar_en_matriz(matriz, valor_a_buscar)

# Mostramos el resultado
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna})")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz")