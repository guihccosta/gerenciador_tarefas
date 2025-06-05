import questionary
from banco import criar_tabelas
from classe.usuario import Usuario
from classe.tarefa import Tarefa
from datetime import datetime


def menu_principal(usuario_id):
    while True:
        opcao = questionary.select(
            "O que deseja fazer?",
            choices=[
                "1. Criar tarefa",
                "2. Listar tarefas",
                "3. Marcar tarefa como concluída",
                "0. Sair"
            ]
        ).ask()[0]  # Pega o número da opção como string

        if opcao == "1":
            titulo = questionary.text("Título da tarefa:").ask()
            descricao = questionary.text("Descrição:").ask()
            prazo = questionary.text("Prazo (AAAA-MM-DD):").ask()
            prioridade = questionary.select(
                "Prioridade:",
                choices=["alta", "média", "baixa"]
            ).ask()
            tarefa = Tarefa(titulo, descricao, prazo, prioridade, usuario_id)
            tarefa.salvar()
            print("Tarefa criada com sucesso!")

        elif opcao == "2":
            tarefas = Tarefa.listar(usuario_id)
            hoje = datetime.today().date()

            for id, titulo, status, prazo, prioridade in tarefas:
                vencida = ""
                try:
                    prazo_date = datetime.strptime(prazo, "%Y-%m-%d").date()
                    if status == "pendente" and prazo_date < hoje:
                        vencida = "\u26a0\ufe0f ATRASADA"
                except ValueError:
                    vencida = "(data inválida)"

                print(f"{id} - {titulo} | Status: {status} | Prazo: {prazo} | Prioridade: {prioridade} {vencida}")

        elif opcao == "3":
            tarefa_id = questionary.text("ID da tarefa a concluir:").ask()
            Tarefa.concluir(tarefa_id)
            print("Tarefa marcada como concluída!")

        elif opcao == "0":
            break


def menu_login():
    print("--- BEM-VINDO ---")
    while True:
        opcao = questionary.select(
            "Escolha uma opção:",
            choices=[
                "1. Login",
                "2. Cadastrar novo usuário",
                "0. Sair"
            ]
        ).ask()[0]

        if opcao == "1":
            nome = questionary.text("Nome de usuário:").ask()
            senha = questionary.password("Senha:").ask()
            usuario_id = Usuario.login(nome, senha)
            if usuario_id:
                print("Login bem-sucedido!")
                menu_principal(usuario_id)
            else:
                print("Usuário ou senha inválidos.")

        elif opcao == "2":
            nome = questionary.text("Escolha um nome de usuário:").ask()
            senha = questionary.password("Escolha uma senha:").ask()
            Usuario.cadastrar(nome, senha)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "0":
            print("Encerrando o sistema.")
            break


if __name__ == "__main__":
    criar_tabelas()
    menu_login()
