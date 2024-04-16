-- Criar o schema aluguel_ferramentas
CREATE SCHEMA IF NOT EXISTS aluguel_ferramentas;

-- Tabela de Usuários
CREATE TABLE aluguel_ferramentas.usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(200)
);

-- Tabela de Ferramentas
CREATE TABLE aluguel_ferramentas.ferramentas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL
);

-- Tabela de Reservas
CREATE TABLE aluguel_ferramentas.reservas (
    id SERIAL PRIMARY KEY,
    ferramenta_id INT REFERENCES aluguel_ferramentas.ferramentas(id),
    usuario_id INT REFERENCES aluguel_ferramentas.usuarios(id),
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    status VARCHAR(50) NOT NULL, -- Status pode ser "Pendente", "Confirmada", "Cancelada", etc.
	FOREIGN KEY (ferramenta_id) REFERENCES aluguel_ferramentas.ferramentas(id),
    FOREIGN KEY (usuario_id) REFERENCES aluguel_ferramentas.usuarios(id)
);

-- Tabela de Pagamentos
CREATE TABLE aluguel_ferramentas.pagamentos (
    id SERIAL PRIMARY KEY,
    reserva_id INT REFERENCES aluguel_ferramentas.reservas(id),
    valor DECIMAL(10, 2) NOT NULL,
	forma_pagamento VARCHAR(50) NOT NULL, -- Status pode ser "Cartão de Credito", "Cartão de Debito", "Boleto", "Pix", etc.
    data_pagamento DATE NOT NULL,
    status VARCHAR(50) NOT NULL, -- Status pode ser "Pago", "Pendente", "Cancelado", etc.
	FOREIGN KEY (reserva_id) REFERENCES aluguel_ferramentas.reservas(id)
);

