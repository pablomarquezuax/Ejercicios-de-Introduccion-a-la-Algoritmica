def calcular_intereses(capital, tasa_interes, tiempo_meses):
    intereses = (capital * tasa_interes / 100) * (tiempo_meses / 12)
    return intereses

# Solicitar al usuario el capital invertido, la tasa de interés y el tiempo en meses
capital = float(input("Ingrese el capital invertido: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
tiempo_meses = int(input("Ingrese el tiempo en meses: "))

# Calcular el importe de los intereses
intereses_generados = calcular_intereses(capital, tasa_interes, tiempo_meses)

# Mostrar el importe de los intereses generados
print("El importe de los intereses generados es:", intereses_generados)
