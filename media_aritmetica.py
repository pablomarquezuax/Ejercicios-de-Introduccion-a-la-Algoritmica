def calcular_media_aritmetica(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Solicitar al usuario ingresar los tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular la media aritmética
media_aritmetica = calcular_media_aritmetica(num1, num2, num3)

# Mostrar la media aritmética calculada
print("La media aritmética de los tres números es:", media_aritmetica)