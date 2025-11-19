#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk
from tkinter import messagebox

def calcular_promedios():
    suma_promedios=0
    contador=0

    for i in range(len(filas)):
        try:
            cal1 = float(filas[i][1].get())
            cal2 = float(filas[i][2].get())
            cal3 = float(filas[i][3].get())
            promedio = (cal1 + cal2 + cal3) / 3
            filas[i][4].config(text=f"{promedio:.2f}")
            suma_promedios += promedio
            contador += 1
        except ValueError:
            messagebox.showerror("Error", f"Calificaciones inválidas en la fila {i + 1}")

    if contador > 0:
        promedio_general = suma_promedios / contador
        label_general.config(text=f"{promedio_general:.2f}")

    nombre = entry_nombre.get()
    messagebox.showinfo("Promedio general", f"El promedio general de {nombre} es: {promedio_general:.2f}")

ventana = tk.Tk()
ventana.title("Boleta de Calificaciones")

tk.Label(ventana, text="Nombre del alumno:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

encabezados = ["Materia", "Unidad 1", "Unidad 2", "Unidad 3", "Promedio"]
for col, encabezado in enumerate(encabezados):
   tk.Label(ventana, text=encabezado, font=('Arial', 10, 'bold')).grid(row=1, column=col, padx=5, pady=5)

filas = []
for i in range(3):
   fila = []


   entry_materia = tk.Entry(ventana)
   entry_materia.grid(row=i+2, column=0, padx=5, pady=5)
   fila.append(entry_materia)

   for j in range(1, 4):
      entry_cal = tk.Entry(ventana, width=10)
      entry_cal.grid(row=i+2, column=j, padx=5)
      fila.append(entry_cal)

   label_promedio = tk.Label(ventana, text="0.00", width=10, bg="lightgray")
   label_promedio.grid(row=i+2, column=4, padx=5)
   fila.append(label_promedio)
     
   filas.append(fila)
   
btn_calcular = tk.Button(ventana, text="Calcular Promedios", command=calcular_promedios)
btn_calcular.grid(row=7, column=0, columnspan=5, pady=10)

tk.Label(ventana, text="Prom General:").grid(row=7, column=3)
label_general = tk.Label(ventana, text="0.00", bg="lightblue", width=10)
label_general.grid(row=7, column=4)


ventana.mainloop()
