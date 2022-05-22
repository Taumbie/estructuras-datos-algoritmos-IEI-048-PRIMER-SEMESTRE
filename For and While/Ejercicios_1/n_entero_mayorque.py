# Lea por teclado un numero entero y diga si es mayor a 10, hasta que escriba el numero impar
# Mostrar por pantalla el numero leido
entrada = 0
while entrada % 2 == 0:
    entrada = int(input("Ingrese un numero entero: "))
    if entrada > 10 and entrada % 2 == 0:
        print('El numero es mayor a 10')
    elif entrada % 2 == 1:
        print('El numero es impar')

