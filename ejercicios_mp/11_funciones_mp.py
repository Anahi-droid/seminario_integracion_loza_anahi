print("Funciones")
print("Autor: Anahi Loza")


def registrar_asistencia():
    print("El empleado marca su entrada")
    print("¡Asistencia registrada!")


registrar_asistencia()


def saludar_empleado(empleado):
    print(empleado, "inicia su jornada laboral")


saludar_empleado("María Andrade")
saludar_empleado("Anahi Loza")


def calcular_pago(horas, tarifa):
    total = horas * tarifa
    return total


resultado = calcular_pago(4, 26)
print("El pago por horas extra de Anahi Loza es", resultado)


def evaluar_ascenso(nombre, puntaje):
    if puntaje >= 90:
        print(f"El ascenso de {nombre} fue aprobado")
    else:
        print(f"{nombre} necesita mejorar su desempeño")


evaluar_ascenso("Anahi Loza", 75)

nombre_empleado: str = "María Andrade"
edad: int = 33
sueldo: float = 620.5
es_activo: bool = True


def calcular_bono(porcentaje: float, sueldo: float) -> float:
    return porcentaje * sueldo


print("El bono de", nombre_empleado, "es", calcular_bono(0.1, sueldo))