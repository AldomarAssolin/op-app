# 🏭 OP-APP – Sistema de Gerenciamento de Ordens de Produção

Sistema backend para gerenciamento de **Ordens de Produção (OP)** em ambiente industrial (montagem, soldagem e inspeção).

Projeto arquitetado com foco em:

* Separação clara de responsabilidades
* Regras de negócio isoladas
* Arquitetura em camadas
* Evolução para produção real

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
* Gerenciar operadores e setores

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
| **Infrastructure** | Banco de dados, CSV, repositórios   |
| **Shared**         | Utilitários transversais            |

Separação pensada para:

* Facilitar testes
* Evitar acoplamento com Flask
* Permitir troca de banco no futuro
* Permitir troca da interface (API → CLI → Web)

---

# 📂 Estrutura do Projeto

```
op-app/
└── backend/
    ├── run.py
    ├── run_dev.sh
    ├── wsgi.py
    ├── .env
    ├── .env.example
    ├── requirements.txt
    ├── src/
    │   ├── interface/
    │   ├── application/
    │   ├── domain/
    │   ├── infrastructure/
    │   └── shared/
    ├── migrations/
    └── tests/
```

---

# 🔄 Fluxo Principal do Sistema

1. PCP envia planilha CSV
2. Sistema importa e valida
3. OPs e Itens são criados/atualizados
4. Líder organiza fila
5. Operador inicia item
6. Operador finaliza item
7. Inspetor aprova ou reprova

---

# 🚀 Como Rodar o Projeto (Desenvolvimento)

## 1️⃣ Criar ambiente virtual

Na pasta `backend/`:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / WSL
# ou
.venv\Scripts\activate         # Windows
```

---

## 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configurar variáveis de ambiente

Copie:

```
.env.example → .env
```

Exemplo de `.env`:

```
DATABASE_URL=sqlite:///op_app.db
SECRET_KEY=dev-secret-key
APP_PORT=8010
```

---

## 4️⃣ Aplicar migrations

Se for primeira vez:

```bash
alembic upgrade head
```

Se alterou models:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

⚠️ Em ambiente dev, se o banco ficou inconsistente:

```bash
rm op_app.db
alembic upgrade head
```

---

## 5️⃣ Rodar aplicação (modo desenvolvimento)

Agora usamos o script:

```bash
./run_dev.sh
```

O app será iniciado via Gunicorn com:

* Reload automático
* Logs habilitados
* Porta definida via `.env`

Por padrão:

```
http://127.0.0.1:8010
```

---

# 🏭 Rodando em Produção

Em produção utilize:

```bash
gunicorn wsgi:app --workers 2 --bind 0.0.0.0:8010
```

⚠️ Em produção real:

* Use Postgres
* Configure variáveis via ambiente do servidor
* Desative reload
* Configure logs estruturados

---

# 🧪 Testes

Rodar todos os testes:

```bash
pytest
```

Estrutura:

```
tests/
├── unit/
└── integration/
```

* Unit → domínio e regras puras
* Integration → endpoints e casos de uso

---

# 🛠 Tecnologias

* Python 3.12+
* Flask
* SQLAlchemy 2.0
* Alembic
* Pytest
* Gunicorn

---

# 📌 Decisões Arquiteturais

* Uso de **Unit of Work** para controle transacional
* Domínio isolado de infraestrutura
* Erros padronizados (`ValidationError`, `NotFoundError`, etc.)
* Operador referencia `setor_id` (FK real)
* Banco desacoplado da regra de negócio

---

# 📈 Evolução Planejada

* Autenticação JWT
* Controle por operador
* Dashboard de produção
* Métricas de eficiência
* API para frontend
* Migração para Postgres
* Logs estruturados
* Observabilidade

---

# 👨‍🏭 Contexto Real

Projeto inspirado em ambiente de metalúrgica:

* Montagem
* Soldagem
* Inspeção
* Liberação

Foco em simplicidade inicial com arquitetura escalável.

