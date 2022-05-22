# Crear un programa en python que permita lo siguiente (Maquina de bebidas)

# Cocacola 500ml = 1200
# Fanta 500ml = 1100
# Sprite 500ml = 1100
# Monster 473ml =1800
# Score Gorilla 500ml =1600

# El cliente debe poder seleccionar una bebida e indicar cuantas de esas quiere comprar
# El programa debe realizar el cobro, solicitar con cuanto dinero pagar y dar vuelto si 
# es necesario
import time

def mostrarMenu():
    print("¿Que Bebida deseas llevar? Tengo: ")
    print("1. Coca Cola 500ml")
    print("2. Fanta 500ml")
    print("3. Sprite 500ml")
    print("4. Monster 473ml")
    print("5. Score Gorilla 500ml")
    print("6. Salir")
    opcionElegida = 0
    while opcionElegida < 1 or opcionElegida > 6:
        opcionElegida = int(input("Selecciona una opcion: "))
    return opcionElegida

def obtenerTotalAPagar(opcion):
    cantidad = 0
    while cantidad < 1:
        cantidad = int(input("Cuantas unidades deseas llevar? "))
    precio = 0
    if opcion == 1:
        precio = 1200
    elif opcion == 2:
        precio = 1100
    elif opcion == 3:
        precio = 1100
    elif opcion == 4:
        precio = 1800
    elif opcion == 5:
        precio = 1600
    print("El total a pagar es: ", cantidad * precio)
    return cantidad * precio

def pagar(total):
    dinero = 0
    while dinero < total:
        dinero = int(input("Ingrese el dinero con el cual va a pagar: "))
        if dinero < total:
            print("Su dinero es insuficiente, intentelo nuevamente")
    return dinero - total

opcion = 0
while(opcion != 6):
    print("Menu: ")
    opcion = mostrarMenu()
    if opcion < 6:
        total = obtenerTotalAPagar(opcion)
        vuelto = pagar(total)
        print("------------------------------")
        print("------------------------------")
        print("------------------------------")
        if vuelto > 0:
            print("Su vuelto es: ", vuelto)
        print("Gracias por su compra")
        print("------------------------------")
        print("------------------------------")
        print("------------------------------")
        time.sleep(3) 
    elif opcion == 6:
        print("Has seleccionado Salir, hasta luego...")
    else:
        print("Opcion incorrecta")