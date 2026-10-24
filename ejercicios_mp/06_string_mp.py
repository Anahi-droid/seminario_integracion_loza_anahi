cargo1 = "Gerente de Recursos Humanos"
print(f"Cargo 1: {cargo1}")
print(f"Tipo de datos: {type(cargo1)}")
cargo2 = "Analista de Nomina"
print(f"Cargo 2: {cargo2}")
print(f"Tipo de datos: {type(cargo2)}")

print("Funciones comunes de texto")
empleado_1 = "Carlos Mendoza"
empleado_2 = "Ana Torres"
longitud_empleado_1 = len(empleado_1)
longitud_empleado_2 = len(empleado_2)
print("Nombre empleado 1:", empleado_1)
print("Longitud nombre empleado 1:", longitud_empleado_1)

print("Nombre empleado 2:", empleado_2)
print("Longitud nombre empleado 2:", longitud_empleado_2)

print("Convertir mayusculas a minusculas")
mensaje = "La empresa abre una vacante en el area de VENTAS"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje en mayuscula:", mensaje_mayuscula)
print("Mensaje en minuscula:", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "El empleado sera transferido a Quito"
nuevo_mensaje = mensaje.replace("Quito", "Guayaquil")
print("Mensaje original:", mensaje)
print("Mensaje reemplazado:", nuevo_mensaje)

departamentos = "Contabilidad, Ventas, Sistemas"
print("Departamentos:", departamentos)
lista_departamentos = departamentos.split(", ")
print(lista_departamentos)
print("Primer departamento:", lista_departamentos[0])

print("Extraer subcadenas")
mensaje = "Bienvenido al equipo de recursos humanos"
sustantivo = mensaje[14:20]
area = mensaje[24:32]
print("El sustantivo es:", sustantivo)
print("El area es:", area)

print("Comprobaciones utiles")
codigo = "EMP2026"
numero = "2026"
nombre = "UniversidadUTE"
identificador = "RH-001"
print(codigo.isalnum())
print(codigo.isdigit())
print(codigo.isalpha())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())