from banco import conectar
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, prazo, prioridade, usuario_id):
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.prioridade = prioridade
        self.status = "pendente"
        self.usuario_id = usuario_id

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tarefas (titulo, descricao, prazo, status, prioridade, usuario_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.titulo, self.descricao, self.prazo, self.status, self.prioridade, self.usuario_id))
        conn.commit()
        conn.close()

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

    @staticmethod
    def concluir(tarefa_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()
