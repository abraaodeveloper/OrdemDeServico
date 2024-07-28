import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from db import buscar_ordens

def criar_tela_principal():
    # Configuração do tema do CustomTkinter
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Criação da janela principal
    app = ctk.CTk()
    app.title("Ordem de Serviço")

    # Frame para o campo de busca
    frame_busca = ctk.CTkFrame(app)
    frame_busca.pack(padx=20, pady=10, fill="x")

    # Label do campo de busca
    label_busca = ctk.CTkLabel(frame_busca, text="Buscar:")
    label_busca.pack(side="left")

    # Campo de entrada para busca
    entry_busca = ctk.CTkEntry(frame_busca)
    entry_busca.pack(side="left", fill="x", expand=True)

    # Botão de busca
    botao_buscar = ctk.CTkButton(frame_busca, text="Buscar", command=lambda: atualizar_listagem(entry_busca.get()))
    botao_buscar.pack(side="right")

    # Frame para a listagem
    frame_listagem = ctk.CTkFrame(app)
    frame_listagem.pack(padx=20, pady=10, fill="both", expand=True)

    # Treeview para exibir as ordens de serviço
    tree = ttk.Treeview(frame_listagem, columns=("ID", "Cliente", "Aparelho", "Problema", "Status"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Cliente", text="Cliente")
    tree.heading("Aparelho", text="Aparelho")
    tree.heading("Problema", text="Problema")
    tree.heading("Status", text="Status")

    tree.pack(fill="both", expand=True)

    # Função para atualizar a listagem com base na busca

    """
    def atualizar_listagem(busca):
        for i in tree.get_children():
            tree.delete(i)
        ordens = buscar_ordens(busca)
        for ordem in ordens:
            tree.insert("", "end", values=ordem)

    # Inicializa a listagem com todos os registros
    atualizar_listagem("")
    """
    # Inicia o loop principal da aplicação
    app.mainloop()
