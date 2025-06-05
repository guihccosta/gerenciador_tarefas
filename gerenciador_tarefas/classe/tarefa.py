from banco import conectar
from datetime import datetime

# Classe que representa uma tarefa
class Tarefa:   
    # Método construtor da classe Tarefa
    def __init__(self, titulo, descricao, prazo, prioridade, usuario_id):
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.prioridade = prioridade
        self.status = "pendente"
        self.usuario_id = usuario_id

    # Método que salva a tarefa no banco de dados
    def salvar(self):
        conn = conectar() # Conecta ao banco
        cursor = conn.cursor() # Cria um cursor para executar comandos SQL

        # Insere os dados da tarefa na tabela
        cursor.execute('''
            INSERT INTO tarefas (titulo, descricao, prazo, status, prioridade, usuario_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.titulo, self.descricao, self.prazo, self.status, self.prioridade, self.usuario_id))
        conn.commit() # Salva (confirma) as alterações no banco
        conn.close() # Fecha a conexão com o banco

    # Método estático que lista todas as tarefas de um usuário, ordenadas por prioridade e prazo
    @staticmethod
    def listar(usuario_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, titulo, status, prazo, prioridade
            FROM tarefas
            WHERE usuario_id = ?
            ORDER BY 
                CASE prioridade
                    WHEN 'alta' THEN 1
                    WHEN 'média' THEN 2
                    WHEN 'baixa' THEN 3
                    ELSE 4
                END,
                prazo ASC
        """, (usuario_id,))
        tarefas = cursor.fetchall()
        conn.close()
        return tarefas

    # Método estático para marcar uma tarefa como "concluída"
    @staticmethod
    def concluir(tarefa_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()
