#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
Producto1 = int(input("Teclea el precio del primer producto: "))
Producto2 = int(input("Teclea el precio del segundo producto: "))

total=Producto1+Producto2

if total >= 500:
    descuento = total * 0.10  
else:
    descuento = total * 0.02  

TP = total - descuento

print("Descuento:",descuento)
print("Total a pagar:",TP )