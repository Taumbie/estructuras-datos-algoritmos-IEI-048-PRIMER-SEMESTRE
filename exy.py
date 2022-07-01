lista= []
Usuarios={"usuario1":"l_leiva",
          "clave1":"02401325",
          "usuario2":"b_leiva",
          "clave2":"123456"}

def login():
    while True:
        Usuario = input("Ingrese Usuario ")
        Pass = input("Ingrese Contraseña ")

        if (Usuarios['usuario1'] or Usuarios ['usuario2']) == Usuario and (Usuarios['clave1'] or Usuarios['clave2']) == Pass:
            iterativo()
        else:
            print("ALV")

def agregarlista():
    print("Agregar un producto a la lista")
    producto = input("ingrese el nombre del producto que desea agregar: ")
    lista.append(producto)
    print("producto agregado")
    print("___________________")

def quitarlista():
    print("Quitar un producto a la lista")
    eliminado = input("ingrese el nombre del producto que desea quitar: ")
    lista.remove(eliminado)
    print("producto Eliminado")
    print("____________________")

def listar():
    print("Mostrar lista del super")
    for x in lista:
        print(x)
    print("_______________________")

def menu():
    print("Bienvenido a la lista de supermercado")
    print("ingrese una opción: ")
    print("1. Agregar producto")
    print("2. Quitar producto")
    print("3. Mostrar lista del super")
    print("4. salir")

def iterativo():
    while True:
        menu()
        opcion = int( input())
        if opcion == 1:
            agregarlista()
        elif opcion == 2:
            quitarlista()
        elif opcion == 3:
            listar()
        elif opcion == 4:
            print("Hasta pronto")
            break

if __name__ == '__main__':
    login()