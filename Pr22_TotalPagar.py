#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y most
total = 0
n = int(input("Cuantos articulos vas a querer comprar: "))

for i in range(n):
    precio = float(input("Teclea el precio del articulo: "))
    total = total + precio

print("Total a pagar: ", total)