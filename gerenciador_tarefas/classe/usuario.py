from banco import conectar

#Criação da classe usuário
class Usuario:
    # @staticmethod é usado aqui porque o método não precisa acessar ou modificar
    # nenhum atributo da instância (self) ou da classe (cls).
    # Ele funciona de forma independente, usando apenas os argumentos passados
    @staticmethod
    def cadastrar(nome, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        conn.close()

    # Também é um método independente: realiza o login sem depender de atributos da instância.
    @staticmethod
    def login(nome, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
        usuario = cursor.fetchone()
        conn.close()
        return usuario[0] if usuario else None
