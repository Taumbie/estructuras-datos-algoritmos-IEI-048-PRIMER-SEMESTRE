# Suma de numeros impares en un rango de 0 a 5
suma = 0
for x in range(0,5):
    numero = int(input("Ingrese sus números"))
    if numero % 2 != 0:
        suma += numero
print("La suma de los numeros ", suma)  