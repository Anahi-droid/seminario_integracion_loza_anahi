for pausa in range(1, 6):
    print("El empleado realiza la pausa activa", pausa)

for horas in range(1, 11):
    print("Pago horas extra", 5, "*", horas, "=", 5 * horas)

for horas in range(1, 11, 3):
    print("Pago horas extra", 5, "*", horas, "=", 5 * horas)

empleados = [
    {"id": 1, "nombre": "María Andrade", "cargo": "Analista de nómina", "estado": "Activo"},
    {"id": 2, "nombre": "Carlos Quishpe", "cargo": "Coordinador de selección", "estado": "Activo"},
    {"id": 3, "nombre": "Lucía Paredes", "cargo": "Jefa de talento humano", "estado": "Activo"},
    {"id": 4, "nombre": "Andrés Villacís", "cargo": "Asistente administrativo", "estado": "Inactivo"},
    {"id": 5, "nombre": "Daniela Cevallos", "cargo": "Especialista en capacitación", "estado": "Activo"},
    {"id": 6, "nombre": "Jorge Naranjo", "cargo": "Analista de bienestar", "estado": "Inactivo"},
    {"id": 7, "nombre": "Paola Mena", "cargo": "Reclutadora", "estado": "Activo"},
    {"id": 8, "nombre": "Diego Cárdenas", "cargo": "Auxiliar de nómina", "estado": "Activo"},
    {"id": 9, "nombre": "Fernanda Salazar", "cargo": "Analista de desempeño", "estado": "Activo"},
    {"id": 10, "nombre": "Esteban Loor", "cargo": "Auxiliar de archivo", "estado": "Inactivo"},
]
for empleado in empleados:
    print(f"{empleado['id']} - nombre: {empleado['nombre']}")

desempeno = {
    "María Andrade": 95,
    "Carlos Quishpe": 88,
    "Lucía Paredes": 72,
}

for nombre, puntaje in desempeno.items():
    if puntaje >= 90:
        print(nombre, "califica para un ascenso")
    else:
        print(nombre, "necesita más capacitación")

candidatos = ["Sofía Armas", "Mateo Rivera"]
for candidato in candidatos:
    print("Entrevista de", candidato)
    for ronda in range(1, 4):
        print("Ronda", ronda)

print("Break y Continue")
candidatos = ["Sofía Armas", "Mateo Rivera", "Valentina Torres", "Diego Cárdenas"]
for candidato in candidatos:
    print("Candidato", candidato)
    if candidato == "Valentina Torres":
        break
    if candidato == "Mateo Rivera":
        continue
    print("Pasa a la siguiente etapa:", candidato)