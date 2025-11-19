#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y most
N = int(input("Teclea el valor de N: "))
X = int(input("Teclea el valor de X: "))

print("Numeros pares del 2 al", N)
for i in range(2, N + 1, 2):
    print(i)

print("Nnmeros nones del 1 al", X)
for i in range(1, X + 1, 2):
    print(i)