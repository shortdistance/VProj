import pymongo
import json


def insert_db(mongodb_url, data):
    client = pymongo.MongoClient(mongodb_url,
                                 connectTimeoutMS=30000,
                                 socketTimeoutMS=None,
                                 socketKeepAlive=True)

    db = client.get_default_database()

    db.my_collection.insert_one(data, safe=True)
