# ejercicio5_radiobutton.py
import tkinter as tk

def cambiar_color():
    color = var.get()
    root.config(bg=color)

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")
root.geometry("300x150")

var = tk.StringVar(value="white")

tk.Label(root, text="Elige tu color favorito:").pack(pady=6)
rb1 = tk.Radiobutton(root, text="Rojo", variable=var, value="red", command=cambiar_color)
rb2 = tk.Radiobutton(root, text="Verde", variable=var, value="green", command=cambiar_color)
rb3 = tk.Radiobutton(root, text="Azul", variable=var, value="blue", command=cambiar_color)

rb1.pack(anchor="w")
rb2.pack(anchor="w")
rb3.pack(anchor="w")

root.mainloop()