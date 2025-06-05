from banco import criar_tabelas # Importa a função para criar as tabelas do banco
from classe.usuario import Usuario # Importa a classe Usuario para login e cadastro
from classe.tarefa import Tarefa # Importa a classe Tarefa para manipulação de tarefas
from datetime import datetime # Importa datetime para lidar com datas (como prazo de tarefas)


# Menu principal mostrado após o login do usuário
def menu_principal(usuario_id):
    while True:
        # Mostra o menu de opções
        print("\nO que deseja fazer?")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("0. Sair")
        opcao = input("Escolha uma opção: ") # Captura a escolha do usuário

        if opcao == "1":
            # Coleta as informações da nova tarefa
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            prazo = input("Prazo (AAAA-MM-DD): ")
            prioridade = input("Prioridade (alta, média, baixa): ").lower()
            
            # Cria a tarefa e salva no banco de dados
            tarefa = Tarefa(titulo, descricao, prazo, prioridade, usuario_id)
            tarefa.salvar()
            print("Tarefa criada com sucesso!")

        elif opcao == "2":
            # Lista todas as tarefas do usuário logado
            tarefas = Tarefa.listar(usuario_id)
            hoje = datetime.today().date() # Data de hoje (para verificar tarefas atrasadas)

            for id, titulo, status, prazo, prioridade in tarefas:
                vencida = ""
                try:
                    # Verifica se a tarefa está vencida (prazo ultrapassado)
                    prazo_date = datetime.strptime(prazo, "%Y-%m-%d").date()
                    if status == "pendente" and prazo_date < hoje:
                        vencida = "\u26a0\ufe0f ATRASADA" # Adiciona aviso visual

                except ValueError:
                    vencida = "(data inválida)" # Se o prazo não for uma data válida

                # Exibe a tarefa com detalhes
                print(f"{id} - {titulo} | Status: {status} | Prazo: {prazo} | Prioridade: {prioridade} {vencida}")

        elif opcao == "3":
            # Permite ao usuário concluir uma tarefa informando o ID
            tarefa_id = input("ID da tarefa a concluir: ")
            Tarefa.concluir(tarefa_id)
            print("Tarefa marcada como concluída!")

        elif opcao == "0":
            # Encerra o menu principal (volta para login)
            print("Saindo do menu principal...")
            break

        else:
            # Caso a opção digitada não seja válida
            print("Opção inválida. Tente novamente.")

# Menu inicial que permite login ou cadastro
def menu_login():
    print("--- BEM-VINDO ---")
    while True:
        print("\nEscolha uma opção:")
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("0. Sair")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            # Login do usuário: coleta nome e senha
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            usuario_id = Usuario.login(nome, senha)
            if usuario_id:
                print("Login bem-sucedido!")
                menu_principal(usuario_id) # Acessa o menu principal após login
            else:
                print("Usuário ou senha inválidos.") # Falha no login

        elif opcao == "2":
            # Cadastro de novo usuário
            nome = input("Escolha um nome de usuário: ")
            senha = input("Escolha uma senha: ")
            Usuario.cadastrar(nome, senha)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "0":
            # Encerra o programa
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.") # Entrada inválida

# Ponto de entrada do programa
if __name__ == "__main__":
    criar_tabelas() # Garante que as tabelas existem antes de qualquer operação
    menu_login() # Inicia o sistema com o menu de login/cadastro
