from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from datetime import datetime
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

#Step 1: Connect to MongoDB - Note: Change connection string as needed
#client = MongoClient(port=27017, user='root', password='ling-n')

#db=client.datamining

#print (client.database_names())
"""
uri = "mongodb://root:ling-n@localhost/datamining?authSource=admin"
client = MongoClient(uri)

db = client.test

print (db.name)

#print (db.movies)

print (db.movies.insert_one({"x": 10}).inserted_id)


cursor = db.movies.find({})

for doc in cursor:
	print (doc)
    #print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
    #       (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))
"""
"""
db.createUser(
{
    user: "root",
    pwd: "ling-n",
    roles: [
              { role: "userAdminAnyDatabase", db: "datamining" },
              { role: "readWriteAnyDatabase", db: "datamining" },
              { role: "dbAdminAnyDatabase", db: "datamining" },
              { role: "clusterAdmin", db: "datamining" }
           ]
})

db.createUser(
  {
    user: "admin",
    pwd: "ling-n",
    roles: [ { role: ["userAdminAnyDatabase", "readWriteAnyDatabase", "dbAdminAnyDatabase", "clusterAdmin"], db: "admin" } ]
  }
)

db.createUser(
{
    user: "admin", 
    pwd: "ling-n", 
    roles:["root"]
})


db.createUser(
{
    user: "tom",
    pwd: "jerry",
    roles: [
              { role: "userAdminAnyDatabase", db: "admin" },
              { role: "readWriteAnyDatabase", db: "admin" },
              { role: "dbAdminAnyDatabase", db: "admin" },
              { role: "clusterAdmin", db: "admin" }
           ]
})

"""
client = MongoClient("mongodb://admin:ling-n@127.0.0.1/datamining")
db = client['datamining']

print (db.name)
print (db.movies)
print (db.movies.insert_one({"x": 10}).inserted_id)


"""
### Create seed data

SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]


def insertMovie():

    client = pymongo.MongoClient(uri)

    db = client.get_default_database()
    
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.

    songs = db['songs']

    # Note that the insert method can take either an array or a single dict.

    songs.insert_many(SEED_DATA)

    # Then we need to give Boyz II Men credit for their contribution to
    # the hit "One Sweet Day".

    query = {'song': 'One Sweet Day'}

    songs.update(query, {'$set': {'artist': 'Mariah Carey ft. Boyz II Men'}})

    # Finally we run a query which returns all the hits that spent 10 or
    # more weeks at number 1.

    cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

    for doc in cursor:
        print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
               (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))
    
    ### Since this is an example, we'll clean up after ourselves.

    db.drop_collection('songs')

    ### Only close the connection when your app is terminating

    client.close()

"""

"""
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

print ( result.inserted_id )
"""
#result = db.testData.insert_one({'x': 1})

#print('Created n of 100 as {1}'.format(result.inserted_id))
"""
print (db.find({}))
print (db.count())
print (client.database_names())
"""
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)

#Step 2: Create sample data
#names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
#company_type = ['LLC','Inc','Company','Corporation']
#company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
#for x in xrange(1, 501):
#    business = {
#        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
#        'rating' : randint(1, 5),
#        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
#    }
    #Step 3: Insert business object directly into MongoDB via isnert_one
#    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
#    print('Created {0} of 100 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
#print('finished creating 100 business reviews')