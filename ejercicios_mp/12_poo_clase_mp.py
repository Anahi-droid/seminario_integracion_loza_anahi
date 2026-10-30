class Empleado:
    nombre: str
    cargo: str

    def __init__(self, nombre: str, cargo: str):
        self.nombre = nombre
        self.cargo = cargo

    def mostrar_info(self):
        print("Nombre", self.nombre)
        print("Cargo", self.cargo)


maria = Empleado("María Andrade", "Analista de nómina")

maria.mostrar_info()
print(maria.nombre)