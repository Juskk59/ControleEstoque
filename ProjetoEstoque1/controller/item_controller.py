from model.item_model import ItemModel
from model.user_model import UserModel


class ItemController:
    def __init__(self, view):
        self.model = ItemModel()  # Interage com a model de itens
        self.user_model = UserModel()  # Interage com a model de usuários
        self.view = view  # A view que se comunica com o usuário

    def add_item(self, item):
        """Adiciona o item ao banco de dados"""
        success = self.model.add_item(item)  # Chama o método da model para adicionar
        return success

    def get_items(self):
        """Retorna todos os itens"""
        return self.model.get_items()  # Chama a model para buscar todos os itens

    def update_item(self, item_id, updated_item):
        """Atualiza o item no banco de dados"""
        return self.model.update_item(item_id, updated_item)  # Atualiza o item através da model

    def delete_item(self, item_id):
        """Deleta o item do banco de dados"""
        return self.model.delete_item(item_id)  # Deleta o item através da model

    def register(self, user):
        """Cadastra um usuário"""
        return self.user_model.add_user(user)  # Cadastra o usuário através da model de usuários

    def login(self, username, password):
        """Verifica o login do usuário"""
        user = self.user_model.get_user_by_username(username)  # Busca o usuário
        if user and user["password"] == password:
            return True  # Login bem-sucedido
        return False  # Falha no login

    def get_item_by_id(self, item_id):
        """Busca um item pelo seu ID"""
        return self.model.get_item_by_id(item_id)  # Chama a model para buscar pelo ID

    