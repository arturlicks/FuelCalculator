from flask import Flask, render_template, request

app = Flask(__name__)


class Combustivel:
    def __init__(self, tipo, preco, rendimento, prendimento, ppreco):
        self.tipo = tipo
        self.preco = preco
        self.rendimento = rendimento
        self.prendimento = prendimento
        self.ppreco = ppreco


CombTeste = Combustivel('Teste', 3.59, 10, 0.70, 0.81)
lista = [CombTeste]


@app.route('/')
def home():
    return render_template('main.html', titulo='Home')


@app.route('/calcular', methods=['POST', ])
def calcular():
    tipo = 'Alcool'
    preco = request.form['apreco']
    rendimento = 7.6
    prendimento = 0.63
    ppreco = 0.93
    combustivel = Combustivel(tipo, preco, rendimento, prendimento, ppreco)
    lista.append(combustivel)
    tipo = 'DtClean'
    preco = request.form['dpreco']
    rendimento = 10.6
    prendimento = 0.71
    ppreco = 0.71
    combustivel = Combustivel(tipo, preco, rendimento, prendimento, ppreco)
    lista.append(combustivel)
    tipo = 'OctaPro'
    preco = request.form['opreco']
    rendimento = 12
    prendimento = 0.88
    ppreco = 1.31
    combustivel = Combustivel(tipo, preco, rendimento, prendimento, ppreco)
    lista.append(combustivel)
    return render_template('calcular.html', titulo='Resultado', combustiveis=lista)


app.run(debug=True)
