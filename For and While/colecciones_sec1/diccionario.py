"""
coleccion de datos que almacenan valores con una relacion
clave:valor

se identifican al declararlos por las { }

"""
datos_persona = {}
#              Clave        Valor
datos_persona["nombre"] = "Alejandra"

datos_persona["apellido"] = "Leal"

datos_persona["edad"] = 25

print( datos_persona["nombre"], datos_persona["apellido"] )

print( "Hay",len(datos_persona),"datos." )
