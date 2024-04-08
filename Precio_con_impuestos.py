def calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_IVA):
    precio_con_impuestos = precio_sin_impuestos * (1 + (porcentaje_IVA / 100))
    return precio_con_impuestos

# Solicitar al usuario el precio sin impuestos y el porcentaje de IVA
precio_sin_impuestos = float(input("Ingrese el precio sin impuestos: "))
porcentaje_IVA = float(input("Ingrese el porcentaje de IVA (%): "))

# Calcular el precio con impuestos incluidos
precio_con_impuestos = calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_IVA)

# Mostrar el precio con impuestos incluidos
print("El precio con todos los impuestos incluidos es:", precio_con_impuestos)
