from pymongo import MongoClient
from pprint import pprint
import requests
import json
from ast import literal_eval
import time
import os
from multiprocessing import Process
import time

WAIT_SECONDS = 5

client = MongoClient()
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

def inserDocMongo(data):
  client = MongoClient()
  db = client['datamining']
  record_id = db.movies_data.insert(data)
  return record_id


def main():
  allMovieData = db.movies_data.find({})
  dicMovieData = []
  dicMovie = []
  for movieData in allMovieData:
    dicMovieData.append(movieData)

  
  #for movie in allMovie:
  #  dicMovie.append(movie)

  count = 0
  #for movie in dicMovie:
  #  if (count >= 0):
  for movieData in dicMovieData:
    if (count >= 4000):
      allMovie = db.training_sets.find({"ID_MOVIE" : int(movieData['ID_MOVIE'])})
      for movie in allMovie:
        try:
          pprint(movie)
          resulto_id = db.training_sets_by_movie_data.insert(movie)
          print(resulto_id)
        except:
          pass
    count += 1
    #if (int(movie['ID_MOVIE']) == int(movieData['ID_MOVIE'])):
      # pprint(movie)
      
   #   count += 1

  """
  print ("init avg")
  listaMoviesRatingAvg = []
  contadorPeliculasRating = 0
  moviesRatingAvg = db.training_sets.aggregate(pipeAvg)
  for movieToLista in moviesRatingAvg:
    db.movies_data.update(
      {
        'ID_MOVIE': str(movieToLista['_id'])
      },
      {
        '$set': {
          'ratingAvg': movieToLista['avgRating']
        }
      }
    )
    contadorPeliculasRating += 1
  print("Contador peliculas rating: {}".format(str(contadorPeliculasRating)))
  """
    #listaMoviesRatingAvg.append(movieToLista)

  #for x in listaMoviesRatingAvg:
  #  pprint(x)

  #with open("peliculas_info2.csv", "w") as myFileWrite3:
  #contadorPeliculas = 0
  #contadorTmp = 0
  #print("Obteniendo informacion")
  #with open("peliculas_info.csv", "rb") as myFileRead2:
  #  for line in myFileRead2:
  #    data = line.split("+")
      #pprint(data)
  #    for x in listaMoviesRatingAvg:
  #      print("[{}] data[20]: {}".format(str(contadorTmp), str(data[20])))
  #      print("[{}] x[_id]: {}".format(str(contadorTmp), str(x['_id'])))
  #      contadorTmp += 1
      #for movieAvg in listaMoviesRatingAvg:
      #  pprint(data)
      #  pprint(movieAvg)
      #  print(movieAvg['_id'])
      #  print(data[20])
      #  if ( int(movieAvg['_id']) == int(data[20]) ):
      #    contadorPeliculas += 1
      #    pprint(data)
      #    pprint(movieAvg)
      #    print(movieAvg['_id'])
      #    print(data[20])

   #print("Total: {}".format(str(contadorPeliculas)))


      #pprint(movie['details'])

      #arrayGenresDetails = movie['details']['genres']
      #idMovieDetails = movie['details']['id']
      #runTime = movie['details']['runtime']
      #voteAverage = movie['details']['vote_average']
      #voteCount = movie['details']['vote_count']
      
    
    #try:
    # popularidadPelicula = movie['details']['popularity']
    #except:
    # popularidadPelicula = movie['POPULARITY']
    
    #anioMovie = movie['YEAR']
    #generoPeliculaArray = movie['GENRE_IDS']
    #idExternoPelicula = movie['ID']
    #idPelicula = movie['ID_MOVIE']
    # popularidadPelicula = movie['POPULARITY']
    #fechaPublicacionPelicula = movie['RELEASE_DATE']
    #tituloPelicula = movie['TITLE_MOVIE']



"""
  allMoviesWithInfo = db.movies_data.find({})
  index = 0
  indexCast = 0
  indexCrew = 0
  indexCredits = 0
  count = 0
  for movie in allMoviesWithInfo:
    try:
      if (len(movie['credits']['cast']) == 0):
        indexCast += 1
      if (len(movie['credits']['crew']) == 0):
        indexCrew += 1
    except:
      indexCredits += 1
      if (count == 0):
        print(movie['ID_MOVIE'])
        movie['credits'] = json.loads(getCredits(int(movie['ID'])))
        try:
          if (len(movie['credits']['cast']) > 0):
            index = 0
            for cast in movie['credits']['cast']:
              try:
                movie['credits']['cast'][index]['details'] = json.loads(getPeopleDetails(int(cast['id'])))
              except:
                movie['credits']['cast'][index]['details'] = []
              index += 1
        except:
          pass
        try:
          if (len(movie['credits']['crew']) > 0):
            index = 0
            for crew in movie['credits']['crew']:
              try:
                movie['credits']['crew'][index]['details'] = json.loads(getPeopleDetails(int(crew['id'])))
              except:
                movie['credits']['crew'][index]['details'] = []
              index += 1
        except:
          pass
        #pprint(movie['credits'])
        db.movies_data.update(
          {
            '_id': movie['_id']
          },
          {
            '$set': {
              'credits': movie['credits']
            }
          }
        )
      else:
        count += 1
  print("Numero de peliculas sin credits: {}".format(str(indexCredits)))
  print("Numero de peliculas sin cast: {}".format(str(indexCast)))
  print("Numero de peliculas sin crew: {}".format(str(indexCrew)))
  print("Numero de peliculas sin alguna de las dos categorias: {}".format(str(indexCrew + indexCast)))
"""

  

  


if __name__ == '__main__':
  main()
