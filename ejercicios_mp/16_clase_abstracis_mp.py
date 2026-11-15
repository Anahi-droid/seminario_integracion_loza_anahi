from abc import ABC, abstractmethod


class Empleado(ABC):
    @abstractmethod
    def calcular_pago(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return "Pago mensual fijo: 1000 USD"


class EmpleadoPorHoras(Empleado):
    def calcular_pago(self):
        return "Pago por horas: 5 USD x horas trabajadas"


juan = EmpleadoTiempoCompleto()
carla = EmpleadoPorHoras()
print(juan.calcular_pago())
print(carla.calcular_pago())