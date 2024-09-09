import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import pandas as pd
import warnings

import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil

warnings.filterwarnings('ignore')

root = tk.Tk()
root.title("Conversor de IFC a Excel")
root.geometry("850x555")
root.resizable(0,0)
root.config(background="#fcfcfc")

title = Label(root, text="IFC a XLS convertidor", font=("Helvetica", 25, "bold"), fg="#000", background="#fcfcfc")
title.pack(pady=30)

fileOpen = '' 
classNames = ''
ifcFile = ''

label = Label(root , text='Selecciona un archivo para convertir', font=("Helvetica", 14, "bold"), fg="#000", background="#fcfcfc" )
label.pack(pady=20, padx=50)

def abrirArchivo():
    global fileOpen
    global classNames 
    global ifcFile
    fileOpen = filedialog.askopenfilename()
    if fileOpen:
        txt = 'File Selected ' + fileOpen

        print(fileOpen)
        print(txt)

        label.config(text=txt)
        ifcFile = ifcopenshell.open(fileOpen)
        classes = ifcFile.by_type("IfcProduct")
        classNames = [ className.is_a() for className in classes]
        classNames = list(set(classNames))
        classNames.sort()
    else: 
        print('Debe elegir un archivo IFC')


def guardarExcel():
    global ifcFile
    global classNames
    fileSave = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    print(fileSave)
    if fileSave:
        with pd.ExcelWriter(fileSave, engine='openpyxl') as writer:
            for className in classNames:
                objects = ifcFile.by_type(className)
                result = pd.DataFrame()
                for object in objects:
                    data = {}
                    psets = ifcopenshell.util.element.get_psets(object)
                    for name, value in psets.items():
                        if isinstance(value, dict):
                            for key, val in value.items():
                                data[key] = val
                            else:
                                pass
                    classDf = pd.DataFrame(data, index=[0])
                    result = pd.concat([result, classDf], ignore_index=True)
                if(result.empty):
                    continue
                result.to_excel(writer, sheet_name=className, index=False)
                worksheet = writer.sheets[className] 
                for idx, col in enumerate(worksheet.columns): 
                    worksheet.column_dimensions[col[0].column_letter].width = 20
        texto = 'Archivo guardado en: ' + fileSave
        label.config(text=texto)
    else: 
        print('Debe elegir una lugar para guardar el archivo')


frame = Frame(root, width=775, height=250, background="#ffffff", padx=10, pady=10)
frame.config(cursor="")    
frame.config(relief="groove")
frame.config(bd=5)         
frame.place(x=40, y=150)

btnFileOpen = Button(frame, padx=25, pady=25, text='Buscar archivo IFC', command=abrirArchivo, background="#588cfc", font="large", fg="#fff", bd=0)
btnFileOpen.place(x=175, y=65)

btnSave = Button(frame, padx=25, pady=25, text='Descargar Excel', command=guardarExcel, background="#588cfc", fg="#fff", bd=0, font="large")
btnSave.place(x=400, y=65)

def hover(button, color1, color2):
    button.bind("<Enter>", func=lambda e: button.config(
        background=color1 ))
 
    button.bind("<Leave>", func=lambda e: button.config(
        background=color2 ))
hover(btnFileOpen, "#5084ec", "#588cfc")

hover(btnSave, "#5084ec", "#588cfc")


root.mainloop()