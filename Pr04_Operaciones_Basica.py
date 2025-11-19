#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año

numero1=int(input("Ingresa el primer número: "))
numero2=int(input("Ingresa el segundo número: "))
res=0 
print("\n")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5. Salir")

opcion=input("Elige una opcion:")
if opcion == "1":
    res=numero1+numero2
    print("El resultado de la SUMA es:" ,res)
elif opcion=="2":
    res=numero1-numero2
    print("El resutado de la Resta es: ",res)
elif opcion=="3":
    res=numero1*numero2
    print("El resutado de la Multiplicacion es: ",res)
elif opcion=="4":
    if(numero1>numero2):
     res=numero1/numero2
     print("El resultado es la Division es: ",res )
    else:
     print("NO se puede realizar la operacion")
elif opcion=="5":
   print("Saliendo del programa.")
else:
   print("Opcion no valida")