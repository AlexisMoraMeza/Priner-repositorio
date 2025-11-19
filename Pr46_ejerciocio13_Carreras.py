#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Carreras")
ventana.geometry("500x200")

etiqueta = tk.Label(ventana, text="Elige tu Carrera")
etiqueta.pack(pady=10)

opciones = ["RH", "Arquitectura", "Comercio", "Programacion", "Construccion"]
ComboCarreras = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboCarreras.pack(pady=5)

def mostrar_seleccion(event):
    seleccion = ComboCarreras.get()
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")

ComboCarreras.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="Aún no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()