#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk

def mostrar_texto():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    etiqueta_resultado.config(text=f"Escribiste: {nombre} {apellido}")

ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("300x200")

# Etiqueta y entrada para el nombre
etiqueta_nombre = tk.Label(ventana, text="Escribe tu nombre:", font=("Arial", 12))
etiqueta_nombre.pack(pady=5)

entrada_nombre = tk.Entry(ventana, font=("Arial", 12))
entrada_nombre.pack(pady=5)

# Etiqueta y entrada para el apellido
etiqueta_apellido = tk.Label(ventana, text="Escribe tu apellido:", font=("Arial", 12))
etiqueta_apellido.pack(pady=5)

entrada_apellido = tk.Entry(ventana, font=("Arial", 12))
entrada_apellido.pack(pady=5)

# Botón para mostrar el nombre y apellido
boton = tk.Button(ventana, text="Mostrar Nombre y Apellido", command=mostrar_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)

ventana.mainloop()