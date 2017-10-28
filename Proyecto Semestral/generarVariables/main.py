#!/usr/bin/python2.7

from pprint import pprint
from pymongo import MongoClient
import json
import ast
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('mongodb://localhost:27017/')

db = client['datamining']

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
    print ("Inicia programa")

    pipe = [
        {
            '$group' : { 
                    '_id' : '$ID_USUARIO', 'count' : {'$sum' : 1}
                }
        }
    ]

    queryMongo = db.training_sets_final_v3.aggregate( pipe )
    pprint (queryMongo)
    contador = 0
    contador2 = 0
    contador3 = 0
    total = 0
    suma = 0
    for data in queryMongo:
        #pprint (data['_id'])
        #pprint (data['count'])
        if (data['count'] > 1):
            contador += 1
        if (data['count'] > 5):
            contador2 += 1
        if (data['count'] > 10):
            contador3 += 1
        suma += data['count']
        total += 1

    print ("Total de usuario: {}".format(str(total)))
    print ("Total de usuario con frecuencia mayor a 1: {}".format(str(contador)))
    print ("Total de usuario con frecuencia mayor a 5: {}".format(str(contador2)))
    print ("Total de usuario con frecuencia mayor a 10: {}".format(str(contador3)))
    print ("Frecuencia promedio: {}".format(str(suma/total)))

    print ("Finaliza programa")
    
    """
    contenido = []
    with open(namefile1, "rb") as myFileRead:
        for line in myFileRead:
            line = line.decode(enc)
            line = line.encode("utf8")
            datos = (line.rstrip()).split(",")
            dicAux = {
                "ID_MOVIE": datos[0],
                "USER_ID": datos[1],
                "RATING": datos[2],
                "DATE_RATING": datos[3]
            }
            contenido.append(dicAux)

    record_id = mydb.training_sets.insert(contenido)
"""

if __name__ == '__main__':
    main()