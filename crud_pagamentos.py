from db import connect_db

def listar_pagamentos():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            p.id, 
            f.nome AS ferramenta, 
            u.nome AS usuario, 
            r.data_inicio, 
            r.data_fim, 
            p.valor, 
            p.forma_pagamento, 
            p.data_pagamento, 
            p.status
        FROM aluguel_ferramentas.pagamentos p
        JOIN aluguel_ferramentas.reservas r ON p.reserva_id = r.id
        JOIN aluguel_ferramentas.ferramentas f ON r.ferramenta_id = f.id
        JOIN aluguel_ferramentas.usuarios u ON r.usuario_id = u.id
        ORDER BY p.id
    """)
    pagamentos = cur.fetchall()
    cur.close()
    conn.close()
    return pagamentos


def adicionar_pagamento(reserva_id, valor, forma_pagamento, data_pagamento, status):
    # Formatar o valor para usar ponto como separador decimal
    valor = str(valor).replace(',', '.')

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO aluguel_ferramentas.pagamentos (reserva_id, valor, forma_pagamento, data_pagamento, status) VALUES (%s, %s, %s, %s, %s)", (reserva_id, valor, forma_pagamento, data_pagamento, status))
    conn.commit()
    cur.close()
    conn.close()

def editar_pagamento(id, reserva_id, valor, forma_pagamento, data_pagamento, status):
    # Formatar o valor para usar ponto como separador decimal
    valor = str(valor).replace(',', '.')
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE aluguel_ferramentas.pagamentos SET reserva_id=%s, valor=%s, forma_pagamento=%s, data_pagamento=%s, status=%s WHERE id=%s", (reserva_id, valor, forma_pagamento, data_pagamento, status, id))
    conn.commit()
    cur.close()
    conn.close()

def excluir_pagamento(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM aluguel_ferramentas.pagamentos WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def buscar_pagamento_por_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM aluguel_ferramentas.pagamentos WHERE id=%s", (id,))
    pagamento = cur.fetchone()
    cur.close()
    conn.close()
    return pagamento
