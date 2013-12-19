from pymongo import MongoClient

def get_db():
    conn = MongoClient()
    return conn['records']
