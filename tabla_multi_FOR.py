# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:52:03 2022

@author: Patricio Haro
"""
ninicio=int(input("Ingrese desde que tabla desea operar: ")) # variable ninicio.
nfinal=int(input("Ingrese hasta que tabla desea operar: ")) # variable nfinal.


while (ninicio > nfinal): # condicion numero ninicio debe ser menor que nfinal.
     print("Error digita el numero inicial, menor que el final.") # imprime error de la condicion.
     ninicio=int(input("Ingrese desde que tabla desea operar: ")) # variable ninicio.
     nfinal=int(input("Ingrese hasta que tabla desea operar: ")) # variable nfinal.


variable=int(input("cuantos filas desea operar por tabla: ")) # variable de filas a impirmir.

while variable<1: # condicion para bloqueo de variable debe ser mayor que 1.
     print("numero de fila incorrecto, el valor ingresado debe ser mayor que 0 ")
     variable=int(input("cuantos filas desea operar por tabla: "))

for j in range (ninicio,nfinal+1): # se da rango al valor con ninicio y nfinal+1.
    suma=0 # barrido de suma.
    promedio=0 # barrido de promedio.
    print("La Tabla de N°:",j) # se manda imprimir la variable j para verificacion de tablas.
    print("\n")# salto de linea 
    par=0
    impar=0
    for i in range (1,variable+1): # rango en de la variable de 1 a variable+1.
        res=i*j # calculo de resultado producido de i*j.
        suma+=res # se realiza la suma de los resultados de la multiplicacion.
        promedio=suma / variable # se realiza el promedio del resltado de la suma realizada.
        print(i,"x",j,"=",res) # se imprime por pantalla el resultado de ixj.
        if res%2==0: # condicional de pares e impares. 
            par=par+1 # si la condicion se cumple adopta esta indicacion de lo contrario impar.
        else:
            impar=impar+1 # se cumple la condicion si en la condion par no se cumplio.
        
    print("La 'SUMA' de los números es:",suma) # imprime la suma de los numeros resultantes. 
    print("El 'PROMEDIO' de los números es:",promedio) # imprime el promedio del resultado.
    print("Hay",par,"números pares.") # muestra el numero de pares en los
    # resultados de la multiplicacion efectuada. 
    print("Hay",impar,"números impares.")# muestra el numero de impres en los
    # resultados de la multiplicacion efectuada.
    print("\n"*2) #salto de linea.
 