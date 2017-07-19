import pymongo
import json

def insert_db(mongodb_url, data):
    client = pymongo.MongoClient(mongodb_url,
                         connectTimeoutMS=30000,
                         socketTimeoutMS=None,
                         socketKeepAlive=True)

    db = client.projdb

    if not isinstance(data, dict):
        try:
            data = json.loads(data)
        except Exception as e:
            data = {}

    if data:
        db.collection.insert_one(data)

