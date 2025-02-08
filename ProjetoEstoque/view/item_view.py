import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from bson.objectid import ObjectId

class ItemView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Controle de Estoque")
        
        # Tema: definindo um tema moderno e claro
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Podemos mudar o tema para 'alt' ou 'classic'
        
        # Alterando estilo dos botões
        self.style.configure('TButton', font=('Arial', 12, 'bold'), background="#4CAF50", foreground="white", padding=10)
        self.style.map('TButton', background=[('active', '#45a049')])  # Cor do botão ao passar o mouse
        
        # Alterando estilo das labels
        self.style.configure('TLabel', font=('Arial', 12), background="#f4f4f4", foreground="#333")
        
        # Alterando estilo das entradas
        self.style.configure('TEntry', font=('Arial', 12), padding=5)
        
        # Criando os frames
        self.login_frame = ttk.Frame(root, padding="10", style="TFrame")
        self.register_frame = ttk.Frame(root, padding="10", style="TFrame")
        self.main_frame = ttk.Frame(root, padding="10", style="TFrame")

        # Adicionando fundo claro ao frame
        self.root.configure(bg='#f4f4f4')  # Fundo claro para a janela

        # Criando as telas
        self.create_login_screen()
        self.create_register_screen()
        self.create_main_screen()

        # Exibindo a tela de login
        self.show_login_screen()

    def create_login_screen(self):
        self.login_label = ttk.Label(self.login_frame, text="Login", font=('Arial', 16, 'bold'), anchor="center")
        self.login_label.pack()

        self.username_label = ttk.Label(self.login_frame, text="Usuário")
        self.username_label.pack()
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = ttk.Label(self.login_frame, text="Senha")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.login_button = ttk.Button(self.login_frame, text="Entrar", command=self.login)
        self.login_button.pack()

        self.register_link = ttk.Button(self.login_frame, text="Não tem uma conta? Registre-se", command=self.show_register_screen)
        self.register_link.pack()

    def create_register_screen(self):
        self.register_label = ttk.Label(self.register_frame, text="Registro", font=('Arial', 16, 'bold'), anchor="center")
        self.register_label.pack()

        self.reg_username_label = ttk.Label(self.register_frame, text="Usuário")
        self.reg_username_label.pack()
        self.reg_username_entry = ttk.Entry(self.register_frame)
        self.reg_username_entry.pack()

        self.reg_password_label = ttk.Label(self.register_frame, text="Senha")
        self.reg_password_label.pack()
        self.reg_password_entry = ttk.Entry(self.register_frame, show="*")
        self.reg_password_entry.pack()

        self.register_button = ttk.Button(self.register_frame, text="Registrar", command=self.register)
        self.register_button.pack()

        self.login_link = ttk.Button(self.register_frame, text="Já tem uma conta? Faça login", command=self.show_login_screen)
        self.login_link.pack()

    def create_main_screen(self):
        self.item_label = ttk.Label(self.main_frame, text="Nome do Item")
        self.item_label.pack()
        self.item_entry = ttk.Entry(self.main_frame)
        self.item_entry.pack()

        self.category_label = ttk.Label(self.main_frame, text="Categoria")
        self.category_label.pack()
        self.category_entry = ttk.Entry(self.main_frame)
        self.category_entry.pack()

        self.price_label = ttk.Label(self.main_frame, text="Preço")
        self.price_label.pack()
        self.price_entry = ttk.Entry(self.main_frame)
        self.price_entry.pack()

        self.quantity_label = ttk.Label(self.main_frame, text="Quantidade em Estoque")
        self.quantity_label.pack()
        self.quantity_entry = ttk.Entry(self.main_frame)
        self.quantity_entry.pack()

        # Botões de Ação
        self.add_button = ttk.Button(self.main_frame, text="Adicionar Item", command=self.add_item)
        self.add_button.pack()

        self.show_button = ttk.Button(self.main_frame, text="Mostrar Itens", command=self.show_items)
        self.show_button.pack()

        self.update_button = ttk.Button(self.main_frame, text="Atualizar Item", command=self.update_item)
        self.update_button.pack()

        self.delete_button = ttk.Button(self.main_frame, text="Deletar Item", command=self.delete_item)
        self.delete_button.pack()

    def show_login_screen(self):
        self.register_frame.pack_forget()
        self.main_frame.pack_forget()
        self.login_frame.pack()

    def show_register_screen(self):
        self.login_frame.pack_forget()
        self.main_frame.pack_forget()
        self.register_frame.pack()

    def show_main_screen(self):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.main_frame.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.login(username, password):
            self.show_main_screen()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        if username and password:
            self.controller.register({"username": username, "password": password})
            messagebox.showinfo("Sucesso", "Registro realizado com sucesso!")
            self.show_login_screen()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")

    def add_item(self):
        item_name = self.item_entry.get()
        category = self.category_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        if item_name and category and price and quantity >= 0:
            self.controller.add_item({"nome": item_name, "categoria": category, "preco": price, "quantidade": quantity})
            self.clear_entries()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")

    def show_items(self):
        # Exibindo os itens em uma nova janela
        items_window = tk.Toplevel(self.root)
        items_window.title("Itens em Estoque")

        items_frame = ttk.Frame(items_window, padding="10")
        items_frame.pack(fill=tk.BOTH, expand=True)

        headers = ["ID", "Nome do Item", "Categoria", "Preço", "Quantidade"]
        for col, header in enumerate(headers):
            label = ttk.Label(items_frame, text=header, font=("Arial", 12, "bold"), background="#f4f4f4", foreground="#333")
            label.grid(row=0, column=col, padx=10, pady=5)

        items = self.controller.get_items()
        for index, item in enumerate(items):
            item_id = item.get("_id", "ID não disponível")
            nome = item.get("nome", "Nome não disponível")
            categoria = item.get("categoria", "Categoria não disponível")
            preco = item.get("preco", 0)
            quantidade = item.get("quantidade", 0)
            
            row = [str(item_id), nome, categoria, f"R${preco:.2f}", f"{quantidade} unidades"]
            for col, data in enumerate(row):
                label = ttk.Label(items_frame, text=data, font=("Arial", 12), background="#f4f4f4", foreground="#333")
                label.grid(row=index + 1, column=col, padx=10, pady=5)

    def update_item(self):
        item_id = simpledialog.askstring("Atualizar Item", "Digite o ID do item:")
        if item_id:
            updated_item = {
                "nome": self.item_entry.get(),
                "categoria": self.category_entry.get(),
                "preco": float(self.price_entry.get()),
                "quantidade": int(self.quantity_entry.get())
            }
            self.controller.update_item(item_id, updated_item)
            messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")

    def delete_item(self):
        item_id = simpledialog.askstring("Deletar Item", "Digite o ID do item:")
        if item_id:
            self.controller.delete_item(item_id)
            messagebox.showinfo("Sucesso", "Item deletado com sucesso!")

    def clear_entries(self):
        self.item_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
