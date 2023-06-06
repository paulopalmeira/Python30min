from tkinter import *
from tkinter import messagebox
import mysql.connector

def mostrar_senha():
    if check_mostrar_senha.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

def inserir_dados():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    if username == '' or password == '' or email == '':
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
    else:
        # Conectar ao banco de dados
        conexao = mysql.connector.connect(
            host="db4free.net",
            user="vidrado",
            password="vidrado51",
            database="pythondata"
        )
        cursor = conexao.cursor()

        # Obter o último ID inserido na tabela
        cursor.execute("SELECT MAX(id) FROM login")
        resultado = cursor.fetchone()
        ultimo_id = resultado[0]

        # Verificar se o último ID é nulo
        if ultimo_id is None:
            novo_id = 1
        else:
            novo_id = ultimo_id + 1

        # Inserir os dados na tabela
        sql = "INSERT INTO login (id, username, password, email) VALUES (%s, %s, %s, %s)"
        valores = (novo_id, username, password, email)
        cursor.execute(sql, valores)
        conexao.commit()

        # Fechar a conexão
        cursor.close()
        conexao.close()

        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

# Criar a janela
window = Tk()

# Definir a geometria da janela
largura = 400
altura = 300
pos_x = int(window.winfo_screenwidth() / 2 - largura / 2)
pos_y = int(window.winfo_screenheight() / 2 - altura / 2)
window.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Centralizar os elementos na janela
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Criar os elementos da janela
label_username = Label(window, text="Nome de usuário:")
entry_username = Entry(window)

label_password = Label(window, text="Senha:")
entry_password = Entry(window, show="*")

check_mostrar_senha = BooleanVar()
checkbutton_mostrar_senha = Checkbutton(window, text="Mostrar senha", variable=check_mostrar_senha, command=mostrar_senha)

label_email = Label(window, text="Email:")
entry_email = Entry(window)

button_inserir = Button(window, text="Inserir", command=inserir_dados)

# Posicionar os elementos na janela
label_username.grid(row=0, column=0, sticky="e")
entry_username.grid(row=0, column=1, sticky="w")

label_password.grid(row=1, column=0, sticky="e")
entry_password.grid(row=1, column=1, sticky="w")

checkbutton_mostrar_senha.grid(row=2, columnspan=2, sticky="nsew")

label_email.grid(row=3, column=0, sticky="e")
entry_email.grid(row=3, column=1, sticky="w")

button_inserir.grid(row=4, column=0, columnspan=2, sticky="nsew")

# Iniciar a janela
window.mainloop()
