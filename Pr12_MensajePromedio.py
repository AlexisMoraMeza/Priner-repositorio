#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
nombre = input("Ingresa tu nombre: ")
cal1 = int(input("Teclea la primera calificacion "))
cal2 = int(input("Teclea la segunda calificacion "))
cal3 = int(input("Teclea la tercer calificacion "))
promedio = (cal1 + cal2 + cal3 ) / 3

if promedio >= 6:
    print(nombre, "Aprobaste")
else:
    print(nombre, "Reprobaste")

print("el promedio es: ", promedio)