def calcular_area_triangulo(base, altura):
    area = (1 / 2) * base * altura
    return area

# Solicitar al usuario la medida del lado y la altura relativa al lado
base = float(input("Ingrese la medida del lado del triángulo: "))
altura = float(input("Ingrese la altura relativa al lado del triángulo: "))

# Calcular el área del triángulo
area_triangulo = calcular_area_triangulo(base, altura)

# Mostrar el área del triángulo calculada
print("El área del triángulo es:", area_triangulo)
