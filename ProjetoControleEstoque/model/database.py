from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Criar banco de dados e coleção
db = client["estoque_db"]
collection = db["produtos"]
