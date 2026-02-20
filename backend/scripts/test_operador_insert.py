from src.op_app.infrastructure.db.init_db import init_db
from src.op_app.infrastructure.db.session import get_session
from src.op_app.infrastructure.db.models.operador_model import OperadorModel


def main():
    init_db()
    print("✅ Tabelas OK")

    session = get_session()
    try:
        operador = OperadorModel(
            nome="João da Silva",
            funcao="Soldador",
            setor="Soldagem",
        )
        session.add(operador)
        session.commit()
        session.refresh(operador)

        print(f"✅ Insert OK: id={operador.id} nome={operador.nome} funcao={operador.funcao} setor={operador.setor}")
    finally:
        session.close()


if __name__ == "__main__":
    main()