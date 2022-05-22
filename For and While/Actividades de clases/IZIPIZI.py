#Desarrolle un algoritmo que consulte una y otra vez si desea terminar el programa,
# se contesta Si o si (en mayusculas o en minusculas) se termina el programa
print("DIGA Si O si PARA TERMINAR")
x = input("¿Desea terminar el programa?: ")

while x != "Si" and x != "si":
    x = input("¿Desea terminar el programa?: ")
print("Programa terminado")