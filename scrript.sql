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

-- Inserir Usuários
INSERT INTO aluguel_ferramentas.usuarios (nome, email, senha, telefone, endereco)
VALUES
    ('João Silva', 'joao@email.com', 'senha123', '(11) 9999-9999', 'Rua A, 123'),
    ('Maria Oliveira', 'maria@email.com', 'senha456', '(11) 8888-8888', 'Rua B, 456'),
    ('Carlos Ferreira', 'carlos@email.com', 'senha789', '(11) 7777-7777', 'Rua C, 789'),
	('Ana Rodrigues', 'ana@email.com', 'senha101', '(11) 6666-6666', 'Rua D, 101'),
    ('Paulo Souza', 'paulo@email.com', 'senha202', '(11) 5555-5555', 'Rua E, 202'),
    ('Julia Almeida', 'julia@email.com', 'senha303', '(11) 4444-4444', 'Rua F, 303');

-- Inserir Ferramentas
INSERT INTO aluguel_ferramentas.ferramentas (nome, descricao, preco)
VALUES
    ('Furadeira', 'Furadeira elétrica de 500W', 50.00),
    ('Martelo', 'Martelo de carpinteiro', 20.00),
    ('Serra Circular', 'Serra circular de bancada', 100.00),
	('Chave de Fenda', 'Chave de fenda multiuso', 15.00),
    ('Lixadeira', 'Lixadeira orbital de 200W', 70.00),
    ('Trena', 'Trena a laser digital', 40.00),
    ('Alicate', 'Alicate universal', 25.00),
    ('Serra Tico-Tico', 'Serra tico-tico profissional', 120.00);

-- Inserir Reservas
INSERT INTO aluguel_ferramentas.reservas (ferramenta_id, usuario_id, data_inicio, data_fim, status)
VALUES
    (1, 2, '2024-05-01', '2024-05-05', 'Pendente'),
    (2, 3, '2024-05-10', '2024-05-15', 'Confirmada'),
    (3, 1, '2024-06-01', '2024-06-10', 'Pendente'),
	(4, 3, '2024-07-01', '2024-07-05', 'Pendente'),
    (5, 1, '2024-07-10', '2024-07-15', 'Confirmada'),
    (3, 2, '2024-08-01', '2024-08-10', 'Pendente'),
    (1, 3, '2024-08-15', '2024-08-20', 'Confirmada'),
    (2, 1, '2024-09-01', '2024-09-05', 'Pendente');
	

-- Inserir Pagamentos
INSERT INTO aluguel_ferramentas.pagamentos (reserva_id, valor, forma_pagamento, data_pagamento, status)
VALUES
    (1, 100.00, 'Cartão de Crédito', '2024-05-01', 'Pendente'),
    (2, 40.00, 'Boleto', '2024-05-10', 'Pago'),
    (3, 900.00, 'Pix', '2024-06-01', 'Pendente'),
    (4, 60.00, 'Cartão de Débito', '2024-07-01', 'Pendente'),
    (5, 85.00, 'Cartão de Crédito', '2024-07-10', 'Pago'),
    (6, 45.00, 'Boleto', '2024-08-01', 'Pendente'),
    (7, 30.00, 'Pix', '2024-08-15', 'Pago'),
    (8, 140.00, 'Cartão de Débito', '2024-09-01', 'Pendente');