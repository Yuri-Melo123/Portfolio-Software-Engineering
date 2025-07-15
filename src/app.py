
import tkinter as tk
from tkinter import messagebox
from utils import conectar, criar_tabelas, hash_senha
from kanban_gui import exibir_kanban_tk

usuario_logado = None
perfil_logado = None

# Função para realizar o login do usuário
def login():
    global usuario_logado, perfil_logado
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, hash_senha(senha)))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        usuario_logado = resultado[1]
        perfil_logado = resultado[3]
        messagebox.showinfo("Login", f"Bem-vindo, {usuario_logado}!")
        exibir_kanban_tk()  # Exibe quadro Kanban após login
        root.destroy()
        abrir_menu()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos")

# Função para abrir o menu principal após o login
def abrir_menu():
    import menu
    menu.iniciar(usuario_logado, perfil_logado)

# Função para exibir a tela de login
def tela_login():
    global root, entry_usuario, entry_senha
    root = tk.Tk()
    root.title("Login - Controle de Estoque")

    tk.Label(root, text="Usuário:").grid(row=0, column=0)
    entry_usuario = tk.Entry(root)
    entry_usuario.grid(row=0, column=1)

    tk.Label(root, text="Senha:").grid(row=1, column=0)
    entry_senha = tk.Entry(root, show="*")
    entry_senha.grid(row=1, column=1)

    tk.Button(root, text="Login", command=login).grid(row=2, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    tela_login()
