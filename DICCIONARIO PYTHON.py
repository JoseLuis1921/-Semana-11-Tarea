# Crear el diccionario
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0963084547"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
