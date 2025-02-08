# model/user_model.py
from pymongo import MongoClient
from bson.objectid import ObjectId

class UserModel:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['controle_estoque']
        self.collection = self.db['usuarios']

    def add_user(self, user):
        self.collection.insert_one(user)

    def get_user_by_username(self, username):
        return self.collection.find_one({"username": username})
