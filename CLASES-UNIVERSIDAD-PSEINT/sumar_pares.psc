//2)	Algoritmo que sume sólo números pares 
//en caso de detectar un número impar, se detiene y entrega el resultado 

Proceso sumar_pares
	definir n1, total Como Entero;
	n1 <- 0;
	total <- 0;
	Mientras n1 mod 2 = 0 Hacer
		Escribir  "Por favor ingrese numero par:"
		Leer n1;
		Si n1 mod 2 = 0 Entonces
			total <- total + n1;
		FinSi
	Fin Mientras
	Escribir "El resultado de la suma de numeros pares es:" total;
	
FinProceso

	
	
	
	
	
	
	
