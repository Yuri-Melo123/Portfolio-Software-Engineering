
import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

KANBAN_STATUSES = ['A Fazer', 'Em Progresso', 'Concluído']
DB_PATH = 'banco_de_dados.db'

# Função para conectar ao banco de dados e criar tabelas se necessário
def conectar_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kanban (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

# Função para carregar as tarefas do banco de dados
def carregar_tarefas():
    conn, cursor = conectar_db()
    tarefas = {status: [] for status in KANBAN_STATUSES}
    for status in KANBAN_STATUSES:
        cursor.execute("SELECT id, titulo FROM kanban WHERE status = ?", (status,))
        tarefas[status] = cursor.fetchall()
    conn.close()
    return tarefas

# Função para adicionar uma nova tarefa
def adicionar_tarefa_gui(atualizar_callback):
    titulo = simpledialog.askstring("Nova Tarefa", "Digite o título da tarefa:")
    if titulo:
        conn, cursor = conectar_db()
        cursor.execute("INSERT INTO kanban (titulo, status) VALUES (?, ?)", (titulo, 'A Fazer'))
        conn.commit()
        conn.close()
        atualizar_callback()

# Função para mover uma tarefa entre os status
def mover_tarefa_gui(atualizar_callback):
    conn, cursor = conectar_db()
    cursor.execute("SELECT id, titulo, status FROM kanban")
    tarefas = cursor.fetchall()
    conn.close()

    if not tarefas:
        messagebox.showinfo("Mover Tarefa", "Nenhuma tarefa para mover.")
        return

    selecao = tk.Toplevel()
    selecao.title("Mover Tarefa")

    tk.Label(selecao, text="Escolha uma tarefa para mover:").pack()

    for id_, titulo, status in tarefas:
        # Função para mover a tarefa para um novo status
        def mover(id_=id_, status_atual=status):
            nova = [s for s in KANBAN_STATUSES if s != status_atual]
            escolha = simpledialog.askstring("Mover Para", f"Escolha novo status ({', '.join(nova)}):")
            if escolha in nova:
                conn, cursor = conectar_db()
                cursor.execute("UPDATE kanban SET status = ? WHERE id = ?", (escolha, id_))
                conn.commit()
                conn.close()
                selecao.destroy()
                atualizar_callback()
            else:
                messagebox.showerror("Erro", "Status inválido.")
        tk.Button(selecao, text=f"[{status}] {titulo}", command=mover).pack()

# Função para exibir o quadro Kanban usando Tkinter
def exibir_kanban_tk():
    root = tk.Toplevel()
    root.title("Quadro Kanban")

    frames = {}
    tarefas_por_status = carregar_tarefas()

    for i, status in enumerate(KANBAN_STATUSES):
        frame = tk.Frame(root, bd=2, relief='groove', padx=10, pady=10)
        frame.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
        tk.Label(frame, text=status, font=('Arial', 12, 'bold')).pack()
        frames[status] = frame

    # Preencher os frames com as tarefas
    def atualizar():
        for status, frame in frames.items():
            for widget in frame.winfo_children()[1:]:
                widget.destroy()
        tarefas = carregar_tarefas()
        for status in KANBAN_STATUSES:
            for _, titulo in tarefas[status]:
                tk.Label(frames[status], text=titulo, bg='white', relief='solid', bd=1).pack(pady=2, fill='x')

    btn_frame = tk.Frame(root)
    btn_frame.grid(row=1, columnspan=3, pady=10)

    tk.Button(btn_frame, text="Adicionar Tarefa", command=lambda: adicionar_tarefa_gui(atualizar)).pack(side='left', padx=10)
    tk.Button(btn_frame, text="Mover Tarefa", command=lambda: mover_tarefa_gui(atualizar)).pack(side='left', padx=10)

    atualizar()
    root.mainloop()
