# ejercicio10_scrollbar.py
import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10 - Scrollbar")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

text = tk.Text(frame, wrap="word")
scroll = tk.Scrollbar(frame, command=text.yview)
text.config(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)

# Rellenar con texto de ejemplo
texto_largo = ("Este es un texto de ejemplo.\n" * 50) + "Fin del texto."
text.insert("1.0", texto_largo)

root.mainloop()