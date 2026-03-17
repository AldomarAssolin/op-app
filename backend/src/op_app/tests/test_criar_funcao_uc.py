import pytest
from unittest.mock import Mock
from src.op_app.application.use_cases.funcoes.criar_funcao_uc import CriarFuncaoUC, CriarFuncaoInput
from src.op_app.application.errors import ValidationError, ConflictError, IntegrityError


class TestCriarFuncaoUC:
    def setup_method(self):
        self.uc = CriarFuncaoUC()
        self.mock_uow = Mock()
        self.mock_uow.funcoes = Mock()
        # Mock para unicidade
        self.mock_uow.funcoes.get_by_nome.return_value = None

    def test_execute_sucesso(self):
        # Arrange
        data = CriarFuncaoInput(nome_funcao="Desenvolvedor")
        self.mock_uow.funcoes.add.side_effect = lambda f: setattr(f, 'id', 1) or f

        # Act
        result = self.uc.execute(self.mock_uow, data)

        # Assert
        assert result.id == 1
        assert result.nome_funcao == "Desenvolvedor"
        self.mock_uow.funcoes.add.assert_called_once()

    def test_execute_nome_obrigatorio(self):
        # Arrange
        data = CriarFuncaoInput(nome_funcao="")

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Campo obrigatório" in str(exc_info.value)

    def test_execute_nome_curto(self):
        # Arrange
        data = CriarFuncaoInput(nome_funcao="A")

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "pelo menos 2 caracteres" in str(exc_info.value)

    def test_execute_funcao_ja_existe(self):
        # Arrange
        data = CriarFuncaoInput(nome_funcao="Desenvolvedor")
        self.mock_uow.funcoes.get_by_nome.return_value = Mock()

        # Act & Assert
        with pytest.raises(ConflictError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "já existe" in str(exc_info.value)

    def test_execute_integrity_error(self):
        # Arrange
        data = CriarFuncaoInput(nome_funcao="Desenvolvedor")
        self.mock_uow.funcoes.add.side_effect = IntegrityError("Unique constraint")

        # Act & Assert
        with pytest.raises(ConflictError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "já existe" in str(exc_info.value)