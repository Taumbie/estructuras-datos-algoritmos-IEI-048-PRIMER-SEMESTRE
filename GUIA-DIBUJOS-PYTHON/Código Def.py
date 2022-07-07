from concurrent.futures.process import _global_shutdown
from sre_parse import GLOBAL_FLAGS


lista= []
Usuarios={"usuario1":"cristobal",
          "clave1":"123",
          "usuario2":"alejandro",
          "clave2":"321"}

def login():
    while True:
        Usuario = input("Ingrese Usuario ")
        Pass = input("Ingrese Contraseña ")
        
        if (Usuarios['usuario1'] and Usuarios ['clave1']) == Pass or (Usuarios['usuario2'] and Usuarios['clave2']) == Pass:
            menu ()
        else:
            print("ALV")
        break

opcion = ""
def menu ():
    opcion = ""
    print("Bienvenido a la verdulería")
    input("""
    Las frutas y verduras son las siguientes:
    1- papa premiun - 1290 kg
    2- manzana - 1690 kg
    3- tomate - 1390 kg
    4- palta hass - 4990 kg
    5- naranja - 1000 kg
    6- platano - 990 kg
    Seleccione el producto a comprar
    """)
    
def opciones ():
    while True:
        menu()
        if opcion == 1:
            opcion_1 ()
        elif opcion == 2:
            opcion_2 ()
        elif opcion == 3:
            opcion_3 ()
        elif opcion == 4:
            opcion_4 ()
        elif opcion == 5:
            opcion_5()

def opcion_1 ():
    try:
        print("Seleccionaste : papa premiun, su valor es 1290 el kg")
        cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
        total = cantidad * 1290
        print(f"Su total a pagar es:{total} ")
        if cantidad > 10:
            print("Se aplica descuento del 15%")
            nuevo_total = total - (total*15/100)
            print("Debe pagar: $", nuevo_total)
        elif cantidad > 5:
            print("Se aplica descuento del 10%")
            nuevo_total = total - (total*10/100)
            print("Debe pagar: $", nuevo_total)
        else:
            print("No tiene descuento ")
            print("Debe pagar: $", total)
    except (ValueError, UnboundLocalError):
        print("Error")
        #return opcion_1()
    #menu ()

def opcion_2 ():
    try:
        print("Seleccionaste : manzana, su valor es 1690 el kg")
        cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
        total = cantidad * 1690
        print(f"Su total a pagar es:{total} ")
        if cantidad > 10:
            print("Se aplica descuento del 15%")
            nuevo_total = total - (total*15/100)
            print("Debe pagar: $", nuevo_total)
        elif cantidad > 5:
            print("Se aplica descuento del 10%")
            nuevo_total = total - (total*10/100)
            print("Debe pagar: $", nuevo_total)
        else:
            print("No tiene descuento ")
            print("Debe pagar: $", total)
    except (ValueError, UnboundLocalError):
        print("Error")
        return opcion_1()
    menu ()

def opcion_3 ():
    try:
        print("Seleccionaste : tomate, su valor es 1390 el kg")
        cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
        total = cantidad * 1390
        print(f"Su total a pagar es:{total} ")
        if cantidad > 10:
            print("Se aplica descuento del 15%")
            nuevo_total = total - (total*15/100)
            print("Debe pagar: $", nuevo_total)
        elif cantidad > 5:
            print("Se aplica descuento del 10%")
            nuevo_total = total - (total*10/100)
            print("Debe pagar: $", nuevo_total)
        else:
            print("No tiene descuento ")
            print("Debe pagar: $", total)
    except (ValueError, UnboundLocalError):
        print("Error")
        return opcion_1()
    menu ()

def opcion_4 ():
    try:
        print("Seleccionaste : palta hass, su valor es 4990 el kg")
        cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
        total = cantidad * 4990
        print(f"Su total a pagar es:{total} ")
        if cantidad > 10:
            print("Se aplica descuento del 15%")
            nuevo_total = total - (total*15/100)
            print("Debe pagar: $", nuevo_total)
        elif cantidad > 5:
            print("Se aplica descuento del 10%")
            nuevo_total = total - (total*10/100)
            print("Debe pagar: $", nuevo_total)
        else:
            print("No tiene descuento ")
            print("Debe pagar: $", total)
    except (ValueError, UnboundLocalError):
        print("Error")
        return opcion_1()
    menu ()

def opcion_5 ():
    try:
        print("Seleccionaste : naranja, su valor es 1000 el kg")
        cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
        total = cantidad * 1000
        print(f"Su total a pagar es:{total} ")
        if cantidad > 10:
            print("Se aplica descuento del 15%")
            nuevo_total = total - (total*15/100)
            print("Debe pagar: $", nuevo_total)
        elif cantidad > 5:
            print("Se aplica descuento del 10%")
            nuevo_total = total - (total*10/100)
            print("Debe pagar: $", nuevo_total)
        else:
            print("No tiene descuento ")
            print("Debe pagar: $", total)
    except (ValueError, UnboundLocalError):
        print("Error")
        return opcion_1()
    menu ()
        
def opcion_6 ():
    try:
        print("Seleccionaste : platano, su valor es 990 el kg")
        cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
        total = cantidad * 990
        print(f"Su total a pagar es:{total} ")
        if cantidad > 10:
            print("Se aplica descuento del 15%")
            nuevo_total = total - (total*15/100)
            print("Debe pagar: $", nuevo_total)
        elif cantidad > 5:
            print("Se aplica descuento del 10%")
            nuevo_total = total - (total*10/100)
            print("Debe pagar: $", nuevo_total)
        else:
            print("No tiene descuento ")
            print("Debe pagar: $", total)
    except (ValueError, UnboundLocalError):
        print("Error")
        return opcion_1()
    menu ()

if __name__ == '__main__':
    login()
