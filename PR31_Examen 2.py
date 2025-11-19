#3º B Programacion Matutino
#Autor: Alexis Mora Meza
nombre= input("¿Como te llamas ") 
edad= int(input ("¿Cuantos años tienes? "))

sum=0

for E in range (edad,0,-1):

 if edad>=18:
  print(E)


 else:
  sum=sum+E

if edad<18:
 print("La suma de todos los numeros son:",sum)