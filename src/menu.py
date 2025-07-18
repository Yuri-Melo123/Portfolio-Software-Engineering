import tkinter as tk
from tkinter import messagebox, simpledialog
from kanban_gui import exibir_kanban_tk
from utils import conectar, hash_senha

# Função para iniciar o menu principal
def iniciar(usuario_logado, perfil_logado):
    # Função para cadastrar um novo produto
    def cadastrar_produto():
        nome = simpledialog.askstring("Produto", "Nome do produto:")
        if not nome:
            return
        try:
            preco = float(simpledialog.askstring("Produto", "Preço:"))
            quantidade = int(simpledialog.askstring("Produto", "Quantidade:"))
            minimo = int(simpledialog.askstring("Produto", "Quantidade mínima:"))
        except (TypeError, ValueError):
            messagebox.showerror("Erro", "Informe valores numéricos válidos.")
            return

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade, minimo) VALUES (?, ?, ?, ?)",
                       (nome, preco, quantidade, minimo))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", f"{nome} cadastrado com sucesso!")

    # Função para atualizar o estoque de um produto
    def atualizar_estoque():
        nome = simpledialog.askstring("Atualizar", "Nome do produto:")
        try:
            preco = float(simpledialog.askstring("Atualizar", "Novo preço:"))
            quantidade = int(simpledialog.askstring("Atualizar", "Nova quantidade:"))
        except (TypeError, ValueError):
            messagebox.showerror("Erro", "Informe valores numéricos válidos.")
            return

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET preco=?, quantidade=? WHERE nome=?", (preco, quantidade, nome))
        if cursor.rowcount == 0:
            messagebox.showerror("Erro", f"{nome} não encontrado.")
        else:
            messagebox.showinfo("Sucesso", f"{nome} atualizado com sucesso!")
        conn.commit()
        conn.close()

    # Função para visualizar o estoque atual
    def visualizar_estoque():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, preco, quantidade, minimo FROM produtos")
        produtos = cursor.fetchall()
        conn.close()

        top = tk.Toplevel(janela)
        top.title("Estoque Atual")
        for i, (nome, preco, qtd, minimo) in enumerate(produtos):
            destaque = " ⚠️" if qtd < minimo else ""
            tk.Label(top, text=f"{nome} - R$ {preco:.2f} - Qtd: {qtd} (mín: {minimo}){destaque}").pack(anchor='w')

    # Função para cadastrar um novo usuário
    def cadastrar_usuario():
        if perfil_logado != 'admin':
            messagebox.showerror("Acesso negado", "Apenas administradores podem cadastrar usuários.")
            return

        novo_usuario = simpledialog.askstring("Usuário", "Nome do novo usuário:")
        senha = simpledialog.askstring("Senha", "Senha:", show="*")
        perfil = simpledialog.askstring("Perfil", "Tipo de usuário (admin/comum):")

        if perfil not in ['admin', 'comum']:
            messagebox.showerror("Erro", "Perfil inválido.")
            return

        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (usuario, senha, perfil) VALUES (?, ?, ?)",
                           (novo_usuario, hash_senha(senha), perfil))
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
        except:
            messagebox.showerror("Erro", "Usuário já existe.")
        finally:
            conn.close()

    # Função para sair do menu
    def sair():
        janela.destroy()

    janela = tk.Tk()
    janela.title("Menu Principal - Estoque")

    tk.Label(janela, text=f"Usuário: {usuario_logado} ({perfil_logado})", font=('Arial', 12)).pack(pady=10)

    tk.Button(janela, text="Cadastrar Produto", width=30, command=cadastrar_produto).pack(pady=5)
    tk.Button(janela, text="Atualizar Estoque", width=30, command=atualizar_estoque).pack(pady=5)
    tk.Button(janela, text="Visualizar Estoque", width=30, command=visualizar_estoque).pack(pady=5)

    if perfil_logado == 'admin':
        tk.Button(janela, text="Cadastrar Novo Usuário", width=30, command=cadastrar_usuario).pack(pady=5)

    tk.Button(janela, text="Abrir Quadro Kanban", width=30, command=sair).pack(pady=20)

    janela.mainloop()
