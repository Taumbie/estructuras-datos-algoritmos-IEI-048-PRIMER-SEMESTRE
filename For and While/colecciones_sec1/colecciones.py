# REPASO COLECCIONES
# -Tuplas        ---> ()
# -Listas        ---> []
# -Diccionarios  ---> {}

"""
Las colecciones son un tipo de variable que pueden almacenar varios datos
sin importar su tipo, es decir un tupla por ejemplo puede almacenar 
números enteros, números flotantes, cadenas de texto, valores logicos ( True or False )
o una tupla, lista o diccionario.
"""

#Tuplas
America = ("Chile", "Brasil", "Argentina")
# Las tuplas no pueden sufrir modificaciones despues de ser definidas
print (America[:])
#              ^ Indice


#Listas

miLista = [5.1,6.0,4.5]
miLista.insert(1, 3.0)
miLista.append(4.0)
# Modificar un elemento segun su indice
miLista[1] = 2.0
#          ^ le da un nuevo valor
miLista.remove(4.0)
#miLista.pop()
acumulador=0
for l in miLista:
    print("Tu nota men: ",l)
    acumulador+=l
promedio = acumulador/len(miLista)
print("El promedio es: ", promedio)
print("La lista tiene",len(miLista),"notas")


#Diccionarios
#Utilizar para describir un elemento u objeto
persona = {"nombre":"Marcelo","apellido":"Perez","edad":20}
#             ^ Clave
persona["ciudad"] = "Concepción"


print(persona["edad"])

print("El nombre completo es: ",persona["nombre"],persona["apellido"])
print("Y su edad es: ",persona["edad"],"años.")
print("Vive en la ciudad de: ",persona["ciudad"])



"""
Tupla: se puede definir una tupla vacia pero no serviria de nada al definir.(sin elementos)
Lista: se puede definir una lista vacia, son modificables
Diccionarios: igual se pueden definir vacias, se pueden modificar.
"""