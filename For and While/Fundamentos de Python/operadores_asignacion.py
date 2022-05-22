"""
operadores de asignacion, me permiten asignar un valor o una varible y tambien nos permite
aumentar o disminuir el valor actual de la variable de manera sencilla

Asignacion normal =
asignacion += Suma al valor actual de la variable con el valor asignado
asignacion -= Resta al valor actual de la variable con el valor asignado
asignacion *= Multiplica al valor actual de la variable con el valor asignado
asignacion /= Divide al valor actual de la variable con el valor asignado
Asignacion **= Eleva al valor actual de la variable con el valor asignado
Asignacion //= Divide pero da un numero entero
Asignacion %= Obtiene el resto de la division entre el valor actual de la variable con el valor asignado 
"""

pais = "Chile"
edad = 20
pi = 3.14
es_verdad = False

edad += 20
print("Despues de la Suma:",edad)
 
edad -= 20
print("Despues de la Resta:",edad)

edad *= 2
print("Despues de la Multiplicacion:",edad)

edad //= 2
print("Despues de la Division:",edad)

edad **= 2
print("Despues de la Exp:",edad)

#edad %= 2
#print("El Resto de la Division Es:",edad)

edad %= 3
print("El Resto de la Division Es:",edad)