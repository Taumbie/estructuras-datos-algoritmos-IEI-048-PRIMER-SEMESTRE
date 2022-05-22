"""
Ciclo While() :
En el ciclo while debemos establecer una comparacion, 
si la comparacion resulta en verdadero las instrucciones
que pertenezcan al ciclo while se ejecutaran, de lo contrario
el ciclo finalizara.

"""

n1 = 10
n2 = 12

while(n1<n2):
    print("Intruccion del Ciclo While")
    n1=20
print("Instruccion Fuera del Ciclo While")

#Solicitar una letra hasta que ingresen una letra p mostrar mensaje correcto

letra=input("Ingrese Una Letra\n")
while (letra!="p"):
    print("No Ingresaste una p, Intente Nuevamente")
    letra=input("Ingrese una Letra\n")

print("Correcto")

"""
solicitar un numero hasta ke el numero sea mayor a 100
"""

N=int(input("Ingrese Un Numero\n"))
while(N<=100):
    print("No Ingreso Numero Mayor a 100")
    print("Intente Nuevamente")
    N=int(input("Ingrese Un Numero\n"))

print("Numero Mayor a 100")

"""
solicitar un numero hasta que el numero ingresado sea un 0
luego mostrar la suma de todos los numeros ingresados
"""
S=0
Num1=float(input("Ingrese Un Numero\n"))
while(Num1!=0):
    S=S+Num1
    print("Reintente")
    Num1=float(input("Ingrese Un Numero\n"))
print("Numero Correcto")
print("La Suma Es : ",S)

"""
solicitar un numero hasta que el numero ingresado sea un 0 
luego mostrar los numero pares ingreso
"""
Par=0
Num5=float(input("Ingrese Un Numero\n"))
while (Num5 != 0):
    if(Num5%2==0):
        Par=Par+1
    Num5=float(input("Ingrese Un Numero\n"))
print("Correcto")
print("La Cantidad de Numeros Pares",Par)


