#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk
from tkinter import messagebox

ventana_principal = tk.Tk()
ventana_principal.title("Calculo de venta ")
ventana_principal.geometry("500x300")
ventana_principal.resizable(False, False)

def Multiplicacion():
   try:
      num1 = float(entrada_prod.get())
      num2 = float(entrada_produ.get())
      Multiplicacion = num1 * num2
      resultado.config(text=f"Resultado: {Multiplicacion}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def IVA():
   try:
      num1 = float(entrada_prod.get())
      num2 = float(entrada_produ.get())
      IVA = (num1*num2*0.16)
      resultado.config(text=f"Resultado: {IVA}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def Total():
   try:
      num1 = float(entrada_prod.get())
      num2 = float(entrada_produ.get())
      Total = (num1*num2*0.16)+(num1*num2)
      resultado.config(text=f"Resultado: {Total}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")



etiqueta = tk.Label(ventana_principal, text="teclea la cantidad de articulos que deseas")
etiqueta.pack(pady=5)
entrada_prod = tk.Entry(ventana_principal, font=("Arial", 12))
entrada_prod.pack(pady=5)
etiqueta1 = tk.Label(ventana_principal, text="precio por articulo")
etiqueta1.pack(pady=5)
entrada_produ = tk.Entry(ventana_principal, font=("Arial", 12))
entrada_produ.pack(pady=5)


boton_subtotal = tk.Button(ventana_principal, text="subtotal", font=("Arial", 12), command=Multiplicacion)
boton_subtotal.pack(pady=5)
boton_IVA = tk.Button(ventana_principal, text="IVA", font=("Arial", 12), command=IVA)
boton_IVA.pack(pady=5)
boton_Total = tk.Button(ventana_principal, text="Total", font=("Arial", 12), command=Total)
boton_Total.pack(pady=5)

resultado = tk.Label(ventana_principal, text="Resultado:")
resultado.pack(pady=5)
ventana_principal.mainloop()