# ejercicio4_checkbutton.py
import tkinter as tk

def actualizar():
    seleccionadas = []
    if var1.get(): seleccionadas.append("Leer")
    if var2.get(): seleccionadas.append("Deporte")
    if var3.get(): seleccionadas.append("Música")
    lbl.config(text="Aficiones: " + (", ".join(seleccionadas) if seleccionadas else "Ninguna"))

root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

cb1 = tk.Checkbutton(root, text="Leer", variable=var1, command=actualizar)
cb2 = tk.Checkbutton(root, text="Deporte", variable=var2, command=actualizar)
cb3 = tk.Checkbutton(root, text="Música", variable=var3, command=actualizar)

cb1.pack(anchor="w")
cb2.pack(anchor="w")
cb3.pack(anchor="w")

lbl = tk.Label(root, text="Aficiones: Ninguna")
lbl.pack(pady=8)

root.mainloop()