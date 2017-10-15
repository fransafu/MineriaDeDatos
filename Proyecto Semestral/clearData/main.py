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

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    count = 0
    count2 = 0
    with open("../../../netflixData/movieTitles.csv", "rb") as myFileRead:
        for line in myFileRead:
            line = line.decode(enc)
            line = line.encode("utf8")
            datos = (line.rstrip()).split(",")
            numeroDeRegistros = coll.find({"ID_MOVIE" : str(datos[0]) }).count()

            for doc in coll.find({"ID_MOVIE" : str(datos[0]), "TITLE_MOVIE": str(datos[2]) }):
                if ( similar(datos[2], doc['ORIGINAL_TITLE']) > 0.75):
                    print ("Titulo buscado: " + str(datos[2]))
                    print ("Titulo Original: " + str(doc['ORIGINAL_TITLE']))
                    print (str(doc['_id']))
                    dicAux = {
                        "ID_MOVIE": doc['ID_MOVIE'],
                        "YEAR": doc['YEAR'],
                        "TITLE_MOVIE": doc['TITLE_MOVIE'],
                        "ID": doc['ID'],
                        "TITLE_SEARCH": doc['TITLE_SEARCH'],
                        "POPULARITY": doc['POPULARITY'],
                        "ORIGINAL_LANGUAGE": doc['ORIGINAL_LANGUAGE'],
                        "ORIGINAL_TITLE": doc['ORIGINAL_TITLE'],
                        "GENRE_IDS": doc['GENRE_IDS'],
                        "ADULT": doc['ADULT'],
                        "RELEASE_DATE": doc['RELEASE_DATE']
                    }
                    db.searchs_filter.insert(dicAux)
            
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