-- Criar extensões se necessário
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Tabelas de Cadastro Base
CREATE TABLE setores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE funcoes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    funcao_id INT REFERENCES funcoes(id),
    setor_id INT REFERENCES setores(id),
    nome VARCHAR(100) NOT NULL,
    pin_hash VARCHAR(255) NOT NULL, -- Armazenar sempre com Bcrypt/Argon2
    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Estrutura de Fluxo
CREATE TABLE etapas (
    id SERIAL PRIMARY KEY,
    nome_etapa VARCHAR(50) NOT NULL,
    ordem_fluxo INT NOT NULL UNIQUE -- 1: Montagem, 2: Soldagem, 3: Inspeção
);

CREATE TABLE codigos_venda (
    id SERIAL PRIMARY KEY,
    codigo_venda VARCHAR(50) NOT NULL UNIQUE,
    cliente VARCHAR(100),
    data_pedido DATE DEFAULT CURRENT_DATE
);

-- 3. Core Operacional
CREATE TYPE status_op_enum AS ENUM ('AGUARDANDO', 'EM_PRODUCAO', 'PARADO', 'CONCLUIDO');

CREATE TABLE ordens_producao (
    id SERIAL PRIMARY KEY,
    cv_id INT NOT NULL REFERENCES codigos_venda(id),
    etapa_atual_id INT NOT NULL REFERENCES etapas(id),
    numero_op BIGINT NOT NULL UNIQUE,
    sequencia_op INT NOT NULL,
    status_op status_op_enum DEFAULT 'AGUARDANDO',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(cv_id, sequencia_op) -- Garante que não existam duplicatas no mesmo lote
);

-- 4. Movimentação e Apontamentos
CREATE TABLE apontamentos_producao (
    id BIGSERIAL PRIMARY KEY,
    op_id INT NOT NULL REFERENCES ordens_producao(id),
    usuario_id INT NOT NULL REFERENCES usuarios(id),
    etapa_id INT NOT NULL REFERENCES etapas(id),
    data_inicio TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_fim TIMESTAMP,
    CONSTRAINT chk_datas_apontamento CHECK (data_fim > data_inicio)
);

CREATE TABLE categorias_parada (
    id SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL
);

CREATE TABLE motivos_parada (
    id SERIAL PRIMARY KEY,
    categoria_id INT NOT NULL REFERENCES categorias_parada(id),
    descricao VARCHAR(100) NOT NULL
);

CREATE TABLE registros_parada (
    id BIGSERIAL PRIMARY KEY,
    op_id INT NOT NULL REFERENCES ordens_producao(id),
    usuario_id INT NOT NULL REFERENCES usuarios(id),
    motivo_id INT NOT NULL REFERENCES motivos_parada(id),
    data_inicio TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_fim TIMESTAMP,
    CONSTRAINT chk_datas_parada CHECK (data_fim > data_inicio)
);

-- 5. Índices para Performance
CREATE INDEX idx_op_status ON ordens_producao(status_op);
CREATE INDEX idx_apontamento_op ON apontamentos_producao(op_id, data_inicio);
CREATE INDEX idx_parada_op ON registros_parada(op_id);