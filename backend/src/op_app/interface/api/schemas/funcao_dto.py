from dataclasses import dataclass


@dataclass(frozen=True)
class FuncaoDTO:
    """DTO para retorno de dados de Funcao."""
    id: int
    nome_funcao: str
