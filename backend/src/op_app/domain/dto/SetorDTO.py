from dataclasses import dataclass
from typing import Optional


@dataclass
class SetorDTO:
    """Entidade de domínio para Setor."""
    nome: str
    codigo_setor: str
    ativo: bool = True
    id: Optional[int] = None

    def __post_init__(self):
        """Validações básicas da entidade."""
        if not self.nome or len(self.nome.strip()) == 0:
            raise ValueError("Nome é obrigatório")
        if len(self.nome) < 2:
            raise ValueError("Nome do setor deve ter pelo menos 2 caracteres")
        if not self.codigo_setor or len(self.codigo_setor.strip()) == 0:
            raise ValueError("Código do setor é obrigatório")
        if len(self.codigo_setor) < 2:
            raise ValueError("Código do setor deve ter pelo menos 2 caracteres")
