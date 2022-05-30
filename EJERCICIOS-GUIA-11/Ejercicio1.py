# Diseña un programa que solicite la lectura de un número entre 10 y 50. Si el usuario 
#teclea un número fuera del rango valido, el programa solicitara nuevamente la introducción
#del valor cuantas veces sea menester.


n1 = int(input("Ingrese un numero entre 10 y 50: "))
for i in range(10, 50):
    if n1 >= int(10) and n1 <= int(50):
        print ("El número",n1,"esta dentro del rango correcto")
        break
    else:
        print ("El número esta fuera del rango solicitado")
        n1 = int(input("Ingrese un numero entre 10 y 50: "))