from src.op_app.infrastructure.db.init_db import init_db
from src.op_app.infrastructure.db.models.operador_model import OperadorModel
from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy


def main():
    init_db()

    with UnitOfWorkSQLAlchemy() as uow:
        op = OperadorModel(nome="Maria", funcao="Montador", setor="Montagem")
        uow.operadores.add(op)

    with UnitOfWorkSQLAlchemy() as uow:
        encontrado = uow.operadores.get_by_id(1)
        print("✅ get_by_id:", encontrado.id, encontrado.nome)

        todos = uow.operadores.list_all()
        print("✅ total operadores:", len(todos))


if __name__ == "__main__":
    main()