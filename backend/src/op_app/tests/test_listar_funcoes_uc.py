import pytest
from unittest.mock import Mock
from src.op_app.application.use_cases.funcoes.listar_funcoes_uc import ListarFuncoesUC

class TestListarFuncoesUC:
    def setup_method(self):
        self.uc = ListarFuncoesUC()
        self.mock_uow = Mock()
        self.mock_uow.funcoes = Mock()

    def test_execute_sucesso(self):
        # Arrange
        mock_funcao_1 = Mock(id=1, nome_funcao="Desenvolvedor")
        mock_funcao_2 = Mock(id=2, nome_funcao="Gerente")
        self.mock_uow.funcoes.list_all.return_value = [mock_funcao_1, mock_funcao_2]

        # Act
        result = self.uc.execute(self.mock_uow)

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[0].nome_funcao == "Desenvolvedor"
        assert result[1].id == 2
        assert result[1].nome_funcao == "Gerente"
        self.mock_uow.funcoes.list_all.assert_called_once()

    def test_execute_lista_vazia(self):
        # Arrange
        self.mock_uow.funcoes.list_all.return_value = []

        # Act
        result = self.uc.execute(self.mock_uow)

        # Assert
        assert len(result) == 0
        self.mock_uow.funcoes.list_all.assert_called_once()