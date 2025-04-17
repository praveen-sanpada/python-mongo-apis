# db.py
from pymongo import MongoClient
from config import Config

class Database:
    def __init__(self):
        # MongoDB connection setup using URI from config
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.MONGO_DBNAME]  # Database Name

    def get_collection(self, collection_name):
        return self.db[collection_name]
