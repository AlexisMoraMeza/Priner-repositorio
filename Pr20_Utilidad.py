#3º B Programacion Matutino
#Autor: Alexis Mora Meza
#Objetivo: saludar al usuario y mostrar su edad el proximo año
añosT = int(input("Teclea tus años trabajados: "))
salM = int(input("Teclea tu salario por mes: "))

if añosT<1:
    util=salM*0.05
    print("tu utilidad es de:",util)
elif añosT>1 and añosT<2:
    util=salM*0.07
    print("tu utilidad es de:",util)
elif añosT>2 and añosT<5:
    util=salM*0.10
    print("tu utilidad es de:",util)
elif añosT>5 and añosT<10:
    util=salM*0.15
    print("tu utilidad es de:",util)
else:
    util=salM*0.20
    print("tu utilidad es de:",util)

salTotal=salM+util
print("tu salario en total seria de:",salTotal)
    