import pymongo
import json
from pymongo import MongoClient, InsertOne

def write():
    connection_string = 'connection-string'
    database = 'database-name'
    collection = 'test1'
    client = pymongo.MongoClient(connection_string)
    db = client.database
    collection = db.collection
    requesting = []

    with open(r"../output.json") as f:
        for jsonObj in f:
            myDict = json.loads(jsonObj)
            print(myDict)
            requesting.append(InsertOne(myDict))

    result = collection.bulk_write(requesting)
    client.close()
