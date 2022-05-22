"""
crear un programa que almacene paises, los paises tienen nombre, continente, poblacion e idioma nativo

registrar paises en este programa
"""
# Lista para almacenar todos los paises
listaPaises = []

# Solicitar los datos de los paises para guardarlos en el diccionario

def RegistrarPais():
    # Diccionario para almacenar los detalles de los paises
    detallesPais = {}
    print("Ingrese los siguientes datos")
    print("Ingrese el nombre del pais : ")
    # Leer el dato
    nombre = input()
    print("Ingrese el continente del pais : ")
    # Leer el dato 
    continente = input()
    print("Ingrese la población del pais (número) : ")
    # Leer el dato 
    poblacion = int(input())
    print("Ingrese el idioma nativo del pais : ")
    # Leer el dato 
    idioma = input()
    # Agregar los datos al diccionario
    detallesPais["nombre"] = nombre
    detallesPais["continente"] = continente
    detallesPais["poblacion"] = poblacion
    detallesPais["idioma"] = idioma

    # Agregar el pais completo a la lista
    listaPaises.append(detallesPais)

    for pais in listaPaises:
        print(pais)
    menu()


"""
Creen una función que imprima un menú con las siguientes
opciones :
1 - Registrar pais
2 - Ver los paises
3 - Eliminar un pais
"""

def menu():
    print("Seleccione un opcion : ")
    print("1 - Registrar pais")
    print("2 - Ver los paises")
    print("3 - Eliminar un pais")
    opcion = int(input())
    if (opcion == 1):
        RegistrarPais()
    elif (opcion == 2):
        verPaises()

def verPaises():
    for pais in listaPaises:
        print("el pais es ",pais["nombre"], "su continente es ",pais["continente"],"su poblacion es de ",pais["poblacion"],"su idioma natal es ",pais["idioma"])
    menu()


menu()