import pymongo
import json
from pymongo import MongoClient, InsertOne

def write():
    connection_string = ''
    database = 'nav-data'
    collection = 'test1'
    f = open("../.config")
    f.readline()
    conf = f.readline().split()
    f.close()
    if conf[0] == 'CONNECTION_STRING':
        connection_string = conf[1]
        client = pymongo.MongoClient(connection_string)
        db = client.database
        collection = db.collection
        requesting = []

        with open(r"../output/YPTN.json") as f:
            for jsonObj in f:
                myDict = json.loads(jsonObj)
                print(myDict)
                requesting.append(InsertOne(myDict))

        result = collection.bulk_write(requesting)
        client.close()
    else:
        print("invalid .config, can't write to database")
        exit()
