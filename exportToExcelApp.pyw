import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

file = "./modal/IFC-2-1.ifc"
ifcFile = ifcopenshell.open(file)
 

classes = ifcFile.by_type("IfcProduct")

classNames = [ className.is_a() for className in classes ]

classNames = list(set(classNames))

classNames.sort()

print(classNames)

fileName = "result.xlsx"

with pd.ExcelWriter(fileName, engine='openpyxl') as writer:
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


