class Empleado:
    nombre: str
    __salario: int

    def __init__(self, nombre: str, salario: int):
        self.nombre = nombre
        self.__salario = salario

    def mostrar_info(self):
        print("Nombre:", self.nombre)

    def get_salario(self):
        return self.__salario


juan = Empleado("Juan", 900)
carla = Empleado("Carla", 1200)
pedro = Empleado("Pedro", 800)
maria = Empleado("Maria", 1500)

juan.mostrar_info()
carla.mostrar_info()
pedro.mostrar_info()
maria.mostrar_info()
print(juan.nombre)
print(carla.nombre)
print(carla.get_salario())