#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y most
total=0
cont=0
while cont < 4:
    precio = float(input("Teclea el precio del articulo: "))
    total = total + precio
    cont = cont + 1
if total > 500:
    descuento = total * 0.05
    total = total - descuento
print("Total a pagar: ",total)