from tkinter import *

window = Tk()

window.title("Calculadora ")

window.geometry("650x350")

label = Label(text="File")
text = Entry(window)
label.pack()
text.pack()

button = Button(window, text="Enviar")
button.pack()

window.mainloop()