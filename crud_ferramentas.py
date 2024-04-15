from db import connect_db

def listar_ferramentas():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM aluguel_ferramentas.ferramentas ORDER BY id")
    ferramentas = cur.fetchall()
    cur.close()
    conn.close()
    return ferramentas

def adicionar_ferramenta(nome, descricao, preco):
    # Formatar o preco para usar ponto como separador decimal
    preco = str(preco).replace(',', '.')

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO aluguel_ferramentas.ferramentas (nome, descricao, preco) VALUES (%s, %s, %s)", (nome, descricao, preco))
    conn.commit()
    cur.close()
    conn.close()

def editar_ferramenta(id, nome, descricao, preco):
    # Formatar o preco para usar ponto como separador decimal
    preco = str(preco).replace(',', '.')
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE aluguel_ferramentas.ferramentas SET nome=%s, descricao=%s, preco=%s WHERE id=%s", (nome, descricao, preco, id))
    conn.commit()
    cur.close()
    conn.close()

def excluir_ferramenta(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM aluguel_ferramentas.ferramentas WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
