# ejercicio12_registro.py
import tkinter as tk
from tkinter import messagebox, filedialog
import json

def añadir_usuario():
    nombre = e_nombre.get().strip()
    edad = scale_edad.get()
    genero = var_genero.get()
    if not nombre:
        messagebox.showwarning("Aviso", "Introduce un nombre")
        return
    usuario = {"nombre": nombre, "edad": edad, "genero": genero}
    usuarios.append(usuario)
    lb.insert(tk.END, f"{nombre} - {edad} - {genero}")
    e_nombre.delete(0, tk.END)

def eliminar_usuario():
    sel = lb.curselection()
    if not sel:
        return
    idx = sel[0]
    lb.delete(idx)
    usuarios.pop(idx)

def guardar_lista():
    path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("Guardar", "Lista guardada")

def cargar_lista():
    path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
    if path:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        usuarios.clear()
        lb.delete(0, tk.END)
        for u in data:
            usuarios.append(u)
            lb.insert(tk.END, f"{u['nombre']} - {u['edad']} - {u['genero']}")
        messagebox.showinfo("Cargar", "Lista cargada")

root = tk.Tk()
root.title("Ejercicio 12 - Registro de usuarios")

usuarios = []

menu = tk.Menu(root)
archivo = tk.Menu(menu, tearoff=0)
archivo.add_command(label="Guardar Lista", command=guardar_lista)
archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu.add_cascade(label="Archivo", menu=archivo)
root.config(menu=menu)

tk.Label(root, text="Nombre:").pack()
e_nombre = tk.Entry(root)
e_nombre.pack()

tk.Label(root, text="Edad:").pack()
scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack()

tk.Label(root, text="Género:").pack()
var_genero = tk.StringVar(value="Otro")
frame_gen = tk.Frame(root)
tk.Radiobutton(frame_gen, text="Masculino", variable=var_genero, value="Masculino").pack(side="left")
tk.Radiobutton(frame_gen, text="Femenino", variable=var_genero, value="Femenino").pack(side="left")
tk.Radiobutton(frame_gen, text="Otro", variable=var_genero, value="Otro").pack(side="left")
frame_gen.pack(pady=6)

btn_add = tk.Button(root, text="Añadir", command=añadir_usuario)
btn_add.pack()

frame_list = tk.Frame(root)
frame_list.pack(fill="both", expand=True, pady=6)
lb = tk.Listbox(frame_list)
scroll = tk.Scrollbar(frame_list, command=lb.yview)
lb.config(yscrollcommand=scroll.set)
lb.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

btn_del = tk.Button(root, text="Eliminar seleccionado", command=eliminar_usuario)
btn_del.pack(pady=4)
btn_exit = tk.Button(root, text="Salir", command=root.quit)
btn_exit.pack(pady=2)

root.mainloop()