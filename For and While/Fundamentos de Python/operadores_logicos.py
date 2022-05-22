"""
edad = 21 #operador asignacion
print (edad>21) #operador aritmetico
edad += 2 #operador de asignacion
"""
"""
operadores logicos, con ellos podemios comparar dos o mas valores a la vez.

and = y 
or = o 
not = no

"""

esta_activada = True
#El Operador not invierte el valor del dato bool.
print(not esta_activada)

#el operador or = una comparacion debe ser verdadera
edad = 17 
tiene_permiso = True

if (edad >= 18 or tiene_permiso == True):
    print ("Puede ir a la Disco") 
else:
    print ("No puede ir a la Disco")

#El operador and = todas las comparacion deben ser verdaderas
username = "admin"
password = "abcd"

if(username == "admin" and password == "abcd"):
    print ("Bienvenido, Iniciaste Sesion")
else:
    print("Error en los Datos")

