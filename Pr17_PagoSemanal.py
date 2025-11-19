#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
DT = int(input("Teclea el numero de dias trabajados: "))
SD = int(input("Teclea el sueldo diario: "))

S = DT * SD

if DT > 5:
    ST = SD + 100  
else:
    ST = SD

print("El sueldo semanal es: ",ST )