
"""
    Las frutas y verduras son las siguientes:
    1- Papa premiun - 1290 kg
    2- manzana - 1690 kg
    3- tomate - 1390 kg
    4- palta hass - 4990 kg
    5- naranja - 1000 kg
    5- platano - $990 kg

    Si compra mas de 5 kg se le da un descuento de 10% al total.
    Si compra mas de 10 kg se le da un descuento del 15% al total.
"""
def menus():
    try:
        print("Bienvenido a la verdulería")
        print("""
        Las frutas y verduras son las siguientes:
        1-) papa premiun - $1290/kg
        2-) manzana - $1690/kg
        3-) tomate - $1390/kg
        4-) palta hass - $4990/kg
        5-) naranja - $1000/kg
        6-) platano - $990/kg
        """)
        menu = int(input("Seleccione una opcion por favor: "))
    except (ValueError, UnboundLocalError):
            print("Error")
            return(menu()) 
    if  menu() == 1:
        menu1()
    elif menu() == 2:
        menu2()
    elif menu() == 3:
        menu3()    
    elif menu() == 4:
        menu4()  
    elif menu() == 5:
        menu5()  
    elif menu() == 6:
        menu6()      

def menu1():
    try:                
        print("Seleccionaste: Papa Premium, su valor es de $1290/kg")
        kilogramos = int(input("Ingrese cantidad que desea comprar"))
        total = kilogramos * 1290
        print(f"El monto que debe pagar es de: {total}")
        if kilogramos > 10:
            print("Se aplica un descuento de 15%")
            total_actualizado = total - (total*15/100)
        elif kilogramos > 5:
            print("Se aplica un descuento de 10%")
            total_actualizado = total - (total*10/100)
        else:
            print("No se aplicara un descuento esta vez")
            print(f"Su total es de: $",total)  
    except (ValueError, UnboundLocalError):
        print("Ha ocurrido un error...")
        return menu1()   
def menu2():
    try:                
        print("Seleccionaste: Manzanas, su valor es de $1690/kg")
        kilogramos = int(input("Ingrese cantidad que desea comprar"))
        total = kilogramos * 1690
        print(f"El monto que debe pagar es de: {total}")
        if kilogramos > 10:
            print("Se aplica un descuento de 15%")
            total_actualizado = total - (total*15/100)
        elif kilogramos > 5:
            print("Se aplica un descuento de 10%")
            total_actualizado = total - (total*10/100)
        else:
            print("No se aplicara un descuento esta vez")
            print("Su total es de: $",total)  
    except (ValueError, UnboundLocalError):
        print("Ha ocurrido un error...")
        return menu2()          
def menu3():
    try:                
        print("Seleccionaste: Tomates, su valor es de $1390/kg")
        kilogramos = int(input("Ingrese cantidad que desea comprar"))
        total = kilogramos * 1390
        print(f"El monto que debe pagar es de: {total}")
        if kilogramos > 10:
            print("Se aplica un descuento de 15%")
            total_actualizado = total - (total*15/100)
        elif kilogramos > 5:
            print("Se aplica un descuento de 10%")
            total_actualizado = total - (total*10/100)
        else:
            print("No se aplicara un descuento esta vez")
            print("Su total es de: $",total)  
    except (ValueError, UnboundLocalError):
        print("Ha ocurrido un error...")
        return menu3()  
def menu4():
    try:                
        print("Seleccionaste: Palta Hass, su valor es de $4990/kg")
        kilogramos = int(input("Ingrese cantidad que desea comprar"))
        total = kilogramos * 4990
        print(f"El monto que debe pagar es de: {total}")
        if kilogramos > 10:
            print("Se aplica un descuento de 15%")
            total_actualizado = total - (total*15/100)
        elif kilogramos > 5:
            print("Se aplica un descuento de 10%")
            total_actualizado = total - (total*10/100)
        else:
            print("No se aplicara un descuento esta vez")
            print("Su total es de: $",total)  
    except (ValueError, UnboundLocalError):
        print("Ha ocurrido un error...")
        return menu4() 
def menu5():
    try:                
        print("Seleccionaste: Naranjas, su valor es de $1000/kg")
        kilogramos = int(input("Ingrese cantidad que desea comprar"))
        total = kilogramos * 1000
        print(f"El monto que debe pagar es de: {total}")
        if kilogramos > 10:
            print("Se aplica un descuento de 15%")
            total_actualizado = total - (total*15/100)
        elif kilogramos > 5:
            print("Se aplica un descuento de 10%")
            total_actualizado = total - (total*10/100)
        else:
            print("No se aplicara un descuento esta vez")
            print("Su total es de: $",total)  
    except (ValueError, UnboundLocalError):
        print("Ha ocurrido un error...")
        return menu5()                  
def menu6():
    try:                
        print("Seleccionaste: Platano, su valor es de $990/kg")
        kilogramos = int(input("Ingrese cantidad que desea comprar"))
        total = kilogramos * 1290
        print(f"El monto que debe pagar es de: {total}")
        if kilogramos > 10:
            print("Se aplica un descuento de 15%")
            total_actualizado = total - (total*15/100)
        elif kilogramos > 5:
            print("Se aplica un descuento de 10%")
            total_actualizado = total - (total*10/100)
        else:
            print("No se aplicara un descuento esta vez")
            print("Su total es de: $",total)  
    except (ValueError, UnboundLocalError):
        print("Ha ocurrido un error...")
        return menu6()  

      

            
if __name__ == "__main__":
    menus()
    

