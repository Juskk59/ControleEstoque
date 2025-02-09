from model.item_model import ItemModel
from model.user_model import UserModel
from model.supplier_model import SupplierModel

class ItemController:
    def __init__(self, view):
        self.model = ItemModel()  # Interage com a model de itens
        self.user_model = UserModel()  # Interage com a model de usuários
        self.view = view  # A view que se comunica com o usuário

    def add_item(self, item):
        """Adiciona o item ao banco de dados"""
        return self.model.add_item(item)

    def get_items(self):
        """Retorna todos os itens"""
        return self.model.get_items()

    def update_item(self, item_id, updated_item):
        """Atualiza o item no banco de dados"""
        return self.model.update_item(item_id, updated_item)

    def delete_item(self, item_id):
        """Deleta o item do banco de dados"""
        return self.model.delete_item(item_id)

    def register(self, user):
        """Cadastra um usuário"""
        return self.user_model.add_user(user)

    def login(self, username, password):
        """Verifica o login do usuário"""
        user = self.user_model.get_user_by_username(username)
        return user and user["password"] == password

    def get_item_by_id(self, item_id):
        """Busca um item pelo seu ID"""
        return self.model.get_item_by_id(item_id)

class SupplierController:
    def __init__(self):
        self.supplier_model = SupplierModel()  # Instanciando o modelo de fornecedores

    def add_supplier(self, supplier):
        return self.supplier_model.add_supplier(supplier)

    def update_supplier(self, supplier_id, updated_supplier):
        return self.supplier_model.update_supplier(supplier_id, updated_supplier)

    def remove_supplier(self, supplier_id):
        return self.supplier_model.remove_supplier(supplier_id)

    def get_supplier_by_id(self, supplier_id):
        return self.supplier_model.get_supplier_by_id(supplier_id)

    def get_suppliers(self):
        """Retorna todos os fornecedores"""
        return self.supplier_model.get_suppliers()
