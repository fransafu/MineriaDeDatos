from pymongo import MongoClient
import datetime
import sys
from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('mongodb://localhost:27017/')

enc = "latin-1"
# data base name : 'test-database-1'
mydb = client['datamining']
"""
contenido = []
with open("../netflixData/movieTitles.csv", "r") as myFileRead:
    for line in myFileRead:
        line = line.decode(enc)
        line = line.encode("utf8")

        datos = (line.rstrip()).split(",")
        dicAux = {
            "ID_MOVIE": datos[0],
            "YEAR": datos[1],
            "TITLE": datos[2]
        }
        contenido.append(dicAux)
"""
#pprint(contenido)
#record_id = mydb.movies.insert(contenido)

#print record_id
#print mydb.collection_names()

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

print ("Inicia final training")
with open("../../../Respaldo_merge_data/final_training_set_v1.csv", "rb") as myFileRead:
    for line in myFileRead:
        contenido = []
        datos = (line.rstrip()).split(",")
        dicAux = {
            "DATE_RATING": datos[0],
            "ID_USUARIO": datos[1],
            "RATING": datos[2],
            "RELEASE_DATE": datos[3],
            "YEAR": datos[4],
            "ID_MOVIE": datos[5],
            "ID": datos[6],
            "GENRE": datos[7],
            "POPULARITY": datos[8],
            "TITLE_SEARCH": datos[9],
            "ORIGINAL_LANGUAGE": datos[10]

        }
        contenido.append(dicAux)
        record_id = mydb.training_sets_final.insert(contenido)



# record_id = mydb.training_sets.insert(contenido)
"""
print ("Inicia namefile2")
contenido = []
with open(namefile2, "rb") as myFileRead:
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

print ("Inicia namefile3")
contenido = []
with open(namefile3, "rb") as myFileRead:
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

print ("Inicia namefile4")
contenido = []
with open(namefile4, "rb") as myFileRead:
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

"""
import pymysql.cursors

def seedMovies(connection):
    with open("movieTitles.csv", "rb") as myFileRead:
        for line in myFileRead:
            datos = (line.rstrip()).split(",") # [0] => ID_MOVIE, [1] => YEAR_RELEASE, [2] => TITLE
            try:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `movies` (`ID_MOVIE`, `YEAR_RELEASE`, `TITLE`) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (datos[0], datos[1], datos[2]))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()

                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT `ID_MOVIE`, `YEAR_RELEASE`, `TITLE` FROM `movies` WHERE `ID_MOVIE`=%s"
                    cursor.execute(sql, (datos[0],))
                    result = cursor.fetchone()
                    print(result)
            except:
                pass

def seedTrainingSet(connection, namefile):
    with open(namefile, "rb") as myFileRead:
        for line in myFileRead:
            datos = (line.rstrip()).split(",") # [0] => ID_MOVIE, [1] => YEAR_RELEASE, [2] => TITLE
            try:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `training_sets` (`MOVIE_ID`, `USER_ID`, `RATING`, `DATE_RATING`) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (datos[0], datos[1], datos[2], datos[3]))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()

                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT `MOVIE_ID`, `USER_ID`, `RATING`, `DATE_RATING` FROM `training_sets` WHERE `MOVIE_ID`=%s AND `USER_ID`=%s"
                    cursor.execute(sql, (datos[0], datos[1]))
                    result = cursor.fetchone()
                    print(result)
            except:
                pass
                

def main():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='ling-n',
                                 db='datamining',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    seedMovies(connection)
    

    namefile1 = "../netflixData/combined_data_1.csv"
    seedTrainingSet(connection, namefile1)
    namefile2 = "../netflixData/combined_data_2.csv"
    seedTrainingSet(connection, namefile2)
    namefile3 = "../netflixData/combined_data_3.csv"
    seedTrainingSet(connection, namefile3)
    namefile4 = "../netflixData/combined_data_4.csv"
    seedTrainingSet(connection, namefile4)
    connection.close()

    

if __name__ == '__main__':
    main()
"""