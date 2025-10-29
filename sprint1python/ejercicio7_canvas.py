# ejercicio7_canvas.py
import tkinter as tk

def dibujar_rect():
    try:
        x1 = int(e_x1.get()); y1 = int(e_y1.get())
        x2 = int(e_x2.get()); y2 = int(e_y2.get())
    except ValueError:
        lbl.config(text="Introduce valores enteros")
        return
    canvas.create_rectangle(x1, y1, x2, y2, outline="black")

def dibujar_circ():
    try:
        cx = int(e_cx.get()); cy = int(e_cy.get()); r = int(e_r.get())
    except ValueError:
        lbl.config(text="Introduce valores enteros")
        return
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black")

root = tk.Tk()
root.title("Ejercicio 7 - Canvas")

frame = tk.Frame(root)
frame.pack(side="top", pady=4)

tk.Label(frame, text="x1 y1 x2 y2:").grid(row=0, column=0)
e_x1 = tk.Entry(frame, width=4); e_y1 = tk.Entry(frame, width=4)
e_x2 = tk.Entry(frame, width=4); e_y2 = tk.Entry(frame, width=4)
e_x1.grid(row=0,column=1); e_y1.grid(row=0,column=2); e_x2.grid(row=0,column=3); e_y2.grid(row=0,column=4)
tk.Button(frame, text="Dibujar rect", command=dibujar_rect).grid(row=0,column=5, padx=6)

tk.Label(frame, text="cx cy r:").grid(row=1,column=0)
e_cx = tk.Entry(frame, width=4); e_cy = tk.Entry(frame, width=4); e_r = tk.Entry(frame, width=4)
e_cx.grid(row=1,column=1); e_cy.grid(row=1,column=2); e_r.grid(row=1,column=3)
tk.Button(frame, text="Dibujar círculo", command=dibujar_circ).grid(row=1,column=5, padx=6)

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=8)

lbl = tk.Label(root, text="")
lbl.pack()

root.mainloop()