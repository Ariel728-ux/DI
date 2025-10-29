# ejercicio2_button.py
import tkinter as tk
from tkinter import messagebox

def mostrar():
    lbl.config(text="Has pulsado el botón mostrar")

def salir():
    root.quit()

root = tk.Tk()
root.title("Ejercicio 2 - Button")

btn1 = tk.Button(root, text="Mostrar mensaje", command=mostrar)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Salir", command=salir)
btn2.pack(pady=5)

lbl = tk.Label(root, text="")
lbl.pack(pady=10)

root.mainloop()