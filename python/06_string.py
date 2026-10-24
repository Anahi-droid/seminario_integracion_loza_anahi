"""
Manjo de Cadena de Caracteres
"""

nombre1="Qui-Gon Jin"
print(f"Jedi 1: {nombre1}")
print(f"TIpo de datos: {type(nombre1)}")
nombre2="Obiwan Kenobi"
print(f"Jedi 2: {nombre2}")
print(f"TIpo de datos: {type(nombre2)}")

### FUnciones comunes de las variables String

print("Funciones comunes de texto")
droide_1 = "R2-D20"
droide_2 = "C3PO"
longitud_droide_1 =len(droide_1)
longitud_droide_2 =len(droide_2)
print("Nombre droide 1", droide_1)
print("Nombre droide 2", longitud_droide_1)

print("Nombre droide 1", droide_2)
print("Nombre droide 2", longitud_droide_2)

print("COnvertir Mayusculas a minisculas")
mensaje = "La federacion invade el planeta NABOO"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje en mayuscula", mensaje_mayuscula)
print("Mensaje en minuscula", mensaje_minuscula)

print("Reemplazoa de Substring")
mensaje = "La nave viajara Tatooine"
nuevo_mensaje = mensaje.replace("Tatooine", "Corusant")
print("Mensaje Original", mensaje)
print("Mensaje Reemplazado", nuevo_mensaje)

planetas = "Naboo, Tatooine, Kmino"
print("planetas:", planetas)
lista_planetas = planetas.split(",")
print(lista_planetas)
print("Primer Planteas:", lista_planetas[0])

print("Extraer subcadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[6:11]
verbo = mensaje[20:28]
print("adjetivo es:", adjetivo)
print("verbo es:", verbo)

print("COmprobaciones utiles")
codigo = "R2D2"
numero = "2026"
nombre = "UniversidadUTE"
identificador = "CROIDE1"
print(codigo.isalnum()) # alfanumerico
print(codigo.isdigit())
print(codigo.isalpha()) # alfabetico
print(identificador.isalnum())
print(identificador.isdigit())

