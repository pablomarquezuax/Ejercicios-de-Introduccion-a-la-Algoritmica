def calcular_media_ponderada(nums, pesos):
    if len(nums) != len(pesos):
        return "Error: La cantidad de números y la cantidad de pesos deben ser iguales."
    
    suma_productos = sum(num * peso for num, peso in zip(nums, pesos))
    suma_pesos = sum(pesos)
    
    if suma_pesos == 0:
        return "Error: La suma de los pesos no puede ser cero."
    
    return suma_productos / suma_pesos

# Solicitar al usuario ingresar los números y los coeficientes de ponderación
nums = []
pesos = []

for i in range(3):
    num = float(input(f"Ingrese el número {i+1}: "))
    nums.append(num)
    peso = float(input(f"Ingrese el coeficiente de ponderación para el número {i+1}: "))
    pesos.append(peso)

# Calcular la media ponderada
media_ponderada = calcular_media_ponderada(nums, pesos)

# Mostrar la media ponderada calculada
if isinstance(media_ponderada, str):
    print(media_ponderada)
else:
    print("La media ponderada de los números dados es:", media_ponderada)
