from banco import conectar

class Usuario:
    @staticmethod
    def cadastrar(nome, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        conn.close()

    @staticmethod
    def login(nome, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
        usuario = cursor.fetchone()
        conn.close()
        return usuario[0] if usuario else None
