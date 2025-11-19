#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk

def sumar():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      suma = num1 + num2
      resultado.config(text=f"Resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def resta():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      resta = num1 - num2
      resultado.config(text=f"Resultado: {resta}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def Multiplicacion():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      Multiplicacion = num1 * num2
      resultado.config(text=f"Resultado: {Multiplicacion}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

def Division():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      Division = num1 / num2
      resultado.config(text=f"Resultado: {Division}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

ventana = tk.Tk()
ventana.title("Suma,resta,multiplicacion,divicion de dos números")
ventana.geometry("350x230")

entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)

entrada1.pack(pady=5)
entrada2.pack(pady=5)


boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)
boton_resta = tk.Button(ventana, text="resta", command=resta)
boton_resta.pack(pady=5)
boton_Multiplicacion = tk.Button(ventana, text="Multiplicacion", command=Multiplicacion)
boton_Multiplicacion.pack(pady=5)
boton_Division = tk.Button(ventana, text="Division", command=Division)
boton_Division.pack(pady=5)


resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

ventana.mainloop()