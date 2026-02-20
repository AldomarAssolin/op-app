from src.op_app.infrastructure.db.init_db import init_db
from src.op_app.infrastructure.db.session import get_session
from src.op_app.infrastructure.db.models.test_model import TestTable


def main():
    init_db()
    print("✅ Tabelas criadas com sucesso.")

    session = get_session()
    try:
        obj = TestTable(nome="primeiro registro")
        session.add(obj)
        session.commit()
        print("✅ Insert OK:", obj.id, obj.nome)
    finally:
        session.close()


if __name__ == "__main__":
    main()