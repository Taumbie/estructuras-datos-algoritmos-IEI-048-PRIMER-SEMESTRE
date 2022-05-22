#Crear un programa en python que permita lo siguiente:
#Maquina de bebidas
#-Cocacola 500ml = 1200
#-Fanta 500ml = 1100
#-Monster 473ml =1800
#-Score Gorilla 500ml =1600
#El cliente debe poder seleccionar una bebida e indicar cuantas de esas quiere comprar
#El programa debe realizar el cobro, solicitar con cuanto dinero pagar y dar vuelto si es necesario


#Menu

opcion = 1
while(opcion != 7):
    print("")
    print("")
    print("¿Que Bebida deseas llevar? Tengo: ")
    print("")
    print("1- Coca cola 500ml =1200")
    print("2- Fanta 500ml = 1100")
    print("3- Sprite 500ml = 1100")
    print("4- Monster 473ml = 1800")
    print("5- Score Gorilla 500ml =1600")
    print("6- Salir")
    print("")
    opcion = int(input("Por Favor Seleccione Una De Las Opciones:"))
    
    if (opcion == 1):

        print("\nElegiste Cocacola 500ml\n")
        pago = int(input("Ingrese Dinero "))
        print("")
        precio = int(1200)
        if (pago < precio):
            pago = int(pago)
            precio = int(precio)
            print("Dinero Insuficiente, Por Favor Intentelo Nuevamente.")
            print("")
        else:
            total = pago - precio
            print ("Compra finalizada, su vuelto es:", total)
            print ("¡Gracias por su compra! ¡Vuelva Pronto! :D")
            print("")
    elif (opcion == 2):
        print("\nElegiste Fanta 500ml\n")
        pago = int(input("Ingrese Dinero "))
        print("")
        precio = int(1100)
        if (pago < precio):
            pago = int(pago)
            precio = int(precio)
            print("Dinero Insuficiente, Por Favor Intentelo Nuevamente.")
            print("")
        else:
            total = pago - precio
            print ("Compra finalizada, su vuelto es:", total)
            print ("¡Gracias por su compra! ¡Vuelva Pronto! :D")
            print("")
    elif (opcion == 3):
        print("\nElegiste Sprite 500ml\n")
        pago = int(input("Ingrese Dinero "))
        print("")
        precio = int(1100)
        if (pago < precio):
            pago = int(pago)
            precio = int(precio)
            print("Dinero Insuficiente, Por Favor Intentelo Nuevamente.")
            print("")
        else:
            total = pago - precio
            print ("Compra finalizada, su vuelto es:", total)
            print ("¡Gracias por su compra! ¡Vuelva Pronto! :D")
            print("")
    elif (opcion == 4):
        print("\nElegiste Monster 473 ml\n")
        pago = int(input("Ingrese Dinero "))
        print("")
        precio = int(1100)
        if (pago < precio):
            pago = int(pago)
            precio = int(precio)
            print("Dinero Insuficiente, Por Favor Intentelo Nuevamente.")
            print("")
        else:
            total = pago - precio
            print ("Compra finalizada, su vuelto es:", total)
            print ("¡Gracias por su compra! ¡Vuelva Pronto! :D")
            print("")
    elif (opcion == 5):
        print("\nScore Gorilla 500ml = 1600\n")
        pago = int(input("Ingrese Dinero "))
        print("")
        precio = int(1100)
        if (pago < precio):
            pago = int(pago)
            precio = int(precio)
            print("Dinero Insuficiente, Por Favor Intentelo Nuevamente.")
            print("")
        else:
            total = pago - precio
            print ("Compra finalizada, su vuelto es:", total)
            print ("¡Gracias por su compra! ¡Vuelva Pronto! :D")
            print("")
    elif (opcion == 6):
        print("")
        print("¡Que tenga un excelente día! ¡Vuelva Pronto! :D")
        print("")
    elif (pago < precio):
        print("")
        print("Dinero Insuficiente, Por Favor Intentelo Nuevamente.")
        print("")