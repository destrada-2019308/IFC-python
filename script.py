import ifcopenshell
import ifcopenshell.util.element as Element

model = ifcopenshell.open('./modal/IFC-1-1.ifc')

#CREAMOS FUNCIÓN PARA FILTRAR POR TIPO
def allData (model, type):
    #ARREGLO VACÍO
    data = []
    #EL FILTRO LO GUARDAMOS EN objects
    objects = model.by_type(type)

    for object in objects:
        #GUARDAMOS CADA UNO DE LOS ID´S OBJECT 
        id = object.id()
        #EL APPEND NOS CREA LOS OBJETOS AL FINAL DE LA LISTA - EN ESTE CASO data QUE ES UN ARRAY -
        data.append({
            "ExpressID": object.id(),
            "GlobalId": object.GlobalId,
            "Class": object.is_a(),
            "PredefinedType": Element.get_predefined_type(object),
            "Name": object.Name,
            "Level": Element.get_container(object).Name
            if Element.get_container(object)
                else  "",
            "ObjectType": Element.get_type(object).Name
            if Element.get_type(object)
                else "",
            "QuantitySets": Element.get_psets(object, qtos_only=True),
            "PropertySets": Element.get_psets(object, psets_only=True),
            "FIN": "LOREM IPSUM"
        })
    return data

import pprint

pp = pprint.PrettyPrinter()
datos = allData(model, 'IfcBuildingElement')

import json
with open('./modal/test.json', 'w') as f: 
    json.dump(datos, f)
