#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk
from tkinter import Toplevel

ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Nombre y Apellido")
    ventana_hija.geometry("250x150")

    etiqueta = tk.Label(ventana_hija, text="Alexis", font=("Arial", 12))
    etiqueta.pack(pady=10)

    etiqueta1 = tk.Label(ventana_hija, text="Mora Meza", font=("Arial", 12))
    etiqueta1.pack(pady=10)

    boton_cerrar = tk.Button(ventana_hija, text="Cerrar", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana de Nombre y Apellido", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)

def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Python")
    ventana_hija.geometry("250x150")

    etiqueta = tk.Label(ventana_hija, text="«Programado con Python»", font=("Arial", 12))
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(ventana_hija, text="Cerrar", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana de Nombre y Apellido", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)


ventana_principal.mainloop()
