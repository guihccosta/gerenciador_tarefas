import sqlite3 # Importa o módulo SQLite, um banco de dados leve embutido no Python

# Função para conectar ao banco de dados (ou criar se não existir)
def conectar():
    return sqlite3.connect("tarefas.db") # Retorna uma conexão com o arquivo 'tarefas.db'


# Função para criar as tabelas do banco, caso ainda não existam
def criar_tabelas():
    conn = conectar() # Estabelece conexão com o banco de dados
    cursor = conn.cursor() # Cria um cursor para executar comandos SQL

    # Cria a tabela de usuários se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    # Cria a tabela de tarefas se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prazo TEXT,
            status TEXT,
            prioridade TEXT,
            usuario_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    ''')

    conn.commit() # Salva as alterações feitas no banco
    conn.close() # Fecha a conexão com o banco
