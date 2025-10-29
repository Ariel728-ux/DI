# ejercicio9_menu.py
import tkinter as tk
from tkinter import messagebox, filedialog

def abrir():
    fichero = filedialog.askopenfilename(title="Abrir archivo")
    if fichero:
        messagebox.showinfo("Archivo seleccionado", fichero)

def acerca_de():
    messagebox.showinfo("Acerca de", "Ejercicio 9 - Menú\nAutor: Tu Nombre")

root = tk.Tk()
root.title("Ejercicio 9 - Menu")
menubar = tk.Menu(root)

menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(menubar, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=menubar)
root.mainloop()