#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
nombre = input("Teclea tu nombre: ")
edad = int(input("Teclea tu edad: "))

if edad >= 18:
    print(nombre, "Tu eres Mayor de edad")
else:
    print(nombre, "Tu eres Menor de edad")