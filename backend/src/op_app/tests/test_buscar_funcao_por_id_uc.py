import pytest
from unittest.mock import Mock
from src.op_app.application.use_cases.funcoes.buscar_funcao_por_id_uc import BuscarFuncaoPorIdUC
from src.op_app.application.errors import NotFoundError

class TestBuscarFuncaoPorIdUC:
    def setup_method(self):
        self.uc = BuscarFuncaoPorIdUC()
        self.mock_uow = Mock()
        self.mock_uow.funcoes = Mock()

    def test_execute_sucesso(self):
        # Arrange
        mock_funcao = Mock(id=1, nome_funcao="Desenvolvedor")
        self.mock_uow.funcoes.get_by_id.return_value = mock_funcao

        # Act
        result = self.uc.execute(self.mock_uow, 1)

        # Assert
        assert result.id == 1
        assert result.nome_funcao == "Desenvolvedor"
        self.mock_uow.funcoes.get_by_id.assert_called_once_with(1)

    def test_execute_nao_encontrado(self):
        # Arrange
        self.mock_uow.funcoes.get_by_id.return_value = None

        # Act & Assert
        with pytest.raises(NotFoundError) as exc_info:
            self.uc.execute(self.mock_uow, 99)
        assert "Função não encontrada" in str(exc_info.value)
        self.mock_uow.funcoes.get_by_id.assert_called_once_with(99)