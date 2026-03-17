from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UsuarioDTO:
    """DTO para retorno de dados de Usuario."""
    id: int
    nome: str
    pin: str
    funcao_id: int
    setor_id: int