print("CRUD DE LAS LISTAS DE PYTHON")
advengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitan America", "estado": "Activo"}
]

id_publico = 4
def create():
    global id_publico
    print("Reclutar advenger")
    nombre = input("Nombre heroe:")
    heroe = input("Heroe:")
    estado = input("Estado activo")
    nuevo_avenger = {
        "id": id_publico,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    advengers.append(nuevo_avenger)

def read():
    print("Lista de Avengers")
    for avenger in advengers:
        print(f"{avenger["id"]} - nombre: {avenger["nombre"]}")

def update():
    print("Actualizar avenger")
    id_update = int(input("id a modificar"))
    for avenger in advengers:
        if (avenger[id]== id_update):
            avenger["nombre"] = input("Nuevo nombre")
            avenger["hereo"] = input("Nuevo hereo")
            avenger["estado"] = input("Nuevo estado")
            print("Actualizado")


def delete():
    print("ELiminar avenger")
    id_delete = int(input("id a borrar"))
    for avenger in advengers:
        if (avenger[id]== id_delete):
            avenger.remove(avenger)
            print("Actualizado")


def menu():
    while True:
        print("Advengers")
        print("1. Crear")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Salir")
        opcion = input("Seleccione la opcion del 1 al 5")
        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Cerrando Sistema")
            break
        else:
            print("Intente nuevamente")

