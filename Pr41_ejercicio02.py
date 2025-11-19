#3º B Programacion Matutino
#Autor: Alexis Mora Meza
import tkinter as tk
from tkinter import messagebox

def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("500x300")
    ventana_principal.configure(bg="#e6f2ff")

    tk.Label(
        ventana_principal,
        text="¡Bienvenido al sistema!",
        font=("Helvetica", 14, "bold"),
        bg="#e6f2ff"
    ).pack(pady=50)

    ventana_principal.mainloop()

def verificar_password():
    if entrada_password.get() == "admin123":
        messagebox.showinfo("Acceso", "Acceso correcto")
        ventana.destroy()
        abrir_ventana_principal()
    else:
        messagebox.showerror("Acceso", "Acceso denegado")
        entrada_password.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Sistema de Acceso")
ventana.geometry("300x150")
ventana.configure(bg="#f0f4f8")

tk.Label(
    ventana,
    text="Ingrese su contraseña:",
    font=("Helvetica", 12),
    bg="#f0f4f8"
).pack(pady=(20, 5))

entrada_password = tk.Entry(ventana, show="*", width=25)
entrada_password.pack()
entrada_password.focus_set()
entrada_password.bind("<Return>", lambda event: verificar_password())

tk.Button(
    ventana,
    text="Ingresar",
    command=verificar_password,
    bg="#4CAF50",
    fg="white"
).pack(pady=15)

ventana.mainloop()
