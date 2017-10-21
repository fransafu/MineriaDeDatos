#!/usr/bin/python2.7
import sys
from pprint import pprint
import ast

reload(sys)
sys.setdefaultencoding('utf-8')

enc = "latin-1"
# data base name : 'test-database-1'

# [0] => RELEASE_DATE
# [1] => YEAR 
# [2] => ID_MOVIE
# [3] => ID
# [4] => GENRE
# [5] => POPULARITY
# [6] => TITLE_SEARCH
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

idiomas = {
    "idiomas" : [
        {
            "id": 1,
            "name" : "en"
        },
        {
            "id": 2,
            "name" : "hi"
        },
        {
            "id": 3,
            "name" : "pt"
        },
        {
            "id": 4,
            "name" : "fr"
        },
        {
            "id": 5,
            "name" : "es"
        },
        {
            "id": 6,
            "name" : "ja"
        },
        {
            "id": 7,
            "name" : "sv"
        },
        {
        "id": 8,
        "name": "de"
        },
        {
        "id": 9,
        "name": "pl"
        },
        {
        "id": 10,
        "name": "it"
        },
        {
        "id": 11,
        "name": "ar"
        },
        {
        "id": 12,
        "name": "cn"
        },
        {
        "id": 13,
        "name": "zh"
        },
        {
        "id": 14,
        "name": "cs"
        },
        {
        "id": 15,
        "name": "no"
        },
        {
        "id": 16,
        "name": "ta"
        },
        {
        "id": 17,
        "name": "la"
        },
        {
        "id": 18,
        "name": "da"
        },
        {
        "id": 19,
        "name": "el"
        },
        {
        "id": 20,
        "name": "hu"
        },
        {
        "id": 21,
        "name": "tr"
        },
        {
        "id": 22,
        "name": "ko"
        },
        {
        "id": 23,
        "name": "ps"
        },
        {
        "id": 24,
        "name": "bs"
        },
        {
        "id": 25,
        "name": "ab"
        },
        {
        "id": 26,
        "name": "is"
        },
        {
        "id": 27,
        "name": "ru"
        },
        {
        "id": 28,
        "name": "nl"
        },
        {
        "id": 29,
        "name": "ca"
        }
    ]
}

def nuevoFormato():
    arregloMovies = []
    arregloMoviesFilter = []
    print ("Cargando datos movieTitles")
    with open("../clearData/archivoConGenero.csv", "rb") as myFileRead:
        with open("nuevoFormato.csv", "w") as myFileWrite:
            # Leer el archivo linea por linea
            for line in myFileRead:
                validarGenero = False
                validarIdioma = False
                datos = (line.rstrip()).split("=")
                nuevoFormato = datos[0].split("-")
                nuevoFormato = "{}/{}/{}".format(nuevoFormato[2], nuevoFormato[1], nuevoFormato[0])

                # Convertir genero a numero
                for genreDic in genres['genres']:
                    if (datos[4] == genreDic['name']):
                        generoId = int(genreDic['id'])
                        validarGenero = True
                # Se debe remover la categoria ADULT porque no hay peliculas clasificadas como adulto
                #if ( datos[7] == "True"):
                #    print (datos[7])
                # Convertir idioma a numero y filtrar dato
                for idiomaDic in idiomas['idiomas']:
                    if ( datos[8] == idiomaDic['name'] and datos[8] != ''):
                        idiomaId = int(idiomaDic['id'])
                        validarIdioma = True
                if (validarGenero and validarIdioma):
                    strResult = "{}={}={}={}={}={}={}={}\n".format(nuevoFormato, datos[1], datos[2], datos[3], generoId, datos[5], datos[6], idiomaId)
                    myFileWrite.write(strResult)

def generarArchivoDesdeArchivos():
    with open("training_set_final_3.csv", "w") as myFileWrite:
        with open("../../../netflixData/combined_data_3.csv", "rb") as myFileRead:
            for line in myFileRead:
                datos = (line.rstrip()).split(",")
                with open("nuevoFormato.csv", "rb") as myFileRead2:
                    for line2 in myFileRead2:
                        datos2 = (line2.rstrip()).split("=")
                        # datos[0] => ID_MOVIE
                        # datos[1] => ID_USUARIO
                        # datos[2] => RATING
                        # datos[3] => DATE_RATING

                        # datos2[0] => RELEASE_DATE
                        # datos2[1] => YEAR 
                        # datos2[2] => ID_MOVIE
                        # datos2[3] => ID
                        # datos2[4] => GENRE
                        # datos2[5] => POPULARITY
                        # datos2[6] => TITLE_SEARCH
                        # datos2[7] => ORIGINAL_LANGUAGE

                        if (datos[0] == datos2[2]):
                            print (line)
                            print (line2)
                            nuevoFormato = datos[3].split("-")
                            nuevoFormato = "{}/{}/{}".format(nuevoFormato[2], nuevoFormato[1], nuevoFormato[0])
                            strResult = "{},{},{},{},{},{},{},{},{},{},{}\n".format(nuevoFormato, datos[1], datos[2], datos2[0], datos2[1], datos2[2], datos2[3], datos2[4], datos2[5], datos2[6], datos2[7])
                            myFileWrite.write(strResult)

def main():
    print ("Inicia")
    # generarArchivoDesdeArchivos()

    nuevo_formato_arreglo = []
    training_set_arreglo = []
    print ("Cargando combined_data")
    with open("../../../netflixData/combined_data_4.csv", "rb") as myFileRead:
        for line in myFileRead:
            datos = (line.rstrip()).split(",")
            training_set_arreglo.append(datos)

    print ("Cargando nuevoFormato")
    with open("nuevoFormato.csv", "rb") as myFileRead2:
        for line2 in myFileRead2:
            datos2 = (line2.rstrip()).split("=")
            nuevo_formato_arreglo.append(datos2)
    print ("Inicia creacion de archivo, orden y grabado.")
    with open("training_set_final_v1_combine_4.csv", "w") as myFileWrite:
        for datos in training_set_arreglo:
            for datos2 in nuevo_formato_arreglo:
                if (datos[0] == datos2[2]):
                    print (line)
                    print (line2)
                    nuevoFormato = datos[3].split("-")
                    nuevoFormato = "{}/{}/{}".format(nuevoFormato[2], nuevoFormato[1], nuevoFormato[0])
                    strResult = "{},{},{},{},{},{},{},{},{},{},{}\n".format(nuevoFormato, datos[1], datos[2], datos2[0], datos2[1], datos2[2], datos2[3], datos2[4], datos2[5], datos2[6], datos2[7])
                    myFileWrite.write(strResult)
    print ("Finaliza programa")

if __name__ == '__main__':
    main()