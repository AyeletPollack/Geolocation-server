import pymongo

mongo = pymongo.MongoClient(
   host='localhost',
   port=27017,
   serverSelectionTimeoutMS=1000
)
db = mongo["geolocation"]
col = db["geolocation"]

#print(mongo.admin.command('replSetGetStatus', check=False))
