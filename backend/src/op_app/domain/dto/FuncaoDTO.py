from dataclasses import dataclass
from typing import Optional


@dataclass
class FuncaoDTO:
    """Entidade de domínio para Funcao."""
    nome_funcao: str
    id: Optional[int] = None

    def __post_init__(self):
        """Validações básicas da entidade."""
        if not self.nome_funcao or len(self.nome_funcao.strip()) == 0:
            raise ValueError("Nome da função é obrigatório")
        if len(self.nome_funcao) < 2:
            raise ValueError("Nome da função deve ter pelo menos 2 caracteres")
