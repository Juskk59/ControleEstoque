from pymongo import MongoClient
from bson import ObjectId
from pymongo.collection import ReturnDocument

class ItemModel:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['controle_estoque']
        self.collection = self.db['itens']
        self.counter_collection = self.db['counter']

    def get_next_item_id(self):
        # Aqui incrementamos o contador para gerar o próximo ID numérico
        counter = self.counter_collection.find_one_and_update(
            {"_id": "item_id"},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return counter['seq']

    def add_item(self, item):
        # Agora adicionamos o item com o ID numérico
        self.collection.insert_one(item)

    def get_items(self):
        return list(self.collection.find())

    def update_item(self, item_id, updated_item):
        # A busca pelo ID agora usa o ID numérico no campo "id"
        self.collection.update_one({"id": item_id}, {"$set": updated_item})

    def delete_item(self, item_id):
        # A busca pelo ID agora usa o ID numérico no campo "id"
        self.collection.delete_one({"id": item_id})
