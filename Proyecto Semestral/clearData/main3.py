#!/usr/bin/python2.7
import sys
from difflib import SequenceMatcher
from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

enc = "latin-1"
# data base name : 'test-database-1'

enc = "latin-1"

def main():
    arregloMovies = []
    arregloMoviesFilter = []
    print ("Cargando datos movieTitles")
    with open("../../../netflixData/movieTitles.csv", "rb") as myFileRead:
        for line in myFileRead:
            line = line.decode(enc)
            line = line.encode("utf8")
            datos = (line.rstrip()).split(",")
            arregloMovies.append(datos)

    print ("Cargando datos resultSearchFilter")
    with open("resultSearchFilter.csv", "r") as myFileRead2:
        for line2 in myFileRead2:
            line2 = line2.decode(enc)
            line2 = line2.encode("utf8")
            datos2 = (line2.rstrip()).split("=")
            arregloMoviesFilter.append(datos2)

    # [0] => RELEASE_DATE
    # [1] => ORIGINAL_TITLE
    # [2] => TITLE_MOVIE
    # [3] => YEAR 
    # [4] => ID_MOVIE
    # [5] => ID
    # [6] => GENRE_IDS
    # [7] => POPULARITY
    # [8] => TITLE_SEARCH
    # [9] => ADULT
    # [10] => ORIGINAL_LANGUAGE

    print ("Filtrando y creando arregloMoviesContador")
    arregloMoviesContador = []
    for datos in arregloMovies:
        contadorMovie = 0
        valido = False
        aux = []
        for datos2 in arregloMoviesFilter:
            if ( int(datos[0]) == int(datos2[4])):
                contadorMovie += 1
                if (str(datos2[5] != '')):
                    valido = True
                    aux.append(str(datos2[5]))
        if (valido):
            aux.append(int(datos[0]))
            aux.append(int(contadorMovie))
            arregloMoviesContador.append(aux)

    # pprint (arregloMoviesContador)

    print ("Generando archivo")
    with open("archivoFiltrado.csv", "w") as myFileWrite:
        indexValido = 0
        for x in arregloMoviesContador:
            if (int(x[2]) == 1):
    #            pprint(x)
                for datos3 in arregloMoviesFilter:
                    # datos3 = (lineaPelicula.rstrip()).split("=")
                    if (x[0] == datos3[5]):
    #                    pprint (datos3)
                        strResult = "{}={}={}={}={}={}={}={}={}\n".format(datos3[0], datos3[3], datos3[4], datos3[5], datos3[6], datos3[7], datos3[8], datos3[9], datos3[10])
                        myFileWrite.write(strResult)
                indexValido += 1

    print ("largo arregloMoviesContador: " + str(len(arregloMoviesContador)))
    print ("IndexValido: " + str(indexValido) )
    print ("Programa finalizado")

    ##print ("Total arregloMovies: " + str(len(arregloMovies)))
    #print ("Total arregloMoviesFilter: " + str(len(arregloMoviesFilter)))
    #print ("Multiplicacion de ambos: " + str(len(arregloMovies) * len(arregloMoviesFilter)))
    #print ("contador total: " + str(contador))


"""
        with open("resultSearchFilter_2.csv", "w") as myFileWrite:
            for datos in arregloMovies:
                # [0] => ID_MOVIE
                # [1] => YEAR_RELEASE
                # [2] => TITLE
                pprint (int(datos[0]))

                contadorMovie = 0
                for line2 in myFileRead2:
                    line2 = line2.decode(enc)
                    line2 = line2.encode("utf8")
                    # [0] => RELEASE_DATE
                    # [1] => ORIGINAL_TITLE
                    # [2] => TITLE_MOVIE
                    # [3] => YEAR 
                    # [4] => ID_MOVIE
                    # [5] => ID
                    # [6] => GENRE_IDS
                    # [7] => POPULARITY
                    # [8] => TITLE_SEARCH
                    # [9] => ADULT
                    # [10] => ORIGINAL_LANGUAGE

                    datos2 = (line2.rstrip()).split("=")
                    print (datos[0])
                    print (datos2[4])
                    pprint ((line2.rstrip()).split("=")[4])
                    if ( datos[0] == datos2[4]):
                        pprint (datos)
                        contadorMovie += 1
                    contador += 1
                if (contadorMovie > 0):
                    result = "{},{}\n".format(str(datos[0]), str(contadorMovie))
                    myFileWrite.write(result)
                
            # arregloContadorMovie.append([datos[0], contadorMovie])
    print ("total: " +str(contador))
"""
if __name__ == '__main__':
    main()