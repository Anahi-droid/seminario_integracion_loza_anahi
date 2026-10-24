print("CRUD DE LISTAS DE PYTHON")
empleados = [
    {"id": 1, "nombre": "Carlos Mendoza", "cargo": "Gerente de RH", "estado": "Activo"},
    {"id": 2, "nombre": "Ana Torres", "cargo": "Analista de Nomina", "estado": "Activo"}
]

id_publico = 3

def create():
    global id_publico
    print("Registrar empleado")
    nombre = input("Nombre del empleado: ")
    cargo = input("Cargo: ")
    estado = input("Estado: ")
    nuevo_empleado = {
        "id": id_publico,
        "nombre": nombre,
        "cargo": cargo,
        "estado": estado
    }
    empleados.append(nuevo_empleado)
    id_publico += 1
    print("Empleado registrado")

def read():
    print("Lista de empleados")
    for empleado in empleados:
        print(f"{empleado['id']} - nombre: {empleado['nombre']} - cargo: {empleado['cargo']} - estado: {empleado['estado']}")

def update():
    print("Actualizar empleado")
    id_update = int(input("Id a modificar: "))
    for empleado in empleados:
        if empleado["id"] == id_update:
            empleado["nombre"] = input("Nuevo nombre: ")
            empleado["cargo"] = input("Nuevo cargo: ")
            empleado["estado"] = input("Nuevo estado: ")
            print("Actualizado")
            return
    print("Id no encontrado")

def delete():
    print("Eliminar empleado")
    id_delete = int(input("Id a borrar: "))
    for empleado in empleados:
        if empleado["id"] == id_delete:
            empleados.remove(empleado)
            print("Eliminado")
            return
    print("Id no encontrado")

def menu():
    while True:
        print("Recursos Humanos")
        print("1. Crear")
        print("2. Listar")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Seleccione la opcion del 1 al 5: ")
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

menu()