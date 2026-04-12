```bash
.
├── alembic.ini
├── check_db.py
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── gunicorn.conf.py
├── init.txt
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 283662ecd34d_create_tables_usuarios_setores_funcoes.py
│       └── ac633c74c5c5_torna_setor_id_e_funcao_id_opcionais.py
├── requirements.txt
├── run_dev.sh
├── run.py
├── src
│   ├── __init__.py
│   └── op_app
│       ├── application
│       │   ├── errors.py
│       │   └── use_cases
│       │       ├── funcoes
│       │       │   ├── atualizar_funcao_uc.py
│       │       │   ├── buscar_funcao_por_id_uc.py
│       │       │   ├── criar_funcao_uc.py
│       │       │   ├── deletar_funcao_uc.py
│       │       │   └── listar_funcoes_uc.py
│       │       ├── setor
│       │       │   ├── atualizar_setor_parcial_uc.py
│       │       │   ├── buscar_setor_por_id_uc.py
│       │       │   ├── criar_setor_uc.py
│       │       │   ├── deletar_setor_uc.py
│       │       │   └── listar_setores_uc.py
│       │       └── usuario
│       │           ├── atualizar_usuario_parcial_uc.py
│       │           ├── buscar_usuario_por_id_uc.py
│       │           ├── criar_usuario_uc.py
│       │           ├── deletar_usuario_uc.py
│       │           └── listar_usuario_uc.py
│       ├── app.py
│       ├── config
│       │   ├── dev_config.py
│       │   └── __init__.py
│       ├── docs
│       │   ├── tree.md
│       │   └── uml
│       │       └── op-app-diagram-2.png
│       ├── domain
│       │   └── dto
│       │       ├── FuncaoDTO.py
│       │       ├── SetorDTO.py
│       │       └── UsuarioDTO.py
│       ├── infrastructure
│       │   ├── db
│       │   │   ├── base.py
│       │   │   ├── init_db.py
│       │   │   ├── models
│       │   │   │   ├── apontamento_model.py
│       │   │   │   ├── codigo_venda_model.py
│       │   │   │   ├── etapa_model.py
│       │   │   │   ├── funcao_model.py
│       │   │   │   ├── __init__.py
│       │   │   │   ├── ordem_producao_model.py
│       │   │   │   ├── parada_model.py
│       │   │   │   ├── setor_model.py
│       │   │   │   ├── test_model.py
│       │   │   │   └── usuario_model.py
│       │   │   ├── session.py
│       │   │   └── sql
│       │   │       └── initial_db.sql
│       │   ├── __init__.py
│       │   ├── repositories
│       │   │   ├── funcao_repository.py
│       │   │   ├── setor_repository.py
│       │   │   └── usuario_repository.py
│       │   └── uow
│       │       └── uow_sqlalchemy.py
│       ├── interface
│       │   └── api
│       │       ├── error_handlers.py
│       │       ├── routes
│       │       │   ├── app_routes.py
│       │       │   ├── funcao_routes.py
│       │       │   ├── health_routes.py
│       │       │   ├── __init__.py
│       │       │   ├── setor_routes.py
│       │       │   └── usuario_routes.py
│       │       └── schemas
│       │           ├── funcao_dto.py
│       │           ├── __init__.py
│       │           ├── setor_dto.py
│       │           └── usuario_dto.py
│       └── tests
│           ├── test_atualizar_funcao_uc.py
│           ├── test_buscar_funcao_por_id_uc.py
│           ├── test_criar_funcao_uc.py
│           ├── test_criar_setor_uc.py
│           ├── test_criar_usuario_uc.py
│           └── test_listar_funcoes_uc.py
└── wsgi.py
```