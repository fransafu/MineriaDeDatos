#!/usr/bin/python2.7

from bs4 import BeautifulSoup
import urllib2
import requests
import eventlet
eventlet.monkey_patch()

URL = "https://www.filmaffinity.com/cl/main.html"
URL = "https://www.filmaffinity.com/cl/search.php?stext="

def main():
    print ("Inicia programa")

    #contenido = urllib2.urlopen(URL).read()
    #soup = BeautifulSoup(contenido)

    #print (soup.prettify())

    #print (soup.title.string)

    with open("../netflixData/movieTitles.csv", "rb") as myFileRead:
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

if __name__ == '__main__':
    main()
