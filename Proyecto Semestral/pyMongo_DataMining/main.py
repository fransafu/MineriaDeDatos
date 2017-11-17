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

def getDetails(ID_EXTERNA):
  url = "https://api.themoviedb.org/3/movie/{}?api_key=926097b9663e23e015f7128e47620eac&language=en-US".format(str(ID_EXTERNA))
  try:
    response = requests.get(url)
  except requests.exceptions.Timeout:
    time.sleep(WAIT_SECONDS)
    response = requests.get(url)

  return json.loads(response.text)

def getKeyWords(ID_EXTERNA):
  url = "https://api.themoviedb.org/3/movie/{}/keywords?api_key=926097b9663e23e015f7128e47620eac".format(ID_EXTERNA)
  try:
    response = requests.get(url)
  except requests.exceptions.Timeout:
    time.sleep(WAIT_SECONDS)
    response = requests.get(url)

  return response.text

def getCredits(ID_EXTERNA):
  url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=926097b9663e23e015f7128e47620eac".format(ID_EXTERNA)
  try:
    response = requests.get(url)
  except requests.exceptions.Timeout:
    time.sleep(WAIT_SECONDS)
    response = requests.get(url)

  return response.text

def getPeopleDetails(ID_PEOPLE):
  url = "https://api.themoviedb.org/3/person/{}?api_key=926097b9663e23e015f7128e47620eac&language=en-US".format(str(ID_PEOPLE))
  try:
    response = requests.get(url)
  except requests.exceptions.Timeout:
    time.sleep(WAIT_SECONDS)
    response = requests.get(url)

  return response.text

def getMovieDetails(ID_EXTERNA):
  url = "https://api.themoviedb.org/3/movie/{}?api_key=926097b9663e23e015f7128e47620eac&language=en-US".format(str(ID_EXTERNA))
  response = requests.get(url)

  return response.text

def getAllData(movie):
  movie['keywords'] = json.loads(getKeyWords(int(movie['ID'])))
  movie['credits'] = json.loads(getCredits(int(movie['ID'])))
  movie['details'] = json.loads(getMovieDetails(int(movie['ID'])))

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

  record_id = inserDocMongo(movie)
  return record_id, movie['ID_MOVIE'], movie['ID'], movie['_id']

def inserDocMongo(data):
  client = MongoClient()
  db = client['datamining']
  record_id = db.movies_data.insert(data)
  return record_id

"""
def main():
  pipe = [
    { 
      '$match': { 
        #'ID_MOVIE': { '$lte': 5000 } 
        'ID_MOVIE': { '$gte': 0, '$lte': 500 } # Ahi quede
      }
    } 
    ,
    { '$group' :
      {
        '_id' : '$ID_MOVIE',
        # '_id' : { $cond: [ { $gte: [ "" ] } ] },
        'GENRE': { '$addToSet': '$GENRE' },
        'POPULARITY': { '$addToSet': '$POPULARITY' },
        'TITLE_SEARCH': { '$addToSet': '$TITLE_SEARCH' },
        'ORIGINAL_LANGUAGE': { '$addToSet': '$ORIGINAL_LANGUAGE' },
        'RELEASE_DATE': { '$addToSet': '$RELEASE_DATE' },
        'YEAR': { '$addToSet': '$YEAR' },
        'ID_EXTERNA': { '$addToSet': '$ID' }
      }
    }
  ]
  #movies = db.training_sets_final_v3.aggregate(pipe)

  pipe2 = [
    {
      '$group': {
        '_id': '$ID_MOVIE',
        'count': {
          '$sum': 1
        }
      }
    }
  ]
"""

  # find repeate movie
  #allMovies = db.searchs_filter.aggregate(pipe2)
  #for noFilterMovie in allMovies:
  # pprint(noFilterMovie)

  # load all movies from searchs filter
  #allMovies = db.searchs_filter.find({})
  #listMovies = []
  #for filterMovie in allMovies:
  # listMovies.append(filterMovie)

  # filter genre 
  # Total de peliculas sin genero asignado: 500
  #count = 0
  #for movie in listMovies:
  # if (len(movie['GENRE_IDS']) == 0):
  #   pprint (movie)
  #   count += 1
  #print("Total de peliculas sin genero asignado: {}".format(str(count)))
  #pprint(len(listMovies))

  # Get movies listo
  #listMoviesReady = []
  #with open("registro", "rb") as myFileRead:
  # for line in myFileRead:
  #   datos = line.split(",")
  #   listMoviesReady.append(datos[1])

  
  # Total de peliculas: 9498
  # Get all data the movie db
  #index = 0
  #contador = 0
  #with open("registro", "w") as myFileWrite:
  # for movie in listMovies:
  #   if (db.movies_data.find_one({'ID_MOVIE': movie['ID_MOVIE']}) is None):
  #     if (contador == 0):
  #       print("Trabajando ID_MOVIE: {}".format(movie['ID_MOVIE']))
  #       record_id, ID_MOVIE, ID_EXTERNA, _id = getAllData(movie)
  #       myFileWrite.write("{},{},{},{}".format(str(record_id), str(ID_MOVIE), str(ID_EXTERNA), str(_id)))
  #     else:
  #       contador += 1
  #   index += 1

  # Total de peliculas con keywords vacias: 2711
  # Set field keywords where lenght keywords is zero
  #allMoviesWithInfo = db.movies_data.find({})
  #index = 0
  #for movie in allMoviesWithInfo:
  # try:
  #   print (movie['keywords']['id'])
  # except:
  #   pprint(movie['keywords'])
  #   db.movies_data.update(
  #     {
  #       '_id': movie['_id']
  #     },
  #     {
  #       '$set': {
  #         'keywords': []
  #       }
  #     }
  #   )
  #   index += 1
  #print("Total de peliculas con keywords vacias: {}".format(index))

  # Numero de peliculas sin credits: 2290
  # Numero de peliculas sin cast: 376
  # Numero de peliculas sin crew: 451
  # Numero de peliculas sin alguna de las dos categorias: 827
  # 
  # aplicacion de correccion
  # Numero de peliculas sin credits: 1470
  # Numero de peliculas sin cast: 435
  # Numero de peliculas sin crew: 517
  # Numero de peliculas sin alguna de las dos categorias: 952
  #
  # aplicacion de correcion
  # Numero de peliculas sin credits: 1199
  # Numero de peliculas sin cast: 451
  # Numero de peliculas sin crew: 540
  # Numero de peliculas sin alguna de las dos categorias: 991
"""
  allMoviesWithInfo = db.movies_data.find({})
  contadorStatusCode = 0
  contadorCastVacio = 0
  for movie in allMoviesWithInfo:
    try:
      try:
        tmp=movie['credits']['cast'][0]
      except:
        
        if (len(movie['credits']['cast']) == 0):
          #print(len(movie['credits']['cast']))
          #pprint(movie['credits']['cast'])
          contadorCastVacio += 1
    except:
      try:
        if( movie['credits']['status_code'] == 25):
          contadorStatusCode += 1
      except:
        pprint(movie['credits'])
"""
  #print("status code: {}".format(str(contadorStatusCode)))
  #print ("cast vacio: {}".format(str(contadorCastVacio)))

def main():
  with open("peliculas_info3.csv", "w") as myFileWrite2:
    #myFileWrite2.write("ACTOR_ID+ACTOR_NOMBRE+ACTOR_GENERO+DIRECTOR_NOMBRE+DIRECTOR_GENERO+DIRECTOR_ID+DIRECTOR_POPULARIDAD+TIEMPO+VOTO_PROMEDIO+PRESUPUESTO+TITULO_ORIGINAL+POPULARIDAD_DETALLE+FECHA_PUBLICACION+LENGUAJE_ORIGINAL+VOTO_CONTADOR+TITULO+ID_DETALLE+INGRESOS+GENERO+ANIO+ID_PELICULA+ID_EXTERNO+POPULARIDAD+RATING_PROMEDIO\n")
    myFileWrite2.write("ACTOR_ID#ACTOR_GENERO#DIRECTOR_GENERO#DIRECTOR_ID#DIRECTOR_POPULARIDAD#TIEMPO#VOTO_PROMEDIO#PRESUPUESTO#POPULARIDAD_DETALLE#FECHA_PUBLICACION#VOTO_CONTADOR#INGRESOS#GENERO#ANIO#ID_PELICULA#POPULARIDAD#RATING_PROMEDIO\n")
    allMoviesWithInfo = db.movies_data.find({})
    contadorCastIncompleto = 0
    contadorCrewIncompleto = 0
    contadorCredits = 0
    contadorDatosCompletos = 0
    contadorStatusCodeDetails = 0
    contadorKeywordsIncompleto = 0
    count = 0
    listDataMovie = []
    for movie in allMoviesWithInfo:
      validarCast = False
      validarCrew = False
      validarCredits = False
      validarDetails = False
      count += 1

      # Validando detalle pelicula
      try:
        if (movie['details']['status_code'] == 25 and count > 1700):
          contadorStatusCodeDetails += 1
          print(movie['ID'])
          movie['details'] = getDetails(movie['ID'])
          movie['credits'] = getCredits(movie['ID'])
          db.movies_data.update(
            {
              '_id': movie['_id']
            },
            {
              '$set': {
                'details': movie['details']
              }
            }
          )

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
          validarDetails = False
      except:
        try:
          arrayGenresDetails = movie['details']['genres']
          validarDetails = True
        except:
          validarDetails = False

      # Validando casting
      try:
        if (len(movie['credits']['cast']) > 0):
          actorPrincipal = movie['credits']['cast'][0]
          generoActor = movie['credits']['cast'][0]['gender']
          nombreActor = movie['credits']['cast'][0]['name']
          identificadorActor = movie['credits']['cast'][0]['id']
          try:
            popularidadActor = movie['credits']['cast'][0]['details']['popularity']
            validarCast = True
          except:
            validarCast = False
            contadorCastIncompleto += 1
      except:
        validarCast = False

      # Validando crew
      if (validarCast):
        try:
          if (len(movie['credits']['crew']) > 0):
            director = movie['credits']['crew'][0]
            generoDirector = movie['credits']['crew'][0]['gender']
            nombreDirector = movie['credits']['crew'][0]['gender']
            identificadorDirector = movie['credits']['crew'][0]['gender']
            try:
              popularidadDirector = movie['credits']['crew'][0]['details']['popularity']
              validarCrew = True
            except:
              validarCrew = False
              contadorCrewIncompleto += 1
            validarCrew = True
        except:
          validarCrew = False

      # Extraer informacion
      if (validarCrew and validarCast and validarDetails):
        contadorDatosCompletos += 1
        data = {}
        try:
          data['ACTOR_ID'] = movie['credits']['crew'][0]['id']
          data['ACTOR_NOMBRE'] = movie['credits']['crew'][0]['name']
          data['ACTOR_GENERO'] = movie['credits']['crew'][0]['gender']

          data['DIRECTOR_NOMBRE'] = movie['credits']['cast'][0]['name']
          data['DIRECTOR_GENERO'] = movie['credits']['cast'][0]['gender']
          data['DIRECTOR_ID'] = movie['credits']['cast'][0]['id']
          data['DIRECTOR_POPULARIDAD'] = movie['credits']['cast'][0]['details']['popularity']

          data['DETALLE_RUNTIME'] = movie['details']['runtime']
          data['DETALLE_VOTE_AVERANGE'] = movie['details']['vote_average']
          data['DETALLE_BUDGET'] = movie['details']['budget']
          data['DETALLE_TITULO_ORIGINAL'] = movie['details']['original_title']
          data['DETALLE_POPULARIDAD'] = movie['details']['popularity']
          data['DETALLE_FECHA_PUBLICACION'] = movie['details']['release_date']
          data['DETALLE_LENGUAJE_ORIGINAL'] = movie['details']['original_language']
          data['DETALLE_VOTE_COUNT'] = movie['details']['vote_count']
          data['DETALLE_TITULO'] = movie['details']['title']
          data['DETALLE_ID'] = movie['details']['id']
          data['DETALLE_REVENUE'] = movie['details']['revenue']

          data['GENERO'] = movie['GENRE_IDS'][0]
          # data['_id'] = movie['_id']
          data['YEAR'] = movie['YEAR']
          data['ID_MOVIE'] = movie['ID_MOVIE']
          data['ID_EXTERNA'] = movie['ID']
          data['ID_POPULARIDAD'] = movie['POPULARITY']

          #for findMovie in findMovieWithId:
          # pprint(findMovie)
          #pprint(json.dumps(data))
          myFileWrite2.write("{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}\n".format(int(movie['credits']['crew'][0]['id']),
                                                                        int(movie['credits']['crew'][0]['gender']),
                                                                        int(movie['credits']['cast'][0]['gender']),
                                                                        int(movie['credits']['cast'][0]['id']),
                                                                        str(float(movie['credits']['cast'][0]['details']['popularity'])).replace(".", ","),
                                                                        int(movie['details']['runtime']),
                                                                        str(float(movie['details']['vote_average'])).replace(".", ","),
                                                                        int(movie['details']['budget']),
                                                                        str(float(movie['details']['popularity'])).replace(".", ","),
                                                                        str(movie['details']['release_date']),
                                                                        str(float(movie['details']['vote_count'])).replace(".", ","),
                                                                        str(float(movie['details']['revenue'])).replace(".", ","),
                                                                        int(movie['GENRE_IDS'][0]),
                                                                        int(movie['YEAR']),
                                                                        int(movie['ID_MOVIE']),
                                                                        str(float(movie['POPULARITY'])).replace(".", ","),
                                                                        str(float(movie['ratingAvg']))).replace(".", ","))

        except Exception as e:
          pprint(e)
          contadorKeywordsIncompleto += 1

  print ("Contador status code details: {}".format(str(contadorStatusCodeDetails)))
  print ("Cast incompleto: {}".format(str(contadorCastIncompleto)))
  print ("Crew incompleto: {}".format(str(contadorCrewIncompleto)))
  print ("Contador keywords incompleto: {}".format(str(contadorKeywordsIncompleto)))
  print ("Datos completos: {}".format(str(contadorDatosCompletos - contadorKeywordsIncompleto)))

  pipeAvg = [
    {
      "$group":
        {
          "_id": "$ID_MOVIE",
          "avgRating": { "$avg": "$RATING" }
        }
    }
  ]

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
