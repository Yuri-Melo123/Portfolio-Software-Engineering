import sqlite3
import hashlib

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("banco_de_dados.db")

# Função para criar as tabelas necessárias no banco de dados
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        perfil TEXT NOT NULL CHECK(perfil IN ('admin', 'comum'))
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL,
        minimo INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# Função para hashear a senha do usuário
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
