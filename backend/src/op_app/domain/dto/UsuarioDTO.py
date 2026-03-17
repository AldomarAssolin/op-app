from dataclasses import dataclass
from typing import Optional


@dataclass
class UsuarioDTO:
    """Entidade de domínio para Usuario."""
    id: Optional[int]
    nome: str
    pin: str
    funcao_id: int
    setor_id: int

    def __post_init__(self):
        """Validações básicas da entidade."""
        if not self.nome or len(self.nome.strip()) == 0:
            raise ValueError("Nome é obrigatório")
        if not self.pin or len(self.pin) < 4:
            raise ValueError("PIN deve ter pelo menos 4 caracteres")
        if self.funcao_id <= 0:
            raise ValueError("funcao_id deve ser um inteiro positivo")
        if self.setor_id <= 0:
            raise ValueError("setor_id deve ser um inteiro positivo")