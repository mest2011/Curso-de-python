from flask import Flask, render_template, request, redirect, flash, session, url_for


app = Flask(__name__)

app.secret_key = 'Mest'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

user1 = Usuario('luan', 'Luan Marques', "1234")
user2 = Usuario('Nico', 'Nico Steppat', '7a1')
user3 = Usuario('flavio', 'Flávio', '123')

users = {user1.id: user1, user2.id : user2, user3.id : user3}

jogo1 = Jogo("Mario odissey", "Ação/RPG", "Nintendo switch")
jogo2 = Jogo("God of war", "Ação", "PS4")
jogo3 = Jogo("CS GO", "FPS", "PC")

lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo ='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='novo jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome, categoria, console)
    lista.append(novo_jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima_pagina = request.args.get('proxima')
    return render_template('login.html', proxima=proxima_pagina)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in users:
        usuario = users[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash('Bem vindo ao sistema!', 'alert alert-success')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuario ou senha invalida', 'alert alert-danger')
            return redirect(url_for('login'))
    else:
        flash('Usuario ou senha invalida', 'alert alert-danger')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!', 'alert alert-warning')
    return redirect(url_for('index'))

app.run(debug=True)