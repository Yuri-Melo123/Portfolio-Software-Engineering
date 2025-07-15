
import os
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

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    status = 'A Fazer'
    conn, cursor = conectar_db()
    cursor.execute("INSERT INTO kanban (titulo, status) VALUES (?, ?)", (titulo, status))
    conn.commit()
    conn.close()
    print("Tarefa adicionada com sucesso!")

# Função para visualizar as tarefas
def visualizar_tarefas():
    conn, cursor = conectar_db()
    for status in KANBAN_STATUSES:
        print(f"\n=== {status} ===")
        cursor.execute("SELECT id, titulo FROM kanban WHERE status = ?", (status,))
        tarefas = cursor.fetchall()
        for tarefa in tarefas:
            print(f"[{tarefa[0]}] {tarefa[1]}")
    conn.close()

# Função para mover uma tarefa entre os status
def mover_tarefa():
    visualizar_tarefas()
    tarefa_id = input("\nDigite o ID da tarefa a ser movida: ")
    print("Para qual status deseja mover?")
    for i, status in enumerate(KANBAN_STATUSES):
        print(f"{i + 1}. {status}")
    escolha = int(input("Escolha uma opção: "))
    if 1 <= escolha <= len(KANBAN_STATUSES):
        novo_status = KANBAN_STATUSES[escolha - 1]
        conn, cursor = conectar_db()
        cursor.execute("UPDATE kanban SET status = ? WHERE id = ?", (novo_status, tarefa_id))
        conn.commit()
        conn.close()
        print("Tarefa movida com sucesso!")
    else:
        print("Opção inválida.")

# Função para exibir o menu do Kanban
def menu_kanban():
    while True:
        print("\n=== Quadro Kanban ===")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Mover tarefa")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            visualizar_tarefas()
        elif opcao == '3':
            mover_tarefa()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
