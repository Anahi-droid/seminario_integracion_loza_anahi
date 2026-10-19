print("Incluir Datos con Input")
nombre_candidato = input("¿Cuál es tu nombre?")
print("Hola", nombre_candidato)
print("Bienvenido al proceso de selección")
print("Hasta luego " + nombre_candidato)

dias_solicitados = input("Anota los días de vacaciones:")
print("Los días solicitados son:", dias_solicitados)

print("Conversiones")
print("=====NÓMINA QUINCENAL=====")
nombre_trabajador = input("Nombre del trabajador:")
pago_por_hora = float(input("Pago por hora:"))
horas_laboradas = int(input("Horas laboradas:"))
pago_total = horas_laboradas * pago_por_hora
print("Pago total:", pago_total)
print("Pago total (round):", round(pago_total, 2))
print(f"Pago total (f): ${pago_total:.2f}")

