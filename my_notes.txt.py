# Escritura de archivo
with open('my_notes.txt', 'w') as output_file:  # Abrimos el archivo en modo escritura
    output_file.write("Nota 1: Recoger los ingredientes de las bodegas.\n")
    output_file.write("Nota 2: Comprar ingredientes para las recetas a los proveedores.\n")
    output_file.write("Nota 3: Llamar a distintos proveedores para la elaboracion de recetas.\n")

# Lectura de archivo
with open('my_notes.txt', 'r') as input_file:  # Abrimos el archivo en modo lectura
    for line in input_file:
        print(line.strip())  # Mostramos cada línea, eliminando los saltos de línea

# El archivo se cierra automáticamente al salir del bloque 'with'
