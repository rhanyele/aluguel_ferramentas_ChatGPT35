from db import connect_db

def listar_usuarios():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM aluguel_ferramentas.usuarios ORDER BY id")
    usuarios = cur.fetchall()
    cur.close()
    conn.close()
    return usuarios

def adicionar_usuario(nome, email, senha, telefone=None, endereco=None):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO aluguel_ferramentas.usuarios (nome, email, senha, telefone, endereco) VALUES (%s, %s, %s, %s, %s)", (nome, email, senha, telefone, endereco))
    conn.commit()
    cur.close()
    conn.close()

def editar_usuario(id, nome, email, senha, telefone=None, endereco=None):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE aluguel_ferramentas.usuarios SET nome=%s, email=%s, senha=%s, telefone=%s, endereco=%s WHERE id=%s", (nome, email, senha, telefone, endereco, id))
    conn.commit()
    cur.close()
    conn.close()

def excluir_usuario(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM aluguel_ferramentas.usuarios WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def autenticar_usuario(email, senha):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, nome FROM aluguel_ferramentas.usuarios WHERE email=%s AND senha=%s", (email, senha))
    usuario = cur.fetchone()
    cur.close()
    conn.close()
    return usuario if usuario else None