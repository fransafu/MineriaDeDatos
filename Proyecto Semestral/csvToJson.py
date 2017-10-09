import csv
import json

# const var
PATHFILECSV = './netflixData/combined_data_4.csv'
PATHFILEJSON = './netflixData/combined_data_4.json'

def csvToJson(reader, jsonFile):
    contador = 0
    jsonFile.write('[')
    for row in reader:
        #json.dump(row, jsonFile)
        #jsonFile.write('\n')
        contador += 1
        #print ("Contador " + str(contador) + " de 24053764")
        if (contador != 24053764):
            json.dump(row, jsonFile)
            jsonFile.write(',\n')
        else:
            print ("Escribiendo ultima linea")
            json.dump(row, jsonFile)
            jsonFile.write('\n')
            
    jsonFile.write(']')

if __name__ == "__main__":
    print ("Inicia programa.")

    # Open file
    csvFile  = open(PATHFILECSV, 'r')
    jsonFile = open(PATHFILEJSON, 'w')

    # declare field
    fieldNames = ("IDMOVIE","IDUSUARIO","RANKING","FECHA")
    reader = csv.DictReader( csvFile, fieldNames)

    # Init function
    csvToJson(reader, jsonFile)

    print ("Finaliza programa")