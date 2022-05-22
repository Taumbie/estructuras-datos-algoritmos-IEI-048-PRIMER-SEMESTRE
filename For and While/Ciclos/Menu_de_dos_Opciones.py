#Crear un programa en python que permita lo siguiente:
#Maquina de bebidas
#-Cocacola 500ml = 1200
#-Fanta 500ml = 1100
#-Sprite 500ml = 1100
#-Monster 473ml =1800
#-Score Gorilla 50ml =1600
#El cliente debe poder seleccionar una bebida e indicar cuantas de esas quiere comprar
#El programa debe realizar el cobro, solicitar con cuanto dinero pagar y dar vuelto si es necesario


#Menu

opcion = 1
while(opcion!=7):
    print("seleccione una opcion")
    print("1- Coca cola 500ml = 1200  2- Fanta 500ml = 1100 3- Sprite 500ml = 1100 =1800 4- Monster 473ml  5- 7-Salir")
    opcion = int(input())
    if(opcion==1):
        n1=float(input("Ingrese Numero 1 : "))
        n2=float(input("Ingrese Numero 2 : "))
        print("La Suma Es",n1+n2)
    elif(opcion==2):
        n1=float(input("Ingrese Numero 1 : "))
        n2=float(input("Ingrese Numero 2 : "))
        print("La Resta Es ",n1-n2)
    elif(opcion==3):
        n1=float(input("Ingrese Numero 1 : "))
        n2=float(input("Ingrese Numero 2 : "))
        print("La Multiplicacion Es",n1*n2)
    elif(opcion==4):
        n1=float(input("Ingrese Numero 1 : "))
        n2=float(input("Ingrese Numero 2 : "))
        while(n1==0):
            n1=float(input("Ingrese Numero 1 : ")) 

        while(n2==0):
            n2=float(input("Ingrese Numero 2 : "))
        print("La Division Es",n1/n2)
    elif(opcion==5):
        n1=float(input("Ingrese Numero 1 : "))
        n2=float(input("Ingrese Numero 2 : "))
        print("El Elevado Es",n1**n2)
    elif(opcion==6):
        n1=int(input("Ingrese Numero 1 : "))
        n2=int(input("Ingrese Numero 2 : "))
        while(n1>n2):
            n2=int(input("Ingrese Numero 2 : "))
        print("El Rango Entre Dos Numeros Es",n1, "Y" ,n2, "Son:")
        for i in range(n1,n2+1):
            print(i)




print("Fin Del Menu")