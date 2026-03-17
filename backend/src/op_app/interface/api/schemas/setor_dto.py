from dataclasses import dataclass


@dataclass(frozen=True)
class SetorDTO:
    """DTO para retorno de dados de Setor."""
    id: int
    nome: str
    codigo_setor: str
    ativo: bool
