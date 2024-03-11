from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://localhost")
    db = client.web20
    return db

