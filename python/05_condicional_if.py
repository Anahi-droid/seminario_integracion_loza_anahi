
print("Condicional If")
print("Condicional Simple")
dinero = 10
if dinero >= 5:
    print("Homero puede comprar rosquillas")

print("Programa Finalizo")
print("Condicional If - else")
print("Condicional Dos Caminos")

creditos = float(input("Cantidad de creditos disponibles"))
precio_repuesto = float(input("Precio repuesto"))

if (creditos>=precio_repuesto):
    print("Compra Autorizada")
else:
    print("Creditos insuficientes")
    print("Buscar solucion o trueque")


print("Condicional if - elif - else")
print("Condicional Condiciones Aisladas")
combustible = float(input("Combustible Anidadas"))

if (combustible>=75):
    print("Optimo")
elif (combustible>=50):
    print("Suficiente")
elif (combustible>=20):
    print("Bajo")
else:
    print("Critico")
    print("Localiza base mas cercana")

print("Condiciones Anidadas")
piloto = input("NOmbre del Piloto")
motor_funciona = input("EL motor funciona SI/NO")
combustible = int(input("Combustible disponible "))

if (motor_funciona=="SI"):
    print("Motor Verificado")
    if (combustible>=50):
        print("Combustible Suficiente")
        print("Participacion Autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede participar")
    print("EL motor necesita reparacion")
