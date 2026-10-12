print("Incluir Datos con Input")
nombre = input("¿Cuàl es tu nombre?")
print("Hola", nombre)
print("Bienvenido Al Mundo de Homero")
print("Hasta luego"+nombre)

cantidad = input("Anota una cantidad:")
print("La cantidad es:", cantidad)

print("Conversiones")
print("=====TIENDA DE APU=====")
nombre_cliente = input("Nombre del cliente:")
precio = float(input("Precio de la rosquilla:"))
cantidad = int(input("Cantidad:"))
total = cantidad * precio
print("Total a pagar:", total)
print("Total a pagar (round):", round(total,2))
print(f"Total a pagar (f): ${total:.2f}")
