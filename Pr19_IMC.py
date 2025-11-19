#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
Peso = int(input("Teclea tu peso: "))
altura = float(input("Teclea tu altura: "))

imc= Peso/(altura*altura)

if imc<18:
    concl=("Tienes Anorexia")
elif imc>=18 and imc<20:
    concl=("Estas Delgado")
elif imc>=20 and imc<27:
    concl=("Estas en tu peso ideal")
elif imc>=27 and imc<30:
    concl=("Tienes Obesidad grado 1")
elif imc>=30 and imc<35:
    concl=("Tienes Obesidad grado 2")
elif imc>=35 and imc<40:
    concl=("Tienes Obesidad grado 3")
else:
    concl=("Tienes Obesidad Morbida")

print("Tu IMC es",imc)
print("Tu",concl)
