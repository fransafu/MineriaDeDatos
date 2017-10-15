#!/usr/bin/python2.7
import requests
import json
from pymongo import MongoClient
import pymongo
import sys

from difflib import SequenceMatcher

from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('mongodb://localhost:27017/')

enc = "latin-1"
# data base name : 'test-database-1'
db = client['datamining']
coll = db['searchs']
searchs_filter = db['searchs_filter']

enc = "latin-1"

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

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    count = 0
    count2 = 0
    with open("../../../netflixData/movieTitles.csv", "rb") as myFileRead:
        with open("resultSearchFilter.csv", "w") as myFileWrite:
            index2 = 0
            for line in myFileRead:
                line = line.decode(enc)
                line = line.encode("utf8")
                datos = (line.rstrip()).split(",")
                numeroDeRegistros = coll.find({"ID_MOVIE" : str(datos[0]) }).count()
                index = 0
                
                for doc in searchs_filter.find({"ID_MOVIE" : str(datos[0]), "TITLE_MOVIE": str(datos[2]) }):
                    if ( similar(datos[2], doc['ORIGINAL_TITLE']) > 0.9 or similar(datos[2], doc['TITLE_MOVIE']) > 0.9):
                        print ("Titulo buscado: " + str(datos[2]))
                        print ("Titulo Original: " + str(doc['ORIGINAL_TITLE']))
                        print ("Titulo Pelicula: " + str(doc['TITLE_MOVIE']))
                        print (str(doc['_id']))

                        rowString = "{}={}={}={}={}={}={}={}={}={}={}\n".format(doc['RELEASE_DATE'], doc['ORIGINAL_TITLE'], doc['TITLE_MOVIE'], doc['YEAR'], doc['ID_MOVIE'], doc['ID'], doc['GENRE_IDS'], doc['POPULARITY'], doc['TITLE_SEARCH'], doc['ADULT'], doc['ORIGINAL_LANGUAGE'])
                        print (rowString)
                        myFileWrite.write(rowString)
                        # print (datos['GENRE_IDS'])
                        
                        #for genero_id in doc['GENRE_IDS']:
                        #    for genero in genres['genres']:
                        #        if (genero_id == genero['id']):
                        #            print (genero['name'])


                        index2 += 1
                    if (index == 1):
                        #pprint(doc)
                        count += 1
                    index += 1
                #if (index == 1):
                #    print ("Unico")
                
                #if ( numeroDeRegistros > 15):
                #    count += 1
                #    for doc in coll.find({"ID_MOVIE" : str(datos[0]), "TITLE_MOVIE": str(datos[2]) }):
                #        if ( similar(datos[2], doc['ORIGINAL_TITLE']) > 0.8):
                #            print ("Titulo buscado: " + str(datos[2]))
                #            print ("Titulo Original: " + str(doc['ORIGINAL_TITLE']))
                ##            print (str(doc['_id']))
                #            mydb.coll_dest.insert(doc)
                #elif ( numeroDeRegistros >= 1 and numeroDeRegistros <= 15 ):
                #    count2 += 1
                    #print (line)
                #many_doc = coll.find({"ID_MOVIE" : "5496"}).count()
                #print (many_doc)
                #for doc in many_doc:
                #    pprint (doc)
    print ("Numero total de doc como unicos: " + str(count))
    print ("Peliculas similares en un 90%: " + str(index2))
    #print ("Registros mayores a 15: " + str(count))
    #print ("Entre 1 a 15 registros: " + str(count2))

if __name__ == '__main__':
    main()

# db.searchs.aggregate([ {"$group" : {_id:"$ID_MOVIE", count:{$sum:1}}} ])
"""
db.searchs.aggregate([
    {
        "$group" : {
            _id:"$ID_MOVIE", 
            count:{$sum:1}
        }
    },
    {
        "$match":{
            count:{
                "$gt": 2
            }
        }
    }
])
"""