# Op-APP
```bash
op-app/
└── backend/
    ├── pyproject.toml                  # ou requirements.txt
    ├── .env
    ├── .env.example
    ├── README.md
    ├── wsgi.py                         # entrypoint p/ produção (gunicorn)
    ├── run.py                          # entrypoint p/ dev (flask --app run)
    │
    ├── src/
    │   ├── app.py                      # create_app(), init extensions, register blueprints
    │   ├── config.py                   # Config classes (Dev/Prod/Test)
    │   ├── extensions.py               # db, migrate, smorest, etc (instâncias)
    │   │
    │   ├── interface/                  # camada de entrada (API)
    │   │   ├── __init__.py
    │   │   ├── api/
    │   │   │   ├── __init__.py         # init_api(app) -> registra docs/schemas
    │   │   │   ├── schemas/
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── op_schema.py
    │   │   │   │   ├── item_schema.py
    │   │   │   │   ├── etapa_schema.py
    │   │   │   │   ├── apontamento_schema.py
    │   │   │   │   └── importacao_schema.py
    │   │   │   └── routes/
    │   │   │       ├── __init__.py
    │   │   │       ├── health_routes.py
    │   │   │       ├── op_routes.py
    │   │   │       ├── itens_routes.py
    │   │   │       ├── etapas_routes.py
    │   │   │       ├── apontamentos_routes.py
    │   │   │       └── importacoes_routes.py
    │   │   └── errors.py               # handlers HTTP (404/400/500) + mapeamento de exceções
    │   │
    │   ├── application/                # casos de uso (orquestração)
    │   │   ├── __init__.py
    │   │   ├── dto/
    │   │   │   ├── __init__.py
    │   │   │   ├── op_dto.py
    │   │   │   ├── item_dto.py
    │   │   │   └── importacao_dto.py
    │   │   ├── services/
    │   │   │   ├── __init__.py
    │   │   │   ├── op_service.py       # regras de fluxo (ex.: criar OP + itens)
    │   │   │   └── fila_service.py     # ordenar/priorizar, regras de fila
    │   │   └── use_cases/
    │   │       ├── __init__.py
    │   │       ├── importar_csv_uc.py
    │   │       ├── criar_op_uc.py
    │   │       ├── listar_ops_uc.py
    │   │       ├── obter_op_uc.py
    │   │       ├── definir_roteiro_uc.py
    │   │       ├── iniciar_item_uc.py
    │   │       ├── finalizar_item_uc.py
    │   │       ├── registrar_inspecao_uc.py
    │   │       └── listar_sequencias_por_cv_uc.py
    │   │
    │   ├── domain/                     # regras do negócio (puro, sem Flask/DB)
    │   │   ├── __init__.py
    │   │   ├── entities/
    │   │   │   ├── __init__.py
    │   │   │   ├── op.py               # OrdemProdução
    │   │   │   ├── item_op.py
    │   │   │   ├── etapa.py
    │   │   │   ├── apontamento.py
    │   │   │   ├── inspecao.py
    │   │   │   └── operador.py
    │   │   ├── value_objects/
    │   │   │   ├── __init__.py
    │   │   │   ├── status_etapa.py     # enums/estados
    │   │   │   ├── prioridade.py
    │   │   │   └── prazo.py
    │   │   ├── policies/
    │   │   │   ├── __init__.py
    │   │   │   └── transicao_status.py # regras de transição (fila->montagem->solda->insp->liberado)
    │   │   └── errors.py               # exceções do domínio (RegraViolada, etc.)
    │   │
    │   ├── infrastructure/             # detalhes do mundo real (DB, arquivos, integrações)
    │   │   ├── __init__.py
    │   │   ├── db/
    │   │   │   ├── __init__.py
    │   │   │   ├── base.py             # Base declarativa SQLAlchemy
    │   │   │   ├── session.py          # engine, SessionLocal, init_db(), remove_session()
    │   │   │   └── models/
    │   │   │       ├── __init__.py
    │   │   │       ├── op_model.py
    │   │   │       ├── item_model.py
    │   │   │       ├── etapa_model.py
    │   │   │       ├── apontamento_model.py
    │   │   │       ├── inspecao_model.py
    │   │   │       └── operador_model.py
    │   │   │
    │   │   ├── repositories/
    │   │   │   ├── __init__.py
    │   │   │   ├── op_repository.py
    │   │   │   ├── item_repository.py
    │   │   │   ├── etapa_repository.py
    │   │   │   ├── apontamento_repository.py
    │   │   │   └── operador_repository.py
    │   │   │
    │   │   ├── uow/
    │   │   │   ├── __init__.py
    │   │   │   └── uow_sqlalchemy.py   # UnitOfWorkSQLAlchemy (commit/rollback + repos)
    │   │   │
    │   │   ├── importers/
    │   │   │   ├── __init__.py
    │   │   │   ├── csv_reader.py       # leitura/normalização
    │   │   │   ├── validators.py       # validações do arquivo/colunas
    │   │   │   └── mappers.py          # transforma linhas -> DTO/entidades
    │   │   │
    │   │   └── logging.py              # logger config (opcional)
    │   │
    │   └── shared/                      # utilitários transversais
    │       ├── __init__.py
    │       ├── clock.py                 # tempo (facilita teste)
    │       └── result.py                # Resultado.ok/falha (se você usa esse padrão)
    │
    ├── migrations/                      # Alembic/Flask-Migrate
    └── tests/
        ├── unit/
        │   ├── test_domain_transicoes.py
        │   └── test_importacao_validators.py
        ├── integration/
        │   ├── test_importar_csv_uc.py
        │   └── test_op_endpoints.py
        └── conftest.py
```

