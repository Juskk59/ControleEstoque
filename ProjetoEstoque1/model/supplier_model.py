from pymongo import MongoClient
from bson.objectid import ObjectId

class SupplierModel:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["controle_estoque"]
        self.collection = self.db["fornecedores"]

    def add_supplier(self, supplier):
        self.collection.insert_one(supplier)

    def update_supplier(self, supplier_id, updated_supplier):
        result = self.collection.update_one({"_id": ObjectId(supplier_id)}, {"$set": updated_supplier})
        return result.modified_count > 0

    def remove_supplier(self, supplier_id):
        result = self.collection.delete_one({"_id": ObjectId(supplier_id)})
        return result.deleted_count > 0

    def get_supplier_by_id(self, supplier_id):
        return self.collection.find_one({"_id": ObjectId(supplier_id)})
