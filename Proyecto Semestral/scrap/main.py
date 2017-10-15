#!/usr/bin/python2.7
import requests
import json
from pymongo import MongoClient
import pymongo
import sys

from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('mongodb://localhost:27017/')

enc = "latin-1"
# data base name : 'test-database-1'
mydb = client['datamining']


def getInfoMovie(titleMovie, page, year):
	response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=926097b9663e23e015f7128e47620eac&query=' + str(titleMovie) + '&page=' + str(page) + '&year=' + str(year))

	assert response.status_code == 200

	result = response.json()
	return result


def main():
	count = 0
	indexMongo = 148
	with open("../../../netflixData/movieTitles.csv", "rb") as myFileRead:
		with open("resultSearch.csv", "w") as myFileWrite:
			for line in myFileRead:
				line = line.decode(enc)
				line = line.encode("utf8")
				datos = (line.rstrip()).split(",") # [0] => ID_MOVIE, [1] => YEAR_RELEASE, [2] => TITLE
				myFileWrite.write(str(line) )
				#if (count < 3):
				contenido = []
				titleMovie = (datos[2])
				yearMovieRelease = (datos[1])
				result = getInfoMovie(titleMovie, 1, yearMovieRelease)
				if ( result['total_results'] >= 0 ): # Si hay resultados
					if ( result['total_pages'] != 1 ): # Si hay mas de una pagina
						page = 1
						while ( page <= result['total_pages'] ):
							result = getInfoMovie(titleMovie, page, yearMovieRelease)
							print ('total_results:' + str(result['total_results']))
							print ('page: ' + str(result['page']))
							print ('total_pages: ' + str(result['total_pages']))

							for res in result['results']:
								tmpBuffer = ""
								tmpBuffer = "{},{},{},{},{},{},{},{},{},{},{}".format(datos[0], datos[1], datos[2], str(res['id']), str(res['title']), str(res['popularity']), str(res['original_language']), str(res['original_title']), str(res['genre_ids']), str(res['adult']), str(res['release_date']))
								dicAux = {
									"ID_MOVIE": datos[0],
									"YEAR": datos[1],
									"TITLE_MOVIE": datos[2],
									"ID": res['id'],
									"TITLE_SEARCH": res['title'],
									"POPULARITY": res['popularity'],
									"ORIGINAL_LANGUAGE": res['original_language'],
									"ORIGINAL_TITLE": res['original_title'],
									"GENRE_IDS": res['genre_ids'],
									"ADULT": res['adult'],
									"RELEASE_DATE": res['release_date']
								}
								indexMongo += 1
								contenido.append(dicAux)
								print(str(tmpBuffer))
								#myFileWrite.write(str(tmpBuffer) + "\n")
							page += 1
					else: 
						# print (result)
						print ("\nUn solo resultado")
						#print json.dumps(result, indent=4, sort_keys=True)
						print ('total_results:' + str(result['total_results']))
						print ('page: ' + str(result['page']))
						print ('total_pages: ' + str(result['total_pages']))

						for res in result['results']:
						#	print ('vote_count: ' + str(res['vote_count']))
							#print ('id: ' + str(res['id']))
						#	print ('video: ' + str(res['video']))
						#	print ('vote_average: ' + str(res['vote_average']))
							#print ('title: ' + str(res['title']))
							#print ('popularity: ' + str(res['popularity']))
						#	print ('poster_path: ' + str(res['poster_path']))
							#print ('original_language: ' + str(res['original_language']))
							#print ('original_title: ' + str(res['original_title']))
							#print ('genre_ids: ' + str(res['genre_ids']))
						#	print ('backdrop_path: ' + str(res['backdrop_path']))
							#print ('adult: ' + str(res['adult']))
						#	print ('overview: ' + str(res['overview']))
							#print ('release_date: ' + str(res['release_date']))
							tmpBuffer = ""
							tmpBuffer = "{},{},{},{},{},{},{},{},{},{},{}".format(datos[0], datos[1], datos[2], str(res['id']), str(res['title']), str(res['popularity']), str(res['original_language']), str(res['original_title']), str(res['genre_ids']), str(res['adult']), str(res['release_date']))
							print(str(tmpBuffer))
							dicAux = {
								"ID_MOVIE": datos[0],
								"YEAR": datos[1],
								"TITLE_MOVIE": datos[2],
								"ID": res['id'],
								"TITLE_SEARCH": res['title'],
								"POPULARITY": res['popularity'],
								"ORIGINAL_LANGUAGE": res['original_language'],
								"ORIGINAL_TITLE": res['original_title'],
								"GENRE_IDS": res['genre_ids'],
								"ADULT": res['adult'],
								"RELEASE_DATE": res['release_date']
							}
							indexMongo += 1
							contenido.append(dicAux)
							#myFileWrite.write(str(tmpBuffer) + "\n")
						#page += 1
				else:
					print ("No hay resultados para la pelicula: " + str(titleMovie))
				try:
					if (len(contenido) == 1):
						mydb.searchs.insert(contenido)
					elif (len(contenido) > 1):
						mydb.searchs.insert_many(contenido)
				except pymongo.errors.BulkWriteError as bwe:
					pprint(bwe.details)				

				#count += 1
	#titleMovie = "Hardware Wars"

	#getInfoMovie(titleMovie)

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