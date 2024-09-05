import ifcopenshell
import ifcopenshell.util.element
model = ifcopenshell.open('./modal/IFC-2-1.ifc')

#print(model.schema)  
# USA EL IFC2X3 
walls = model.by_type('IfcWall') 
#wall = model.by_type('IfcWall')[0]
  
data = {}

#FOR para recorrer todos los arreglos 
for wall in range(len(walls)):
    print(wall)   
    wall1 = model.by_type('IfcWall')[wall]
    print(wall1)
    print("----------------------------------------")
    print(ifcopenshell.util.element.get_psets(wall1))
 
# 
"""
print(model.by_id(1))

walls = model.by_type('IfcWall')

print(walls[0])

print(len(walls))
"""#