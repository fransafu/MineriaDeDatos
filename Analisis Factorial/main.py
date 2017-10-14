#!/usr/bin/python2.7

import numpy as np

def main():
	print ("Inicia programa para analisis factorial.")
	
	# Solicitar elementos
	numeroDeElementos = input("Ingresar el numero de elementos: ")
	print ("El numero de elementos es: %s" %(str(numeroDeElementos)))

    contadorElementos = 0
    while (contadorElementos < numeroDeElementos):
        print ("X1 = a * F + a * F + U")
        nombreDelElemento = str(input("Ingrese el nombre del elemento (Xi): "))
        constante1 = input("Ingresar constante del factor 1 (a): ")
        factor1 = input("Ingresar factor 1 (F1): ")

        constante2 = input("Ingresar constante del factor 2 (a): ")
        factor2 = input("Ingresar factor 2 (F2): ")

        VarianzaElemento = input("Ingresar la varianza del elemento (U): ")
        

        contadorElementos += 1

if __name__ == '__main__':
	main()