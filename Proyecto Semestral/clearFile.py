# -*- coding: utf-8 -*-

# Autor: Francisco Sanchez
# Descripcion: Convertir estructura de archivos a csv

# Import file
import csv

# Const Var
PATHFILETXT = './netflixData/combined_data_4.txt'
PATHFILECSV = './netflixData/combined_data_4.csv'
ID_MOVIE = ''

def transformFile(fileOpen, csvResult):
    contadorLineasArchivo = 0
    for line in fileOpen:
        if ( ":" in line ):
            print ( "ID MOVIE: " + line.split(":")[0] )
            ID_MOVIE = str(line.split(":")[0])
        else:
            text = str(ID_MOVIE + "," + line)
            csvResult.write(text)
        contadorLineasArchivo += 1
    return contadorLineasArchivo, True

if __name__ == "__main__":
    print ("Inicializando programa.")

    # Init file
    fileOpen  = open(PATHFILETXT, 'r')
    csvResult = open(PATHFILECSV, 'w')

    # Init function
    numeroLineas, validar = transformFile(fileOpen, csvResult)

    if ( validar ):
        print ("transformación terminada.")
        print ("Numero de lineas del archivo .txt: " + str(numeroLineas))

    # Cerrar archivo y limpiar buffer
    fileOpen.close()
    csvResult.close()

    print ("Programa finalizado")