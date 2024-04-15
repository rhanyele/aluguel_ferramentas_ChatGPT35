from db import connect_db

def listar_reservas():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM aluguel_ferramentas.reservas ORDER BY id")
    reservas = cur.fetchall()
    cur.close()
    conn.close()
    return reservas

def adicionar_reserva(ferramenta_id, usuario_id, data_inicio, data_fim, status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO aluguel_ferramentas.reservas (ferramenta_id, usuario_id, data_inicio, data_fim, status) VALUES (%s, %s, %s, %s, %s)", (ferramenta_id, usuario_id, data_inicio, data_fim, status))
    conn.commit()
    cur.close()
    conn.close()

def editar_reserva(id, ferramenta_id, usuario_id, data_inicio, data_fim, status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE aluguel_ferramentas.reservas SET ferramenta_id=%s, usuario_id=%s, data_inicio=%s, data_fim=%s, status=%s WHERE id=%s", (ferramenta_id, usuario_id, data_inicio, data_fim, status, id))
    conn.commit()
    cur.close()
    conn.close()

def excluir_reserva(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM aluguel_ferramentas.reservas WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def buscar_nome_ferramenta_por_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT nome FROM aluguel_ferramentas.ferramentas WHERE id=%s", (id,))
    nome = cur.fetchone()[0]
    cur.close()
    conn.close()
    return nome

def buscar_nome_usuario_por_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT nome FROM aluguel_ferramentas.usuarios WHERE id=%s", (id,))
    nome = cur.fetchone()[0]
    cur.close()
    conn.close()
    return nome

def buscar_reserva_por_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM aluguel_ferramentas.reservas WHERE id=%s", (id,))
    reserva = cur.fetchone()
    cur.close()
    conn.close()
    return reserva
