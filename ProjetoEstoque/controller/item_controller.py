from model.item_model import ItemModel
from model.user_model import UserModel

class ItemController:
    def __init__(self, view):
        self.model = ItemModel()
        self.user_model = UserModel()
        self.view = view

    def get_next_item_id(self):
        return self.model.get_next_item_id()

    def add_item(self, item):
        item['id'] = self.get_next_item_id()
        self.model.add_item(item)

    def get_items(self):
        return self.model.get_items()

    def update_item(self, item_id, updated_item):
        self.model.update_item(item_id, updated_item)

    def delete_item(self, item_id):
        self.model.delete_item(item_id)

    def record_entry(self, item_id, quantity):
        self.model.record_entry(item_id, quantity)

    def record_exit(self, item_id, quantity):
        self.model.record_exit(item_id, quantity)

    def register(self, user):
        self.user_model.add_user(user)

    def login(self, username, password):
        user = self.user_model.get_user_by_username(username)
        if user and user["password"] == password:
            return True
        return False
