from mongoConnection import col, mongo
import pymongo

def check_connection():
    try:
        mongo.server_info()
    except pymongo.errors.ServerSelectionTimeoutError as s:
        raise Exception(s)


def get_location(source, destination):
    return list(col.find({"$or": [{"locationA": destination, "locationB": source},{"locationA": source, "locationB": destination}]}))


def update_hits(id, oldhits):
    oldvalue = {"_id": id}
    newvalue = {"$set": {"hits": str(oldhits + 1)}}
    col.update_one(oldvalue, newvalue)


def update_distance(id, numberOfKMs):
    oldvalue = {"_id": id}
    newvalue = {"$set": {"distance": str(numberOfKMs)}}
    col.update_one(oldvalue, newvalue)


def insert(source, destination, numberOfKMs):
    col.insert_one({"locationA": source, "locationB": destination, "hits": "0", "distance": numberOfKMs})


def find_all():
    return list(col.find())


def find_max_hits():
    return col.find_one(sort=[("hits", -1)])





