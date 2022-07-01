"""
    Las frutas y verduras son las siguientes:
    a- papa premiun - 1290 kg
    b- manzana - 1690 kg
    c- tomate - 1390 kg
    d- palta hass - 4990 kg
    e- naranja - 1000 kg
    f- platano - 990 kg

    sni se venden mas de 5 kg se aplica un descuento de 10% al total.
    si se venden mas de 10 kg se aplica un descuento del 15% al total.
"""
opcion = ""
print("Bienvenido a la verdulería")
print("""
Las frutas y verduras son las siguientes:
a- papa premiun - 1290 kg
b- manzana - 1690 kg
c- tomate - 1390 kg
d- palta hass - 4990 kg
e- naranja - 1000 kg
f- platano - 990 kg
Seleccione el producto a comprar
""")

opcion = input()
if opcion == "a" or opcion == "A" :
    print("Seleccionaste : papa premiun, su valor es 1290 el kg")
    cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
    total = cantidad * 1290
elif opcion == "b" or opcion == "B" :
    print("Seleccionaste : manzana, su valor es 1690 el kg")
    cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
    total = cantidad * 1690
elif opcion == "c" or opcion == "C" :
    print("Seleccionaste : tomate, su valor es 1390 el kg")
    cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
    total = cantidad * 1390
elif opcion == "d" or opcion == "D" :
    print("Seleccionaste : palta hass, su valor es 4990 el kg")
    cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
    total = cantidad * 4990
elif opcion == "e" or opcion == "E" :
    print("Seleccionaste : naranja, su valor es 1000 el kg")
    cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
    total = cantidad * 1000
elif opcion == "f" or opcion == "F" :
    print("Seleccionaste : platano, su valor es 990 el kg")
    cantidad = int(input("Ingrese la cantidad en kg que desea comprar : "))
    total = cantidad * 990

if cantidad > 10 :
    print("Se aplica descuento del 15%")
    nuevo_total = total - (total*15/100)
    print("Debe pagar : $",nuevo_total)
elif cantidad > 5 :
    print("Se aplica descuento del 10%")
    nuevo_total = total - (total*10/100)
    print("Debe pagar : $",nuevo_total)
else :
    print("No tiene descuento")
    print("Debe pagar : $",total)    

