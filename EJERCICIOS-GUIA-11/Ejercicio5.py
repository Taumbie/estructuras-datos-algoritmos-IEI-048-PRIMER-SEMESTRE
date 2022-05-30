#5.- Desarrolle un programa que lea una (cadena), un texto ingresado por consola y muestre
#el número de espacios en blanco que contiene

def check_space(string): 
    count = 0
    for i in string:   
        if i == " ": 
            count += 1   
    return count 
string = input("Escriba su texto: ")
print("Número de espacios en blanco ",check_space(string)) 