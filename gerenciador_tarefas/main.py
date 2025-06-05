from banco import criar_tabelas
from classe.usuario import Usuario
from classe.tarefa import Tarefa
from datetime import datetime


def menu_principal(usuario_id):
    while True:
        print("\nO que deseja fazer?")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            prazo = input("Prazo (AAAA-MM-DD): ")
            prioridade = input("Prioridade (alta, média, baixa): ").lower()
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
            tarefa_id = input("ID da tarefa a concluir: ")
            Tarefa.concluir(tarefa_id)
            print("Tarefa marcada como concluída!")

        elif opcao == "0":
            print("Saindo do menu principal...")
            break

        else:
            print("Opção inválida. Tente novamente.")


def menu_login():
    print("--- BEM-VINDO ---")
    while True:
        print("\nEscolha uma opção:")
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("0. Sair")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            usuario_id = Usuario.login(nome, senha)
            if usuario_id:
                print("Login bem-sucedido!")
                menu_principal(usuario_id)
            else:
                print("Usuário ou senha inválidos.")

        elif opcao == "2":
            nome = input("Escolha um nome de usuário: ")
            senha = input("Escolha uma senha: ")
            Usuario.cadastrar(nome, senha)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    criar_tabelas()
    menu_login()
