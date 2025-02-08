# main.py
import tkinter as tk
from controller.item_controller import ItemController
from view.item_view import ItemView

def main():
    root = tk.Tk()
    view = ItemView(root, None)  # Inicializa sem o controller
    controller = ItemController(view)
    view.controller = controller  # Define o controller na view

    # Definir as dimensões da janela
    root.geometry("500x500")  # Largura x Alturax'

    root.mainloop()

if __name__ == "__main__":
    main()  
