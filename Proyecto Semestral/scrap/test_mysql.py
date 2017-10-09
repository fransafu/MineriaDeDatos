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