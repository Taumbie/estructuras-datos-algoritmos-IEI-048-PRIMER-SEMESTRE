from time import sleep

usuario={"username":"nicolas",
         "clave":"panconqueso"}

def login():
    while True:
        usuarios = input("Ingrese su nombre de usuario: ")
        claveunica = input("Ingrese su contraseña: ")
         
        if usuario['username'] == usuarios and usuario['clave'] == claveunica:
            calculadora()
        else:
            print("ALV")    
          
    

def sumar (a, b):
    resultado = (a + b)
    return resultado

def restar (a, b):
    resultado = (a - b)
    return resultado

def multiplicar (a, b):
    resultado = (a * b)
    return resultado

def dividir (a, b):
    resultado = (a / b)
    return resultado


   

def calculadora ():
    print(f'''
        Calculadora

        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir

    ''')
    while True:
       opcion = int(input("Ingrese una opcion: "))
       a = int(input("Ingrese un numero: "))
       b = int(input("Ingrese otro numero: "))

       if opcion == 1:
           print(sumar(a, b))
       elif opcion == 2:
           print(restar(a, b))
       elif opcion == 3:
           print(multiplicar(a, b))
       elif opcion == 4:
           print(dividir(a, b))
       elif opcion == 5:
           pass
       elif opcion < 1 or opcion > 5:
        print("Error en la calculadora, tendra que comenzar denuevo eligiendo una opcion correctamente.")
        login()
        
if __name__ == '__main__':
    login()
                   
    
    