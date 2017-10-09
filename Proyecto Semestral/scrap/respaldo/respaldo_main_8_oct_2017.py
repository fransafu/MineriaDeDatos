#!/usr/bin/python2.7
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getInfoMovie(titleMovie, page):
	response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=926097b9663e23e015f7128e47620eac&query=' + str(titleMovie) + '&page=' + str(page))

	assert response.status_code == 200

	result = response.json()
	return result


def main():
	count = 0
	with open("movieTitles.csv", "rb") as myFileRead:
		with open("resultSearch.csv", "w") as myFileWrite:
			for line in myFileRead:
				# print (line.rstrip()).split(",")
				datos = (line.rstrip()).split(",")
				
				if (count < 3):
					titleMovie = (datos[2])
					result = getInfoMovie(titleMovie, 1)
					print ("-"*30)
					if ( result['total_results'] >= 0 ): # Si hay resultados
						if ( result['total_pages'] != 1 ): # Si hay mas de una pagina
							page = 1
							while ( page <= result['total_pages'] ):
								result = getInfoMovie(titleMovie, page)
								#print (result)
								#print json.dumps(result, indent=4, sort_keys=True)
								print ('total_results:' + str(result['total_results']))
								print ('page: ' + str(result['page']))
								print ('total_pages: ' + str(result['total_pages']))

								for res in result['results']:
									#print ('vote_count: ' + str(res['vote_count']))
								#	print ('id: ' + str(res['id']))
									#print ('video: ' + str(res['video']))
									# print ('vote_average: ' + str(res['vote_average']))
								#	print ('title: ' + str(res['title']))
								#	print ('popularity: ' + str(res['popularity']))
									#print ('poster_path: ' + str(res['poster_path']))
								#	print ('original_language: ' + str(res['original_language']))
								#	print ('original_title: ' + str(res['original_title']))
								#	print ('genre_ids: ' + str(res['genre_ids']))
									#print ('backdrop_path: ' + str(res['backdrop_path']))
								#	print ('adult: ' + str(res['adult']))
									#print ('overview: ' + str(res['overview']))
								#	print ('release_date: ' + str(res['release_date']))
									tmpBuffer = ""
									tmpBuffer = "{},{},{},{},{},{},{},{},{},{},{}".format(datos[0], datos[1], datos[2], str(res['id']), str(res['title']), str(res['popularity']), str(res['original_language']), str(res['original_title']), str(res['genre_ids']), str(res['adult']), str(res['release_date']))
									print(str(tmpBuffer))
									myFileWrite.write(str(tmpBuffer) + "\n")
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
								myFileWrite.write(str(tmpBuffer) + "\n")
							#page += 1
					else:
						print ("No hay resultados para la pelicula: " + str(titleMovie))


				count += 1
	#titleMovie = "Hardware Wars"

	#getInfoMovie(titleMovie)

if __name__ == '__main__':
	main()
#for repo in response.json():
#	print repo
    #print '[{}] {}'.format(repo['language'], repo['name'])


"""
    with open("movieTitles.csv", "rb") as myFileRead:
        for line in myFileRead:
            print (line.rstrip()).split(",")
            datos = (line.rstrip()).split(",")
            URL_BUSCAR = str('https://www.filmaffinity.com/cl/advsearch.php?stext={0}&stype%5B%5D=title&country=&genre=&fromyear={1}&toyear={1}'.format(str(datos[2]), str(datos[1])))
            print (URL_BUSCAR)
            with eventlet.Timeout(10):
                page = requests.get(URL_BUSCAR)
                soup = BeautifulSoup(page.content, 'html.parser')
                for link in soup.find_all('a'):
                    if (datos[2] in link):
                        print(link.get('title'))
"""