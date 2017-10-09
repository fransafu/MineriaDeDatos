# Contexto

Netflix celebró el Premio Netflix concurso abierto para el mejor algoritmo para predecir las calificaciones de los usuarios para las películas. El gran premio fue de $ 1,000,000 y fue ganado por el equipo de BellKor Pragmatic Chaos. Este es el conjunto de datos que se utilizó en esa competencia.

# Contenido

## DATASET DE FORMACIÓN DESCRIPCIÓN DE ARCHIVO

El archivo "training_set.tar" es un tar de un directorio que contiene 17770 archivos, uno por película. La primera línea de cada archivo contiene el ID de película seguido de dos puntos. Cada línea posterior del archivo corresponde a una calificación de un cliente y su fecha en el siguiente formato:

## CustomerID, Rating, Fecha

Los ID de película varían de 1 a 17770 secuencialmente.
Los CustomerIDs van de 1 a 2649429, con espacios vacíos. Hay 480189 usuarios.
Las calificaciones están en una escala de cinco estrellas (integral) de 1 a 5.
Las fechas tienen el formato AAAA-MM-DD.

## DESCRIPCIÓN DE ARCHIVOS DE PELÍCULAS

La información de la película en "movie_titles.txt" tiene el siguiente formato:

MovieID, YearOfRelease, Título

MovieID no corresponden a ids de película Netflix o ID de película IMDB.
YearOfRelease puede variar de 1890 a 2005 y puede corresponder al lanzamiento del DVD correspondiente, no necesariamente su versión teatral.
Título es el título de la película de Netflix y puede no corresponder a títulos utilizados en otros sitios. Los títulos están en inglés.

## DATOSET DE CALIFICACIÓN Y PREDICCIÓN DESCRIPCIÓN DE ARCHIVO

El conjunto de datos que califica para el Premio Netflix se encuentra en el archivo de texto "qualifying.txt". Consta de líneas que indican un id de película, seguido de dos puntos y, a continuación, los identificadores de cliente y las fechas de calificación, uno por línea para ese id de película. La película y los identificadores de cliente están contenidos en el conjunto de entrenamiento. Por supuesto, las calificaciones son retenidas. No hay líneas vacías en el archivo.

MovieID1:

CustomerID11, Date11

CustomerID12, Date12

...

MovieID2:

CustomerID21, Date21

CustomerID22, Date22

Para el Premio Netflix, su programa debe predecir todas las calificaciones que los clientes dieron a las películas en el conjunto de datos de calificación basado en la información del conjunto de datos de formación.

El formato del archivo de predicción enviado sigue la película y el ID de cliente, el orden de fecha del conjunto de datos que califica. Sin embargo, su calificación predicha toma el lugar del id de cliente correspondiente (y fecha), uno por línea.

Por ejemplo, si el conjunto de datos calificativo se parecía a:

111:

3245,2005-12-19

5666,2005-12-23

6789,2005-03-14

225:

1234,2005-05-26

3456,2005-11-07

entonces un archivo de predicción debería ser algo como:

111:

3,0

3,4

4.0

225:

1.0

2,0

que predice que el cliente 3245 habría clasificado la película 111 3.0 estrellas el 19 de Diciembre de 2005, que el cliente 5666 lo habría clasificado ligeramente más alto en 3.4 estrellas el 23 de Diciembre, 2005, etc.

Debe hacer predicciones para todos los clientes para todas las películas en el conjunto de datos de calificación.

## DESCRIPCIÓN DEL ARCHIVO DATASET PROBE

Para permitir que pruebe su sistema antes de enviar un conjunto de predicciones basado en el conjunto de datos de calificación, hemos proporcionado un conjunto de datos de sondeo en el archivo "probe.txt". Este archivo de texto contiene líneas que indican un id de película, seguido de dos puntos y, a continuación, los identificadores de cliente, uno por línea para ese id de película.

MovieID1:

CustomerID11

CustomerID12

...

MovieID2:

CustomerID21

CustomerID22

Al igual que el conjunto de datos de calificación, la película y los pares de identificación del cliente están contenidos en el conjunto de formación. Sin embargo, a diferencia del conjunto de datos que califica, las calificaciones (y las fechas) para cada par están contenidas en el conjunto de datos de formación.

Si lo desea, puede calcular el RMSE de sus predicciones en comparación con esas clasificaciones y comparar su RMSE con el RMSE de Cinematch en los mismos datos. Consulte http://www.netflixprize.com/faq#probe para obtener ese valor.

## Notas

El conjunto de datos se descargó desde: https://archive.org/download/nf_prize_dataset.tar
