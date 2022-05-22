"""
Las listas son un tipo de coleccion mutable 
por lo tanto, despues de crear una lista podemos:
agregar un nuevo elemento, modificar un elemento, eliminar un elemento

se identifica al declararlas con []
"""

listaAlumnos = []
#Agregar elemento a la lista
listaAlumnos.append("José Ferreira")
listaAlumnos.insert(0, "Juanito Perez")

miNombre = input("Ingrese su nombre : ")
listaAlumnos.append(miNombre)
# Eliminar un elemento de la lista
#listaAlumnos.remove ("José")
# Modificar un elemento de la lista
listaAlumnos[0] = "Juanito Vegas"
# La función len sirve para contar los elementos de la lista
print("Hay",len(listaAlumnos),"alumnos en el curso")
for nombre in listaAlumnos:
    print (nombre)