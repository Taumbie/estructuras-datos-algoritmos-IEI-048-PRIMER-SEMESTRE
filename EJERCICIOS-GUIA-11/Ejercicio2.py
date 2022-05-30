#Diseña un programa que solicite la lectura de un texto que no contenga letras 
#mayúsculas. Si el usuario teclea una letra mayúscula, el programa solicitara nuevamente la 
#introducción del texto cuantas veces sea preciso

letra = True
texto = input("Ingrese un texto sin letras mayusculas: ")
while letra == True:
    if texto != texto.lower():
        texto = input("El texto no es valido, ingrese un texto sin mayúsculas: ")
    else:
        letra = False
        print("Su texto no tiene mayusculas")
        