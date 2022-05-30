#Muestra los multiplos de un numero

número = float(input("ingrese un numero que desea multiplicar: "))
for i in range(1,11):
    print(f"{i} x {número} = {i * número}")