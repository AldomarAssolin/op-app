# Op-APP
```bash
src/op_app/
├── application/
│   ├── errors.py
│   └── use_cases/
│       ├── usuario/
│       ├── setor/
│       ├── funcao/
│       ├── etapa/
│       ├── ordem_producao/
│       ├── historico/
│       ├── parada/
│       ├── motivo/
│       └── categoria_parada/
├── domain/
│   ├── entities/
│   │   ├── usuario.py
│   │   ├── setor.py
│   │   ├── funcao.py
│   │   ├── etapa.py
│   │   ├── ordem_producao.py
│   │   ├── historico.py
│   │   ├── parada.py
│   │   ├── motivo.py
│   │   └── categoria_parada.py
│   └── repositories/
│       ├── usuario_repository.py
│       ├── setor_repository.py
│       ├── funcao_repository.py
│       ├── etapa_repository.py
│       ├── ordem_producao_repository.py
│       ├── historico_repository.py
│       ├── parada_repository.py
│       ├── motivo_repository.py
│       └── categoria_parada_repository.py
├── infrastructure/
│   ├── db/
│   │   ├── models/
│   │   │   ├── usuario_model.py
│   │   │   ├── setor_model.py
│   │   │   ├── funcao_model.py
│   │   │   ├── etapa_model.py
│   │   │   ├── ordem_producao_model.py
│   │   │   ├── historico_model.py
│   │   │   ├── parada_model.py
│   │   │   ├── motivo_model.py
│   │   │   └── categoria_parada_model.py
│   ├── repositories/
│   │   ├── usuario_repository.py
│   │   ├── setor_repository.py
│   │   ├── funcao_repository.py
│   │   ├── etapa_repository.py
│   │   ├── ordem_producao_repository.py
│   │   ├── historico_repository.py
│   │   ├── parada_repository.py
│   │   ├── motivo_repository.py
│   │   └── categoria_parada_repository.py
│   └── uow/
│       └── uow_sqlalchemy.py
└── interface/
    └── api/
        ├── routes/
        │   ├── usuario_routes.py
        │   ├── setor_routes.py
        │   ├── funcao_routes.py
        │   ├── etapa_routes.py
        │   ├── ordem_producao_routes.py
        │   ├── historico_routes.py
        │   ├── parada_routes.py
        │   ├── motivo_routes.py
        │   └── categoria_parada_routes.py
        └── schemas/
```

