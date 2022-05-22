"""
Ciclo for()
ciclo repetivo que nos permite navegar en un rango
 de numeros y tambien nos sirve par 
recorrer colecciones de datos
"""

for numero in range (1,10):
    print(numero)

for numero in range (1,101):
    print(numero)

"""
muestre en pantalla los numero pares entre el 1 y el 1000

"""
for numero in range (1,1001):
    if (numero%2==0):
        print(numero)

n1 = int(input("Ingrese Rango 1\n"))
n2 = int(input("Ingrese Rango 2\n"))
for numero in range (n1,n2):
    print(numero)
        
