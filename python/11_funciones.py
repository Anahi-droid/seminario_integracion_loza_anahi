print("Funciones")
print("Autor: Anahi Loza")

def kamehameha():
    print("Goku ce¡oncentra su energia")
    print("¡kamehamkea")

kamehameha()

def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Anahi Loza")

def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio

resultado = calcular_poder(4,26)
print("EL poder de Anahi Loza es", resultado)

def transformar_saiyayin(nombre, poder):
    if poder >=9000:
        print(f"Transfromación de {nombre} a SuperSayayin exitosa")
    else:
        print(f"{nombre} Necesito aumentar tu poder")

transformar_saiyayin("Anahi Loza", 5000)

nombre_personaje : str = "Goku"
edad: int = 33
altura: float = 1.74
es_activo: bool = True

def multiplicador_poder(entrenamiento: float, edad: int) -> float:
    return entrenamiento*edad

multiplicador_poder(2.5, 8)
