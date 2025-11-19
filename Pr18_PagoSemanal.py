#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
P1 = int(input("Teclea el precio del primer producto: "))
P2 = int(input("Teclea el precio del segundo producto: "))
P3 = int(input("Teclea el precio del primer producto: "))

Total=P1+P2+P3

if Total<1000:
    desc=Total*0.05
elif Total>=1000 and Total<2500:
    desc=Total*0.10
else:
    desc=Total*0.20

TotalCD=Total-desc

print("Tu descuento es de:",desc)
print("TU total con el descuento es",TotalCD)
