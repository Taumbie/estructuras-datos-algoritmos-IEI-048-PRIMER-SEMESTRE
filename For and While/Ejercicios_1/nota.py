# Dado una nota ingresada por teclado verifique si lanota esta en rango correcto entre 4 y 7
#de lo contrario volver a solicitar la nota hasta que se ingrese una correcta
nota = 0
while nota < 4 or nota > 7:
    nota = float(input("Ingrese nota: "))
    if nota < 4 or nota > 7:
        print("La nota debe estar entre 4 y 7")
print("Nota valida")        