from flask import Flask, render_template, request, session, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pupum'

posts = [
    {
        'titulo': 'Minha primeira postagem',
        'texto': 'teste'
    },
    {
        'titulo': 'Segundo post',
        'texto': 'teste2'    
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template('exibir_entrada.html', entradas = entradas)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/login', methods = ["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logado'] = True
            flash('Bem vindo!')
            return redirect(url_for('exibir_entradas'))
        erro = 'Usuario ou senha Invalidos'
    return render_template('login.html', erro = erro)