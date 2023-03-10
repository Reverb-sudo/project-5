import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.lists


def brevet_insert(start, brevet_dist_km, controllist):
    print("hit brevet_insert")
    thecollection = collection.insert_one(
    {'start': start,
    'brevet_dist_km': brevet_dist_km,
    'controllist': controllist}
    )
    theid = thecollection.inserted_id
    return str(theid)

def brevet_fetch():
    lists = collection.find().sort("_id",-1).limit(1)
    for list in lists:
        del list["_id"]
        return list
