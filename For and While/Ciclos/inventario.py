#Tenga un login por diccionario, el cual si no se encuentra el usuario no puede
#acceder al sistema
#Crea un sistema de inventario que pueda agregar productos, 
#quitar productos y mostrar toda la lista de productos anexados.

productos = []

login = {"usuario1": "profesorcito","contraseña1": "123","usuario2": "estrella","contraseña2": "1234"}



def iniciosesion():
    while True:
        usuario = input("Ingrese su usuario:\n ")
        password = input("Ingrese su password:\n ")
        if (login["usuario1"] or login["usuario2"]) == usuario and (login["contraseña1"] or login["contraseña2"]) == password:
            menu()
            proceso()
        else:
            print ("Usuario o contraseña incorrectos")

def menu():
 print("Seleccione una opcion: \n"
    "1. Agregar productos\n"
    "2. Quitar productos\n"
    "3. Mostrar productos\n"
    "4. Terminar programa\n")

def agregar():
    agregar_producto = input("Ingrese el producto: ")
    productos.append(agregar_producto)
    print(productos)

def quitar():
    quitar_producto = input("Ingrese el producto: ")
    productos.remove(quitar_producto)
    print(productos)

def historial():
    for i in (productos):
        print(i)
def proceso():
    while True:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_productos = input("Ingrese su producto a añadir: ")
            productos.append(agregar_productos)
            print(productos)
        elif opcion == 2:
            quitar_productos = input("Ingrese su producto a quitar: ")
            productos.remove(quitar_productos)
            print(productos)
        elif opcion == 3:
            historial()    
        elif opcion == 4:
            break

if __name__ == "__main__":
    iniciosesion()
    menu()
    opcion = int(input("Ingrese una opcion: "))
    


