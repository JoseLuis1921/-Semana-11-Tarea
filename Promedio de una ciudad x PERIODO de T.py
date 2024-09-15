from typing import List, Dict


def calcular_temperatura_promedio(datos: List[Dict[str, List[float]]], ciudad: str) -> float:
    """
    Calcula la temperatura promedio para una ciudad durante un período de tiempo.

    :param datos: Lista de diccionarios, cada uno con la clave 'ciudad' y 'temperaturas'.
    :param ciudad: El nombre de la ciudad para la que queremos calcular la temperatura promedio.
    :return: La temperatura promedio de la ciudad durante el período.
    """
    temperaturas = []

    for entrada in datos:
        if entrada['ciudad'] == ciudad:
            temperaturas.extend(entrada['temperaturas'])

    if not temperaturas:
        raise ValueError(f"No se encontraron datos para la ciudad: {ciudad}")

    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

datos = [
    {'ciudad': 'QUITO', 'temperaturas': [58, 60, 33.0, 84, 68, 70, 60, 88,80]},
    {'ciudad': 'AMBATO', 'temperaturas': [75, 69, 65, 75, 74, 71, 69]},
    {'ciudad': 'SANTO DOMINGO', 'temperaturas': [63, 75, 74, 71, 61, 78, 72, 82]},
]
print("Temperaturas Promedio por Ciudad:")

print(calcular_temperatura_promedio(datos, 'QUITO'))  # Ejemplo de salida: 31.071428571428573
print(calcular_temperatura_promedio(datos, 'SANTO DOMINGO'))  # Ejemplo de salida: 28.5



