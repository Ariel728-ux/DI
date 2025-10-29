# ejercicio14_clases.py
import tkinter as tk
from tkinter import messagebox, filedialog
import json

class RegistroApp:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 14 - RegistroApp (clases)")
        self.usuarios = []

        menubar = tk.Menu(root)
        archivo = tk.Menu(menubar, tearoff=0)
        archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menubar.add_cascade(label="Archivo", menu=archivo)
        root.config(menu=menubar)

        tk.Label(root, text="Nombre:").pack()
        self.e_nombre = tk.Entry(root); self.e_nombre.pack()

        tk.Label(root, text="Edad:").pack()
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal"); self.scale_edad.pack()

        tk.Label(root, text="Género:").pack()
        self.var_genero = tk.StringVar(value="Otro")
        frame_gen = tk.Frame(root)
        tk.Radiobutton(frame_gen, text="Masculino", variable=self.var_genero, value="Masculino").pack(side="left")
        tk.Radiobutton(frame_gen, text="Femenino", variable=self.var_genero, value="Femenino").pack(side="left")
        tk.Radiobutton(frame_gen, text="Otro", variable=self.var_genero, value="Otro").pack(side="left")
        frame_gen.pack(pady=6)

        tk.Button(root, text="Añadir", command=self.añadir_usuario).pack()
        frame_list = tk.Frame(root); frame_list.pack(fill="both", expand=True, pady=6)
        self.lb = tk.Listbox(frame_list)
        scroll = tk.Scrollbar(frame_list, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        self.lb.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        tk.Button(root, text="Eliminar seleccionado", command=self.eliminar_usuario).pack(pady=4)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=2)

    def añadir_usuario(self):
        nombre = self.e_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Introduce un nombre")
            return
        usuario = {"nombre": nombre, "edad": self.scale_edad.get(), "genero": self.var_genero.get()}
        self.usuarios.append(usuario)
        self.lb.insert(tk.END, f"{usuario['nombre']} - {usuario['edad']} - {usuario['genero']}")
        self.e_nombre.delete(0, tk.END)

    def eliminar_usuario(self):
        sel = self.lb.curselection()
        if not sel: return
        idx = sel[0]
        self.lb.delete(idx)
        self.usuarios.pop(idx)

    def guardar_lista(self):
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.usuarios, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Guardar", "Lista guardada")

    def cargar_lista(self):
        path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if path:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            self.usuarios = data
            self.lb.delete(0, tk.END)
            for u in data:
                self.lb.insert(tk.END, f"{u['nombre']} - {u['edad']} - {u['genero']}")
            messagebox.showinfo("Cargar", "Lista cargada")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()