# ejercicio6_listbox.py
import tkinter as tk

def mostrar_seleccion():
    sel = lb.curselection()
    if sel:
        fruta = lb.get(sel[0])
        lbl.config(text=f"Seleccionaste: {fruta}")
    else:
        lbl.config(text="No hay selección")

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")

lb = tk.Listbox(root, height=5)
for fruta in ["Manzana", "Banana", "Naranja", "Pera", "Uva"]:
    lb.insert(tk.END, fruta)
lb.pack(pady=6)

btn = tk.Button(root, text="Mostrar fruta", command=mostrar_seleccion)
btn.pack(pady=4)

lbl = tk.Label(root, text="")
lbl.pack(pady=6)

root.mainloop()