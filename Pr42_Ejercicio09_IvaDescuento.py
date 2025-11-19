#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk
from tkinter import messagebox

# Function para calcular el 10% de "Descuento"
def calcular_descuento():
    try:
        # Obtenemos el valor ingresado por el usuario
        cantidad = float(entrada_cantidad.get())
        # Calculemos el 10% de "Descuento"
        descuento = cantidad * 0.10
        # Mostramos el resultado en la etiqueta
        etiqueta_resultado.config(text=f"Descuento (10%): ${descuento:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Función para calcular el IVA
def calcular_iva():
    try:
        cantidad = float(entrada_cantidad.get())
        # Calculamos el IVA (16%)
        iva = cantidad * 0.16
        # Mostramos el resultado en la etiqueta
        etiqueta_resultado.config(text=f"IVA (16%): ${iva:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Funcion para calcular el total a pagar (considerando IVA y "Descuento")
def calcular_total():
    try:
        cantidad = float(entrada_cantidad.get())
        # Calculamos IVA y "Descuento"
        iva = cantidad * 0.16
        descuento = cantidad * 0.10
        # Total = cantidad original + IVA - Descuento
        total = cantidad + iva - descuento
        # Mostramos el total en pantalla
        etiqueta_resultado.config(text=f"Total a pagar: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# INTERFAZ GRÁFICA DE LA VENTANA PRINCIPAL

# Creamos la ventana principal
ventana = tk.Tk()
# Inicia la aplicación gráfica
ventana.title("Calcular IVA y Descuento")  # Título de la ventana
ventana.geometry("380x300")  # Tamaño (ancho x alto)
ventana.resizable(False, False)  # Evita que el usuario cambie el tamaño de la ventana

# ETIQUETA Y CAJA DE TEXTO

# Creamos una etiqueta que indica qué debe escribir al usuario
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)  # pack() coloca el elemento y pady da un margen vertical

# Caja de texto donde se escribirá la cantidad
entrada_cantidad = tk.Entry(ventana, justify="center")  # justify centra el texto
entrada_cantidad.pack()  # se apega a la ventana

# BOTONES DE ACCIÓN

# Puedes buscar los códigos de los colores en esta página https://python-charts.com/es/colores/

# Botón que calcula el IVA
btn_iva = tk.Button(
    ventana,
    text="Calcular IVA",
    command=calcular_iva,  # Llama a la función calcular_iva cuando se presiona
    bg="#E2DCD6"  # Color de fondo
)
btn_iva.pack(pady=5)

# Botón que calcula el descuento
btn_descuento = tk.Button(
    ventana,
    text="Calcular 10% Descuento",
    command=calcular_descuento,
    bg="yellow", fg="red"  # Color de fondo (amarillo) y texto (rojo)
)
btn_descuento.pack(pady=5)

# Botón que calcula el total
btn_total = tk.Button(
    ventana,
    text="Calcular Total a Pagar",
    command=calcular_total,
    bg="blue", fg="white"  # Color de fondo (azul) y texto (blanco)
)
btn_total.pack(pady=5)

# ETIQUETA DE RESULTADOS

# Aquí se mostrará el resultado después de presionar un botón
etiqueta_resultado = tk.Label(
    ventana,
    text="",  # Vacío al inicio
    font=("Arial", 12, "bold")  # Tamaño y estilo de letra
)
etiqueta_resultado.pack(pady=15)

# INICIO DEL PROGRAMA

# Inicia el ciclo principal de la aplicación
# Este ciclo mantiene la ventana abierta y esperando interacción del usuario
ventana.mainloop()