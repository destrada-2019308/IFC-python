import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import pandas as pd
import warnings
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import shutil

warnings.filterwarnings('ignore')
root = tk.Tk() 
root.title("Conversor de IFC a Excel")
root.geometry("650x550")

file = 0 
classNames = 0
ifcFile = 0 

def abrir():
    global file
    global classNames
    global ifcFile
    file = filedialog.askopenfilename()
    print('Esto es file',file)   

    if file: 
        label.config(text=f"File selected: {file}")
        destino = './modal'
        shutil.copy(file, destino)
        ifcFile = ifcopenshell.open(file)
        classes = ifcFile.by_type("IfcProduct")
        classNames = [ className.is_a() for className in classes ]
        classNames = list(set(classNames))
        classNames.sort()
    else: 
        print('Debe elegir un archivo IFC')

def guardar():
    #Esta funcion guarda el archivo excel donde el usuario deseé#
    global file
    global classNames
    global ifcFile 
    fileSave = filedialog.asksaveasfilename(defaultextension='xlsx', filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    print(fileSave)

    if fileSave:
        with pd.ExcelWriter(fileSave, engine='openpyxl') as writer:
            for className in classNames:
                objects = ifcFile.by_type(className)
                result = pd.DataFrame()
                for object in objects:
                    data = {}
                    psets = ifcopenshell.util.element.get_psets(object)
                    for value in psets.items():
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
                for col in enumerate(worksheet.columns): 
                    worksheet.column_dimensions[col[0].column_letter].width = 20    
    else: 
        print('Debe de selecionar una ruta para guardar')   

btnFile = Button(root, pady=10, padx=10, text='Abrir IFC', command=abrir)
btnFile.place(x=100, y=100)

frame = Frame(root, width=100, height=150)
frame.pack()

label = Label(root , text='Selecciona un archivo para convertir', font=("Helvetica", 14, "bold"), fg="#333333", bg="#F0F0F0")
label.pack(pady=20)


btnSave = Button(root, pady=10, padx=10, text='Descargar Excel', command=guardar)
btnSave.place(x=175, y=100)

root.mainloop()