#Hacer un algoritmo que dado dos numeros ingresados por teclado imprima todos 
# los numeros impares que hay en el rango que conforman ambos numeros. No deben ser iguales
n1 = int(input("Ingrese un rango: "))
n2 = int(input("Ingrese otro rango: "))
for x in range(n1,n2):
    if (x%2 != 0):
        print(x, end=" ")
    else:
        print("El número",x,"es impar")
