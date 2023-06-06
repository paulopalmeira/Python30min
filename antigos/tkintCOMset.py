import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

nomes = {"Alice", "Bob", "Charlie"}  # Conjunto inicial de nomes
itens_adicionados = set()
itens_removidos = set()

def adicionar_nome():
    nome = entry_nome.get()
    if nome in nomes:
        messagebox.showinfo("Aviso", f"O nome '{nome}' já existe no conjunto.")
    else:
        nomes.add(nome)
        itens_adicionados.add(nome)
        messagebox.showinfo("Sucesso", f"O nome '{nome}' foi adicionado ao conjunto.")
        atualizar_planilha()
    entry_nome.delete(0, tk.END)  # Limpa o campo de entrada

def remover_nome():
    nome = entry_nome.get()
    if nome in nomes:
        nomes.remove(nome)
        itens_removidos.add(nome)
        messagebox.showinfo("Sucesso", f"O nome '{nome}' foi removido do conjunto.")
        atualizar_planilha()
    else:
        messagebox.showinfo("Aviso", f"O nome '{nome}' não existe no conjunto.")
    entry_nome.delete(0, tk.END)  # Limpa o campo de entrada

def atualizar_planilha():
    # Limpar a planilha
    for row in treeview.get_children():
        treeview.delete(row)
    # Adicionar itens adicionados
    for item in itens_adicionados:
        treeview.insert("", "end", text=item, values=("Adicionado",))
    # Adicionar itens removidos
    for item in itens_removidos:
        treeview.insert("", "end", text=item, values=("Removido",))

# Criação da janela principal
janela = tk.Tk()
janela.title("Manipulação de Nomes")
janela.geometry("400x300")

# Frame para a seção de adicionar/remover nomes
frame_secao = tk.Frame(janela)
frame_secao.pack(pady=10)

# Label para exibir a opção selecionada
label_opcao = tk.Label(frame_secao, text="Opção selecionada: ")
label_opcao.grid(row=0, column=0, padx=5)

# Entry para digitar o nome
entry_nome = tk.Entry(frame_secao)
entry_nome.grid(row=1, column=0, padx=5)

# OptionMenu para selecionar a opção
opcoes = ["Adicionar", "Remover"]
opcao_var = tk.StringVar(janela)
opcao_var.set(opcoes[0])  # Definir a primeira opção como padrão
opcao_menu = tk.OptionMenu(frame_secao, opcao_var, *opcoes)
opcao_menu.grid(row=2, column=0, padx=5)

# Botão para executar a ação selecionada
botao_executar = tk.Button(frame_secao, text="Executar", command=lambda: adicionar_nome() if opcao_var.get() == "Adicionar" else remover_nome())
botao_executar.grid(row=3, column=0, pady=5)

# Frame para a planilha
frame_planilha = tk.Frame(janela)
frame_planilha.pack(pady=10)

# Label da planilha
label_planilha = tk.Label(frame_planilha, text="Planilha:")
label_planilha.pack()

# Treeview para exibir os itens adicionados e removidos
treeview = ttk.Treeview(frame_planilha)
treeview["columns"] = ("Status")
treeview.column("#0", width=150, minwidth=150, stretch=tk.NO)
treeview.column("Status", width=100, minwidth=100, stretch=tk.NO)
treeview.heading("#0", text="Nome", anchor=tk.W)
treeview.heading("Status", text="Status", anchor=tk.W)
treeview.pack()

# Função para atualizar a planilha
def atualizar_planilha():
    # Limpar a planilha
    for row in treeview.get_children():
        treeview.delete(row)
    # Adicionar itens adicionados
    for item in itens_adicionados:
        treeview.insert("", "end", text=item, values=("Adicionado",))
    # Adicionar itens removidos
    for item in itens_removidos:
        treeview.insert("", "end", text=item, values=("Removido",))

# Exibir a janela
janela.mainloop()
