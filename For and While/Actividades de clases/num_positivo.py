#Pedir un numero positivo al usuario una y otra vez hasta que el usuario lo haga correctamente:
n = int(input("Escriba un numero positivo: "))
while n <= 0:
    n = int(input("Dije... escribe un numero POSITIVO: "))
print("Gracias por su colaboracion")