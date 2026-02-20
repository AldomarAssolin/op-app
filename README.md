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

---

## 🏗 Arquitetura

O projeto segue uma abordagem inspirada em:

* Clean Architecture
* Domain-Driven Design (DDD)
* Arquitetura em Camadas

### Camadas

| Camada             | Responsabilidade                   |
| ------------------ | ---------------------------------- |
| **Interface**      | API HTTP (Flask + Schemas + Rotas) |
| **Application**    | Casos de uso e orquestração        |
| **Domain**         | Regras de negócio puras            |
| **Infrastructure** | Banco de dados, CSV, repositórios  |
| **Shared**         | Utilitários transversais           |

Separação pensada para:

* Facilitar testes
* Evitar acoplamento com Flask
* Permitir troca de banco ou interface no futuro

---

## 📂 Estrutura do Projeto

```
op-app/
└── backend/
    ├── run.py
    ├── wsgi.py
    ├── src/
    │   ├── interface/
    │   ├── application/
    │   ├── domain/
    │   ├── infrastructure/
    │   └── shared/
    ├── migrations/
    └── tests/
```

### 🔹 domain/

Contém regras puras de negócio:

* Entidades (OP, Item, Etapa, Operador…)
* Value Objects (Status, Prioridade, Prazo)
* Policies (transições de status)
* Exceções de regra

Nenhuma dependência de Flask ou SQLAlchemy.

---

### 🔹 application/

Casos de uso do sistema:

* `importar_csv_uc.py`
* `criar_op_uc.py`
* `iniciar_item_uc.py`
* `finalizar_item_uc.py`
* `registrar_inspecao_uc.py`

Orquestra entidades + repositórios via Unit of Work.

---

### 🔹 infrastructure/

Implementações concretas:

* SQLAlchemy Models
* Repositórios
* Unit of Work
* Leitura de CSV
* Validações
* Mapeadores

Aqui vivem os detalhes técnicos.

---

### 🔹 interface/

Camada HTTP:

* Rotas
* Schemas (Marshmallow / Smorest)
* Handlers de erro
* Health check

---

## 🔄 Fluxo Principal do Sistema

1. PCP envia planilha CSV
2. Sistema importa e valida
3. OPs e Itens são criados/atualizados
4. Líder organiza fila
5. Operador inicia item
6. Operador finaliza item
7. Inspetor aprova ou reprova

---

## 🚀 Como Rodar o Projeto (Dev)

### 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux
# ou
.venv\Scripts\activate      # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar variáveis

Copie:

```
.env.example -> .env
```

Configure:

```
DATABASE_URL=
SECRET_KEY=
```

### 4️⃣ Rodar aplicação

```bash
flask --app run run
```

Ou:

```bash
python run.py
```

---

## 🧪 Testes

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

* Unit: domínio e validações
* Integration: endpoints e casos de uso

---

## 🛠 Tecnologias

* Python 3.12+
* Flask
* Flask-Smorest
* SQLAlchemy
* Alembic / Flask-Migrate
* Pytest

---

## 📌 Decisões Arquiteturais

* Uso de **Unit of Work** para controle transacional
* Domínio isolado de infraestrutura
* Regras de transição de status centralizadas
* DTOs para desacoplamento entre camadas

---

## 📈 Evolução Planejada

* Autenticação de usuários
* Controle por operador
* Dashboard de produção
* Métricas de eficiência
* API para frontend mobile

---

## 👨‍🏭 Contexto Real

Projeto inspirado em ambiente de metalúrgica:

* Montagem
* Soldagem
* Inspeção
* Liberação

>Foco em simplicidade inicial com arquitetura escalável.

