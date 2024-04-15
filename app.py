from flask import Flask, render_template, request, redirect, url_for, session
from crud_ferramentas import listar_ferramentas, adicionar_ferramenta, editar_ferramenta, excluir_ferramenta
from crud_usuarios import listar_usuarios, adicionar_usuario, editar_usuario, excluir_usuario, autenticar_usuario
from crud_reservas import listar_reservas, adicionar_reserva, editar_reserva, excluir_reserva, buscar_nome_ferramenta_por_id, buscar_nome_usuario_por_id, buscar_reserva_por_id
from crud_pagamentos import listar_pagamentos, adicionar_pagamento, editar_pagamento, excluir_pagamento, buscar_pagamento_por_id
from crud_usuarios import autenticar_usuario
from db import connect_db
from functools import wraps

app = Flask(__name__)
app.secret_key = 'e10adc3949ba59abbe56e057f20f883e'

# Função para verificar se o usuário está autenticado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login_route', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = autenticar_usuario(email, senha)
        
        if usuario:
            session['usuario_id'] = usuario[0]
            session['usuario_nome'] = usuario[1]
            return redirect(url_for('index_route'))
        else:
            return render_template('login.html', error='Email ou senha incorretos.')
    
    return render_template('login.html')

@app.route('/logout')
def logout_route():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('login_route'))

@app.route('/')
@login_required
def index_route():
    return render_template('index.html')

@app.route('/outra_rota')
@login_required
def outra_rota():
    return render_template('outra_rota.html')

# Rotas CRUD de Usuários
@app.route('/usuarios', methods=['GET'])
@login_required
def listar_usuarios_route():
    return render_template('usuario/usuarios.html', usuarios=listar_usuarios())

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
@login_required
def cadastrar_usuario_route():
    if request.method == 'POST':
        data = request.form
        adicionar_usuario(data['nome'], data['email'], data['senha'], data['telefone'], data['endereco'])
        return redirect(url_for('listar_usuarios_route'))
    return render_template('usuario/cadastrar_usuario.html')

@app.route('/usuarios/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_usuario_route(id):
    if request.method == 'POST':
        data = request.form
        editar_usuario(id, data['nome'], data['email'], data['senha'], data['telefone'], data['endereco'])
        return redirect(url_for('listar_usuarios_route'))
    return render_template('usuario/editar_usuario.html', usuario=listar_usuarios()[id - 1])

@app.route('/usuarios/<int:id>/excluir', methods=['POST'])
@login_required
def excluir_usuario_route(id):
    excluir_usuario(id)
    return redirect(url_for('listar_usuarios_route'))

# Rotas CRUD de Ferramentas
@app.route('/ferramentas', methods=['GET'])
@login_required
def listar_ferramentas_route():
    return render_template('ferramenta/ferramentas.html', ferramentas=listar_ferramentas())

@app.route('/cadastrar_ferramenta', methods=['GET', 'POST'])
@login_required
def cadastrar_ferramenta_route():
    if request.method == 'POST':
        data = request.form
        adicionar_ferramenta(data['nome'], data['descricao'], data['preco'])
        return redirect(url_for('listar_ferramentas_route'))
    
    return render_template('ferramenta/cadastrar_ferramenta.html')

@app.route('/ferramentas/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_ferramenta_route(id):
    if request.method == 'POST':
        data = request.form
        editar_ferramenta(id, data['nome'], data['descricao'], data['preco'])
        return redirect(url_for('listar_ferramentas_route'))

    ferramenta = listar_ferramentas()[id - 1]
    
    return render_template('ferramenta/editar_ferramenta.html', ferramenta=ferramenta)

@app.route('/ferramentas/<int:id>/excluir', methods=['POST'])
@login_required
def excluir_ferramenta_route(id):
    excluir_ferramenta(id)
    return redirect(url_for('listar_ferramentas_route'))

# Rotas CRUD de Reservas
@app.route('/reservas', methods=['GET'])
@login_required
def listar_reservas_route():
    reservas = listar_reservas()
    reservas_com_nomes = []
    for reserva in reservas:
        nome_ferramenta = buscar_nome_ferramenta_por_id(reserva[1])
        nome_usuario = buscar_nome_usuario_por_id(reserva[2])
        reservas_com_nomes.append((reserva[0], nome_ferramenta, nome_usuario, reserva[3], reserva[4], reserva[5]))
    
    return render_template('reserva/reservas.html', reservas=reservas_com_nomes)

@app.route('/cadastrar_reserva', methods=['GET', 'POST'])
@login_required
def cadastrar_reserva_route():
    if request.method == 'POST':
        data = request.form
        adicionar_reserva(data['ferramenta_id'], data['usuario_id'], data['data_inicio'], data['data_fim'], data['status'])
        return redirect(url_for('listar_reservas_route'))

    ferramentas = listar_ferramentas()
    usuarios = listar_usuarios()

    return render_template('reserva/cadastrar_reserva.html', ferramentas=ferramentas, usuarios=usuarios)

@app.route('/reservas/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_reserva_route(id):
    reserva = buscar_reserva_por_id(id)
    ferramentas = listar_ferramentas()
    usuarios = listar_usuarios()
    
    if request.method == 'POST':
        data = request.form
        editar_reserva(id, data['ferramenta_id'], data['usuario_id'], data['data_inicio'], data['data_fim'], data['status'])
        return redirect(url_for('listar_reservas_route'))

    nome_ferramenta = buscar_nome_ferramenta_por_id(reserva[1])
    nome_usuario = buscar_nome_usuario_por_id(reserva[2])

    return render_template('reserva/editar_reserva.html', reserva=reserva, nome_ferramenta=nome_ferramenta, nome_usuario=nome_usuario, ferramentas=ferramentas, usuarios=usuarios)

@app.route('/reservas/<int:id>/excluir', methods=['POST'])
@login_required
def excluir_reserva_route(id):
    excluir_reserva(id)
    return redirect(url_for('listar_reservas_route'))

# Rotas CRUD de Pagamentos
@app.route('/pagamentos', methods=['GET'])
@login_required
def listar_pagamentos_route():
    pagamentos = listar_pagamentos()
    return render_template('pagamento/pagamentos.html', pagamentos=pagamentos)

@app.route('/cadastrar_pagamento', methods=['GET', 'POST'])
@login_required
def cadastrar_pagamento_route():
    if request.method == 'POST':
        data = request.form
        adicionar_pagamento(data['reserva_id'], data['valor'], data['forma_pagamento'], data['data_pagamento'], data['status'])
        return redirect(url_for('listar_pagamentos_route'))
    
    # Buscar reservas com status "Confirmada"
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.id, r.ferramenta_id, r.usuario_id, r.data_inicio, r.data_fim, p.valor, p.forma_pagamento, p.data_pagamento, p.status 
        FROM aluguel_ferramentas.reservas AS r
        LEFT JOIN aluguel_ferramentas.pagamentos AS p ON r.id = p.reserva_id
        WHERE r.status = 'Confirmada' AND p.id IS NULL
    """)
    reservas_confirmadas = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('pagamento/cadastrar_pagamento.html', reservas_confirmadas=reservas_confirmadas)

@app.route('/pagamentos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_pagamento_route(id):
    pagamento = buscar_pagamento_por_id(id)
    
    if request.method == 'POST':
        data = request.form
        editar_pagamento(id, data['reserva_id'], data['valor'], data['forma_pagamento'], data['data_pagamento'], data['status'])
        return redirect(url_for('listar_pagamentos_route'))

    return render_template('pagamento/editar_pagamento.html', pagamento=pagamento)

@app.route('/pagamentos/<int:id>/excluir', methods=['POST'])
@login_required
def excluir_pagamento_route(id):
    excluir_pagamento(id)
    return redirect(url_for('listar_pagamentos_route'))

if __name__ == '__main__':
    app.run(debug=True)
