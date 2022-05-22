
palabra = input("Ingrese una palabra: ")

vocales = 0
for letra in palabra.lower():
    if letra == "a" or letra =="e" or letra == "i" or letra =="o" or letra == "u":
        vocales += 1
print("La palabra tiene", vocales, "vocales")