def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devuelve el monto del descuento calculado
    return descuento
# Monto total de la compra
monto = 120
descuento_calculado = calcular_descuento(monto)

print(f"El descuento calculado es: {descuento_calculado}")

