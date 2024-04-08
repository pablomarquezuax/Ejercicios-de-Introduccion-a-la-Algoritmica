'''
Sí, puedes utilizar este algoritmo para calcular el área de un triángulo rectángulo
si se proporcionan las medidas de sus dos lados perpendiculares. En un triángulo rectángulo, 
la base y la altura son simplemente los dos lados perpendiculares. Puedes usar la longitud 
de uno de estos lados como base y la longitud del otro lado como altura.
'''

def calcular_area_triangulo_rectangulo(lado1, lado2):
    area = (1 / 2) * lado1 * lado2
    return area

# Solicitar al usuario la medida de los dos lados perpendiculares del triángulo rectángulo
lado1 = float(input("Ingrese la medida del primer lado perpendicular del triángulo rectángulo: "))
lado2 = float(input("Ingrese la medida del segundo lado perpendicular del triángulo rectángulo: "))

# Calcular el área del triángulo rectángulo
area_triangulo_rectangulo = calcular_area_triangulo_rectangulo(lado1, lado2)

# Mostrar el área del triángulo rectángulo calculada
print("El área del triángulo rectángulo es:", area_triangulo_rectangulo)
