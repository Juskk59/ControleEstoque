from pymongo import MongoClient
from bson import ObjectId
from pymongo.errors import PyMongoError

class ItemModel:
    def __init__(self, db_uri="mongodb://localhost:27017", db_name="controle_estoque", collection_name="itens"):
        try:
            # Conectando ao MongoDB
            self.client = MongoClient(db_uri)  # Use o URI correto do seu MongoDB
            self.db = self.client[db_name]  # Nome do seu banco de dados
            self.collection = self.db[collection_name]  # Nome da sua coleção de itens
        except PyMongoError as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            raise

    def add_item(self, item):
        """Adiciona um novo item à coleção."""
        try:
            # O MongoDB gera automaticamente o campo _id
            self.collection.insert_one(item)
        except PyMongoError as e:
            print(f"Erro ao adicionar item: {e}")
            return False
        return True

    def get_items(self):
        """Retorna todos os itens com _id convertido para string."""
        try:
            items = [{"id": str(item["_id"]), **item} for item in self.collection.find()]
        except PyMongoError as e:
            print(f"Erro ao buscar itens: {e}")
            return []
        return items

    def update_item(self, item_id, updated_item):
        """Atualiza um item no banco de dados."""
        try:
            result = self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
            return result.modified_count > 0  # Retorna True se o item foi atualizado
        except PyMongoError as e:
            print(f"Erro ao atualizar item: {e}")
            return False

    def delete_item(self, item_id):
        """Deleta o item usando o _id."""
        try:
            result = self.collection.delete_one({"_id": ObjectId(item_id)})
            return result.deleted_count > 0  # Retorna True se o item foi deletado
        except PyMongoError as e:
            print(f"Erro ao deletar item: {e}")
            return False

    def get_item_by_id(self, item_id):
        """Busca um item pelo _id."""
        try:
            item = self.collection.find_one({"_id": ObjectId(item_id)})
            if item:
                return {"id": str(item["_id"]), **item}  # Retorna o item com _id como string
            return None  # Retorna None caso o item não seja encontrado
        except PyMongoError as e:
            print(f"Erro ao buscar item por ID: {e}")
            return None
