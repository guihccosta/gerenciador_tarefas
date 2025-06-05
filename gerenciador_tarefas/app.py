from flask import Flask, render_template, request, redirect, url_for
from banco import criar_tabelas, conectar
from classe.usuario import Usuario
from classe.tarefa import Tarefa
from datetime import datetime

app = Flask(__name__)
criar_tabelas()

# Página inicial - Login simples
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        usuario_id = Usuario.login(nome, senha)
        if usuario_id:
            return redirect(url_for('tarefas', usuario_id=usuario_id))
        else:
            return "Usuário ou senha inválidos"
    return render_template('login.html')

# Página das tarefas
@app.route('/tarefas/<int:usuario_id>')
def tarefas(usuario_id):
    tarefas = Tarefa.listar(usuario_id)
    hoje = datetime.today().date()
    return render_template('tarefas.html', tarefas=tarefas, hoje=hoje, usuario_id=usuario_id)

# Rota para criar tarefa
@app.route('/tarefas/<int:usuario_id>/criar', methods=['GET', 'POST'])
def criar_tarefa(usuario_id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        prazo = request.form['prazo']
        prioridade = request.form['prioridade']
        tarefa = Tarefa(titulo, descricao, prazo, prioridade, usuario_id)
        tarefa.salvar()
        return redirect(url_for('tarefas', usuario_id=usuario_id))
    return render_template('criar_tarefa.html', usuario_id=usuario_id)

# Rota para concluir tarefa
@app.route('/tarefas/<int:usuario_id>/concluir/<int:tarefa_id>')
def concluir_tarefa(usuario_id, tarefa_id):
    Tarefa.concluir(tarefa_id)
    return redirect(url_for('tarefas', usuario_id=usuario_id))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        Usuario.cadastrar(nome, senha)
        return redirect(url_for('login'))
    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)
