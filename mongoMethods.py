from mongoConnection import col


def get_location(source, destination):
    return list(col.geolocation.find({"$or": [{"locationA": destination, "locationB": source},{"locationA": source, "locationB": destination}]}))

def update_hits(id, oldhits):
    oldvalue = {"_id": id}
    newvalue = {"$set": {"hits": str(oldhits + 1)}}
    col.geolocation.update_one(oldvalue, newvalue)


def update_distance(id, numberOfKMs):
    oldvalue = {"_id": id}
    newvalue = {"$set": {"distance": str(numberOfKMs)}}
    col.geolocation.update_one(oldvalue, newvalue)


def insert(source, destination, numberOfKMs):
    col.geolocation.insert_one({"locationA": source, "locationB": destination, "hits": "0", "distance": numberOfKMs})

def find_all():
    return list(col.geolocation.find())








