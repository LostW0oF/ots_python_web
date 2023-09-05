from flask import Flask
from flask import render_template

app = Flask('meu app')

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