print("OPERADORES")
print("Operadores Aritméticos")
print("+ Suma: ", 8, "+", 2, "=", 8+2)
print("- Resta: ", 8, "-", 2, "=", 8-2)
print("* Multiplicación: ", 8, "*", 2, "=", 8*2)
print("/ División: ", 20, "/", 4, "=", 20/4)
print("// División entera: ", 17, "//", 5, "=", 17//5)
print("% Residuo: ", 17, "%", 5, "=", 17%5)
print("** Potencia: ", 3, "**", 2, "=", 3**2)

print("Tabla de multiplicar del 8")
print(8, "*", 1, "=", 8*1)
print(8, "*", 2, "=", 8*2)
print(8, "*", 3, "=", 8*3)
print(8, "*", 4, "=", 8*4)
print(8, "*", 5, "=", 8*5)
print(8, "*", 6, "=", 8*6)
print(8, "*", 7, "=", 8*7)
print(8, "*", 8, "=", 8*8)
print(8, "*", 9, "=", 8*9)
print(8, "*", 10, "=", 8*10)

print("Operadores de Comparación")
print("== Igual a : ", 40, "==", 40, 40 == 40)
print("== Igual a : ", 40, "==", 35, 40 == 35)
print("!= Diferente de : ", 40, "!=", 40, 40 != 40)
print("!= Diferente de : ", 40, "!=", 35, 40 != 35)
print("> Mayor que: ", 30, ">", 25, 30 > 25)
print("> Mayor que: ", 30, ">", 45, 30 > 45)
print("< Menor que: ", 30, "<", 25, 30 < 25)
print("< Menor que: ", 30, "<", 45, 30 < 45)

print("OPERADORES LOGICOS")
print("Operador and : (6==6)and(9>3)", (6 == 6) and (9 > 3))
print("Operador and : (6==6)and(9>12)", (6 == 6) and (9 > 12))
print("Operador or : (6==6)or(9>12)", (6 == 6) or (9 > 12))
print("Operador or : (6==7)or(9>12)", (6 == 7) or (9 > 12))
print("Operador not : not(6==7)", not (6 == 7))
print("Operador not : not(6==6)", not (6 == 6))

tiene_documentos = True
paso_entrevista = True

puede_ser_contratado = tiene_documentos and paso_entrevista
print("¿Puede ser contratado? ", puede_ser_contratado)

es_empleado_destacado = True
tiene_sancion = False
recibe_bono = es_empleado_destacado or tiene_sancion
print("¿Bono aprobado? ", recibe_bono)