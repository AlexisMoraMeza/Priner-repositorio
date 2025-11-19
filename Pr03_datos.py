#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año

nombre= input("¿Como te llamas ") #pedir un dato (string)
edad= input ("¿Cuantos años tienes? ")

#input siempre devuelve texto; si necesito operar con nùmeros
edad=int(edad)

print() #linea en blanco
print("Encantado de conocerte,", nombre)
print("El año que viene tendras", edad + 1, "años.")