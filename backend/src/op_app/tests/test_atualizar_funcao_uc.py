import pytest
from unittest.mock import Mock
from src.op_app.application.use_cases.funcoes.atualizar_funcao_uc import AtualizarFuncaoUC
from src.op_app.application.errors import ValidationError, NotFoundError, ConflictError

class TestAtualizarFuncaoUC:
    def setup_method(self):
        self.uc = AtualizarFuncaoUC()
        self.mock_uow = Mock()
        self.mock_uow.funcoes = Mock()
        
        # Setup padrão de mocks
        self.mock_funcao = Mock(id=1, nome_funcao="Desenvolvedor Velho")
        self.mock_uow.funcoes.get_by_id.return_value = self.mock_funcao
        self.mock_uow.funcoes.get_by_nome.return_value = None

    def test_execute_sucesso(self):
        # Arrange
        payload = {"nome_funcao": "Desenvolvedor Novo"}

        # Act
        result = self.uc.execute(self.mock_uow, 1, payload)

        # Assert
        assert result.id == 1
        assert result.nome_funcao == "Desenvolvedor Novo"
        self.mock_uow.funcoes.get_by_id.assert_called_once_with(1)
        self.mock_uow.funcoes.get_by_nome.assert_called_once_with("Desenvolvedor Novo")

    def test_execute_nao_encontrado(self):
        # Arrange
        self.mock_uow.funcoes.get_by_id.return_value = None
        payload = {"nome_funcao": "Desenvolvedor Novo"}

        # Act & Assert
        with pytest.raises(NotFoundError) as exc_info:
            self.uc.execute(self.mock_uow, 99, payload)
        assert "Função não encontrada" in str(exc_info.value)

    def test_execute_nome_vazio(self):
        # Arrange
        payload = {"nome_funcao": "   "}

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            self.uc.execute(self.mock_uow, 1, payload)
        assert "nome não pode ser vazio" in str(exc_info.value)

    def test_execute_conflito_nome_existente(self):
        # Arrange
        payload = {"nome_funcao": "Gerente"}
        # Simular que já existe UMA OUTRA função com id=2 e nome="Gerente"
        self.mock_uow.funcoes.get_by_nome.return_value = Mock(id=2, nome_funcao="Gerente")

        # Act & Assert
        with pytest.raises(ConflictError) as exc_info:
            self.uc.execute(self.mock_uow, 1, payload)
        assert "Já existe uma função com esse nome" in str(exc_info.value)