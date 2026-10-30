for flexion in range(1,6):
    print("Goku hace la flexion", flexion)

for numero in range(1,11):
    print("Multiplicacion" ,5, "*", numero, "=", 5*numero)

for numero in range(1,11,3):
    print("Multiplicacion" ,5, "*", numero, "=", 5*numero)

avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitán América", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"},
    {"id": 4, "nombre": "Bruce Banner", "heroe": "Hulk", "estado": "Activo"},
    {"id": 5, "nombre": "Natasha Romanoff", "heroe": "Black Widow", "estado": "Inactivo"},
    {"id": 6, "nombre": "Clint Barton", "heroe": "Hawkeye", "estado": "Activo"},
    {"id": 7, "nombre": "Peter Parker", "heroe": "Spider-Man", "estado": "Activo"},
    {"id": 8, "nombre": "Wanda Maximoff", "heroe": "Scarlet Witch", "estado": "Activo"},
    {"id": 9, "nombre": "Sam Wilson", "heroe": "Falcon", "estado": "Activo"},
    {"id": 10, "nombre": "T'Challa", "heroe": "Black Panther", "estado": "Inactivo"}
]
for avenger in avengers:
    print(f"{avenger['id']} - nombre: {avenger['nombre']}")

guerreros = {
    "Goku": 9500,
    "Vegeta": 6000,
    "Piccolo": 4500,
}

for nombre, poder in guerreros.items():
    if poder >= 9000:
        print(nombre, "puede enfrentar a Freezer")
    else:
        print(nombre, "necesira entrenar mas")

guerreros = ["Goku", "Vegeta"]
for guerrero in guerreros:
    print("Turno de", guerrero)
    for ronda in range(1,4):
        print("Ronda", ronda)

print("Break and COntinue")
for guerrero in guerreros:
    print("Guerrero", guerrero)
    if (guerrero == "Picolo"):
        break
    if(guerrero == "Vegeta"):
        continue
    print("Guerrero", guerrero)