# Ejercicio 3 - Una empresa cuenta con dos tipos de empleados
# Hecho por: Wesly Umanzor, Keyla Canales 

def calcular_bono(anios_trabajados):
    return 500 if anios_trabajados > 5 else 0

def calcular_pago_empleado_fijo(comisiones, anios_trabajados):
    salario_base = 360  # Salario base definido
    bono = calcular_bono(anios_trabajados)
    return salario_base + comisiones + bono

def calcular_pago_empleado_por_horas(tarifa_hora, horas_trabajadas, anios_trabajados):
    bono = calcular_bono(anios_trabajados)
    return (tarifa_hora * horas_trabajadas) + bono

def main():
    tipo_empleado = input("Ingrese el tipo de empleado (fijo/horas): ").lower()

    nombre = input("Ingrese el nombre del empleado: ")
    anios_trabajados = int(input("Ingrese los años trabajados: "))

    if tipo_empleado == "fijo":
        comisiones = float(input("Ingrese las comisiones: "))
        pago_total = calcular_pago_empleado_fijo(comisiones, anios_trabajados)
    elif tipo_empleado == "horas":
        tarifa_hora = float(input("Ingrese la tarifa por hora: "))
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        pago_total = calcular_pago_empleado_por_horas(tarifa_hora, horas_trabajadas, anios_trabajados)
    else:
        print("Tipo de empleado no válido.")
        return

    print(f"\nEl pago total para {nombre} es: ${pago_total}")

if __name__ == "__main__":
    main()
