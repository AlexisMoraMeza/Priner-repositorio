#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
num1 = int(input("Teclea el primer número: "))
num2 = int(input("Teclea el segundo número: "))

#iguales
if num1 == num2:
    resultado = num1 * num2
    print("Los números son iguales. El resultado de la multiplicación es:", resultado)
#primer numero mayor
elif num1 > num2:
    resultado = num1 - num2
    print("El primer número es mayor. El resultado de la resta es:", resultado)
#primer numero menor
else:
    resultado = num1 + num2
    print("El primer número es menor. El resultado de la suma es:", resultado)