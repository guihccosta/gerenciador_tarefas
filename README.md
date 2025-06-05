Este projeto é um sistema simples de gerenciamento de tarefas, criado para fins acadêmicos. Ele permite que usuários criem contas, façam login, registrem tarefas com prioridade e prazos, e acompanhem tarefas pendentes ou atrasadas.

Tecnologias utilizadas:
-Python 3

-SQLite3 (banco de dados embutido)

-Programação Orientada a Objetos (POO)

-Desenvolvido no Visual Studio Code



Estrutura do projeto:
gerenciador_tarefas/
├── banco.py                ← Conexão com o banco SQLite
├── tarefas.db              ← Arquivo do banco (criado automaticamente)
├── README.md               ← Explicação do projeto
│
├── classe/
│   ├── usuario.py          ← Classe de usuário
│   └── tarefa.py           ← Classe de tarefa




Funcionalidades:

-Cadastro de usuários

-Login de usuários

-Criação de tarefas com:
    Título;

    Descrição;

    Prazo;

    Prioridade (alta, média, baixa);

-Listagem de tarefas:
    Ordenadas por prioridade e prazo;

    Com alerta para tarefas atrasadas;

-Marcar tarefas como concluídas

-Menus interativos que facilitam a navegação usando teclado

Trabalho realizado como parte da disciplina de Programação Orientada a Objetos 

aluno: Guilherme Campos

