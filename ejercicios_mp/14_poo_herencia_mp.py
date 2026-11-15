class Empleado:
    nombre: str
    departamento: str

    def __init__(self, nombre: str, departamento: str):
        self.nombre = nombre
        self.departamento = departamento

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Departamento:", self.departamento)


class Gerente(Empleado):
    def __init__(self, nombre: str, departamento: str):
        super().__init__(nombre, departamento)

    def mostrar_info(self):
        print("El gerente", self.nombre, "dirige el departamento de", self.departamento)


juan = Gerente("Juan", "Recursos Humanos")
carla = Gerente("Carla", "Finanzas")
juan.mostrar_info()
carla.mostrar_info()