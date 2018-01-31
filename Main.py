from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Combustivel:
    def __init__(self, tipo, preco, rendimento):
        self.tipo = tipo
        self.preco = preco
        self.rendimento = rendimento
#
#
# jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
# jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
CombTeste = Combustivel('Teste',3.59,10)
lista = [CombTeste]


# @app.route('/')
# def index():
@app.route('/', methods=['POST',])
def index():
    tipo = request. form['tipo']
    preco = request. form['preco']
    rendimento = request. form['rendimento']
    combustivel = Combustivel(tipo, preco, rendimento)
    lista.append(combustivel)
    return render_template('main.html', titulo='Homepage')
# return render_template('main.html', titulo='Jogos', jogos=lista)

@app.route('/calcular')
def calcular():
    return render_template('calcular.html', titulo='Resultado')


# @app.route('/criar', methods=['POST',])
# def criar():
#     nome = request. form['nome']
#     categoria = request. form['categoria']
#     console = request. form['console']
#     jogo = Jogo(nome, categoria, console)
#     lista.append(jogo)
#     return redirect('/')


app.run(debug=True)
