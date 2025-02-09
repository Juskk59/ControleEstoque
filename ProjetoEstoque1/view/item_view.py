import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from bson import ObjectId

class ItemView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Controle de Estoque")
        
        # Tema e estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 12, 'bold'), background="#4CAF50", foreground="white", padding=10)
        self.style.map('TButton', background=[('active', '#45a049')])
        self.style.configure('TLabel', font=('Arial', 12), background="#f4f4f4", foreground="#333")
        self.style.configure('TEntry', font=('Arial', 12), padding=5)
        
        # Frames
        self.login_frame = ttk.Frame(root, padding="10", style="TFrame")
        self.register_frame = ttk.Frame(root, padding="10", style="TFrame")
        self.main_frame = ttk.Frame(root, padding="10", style="TFrame")
        
        self.root.configure(bg='#f4f4f4')  # Fundo claro

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

    def create_main_screen(self):
        self.add_button = ttk.Button(self.main_frame, text="Adicionar Item", command=self.show_add_item_screen)
        self.add_button.pack()
        self.show_button = ttk.Button(self.main_frame, text="Mostrar Itens", command=self.show_items)
        self.show_button.pack()
        self.update_button = ttk.Button(self.main_frame, text="Atualizar Item", command=self.show_update_item_screen)
        self.update_button.pack()
        self.delete_button = ttk.Button(self.main_frame, text="Deletar Item", command=self.delete_item)
        self.delete_button.pack()

    def show_add_item_screen(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Adicionar Item")
        add_window.geometry("300x300")

        ttk.Label(add_window, text="Nome do Item").pack()
        item_entry = ttk.Entry(add_window)
        item_entry.pack()

        ttk.Label(add_window, text="Categoria").pack()
        category_entry = ttk.Entry(add_window)
        category_entry.pack()

        ttk.Label(add_window, text="Preço").pack()
        price_entry = ttk.Entry(add_window)
        price_entry.pack()

        ttk.Label(add_window, text="Descrição").pack()
        description_entry = ttk.Entry(add_window)
        description_entry.pack()

        ttk.Label(add_window, text="Quantidade").pack()
        quantity_entry = ttk.Entry(add_window)
        quantity_entry.pack()

        def add_item():
            nome = item_entry.get()
            categoria = category_entry.get()
            preco = float(price_entry.get())
            quantidade = int(quantity_entry.get())
            descricao = description_entry.get()

            if nome and categoria and preco >= 0 and quantidade >= 0:
                self.controller.add_item({"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade, "descricao": descricao})
                messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
                add_window.destroy()

        ttk.Button(add_window, text="Salvar", command=add_item).pack()

    def show_items(self):
        items_window = tk.Toplevel(self.root)
        items_window.title("Itens em Estoque")

        items_frame = ttk.Frame(items_window, padding="10")
        items_frame.pack(fill=tk.BOTH, expand=True)

        headers = ["ID", "Nome do Item", "Categoria", "Preço", "Quantidade", "Descrição"]
        for col, header in enumerate(headers):
            label = ttk.Label(items_frame, text=header, font=("Arial", 12, "bold"), background="#f4f4f4", foreground="#333")
            label.grid(row=0, column=col, padx=10, pady=5)

        items = self.controller.get_items()
        for index, item in enumerate(items):
            item_id = item.get("_id", "ID não disponível")  # Usando ObjectId diretamente
            nome = item.get("nome", "Nome não disponível")
            categoria = item.get("categoria", "Categoria não disponível")
            preco = item.get("preco", 0)
            quantidade = item.get("quantidade", 0)
            descricao = item.get("descricao", "Descrição não disponível")

            row = [str(item_id), nome, categoria, f"R${preco:.2f}", f"{quantidade} unidades", descricao]
            for col, data in enumerate(row):
                label = ttk.Label(items_frame, text=data, font=("Arial", 12), background="#f4f4f4", foreground="#333")
                label.grid(row=index + 1, column=col, padx=10, pady=5)

    def show_update_item_screen(self):
        # Janela para o usuário digitar o ID do item a ser alterado
        item_id_str = simpledialog.askstring("Atualizar Item", "Digite o ID do item que você deseja atualizar:")

        if item_id_str:
            try:
                # Convertendo o ID para ObjectId do MongoDB
                item_id = ObjectId(item_id_str)
            except Exception as e:
                messagebox.showerror("Erro", "ID inválido. Tente novamente.")
                return
            
            # Buscando o item no banco de dados com o ID informado
            item = self.controller.get_item_by_id(item_id)
            
            if item:  # Verificando se o item existe
                update_window = tk.Toplevel(self.root)
                update_window.title("Atualizar Item")
                update_window.geometry("300x350")  # Ajuste de tamanho para garantir que tudo caiba

                # Campos de edição com os dados atuais do item
                ttk.Label(update_window, text="Nome do Item").pack()
                item_entry = ttk.Entry(update_window)
                item_entry.insert(0, item["nome"])  # Preenchendo com os dados do item
                item_entry.pack()

                ttk.Label(update_window, text="Categoria").pack()
                category_entry = ttk.Entry(update_window)
                category_entry.insert(0, item["categoria"])  # Preenchendo com os dados do item
                category_entry.pack()

                ttk.Label(update_window, text="Preço").pack()
                price_entry = ttk.Entry(update_window)
                price_entry.insert(0, str(item["preco"]))  # Preenchendo com os dados do item
                price_entry.pack()

                ttk.Label(update_window, text="Descrição").pack()
                description_entry = ttk.Entry(update_window)
                description_entry.insert(0, item["descricao"])  # Preenchendo com os dados do item
                description_entry.pack()

                ttk.Label(update_window, text="Quantidade").pack()
                quantity_entry = ttk.Entry(update_window)
                quantity_entry.insert(0, str(item["quantidade"]))  # Preenchendo com os dados do item
                quantity_entry.pack()

                # Função para atualizar o item
                def update_item():
                    updated_item = {
                        "nome": item_entry.get(),
                        "categoria": category_entry.get(),
                        "preco": float(price_entry.get()),
                        "quantidade": int(quantity_entry.get()),
                        "descricao": description_entry.get()
                    }

                    # Atualizando o item no banco de dados
                    success = self.controller.update_item(item_id, updated_item)
                    if success:
                        messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")
                        update_window.destroy()
                    else:
                        messagebox.showerror("Erro", "Erro ao atualizar o item. Tente novamente.")

                ttk.Button(update_window, text="Salvar", command=update_item).pack()

            else:
                messagebox.showerror("Erro", "Item não encontrado. Verifique o ID.")


    
    def delete_item(self):
        item_id = simpledialog.askstring("Deletar Item", "Digite o ID do item:")
        if item_id: 
            self.controller.delete_item(item_id)
            messagebox.showinfo("Sucesso", "Item deletado com sucesso!")
