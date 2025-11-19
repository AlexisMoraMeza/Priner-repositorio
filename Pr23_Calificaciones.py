#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y most
nombre = input("teclea tu nombre: ")
suma = 0
for i in range(3):
    calificacion = float(input("Teclea una calificacion: "))
    suma = suma + calificacion
promedio = suma / 3
print("Promedio: ", promedio)
if promedio >= 6:
    print("Aprobaste")
else:
    print("Reprobaste")