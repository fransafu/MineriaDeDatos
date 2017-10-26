#!/usr/bin/python2.7
import sys
from pprint import pprint
import ast

reload(sys)
sys.setdefaultencoding('utf-8')

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

def main():
    print ("Inicia")

    nuevo_formato_arreglo = []
    training_set_arreglo = []
    validarPrimeraLinea = False
    print ("Cargando final training set v1")
    with open("../../../Respaldo_merge_data/final_training_set_v1.csv", "rb") as myFileRead:
        with open("../../../Respaldo_merge_data/final_training_set_v1.csv", "rb") as myFileRead2:
            ID_USUARIO = None
            for line in myFileRead:
                # [0] => DATE_RATING
                # [1] => ID_USUARIO
                # [2] => RATING
                # [3] => RELEASE_DATE
                # [4] => YEAR
                # [5] => ID_MOVIE
                # [6] => ID
                # [7] => GENRE
                # [8] => POPULARITY
                # [9] => TITLE_SEARCH
                # [10] => ORIGINAL_LANGUAGE
                datos = (line.rstrip()).split(",")
                if (validarPrimeraLinea == False):
                    validarPrimeraLinea = True
                elif (ID_USUARIO != datos[1]):
                    ID_USUARIO = datos[1]
                    print ("Nuevo usuario: {}".format(str(ID_USUARIO)))
                    sumRating = 0.0
                    count = 1

                    for line2 in myFileRead2:
                        datos2 = (line2.rstrip()).split(",")
                        if (ID_USUARIO == datos2[1]):
                            
                            if (datos[2] == '1'):
                                sumRating += 1
                            elif (datos[2] == '2'):
                                sumRating += 2
                            elif (datos[2] == '3'):
                                sumRating += 3
                            elif (datos[2] == '4'):
                                sumRating += 4
                            elif (datos[2] == '5'):
                                sumRating += 5
                            count += 1
                            
                    print ("Puntuacion media: {}".format(sumRating/count))
                    print ("suma puntuacion: {}".format(sumRating))
                    print ("contador: {}".format(count))


                

if __name__ == '__main__':
    main()