#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk

ventana = tk.Tk()
ventana.title("Abarrotes")
ventana.geometry("500x300")
ventana.resizable(False, False)

etiqueta = tk.Label(ventana, text="Teclea el precio del producto")
etiqueta.pack(pady=5)

entrada_precio = tk.Entry(ventana, font=("Arial", 15), justify="center")
entrada_precio.pack(pady=10)

seleccion = tk.IntVar()

def mostrar_radio():
    opcion = seleccion.get()
    try:
        cantidad = float(entrada_precio.get())
    except ValueError:
        resultado.config(text="Por favor, ingresa un número válido.")
        return

    if opcion == 1:
        descuento = cantidad * 0.05
        resultado.config(text=f"Estimado cliente, su descuento del 5% es: ${descuento:.2f}")
    elif opcion == 2:
        descuento = cantidad * 0.10
        resultado.config(text=f"Estimado cliente, su descuento del 10% es: ${descuento:.2f}")
    elif opcion == 3:
        descuento = cantidad * 0.15
        resultado.config(text=f"Estimado cliente, su descuento del 15% es: ${descuento:.2f}")
    else:
        resultado.config(text="Seleccione una opción de descuento.")

radio1 = tk.Radiobutton(ventana, text="Descuento del 5%", variable=seleccion, value=1, command=mostrar_radio)
radio2 = tk.Radiobutton(ventana, text="Descuento del 10%", variable=seleccion, value=2, command=mostrar_radio)
radio3 = tk.Radiobutton(ventana, text="Descuento del 15%", variable=seleccion, value=3, command=mostrar_radio)

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

resultado = tk.Label(ventana, text="", justify="left", font=("Arial", 10), fg="#c04f03")
resultado.pack(pady=15)

ventana.mainloop()