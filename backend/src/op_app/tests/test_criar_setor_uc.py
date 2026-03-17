import pytest
from unittest.mock import Mock
from src.op_app.application.use_cases.setor.criar_setor_uc import CriarSetorUC, CriarSetorInput
from src.op_app.application.errors import ValidationError, ConflictError, IntegrityError


class TestCriarSetorUC:
    def setup_method(self):
        self.uc = CriarSetorUC()
        self.mock_uow = Mock()
        self.mock_uow.setores = Mock()
        # Mock para unicidade
        self.mock_uow.setores.get_by_nome.return_value = None
        self.mock_uow.setores.get_by_codigo.return_value = None

    def test_execute_sucesso(self):
        # Arrange
        data = CriarSetorInput(nome="TI", codigo_setor="IT01", ativo=True)
        self.mock_uow.setores.add.side_effect = lambda s: setattr(s, 'id', 1) or s

        # Act
        result = self.uc.execute(self.mock_uow, data)

        # Assert
        assert result.id == 1
        assert result.nome == "TI"
        assert result.codigo_setor == "IT01"
        assert result.ativo == True
        self.mock_uow.setores.add.assert_called_once()

    def test_execute_nome_obrigatorio(self):
        # Arrange
        data = CriarSetorInput(nome="", codigo_setor="IT01", ativo=True)

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Campos obrigatórios" in str(exc_info.value)

    def test_execute_codigo_obrigatorio(self):
        # Arrange
        data = CriarSetorInput(nome="TI", codigo_setor="", ativo=True)

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Campos obrigatórios" in str(exc_info.value)

    def test_execute_nome_curto(self):
        # Arrange
        data = CriarSetorInput(nome="A", codigo_setor="IT01", ativo=True)

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "pelo menos 2 caracteres" in str(exc_info.value)

    def test_execute_codigo_curto(self):
        # Arrange
        data = CriarSetorInput(nome="TI", codigo_setor="I", ativo=True)

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "pelo menos 2 caracteres" in str(exc_info.value)

    def test_execute_setor_ja_existe_por_nome(self):
        # Arrange
        data = CriarSetorInput(nome="TI", codigo_setor="IT01", ativo=True)
        self.mock_uow.setores.get_by_nome.return_value = Mock()

        # Act & Assert
        with pytest.raises(ConflictError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "já existe" in str(exc_info.value)

    def test_execute_setor_ja_existe_por_codigo(self):
        # Arrange
        data = CriarSetorInput(nome="TI", codigo_setor="IT01", ativo=True)
        self.mock_uow.setores.get_by_codigo.return_value = Mock()

        # Act & Assert
        with pytest.raises(ConflictError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "já existe" in str(exc_info.value)

    def test_execute_integrity_error(self):
        # Arrange
        data = CriarSetorInput(nome="TI", codigo_setor="IT01", ativo=True)
        self.mock_uow.setores.add.side_effect = IntegrityError("Unique constraint")

        # Act & Assert
        with pytest.raises(ConflictError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Erro ao criar setor" in str(exc_info.value)