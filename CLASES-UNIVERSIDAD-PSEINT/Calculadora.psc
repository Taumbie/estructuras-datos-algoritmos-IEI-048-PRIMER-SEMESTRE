
SubProceso resultado <- sumar ( a, b )
	Definir resultado Como Real;
    resultado = (a + b);
Fin SubProceso

SubProceso resultado <- restar ( a, b )
	Definir resultado Como Real;
    resultado = a - b;	
Fin SubProceso

SubProceso resultado <- multiplicar ( a, b )
	Definir resultado Como Real;
    resultado <- a * b;
Fin SubProceso

SubProceso resultado <- dividir ( a, b )
	Definir resultado Como Real;
    resultado <- a / b;
Fin SubProceso

Proceso Calculadora
    Escribir "Menu";
    Escribir "1: sumar";
    Escribir "2: restar";
    Escribir "3: multiplicar";
    Escribir "4: dividir";
    Definir menuSeleccionado Como Entero;
    menuSeleccionado = 0;
    Mientras menuSeleccionado < 1 o menuSeleccionado > 4 Hacer
        Escribir "Seleccione del menu";
        Leer menuSeleccionado;
    Fin Mientras
    Definir n1, n2, resultado Como Real;
	Escribir "Ingrese 2 numeros";
    Leer n1, n2;
    Segun menuSeleccionado Hacer
        1:
            resultado = sumar (n1, n2);
            Escribir "El resultado es: " resultado;
        2:
            resultado = restar (n1, n2);
            Escribir "El resultado es: " resultado;
        3:
            resultado = multiplicar (n1, n2);
            Escribir "El resultado es: " resultado;
        4:
            si n2 = 0 Entonces
                Escribir "El resultado es indefinido ";
            SiNo
                resultado = dividir (n1, n2);
                Escribir "El resultado es: " resultado;
            FinSi
            
	Fin Segun
    
FinProceso