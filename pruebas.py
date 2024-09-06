import tkinter as tk
from tkinter import filedialog

def open_file1():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        label.config(text=f"File 1 selected: {file_path}")

def open_file2():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        label.config(text=f"File 2 selected: {file_path}")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Estilizada")

# Dimensiones y color de fondo
root.geometry("600x400")
root.configure(bg="#F0F0F0")
root.resizable(0,0)

# Crear un label con texto por defecto, estilizado
label = tk.Label(root, text="Selecciona un archivo", font=("Helvetica", 14, "bold"), fg="#333333", bg="#F0F0F0")
label.pack(pady=20)

# Crear botones con estilización
button_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049", "padx": 20, "pady": 10}

button1 = tk.Button(root, text="Abrir archivo 1", command=open_file1, **button_style)
button1.pack(pady=10)

button2 = tk.Button(root, text="Abrir archivo 2", command=open_file2, **button_style)
button2.pack(pady=10)

# Iniciar el loop de la ventana
root.mainloop()
