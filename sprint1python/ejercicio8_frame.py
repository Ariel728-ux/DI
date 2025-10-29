# ejercicio8_frame.py
import tkinter as tk

def mostrar():
    lbl_inferior.config(text=f"Contenido: {entry.get()}")

def borrar():
    entry.delete(0, tk.END)
    lbl_inferior.config(text="Contenido: ")

root = tk.Tk()
root.title("Ejercicio 8 - Frame")

frame_sup = tk.Frame(root, bd=2, relief="sunken", padx=5, pady=5)
frame_sup.pack(fill="x", pady=4)
tk.Label(frame_sup, text="Etiqueta 1").grid(row=0, column=0, padx=4)
tk.Label(frame_sup, text="Etiqueta 2").grid(row=0, column=1, padx=4)
entry = tk.Entry(frame_sup)
entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=4)

frame_inf = tk.Frame(root, padx=5, pady=5)
frame_inf.pack(fill="x", pady=4)
btn_mostrar = tk.Button(frame_inf, text="Mostrar", command=mostrar)
btn_borrar = tk.Button(frame_inf, text="Borrar", command=borrar)
btn_mostrar.pack(side="left", padx=6)
btn_borrar.pack(side="left", padx=6)
lbl_inferior = tk.Label(root, text="Contenido: ")
lbl_inferior.pack(pady=6)

root.mainloop()


