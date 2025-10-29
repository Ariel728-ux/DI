# ejercicio3_entry.py
import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if nombre:
        lbl.config(text=f"¡Hola, {nombre}!")
    else:
        lbl.config(text="Introduce tu nombre.")

root = tk.Tk()
root.title("Ejercicio 3 - Entry")

tk.Label(root, text="Introduce tu nombre:").pack(pady=4)
entrada = tk.Entry(root)
entrada.pack(pady=4)

btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=6)

lbl = tk.Label(root, text="")
lbl.pack(pady=6)

root.mainloop()