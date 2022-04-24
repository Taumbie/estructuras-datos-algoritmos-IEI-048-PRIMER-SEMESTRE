Funcion mayor <- numeroMayor ( n1,n2 )
    Si n1>n2 entonces;
        mayor = n1;
    Sino 
        mayor = n2;
    FinSi
Fin Funcion

Algoritmo El_mayor_de_cinco_números
    Definir a,b,c,d,e,x Como Real;
    leer a,b,c,d,e;
    x = numeroMayor(a,b); 
    x = numeroMayor(x,c);
    x = numeroMayor(x,d);
    x = numeroMayor(x,e);
    escribir " El número mayor es ", x;
FinAlgoritmo