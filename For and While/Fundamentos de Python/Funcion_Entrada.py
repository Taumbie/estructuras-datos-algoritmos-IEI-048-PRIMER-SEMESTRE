"""
Funcion de entrada (input())

nos permite recoger datos desde el teclado, pero solo en 
formato str.


"""
numero1 = input("Ingrese un Numero : ")
print("El Numero Ingresado es",numero1)


numero1 = input("Ingrese un Numero : ")
numero2 = input("Ingrese un Numero : ")
print("El numero Ingresado es",numero1+numero2)

numero1 =float(input("Ingrese un Numero : "))
numero2 =float(input("Ingrese un Numero : "))
print("La Suma es",numero1+numero2)
print("La Resta Es",numero1-numero2)
print("La Multiplicacion Es",numero1*numero2)
try:
    print("La Division Decimal Es",numero1/numero2)
except ZeroDivisionError:
    print("sin cero wn")
try:
    print("La Division Entera Es",numero1//numero2)
except ZeroDivisionError:
    print("sin cero wn")
try:
    print("El Resto De La Division Es",numero1%numero2)
except ZeroDivisionError:
    print("sin cero wn")
print("El Numero Uno Elevado Al Numero Dos Es",numero1**numero2)


#leer dos numeros enteros y utiluzando todos los 
# operadores aritmeticos mostrar el resultado en pantalla 

