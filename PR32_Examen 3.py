#3º B Programacion Matutino
#Autor: Alexis Mora Meza
pares = 0
impares = 0
nulos = 0
suma = 0

for i in range(5):
    numero = int(input("Teclea un número: "))
    suma = suma + numero

    if numero == 0:
        nulos = nulos + 1
    elif numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Pares:", pares)
print("Impares:", impares)
print("Nulos:", nulos)
print("Suma total:", suma)
