def calcular_tarifa_hora_normal(salario_mensual_bruto):
    salario_anual_bruto = salario_mensual_bruto * 12
    salario_semanal_bruto = salario_anual_bruto / 52
    salario_hora_normal = salario_semanal_bruto / 35
    return salario_hora_normal

def calcular_importe_horas_extra(salario_mensual_bruto, horas_extra_trabajadas):
    salario_hora_normal = calcular_tarifa_hora_normal(salario_mensual_bruto)
    horas_extra_36_43 = min(horas_extra_trabajadas, 8)  # máximo de horas extra entre 36ª y 43ª
    horas_extra_44_mas = max(horas_extra_trabajadas - 8, 0)  # horas extra a partir de la 44ª

    # Tarifas aumentadas según las normas administrativas
    tarifa_36_43 = salario_hora_normal * 1.25
    tarifa_44_mas = salario_hora_normal * 1.5

    # Calcular el importe de las horas extra
    importe_horas_extra = (horas_extra_36_43 * tarifa_36_43) + (horas_extra_44_mas * tarifa_44_mas)
    return importe_horas_extra

# Solicitar al usuario el salario mensual bruto y la cantidad de horas extra trabajadas
salario_mensual_bruto = float(input("Ingrese el salario mensual bruto: "))
horas_extra_trabajadas = float(input("Ingrese la cantidad de horas extra trabajadas en el mes: "))

# Calcular el importe de las horas extra
importe_horas_extra = calcular_importe_horas_extra(salario_mensual_bruto, horas_extra_trabajadas)

# Mostrar el importe de las horas extra calculado
print("El importe de las horas extra a pagar es:", importe_horas_extra)
