class Guerrero: 
    nombre: str
    __poder: int

    def __init__(self, nombre:str, poder:int):
        self.nombre = nombre
        self.poder = poder

    def mostar_info(self):
        print("Nombre ", self.nombre)

    def get_poder(self):
        print()


goku = Guerrero("Goku", 9000)
vegeta = Guerrero("vegeta", 6000)
piccolo = Guerrero("piccolo", 1000)
maria = Guerrero("Goku", 5000)


goku.mostar_info()
vegeta.mostar_info()
piccolo.mostar_info()
maria.mostar_info()
print(goku.nombre)
print(vegeta.nombre)
print(vegeta)