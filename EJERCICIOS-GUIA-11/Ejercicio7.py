from time import sleep

import time
papa_premium = 1290
manzana = 1690
tomate = 1390
palta_hass = 4990
naranja = 1000
platano = 990

opcion = 1
while(opcion!=7):
    print("BIENVENIDO A LA TIENDA DE VERDURAS.")
    print("\n1-Papa premium: $1290 \n2-Manzana $1690 \n3-Tomate $1390 \n4-Palta Hass $4990 \n5-Naranja $1000 \n6-Platano $990 \n7-Salir" )
    opcion = int(input("¿Que desea llevar? "))

    if(opcion==1):

        print("¿Cuantos kilogramos desea llevar?")
        
        opcion2 = int(input())    

        if (opcion2 >= 8 and opcion2 <= 14):

            valor_original = opcion2 * papa_premium
            porcentaje_aumento = 10
            descuento = valor_original * (porcentaje_aumento / 100)   
            valor_con_descuento = valor_original - descuento
            print ("Se le a agregado un descuento de 10% por la compra de mas de 8 Kg")
            print(f"El valor con descuento es {valor_con_descuento}")
    
            compra=int(input("Ingrese Dinero\n"))
        
            while(compra<valor_con_descuento):

                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento

            if(compra>valor_con_descuento):     
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)
                

        elif(opcion2 >= 15):

            valor_original = opcion2 * papa_premium 
            porcentaje_aumento = 20
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento2 = valor_original - descuento
            print ("Se le a agregado un descuento de 20% por la compra de mas de 15 Kg")
            print(f"El valor con descuento es {valor_con_descuento2}")

            compra=int(input("Ingrese Dinero\n"))
        
            while(compra<valor_con_descuento2):

                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento2

            if(compra>valor_con_descuento2):   
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

           

        
            
    elif(opcion==2):

        print("¿Cuantos kilogramos desea llevar?")
        opcion2 = 1
        opcion2 = int(input())   

        if (opcion2 >= 8 and opcion2 <= 14):

            valor_original = opcion2 * manzana
            porcentaje_aumento = 10
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento = valor_original - descuento
            print ("Se le a agregado un descuento de 10% por la compra de mas de 8 Kg")
            print(f"El valor con descuento es {valor_con_descuento}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento

            if(compra>valor_con_descuento):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

        elif(opcion2 >= 15):

            valor_original = opcion2 * manzana

            porcentaje_aumento = 20
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento2 = valor_original - descuento
            print ("Se le a agregado un descuento de 20% por la compra de mas de 15 Kg")
            print(f"El valor con descuento es {valor_con_descuento2}")
            total = opcion2 * manzana
            print(f"El valor total es {total}")

    elif(opcion==3):

        print("¿Cuantos kilogramos desea llevar?")
        opcion2 = 1
        opcion2 = int(input())  

        if (opcion2 >= 8 and opcion2 <= 14):

            valor_original = opcion2 * tomate
            porcentaje_aumento = 10
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento = valor_original - descuento
            print ("Se le a agregado un descuento de 10% por la compra de mas de 8 Kg")
            print(f"El valor con descuento es {valor_con_descuento}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento

            if(compra>valor_con_descuento):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

        elif(opcion2 >= 15):

            valor_original = opcion2 * tomate
            porcentaje_aumento = 20
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento2 = valor_original - descuento
            print ("Se le a agregado un descuento de 20% por la compra de mas de 15 Kg")
            print(f"El valor con descuento es {valor_con_descuento2}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento2):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento2

            if(compra>valor_con_descuento2):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

    elif(opcion==4):

        print("¿Cuantos kilogramos desea llevar?")
        opcion2 = 1
        opcion2 = int(input())    

        if (opcion2 >= 8 and opcion2 <= 14):

            valor_original = opcion2 * palta_hass
            porcentaje_aumento = 10
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento = valor_original - descuento
            print ("Se le a agregado un descuento de 10% por la compra de mas de 8 Kg")
            print(f"El valor con descuento es {valor_con_descuento}")
        
            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento

            if(compra>valor_con_descuento):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

        elif(opcion2 >= 15):

            valor_original = opcion2 * palta_hass
            porcentaje_aumento = 20
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento2 = valor_original - descuento
            print ("Se le a agregado un descuento de 20% por la compra de mas de 15 Kg")
            print(f"El valor con descuento es {valor_con_descuento2}")

            total = opcion2 * palta_hass
            print(f"El valor total es {total}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento2):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento2

            if(compra>valor_con_descuento2):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

    elif(opcion==5):

        print("¿Cuantos kilogramos desea llevar?")
        opcion2 = 1
        opcion2 = int(input()) 

        if (opcion2 >= 8 and opcion2 <= 14):

            totalpapapremium = opcion2 * naranja
            valor_original = totalpapapremium
            porcentaje_aumento = 10
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento = valor_original - descuento
            print ("Se le a agregado un descuento de 10% por la compra de mas de 8 Kg")
            print(f"El valor con descuento es {valor_con_descuento}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento

            if(compra>valor_con_descuento):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

        elif(opcion2 >= 15):

            valor_original = opcion2 * naranja
            porcentaje_aumento = 20
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento2 = valor_original - descuento
            print ("Se le a agregado un descuento de 20% por la compra de mas de 15 Kg")
            print(f"El valor con descuento es {valor_con_descuento2}")

            total = opcion2 * naranja
            print(f"El valor total es {total}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento2):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento2

            if(compra>valor_con_descuento2):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

    elif(opcion==6):

        print("¿Cuantos kilogramos desea llevar?")
        opcion2 = 1
        opcion2 = int(input())  

        if (opcion2 >= 8 and opcion2 <= 14):

            valor_original = opcion2 * platano
            porcentaje_aumento = 10
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento = valor_original - descuento
            print ("Se le a agregado un descuento de 10% por la compra de mas de 8 Kg")
            print(f"El valor con descuento es {valor_con_descuento}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento

            if(compra>valor_con_descuento):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)

        elif(opcion2 >= 15):
            valor_original = opcion2 * platano
            porcentaje_aumento = 20
            descuento = valor_original * (porcentaje_aumento / 100)
            valor_con_descuento2 = valor_original - descuento
            print ("Se le a agregado un descuento de 20% por la compra de mas de 15 Kg")
            print(f"El valor con descuento es {valor_con_descuento2}")

            total = opcion2 * platano
            print(f"El valor total es {total}")

            compra=int(input("Ingrese Dinero\n"))
            

            while(compra<valor_con_descuento2):
                print("Dinero Insuficiente")
                
                compra=int(input("Ingrese Dinero\n"))

            vuelto = compra - valor_con_descuento2

            if(compra>valor_con_descuento2):
                print("------Compra exitosa------")     
                print("===========================")
                print("===========================")     
                print("===========================")          
                print("Su vuelto es: ",vuelto)
                time.sleep(3)
    

    else:

        print("Fin Del Menu")




