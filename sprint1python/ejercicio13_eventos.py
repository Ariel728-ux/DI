# ejercicio13_eventos.py
import tkinter as tk

def al_click(event):
    r = 15
    canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="black")

def al_teclado(event):
    if event.char.lower() == 'c':
        canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13 - Eventos")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()
canvas.bind("<Button-1>", al_click)
root.bind("<Key>", al_teclado)

tk.Label(root, text="Haz clic para dibujar un círculo. Presiona 'c' para limpiar.").pack()

root.mainloop()