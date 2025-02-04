from model.database import collection

class ProdutoModel:
    @staticmethod
    def inserir_produto(nome, categoria, quantidade, preco):
        produto = {
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade,
            "preco": preco
        }
        return collection.insert_one(produto)

    @staticmethod
    def listar_produtos():
        return list(collection.find({}, {"_id": 0}))  # Retorna todos os produtos sem o ID

    @staticmethod
    def atualizar_produto(nome, novos_dados):
        return collection.update_one({"nome": nome}, {"$set": novos_dados})

    @staticmethod
    def deletar_produto(nome):
        return collection.delete_one({"nome": nome})
