# 🏭 OP-APP – Sistema de Gerenciamento de Ordens de Produção

Sistema backend para gerenciamento de **Ordens de Produção (OP)** em ambiente industrial (montagem, soldagem e inspeção).

Projeto arquitetado com foco em:

* Separação clara de responsabilidades
* Regras de negócio isoladas
* Arquitetura em camadas
* Evolução para produção real
* Ambiente totalmente containerizado (Docker)

---

## 🎯 Objetivo

O OP-APP resolve um problema comum no chão de fábrica:

> Controle manual de OPs, status, fila de produção e inspeção.

O sistema permite:

* Importar planilhas (CSV) do PCP
* Criar/atualizar OPs e itens
* Definir roteiros de produção
* Controlar status por item
* Registrar inspeções
* Organizar fila por prioridade
* Gerenciar operadores, funções e setores

---

# 🏗 Arquitetura

O projeto segue abordagem inspirada em:

* Clean Architecture
* Domain-Driven Design (DDD)
* Arquitetura em Camadas

## Camadas

| Camada             | Responsabilidade                    |
| ------------------ | ----------------------------------- |
| **Interface**      | API HTTP (Flask + Rotas + Handlers) |
| **Application**    | Casos de uso e orquestração         |
| **Domain**         | Regras de negócio puras             |
| **Infrastructure** | Banco de dados, repositórios        |
| **Shared**         | Utilitários transversais            |

---

# 📂 Estrutura do Projeto

```bash

op-app/
└── backend/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── run.py
├── run_dev.sh
├── wsgi.py
├── requirements.txt
├── src/
├── migrations/
└── tests/

```

---

# 🐳 Ambiente com Docker (Recomendado)

## 🚀 Subir aplicação completa

```bash
docker compose up --build
````

Isso irá subir:

* API (Flask + Gunicorn)
* Banco PostgreSQL

---

## 🌐 Acesso

API:

```
http://localhost:8010
```

Health check:

```
GET /health
```

---

## 🧠 Banco de Dados

* PostgreSQL rodando via container
* Comunicação interna via hostname:

```
db:5432
```

---

## 🔄 Migrations (Alembic)

Executar migrations:

```bash
docker exec -it op-app-backend alembic upgrade head
```

Criar nova migration:

```bash
docker exec -it op-app-backend alembic revision --autogenerate -m "descricao"
```

---

## ⚠️ Resetar banco (apenas desenvolvimento)

```bash
docker compose down -v
docker compose up --build
```

---

# 💻 Rodar sem Docker (modo legado/dev)

## 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configurar `.env`

Exemplo:

```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/op_app
APP_PORT=8010
```

---

## 4️⃣ Rodar aplicação

```bash
./run_dev.sh
```

---

# 🧪 Testes

```bash
pytest
```

---

# 🛠 Tecnologias

* Python 3.11+
* Flask
* SQLAlchemy 2.0
* Alembic
* PostgreSQL
* Docker / Docker Compose
* Pytest
* Gunicorn

---

# 📌 Decisões Arquiteturais

* Uso de **Unit of Work** para controle transacional
* Separação clara entre domínio e infraestrutura
* Uso de migrations com Alembic
* Banco PostgreSQL como padrão
* Campos `setor_id` e `funcao_id` agora opcionais no usuário
* Erros padronizados (`ValidationError`, `NotFoundError`)

---

# 📈 Evolução Planejada

* Autenticação JWT
* Controle por operador
* Dashboard de produção
* Métricas de eficiência
* API para frontend
* Observabilidade (logs + métricas)

---

# 👨‍🏭 Contexto Real

Projeto inspirado em ambiente de metalúrgica:

* Montagem
* Soldagem
* Inspeção
* Liberação

>Foco em simplicidade inicial com arquitetura escalável.

