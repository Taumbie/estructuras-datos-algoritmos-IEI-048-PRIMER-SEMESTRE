// Escribir el pseudocódigo en Pseint de 3 números ingresados por teclado y
// muestre el mayor de ellos y el producto de los tres.
Funcion mayor <- numeroMayor (n1,n2)
	Si n1>n2 Entonces
		mayor <- n1
	SiNo
		mayor <- n2
	FinSi
FinFuncion

Algoritmo mayor_de_tres
	Definir a,b,c,x Como Real
	Escribir 'Ingrese 3 números para determinar cual es el mayor:'
	Leer a,b,c
	x <- numeroMayor(a,b)
	x <- numeroMayor(x,c)
	Escribir 'El numero mayor de los tres numeros es :',x
FinAlgoritmo
