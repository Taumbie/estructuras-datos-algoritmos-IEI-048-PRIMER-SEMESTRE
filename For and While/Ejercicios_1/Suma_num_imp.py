#Suma los numeros impares entre 100 y 350
suma = 0
for i in range (100, 350):
    if i % 2 != 0:
        suma += i
print("La suma de todos los numeros impares es: ", suma)        
