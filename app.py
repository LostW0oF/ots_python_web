from flask import Flask

app = Flask('meu app')

@app.route('/')
def hello():
    return 'IMPOSSIVEL COM ESSA GALERA'

@app.route('/novo')
def nova():
    return '<h1> PAGINA NOVA </h1>'