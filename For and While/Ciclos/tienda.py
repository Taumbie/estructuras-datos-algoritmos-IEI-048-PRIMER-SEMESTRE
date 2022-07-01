from time import sleep
from os import system, name

menuPrint = """
1. Agregar producto al carrito
2. Eliminar producto del carrito
3. Mostrar carrito
4. Pagar carrito
5. Historial de compras
6. Salir"""

productosDisponibles = {
    1: ("Papa premium", 1290),
    2: ("Manzana", 1690),
    3: ("Tomate", 1390),
    4: ("Palta hass", 4990),
    5: ("Naranja", 1000),
    6: ("Platano", 990)
}

productosPrint = """
Productos dispopnibles:
1. Papa premium - $1.290/kg
2. Manzana - $1.690/kg
3. Tomate - $1.390/kg
4. Palta hass - $4.990/kg
5. Naranja - $1.000/kg
6. Platano - $990/kg
"""

carrito = []
historialCompras = []

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    try:
        print(menuPrint)
        opcion = int(input("Ingrese una opcion: "))
        if opcion < 1 or opcion > 6:
            raise ValueError
        return opcion
    except:
        print("Opcion invalida")
        return menu()

def preguntarCantidad():
    try:
        cantidad = int(input("Ingrese la cantidad en kg: "))
        if cantidad < 1:
            raise ValueError
        return cantidad
    except:
        print("Cantidad invalida")
        return preguntarCantidad()

def agregarProducto():
    try:
        print(productosPrint)
        producto = int(input("Que producto desea agregar: "))
        if producto < 1 or producto > 6:
            raise ValueError
        cantidad = preguntarCantidad()
        carrito.append((producto, cantidad))
    except:
        print("Opcion invalida")
        return agregarProducto()

def mostrarCarrito(carrito):
    valorTotal = 0
    cantidadTotal = 0
    print('##############################################################')
    for i, producto in enumerate(carrito):
        etiqueta = productosDisponibles[producto[0]][0]
        cantidad = producto[1]
        valor = productosDisponibles[producto[0]][1] * producto[1]
        print(f"{i + 1}: {etiqueta} - {cantidad}kg - ${valor}")
        valorTotal += valor
        cantidadTotal += cantidad
    if cantidadTotal > 5 and cantidadTotal <= 10:
        valorTotal-= (valorTotal * 0.1)
        print("Se aplica un descuento del 10% en su total")
    elif cantidadTotal > 10:
        valorTotal-= (valorTotal * 0.15)
        print("Se aplica un descuento del 15% en su total")
    print(f"Total: ${valorTotal} - {cantidadTotal}kg")
    print('##############################################################')
    return valorTotal

def eliminarProducto():
    try:
        mostrarCarrito(carrito)
        if len(carrito) == 0:
            print("No hay productos en el carrito")
            return
        producto = int(input("Que producto desea eliminar (0 para cancelar): "))
        if producto < 0 or producto > len(carrito):
            raise ValueError
        if producto == 0:
            return
        carrito.pop(producto - 1)
    except:
        print("Opcion invalida")
        return eliminarProducto()

def pagarCarrito():
    try:
        valorTotal = mostrarCarrito(carrito)
        if valorTotal == 0:
            print("No hay productos en el carrito")
            return
        print("Pago:")
        pago = int(input("Ingrese el pago: "))
        if pago < valorTotal:
            raise ValueError
        historialCompras.append(carrito.copy())
        carrito.clear()
        vuelto = pago - valorTotal
        if vuelto > 0:
            print(f"Su vuelto es: ${vuelto}, gracias por su compra")
        else:
            print("Gracias por su compra")
    except:
        print("Valor menor al total")
        return pagarCarrito()

def historial():
    print("Historial de compras:")
    for i, carrito in enumerate(historialCompras):
        print(f"Compra nro. {i + 1}:")
        mostrarCarrito(carrito)

if __name__ == "__main__":
    clear()
    opcionElegida = menu()
    while opcionElegida != 6:
        if opcionElegida == 1:
            agregarProducto()
        elif opcionElegida == 2:
            eliminarProducto()
        elif opcionElegida == 3:
            mostrarCarrito(carrito)
            input("Pulse enter para continuar")
        elif opcionElegida == 4:
            pagarCarrito()
        elif opcionElegida == 5:
            historial()
            input("Pulse enter para continuar")
        sleep(2)
        clear()
        opcionElegida = menu()
        if opcionElegida == 6:
            print("Gracias por usar nuestra tienda")