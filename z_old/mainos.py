import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de ttk.LabelFrame")
root.geometry("400x200")

# Crear un LabelFrame
label_frame = ttk.LabelFrame(root, text="Caja de Texto y Botón")
label_frame.pack(padx=20, pady=20, fill="both", expand="yes")

# Crear una caja de texto dentro del LabelFrame
caja_texto = tk.Text(label_frame, height=5, width=30)
caja_texto.grid(row=0, column=0, padx=10, pady=10)

# Crear un botón dentro del LabelFrame
boton = ttk.Button(label_frame, text="Enviar", command=lambda: print(caja_texto.get("1.0", tk.END)))
boton.grid(row=0, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
