# ejercicio11_scale.py
import tkinter as tk

def actualizar(val):
    lbl.config(text=f"Valor: {val}")

root = tk.Tk()
root.title("Ejercicio 11 - Scale")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar)
scale.pack(pady=10)

lbl = tk.Label(root, text="Valor: 0")
lbl.pack(pady=6)

root.mainloop()