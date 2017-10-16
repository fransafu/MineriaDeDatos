#!/usr/bin/python2.7
import sys
from pprint import pprint
import ast

reload(sys)
sys.setdefaultencoding('utf-8')

enc = "latin-1"
# data base name : 'test-database-1'

enc = "latin-1"

# [0] => RELEASE_DATE
# [1] => YEAR 
# [2] => ID_MOVIE
# [3] => ID
# [4] => GENRE_IDS
# [5] => POPULARITY
# [6] => TITLE_SEARCH
# [7] => ADULT
# [8] => ORIGINAL_LANGUAGE

genres = {
    "genres": [
        {
            "id": 28,
            "name": "Action"
        },
        {
            "id": 12,
            "name": "Adventure"
        },
        {
            "id": 16,
            "name": "Animation"
        },
        {
            "id": 35,
            "name": "Comedy"
        },
        {
            "id": 80,
            "name": "Crime"
        },
        {
            "id": 99,
            "name": "Documentary"
        },
        {
            "id": 18,
            "name": "Drama"
        },
        {
            "id": 10751,
            "name": "Family"
        },
        {
            "id": 14,
            "name": "Fantasy"
        },
        {
            "id": 36,
            "name": "History"
        },
        {
            "id": 27,
            "name": "Horror"
        },
        {
            "id": 10402,
            "name": "Music"
        },
        {
            "id": 9648,
            "name": "Mystery"
        },
        {
            "id": 10749,
            "name": "Romance"
        },
        {
            "id": 878,
            "name": "Science Fiction"
        },
        {
            "id": 10770,
            "name": "TV Movie"
        },
        {
            "id": 53,
            "name": "Thriller"
        },
        {
            "id": 10752,
            "name": "War"
        },
        {
            "id": 37,
            "name": "Western"
        }
    ]
}


def main():
    arregloMovies = []
    arregloMoviesFilter = []
    print ("Cargando datos movieTitles")
    contadorTotal = 0
    contadorPeliculaGeneroUnico = 0
    contadorPeliculaSinGenero = 0
    contadorPeliculaMasDeUnGenero = 0
    with open("archivoFiltrado.csv", "rb") as myFileRead:
        with open("archivoConGenero.csv", "w") as myFileWrite:
            # Leer el archivo linea por linea
            for line in myFileRead:
                datos = (line.rstrip()).split("=")
                arregloGenero = ast.literal_eval(datos[4])
                # Leer arreglo de generos por cada linea
                if (len(arregloGenero) == 1):
                    for genero in arregloGenero:
                        #print (genero)
                        # Leer diccionario de generos
                        for generoDic in genres['genres']:
                            if (genero == generoDic['id']):
                                print (generoDic['name'])
                                strResult = "{}={}={}={}={}={}={}={}={}\n".format(datos[0], datos[1], datos[2], datos[3], str(generoDic['name']), datos[5], datos[6], datos[7], datos[8])
                                myFileWrite.write(strResult)
                                contadorPeliculaGeneroUnico += 1
                elif (len(arregloGenero) > 1):
                    generoAsignado = False
                    for genero in arregloGenero:
                        #print (genero)
                        # Leer diccionario de generos
                        for generoDic in genres['genres']:
                            if (genero == generoDic['id'] and generoAsignado == False):
                                print (generoDic['name'])
                                strResult = "{}={}={}={}={}={}={}={}={}\n".format(datos[0], datos[1], datos[2], datos[3], str(generoDic['name']), datos[5], datos[6], datos[7], datos[8])
                                myFileWrite.write(strResult)
                                generoAsignado = True
                    contadorPeliculaMasDeUnGenero += 1
                else:
                    contadorPeliculaSinGenero += 1

                contadorTotal += 1
    print ("Total de peliculas con generos: " + str(contadorTotal))
    print ("Total de peliculas con genero unico: " + str(contadorPeliculaGeneroUnico))
    print ("Total de peliculas con mas de un genero: " + str(contadorPeliculaMasDeUnGenero))
    print ("Total de peliculas sin genero: " + str(contadorPeliculaSinGenero))



if __name__ == '__main__':
    main()