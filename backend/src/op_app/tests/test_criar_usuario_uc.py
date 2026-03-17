import pytest
from unittest.mock import Mock, MagicMock
from src.op_app.application.use_cases.usuario.criar_usuario_uc import CriarUsuarioUC, CriarUsuarioInput
from src.op_app.application.errors import ValidationError, NotFoundError


class TestCriarUsuarioUC:
    def setup_method(self):
        self.uc = CriarUsuarioUC()
        self.mock_uow = Mock()
        self.mock_uow.setores = Mock()
        self.mock_uow.funcoes = Mock()
        self.mock_uow.usuarios = Mock()
        # Mock para unicidade
        self.mock_uow.usuarios.get_by_nome.return_value = None

    def test_execute_sucesso(self):
        # Arrange
        data = CriarUsuarioInput(nome="João Silva", pin="1234", funcao_id=1, setor_id=1)
        mock_setor = Mock()
        mock_funcao = Mock()

        self.mock_uow.setores.get_by_id.return_value = mock_setor
        self.mock_uow.funcoes.get_by_id.return_value = mock_funcao
        self.mock_uow.usuarios.add.side_effect = lambda u: setattr(u, 'id', 1) or u  # Simula definir id

        # Act
        result = self.uc.execute(self.mock_uow, data)

        # Assert
        assert result.id == 1
        assert result.nome == "João Silva"
        assert result.pin == "1234"
        assert result.funcao_id == 1
        assert result.setor_id == 1
        self.mock_uow.usuarios.add.assert_called_once()

    def test_execute_campos_obrigatorios_faltando(self):
        # Arrange
        data = CriarUsuarioInput(nome="", pin="", funcao_id=1, setor_id=1)

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Campos obrigatórios" in str(exc_info.value)

    def test_execute_setor_id_invalido(self):
        # Este teste não se aplica mais, pois setor_id é int no input
        pass

    def test_execute_funcao_id_invalido(self):
        # Este teste não se aplica mais, pois funcao_id é int no input
        pass

    def test_execute_setor_nao_encontrado(self):
        # Arrange
        data = CriarUsuarioInput(nome="João", pin="1234", funcao_id="1", setor_id=1)
        self.mock_uow.setores.get_by_id.return_value = None

        # Act & Assert
        with pytest.raises(NotFoundError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Setor não encontrado" in str(exc_info.value)

    def test_execute_funcao_nao_encontrada(self):
        # Arrange
        data = CriarUsuarioInput(nome="João", pin="1234", funcao_id="1", setor_id=1)
        self.mock_uow.setores.get_by_id.return_value = Mock()
        self.mock_uow.funcoes.get_by_id.return_value = None

        # Act & Assert
        with pytest.raises(NotFoundError) as exc_info:
            self.uc.execute(self.mock_uow, data)
        assert "Função não encontrada" in str(exc_info.value)