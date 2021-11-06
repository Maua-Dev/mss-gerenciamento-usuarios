import pytest

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
import tests.mock_objetos as mo
from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
from src.usecases.aluno.uc_cadastrar_aluno import UCCadastrarAluno
from unittest.mock import patch, Mock

from src.usecases.erros.erros_uc_aluno import ErroAlunoJaCadastrado


class TestUCCadastrarAluno:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoAlunoVolatil()
        self.aluno = mo.mockAluno()
        self.uc = UCCadastrarAluno(self.armazenamento)

        yield
        # Teardown

    # #TODO Considerar usar algo assim ao inves do mock que fizemos, será que fica mais facil? - só fazemos a interface
    # @patch.object(IArmazenamentoAluno, "__abstractmethods__")
    # def testFuncionamentoPadrao(self, mockRepo):
    #     mockRepo.getAlunoPorRA.side_effect = ErroAlunoNaoEncontrado()
    #
    #     UCCadastrarAluno(mockRepo)(self.aluno)
    #
    #     mockRepo.getAlunoPorRA.assert_called_once_with(self.aluno.ra)
    #     mockRepo.cadastrarAluno.assert_called_once_with(self.aluno)
    #
    # @patch.object(IArmazenamentoAluno, "__abstractmethods__")
    # def testErroAlunoJaCadastrado(self, mockRepo):
    #     mockRepo.getAlunoPorRA.return_value = self.aluno
    #
    #     with pytest.raises(ErroAlunoJaCadastrado):
    #         UCCadastrarAluno(mockRepo)(self.aluno)
    #
    #     mockRepo.getAlunoPorRA.assert_called_once_with(self.aluno.ra)
    #     mockRepo.cadastrarAluno.assert_not_called()

    def testFuncionamentoNormal(self):
        assert len(self.armazenamento.armazem) == 0

        self.uc(self.aluno)

        assert len(self.armazenamento.armazem) == 1

    def testCadastrarComErroAlunoJaCadastrado(self):
        self.armazenamento.cadastrarAluno(self.aluno)

        assert len(self.armazenamento.armazem) == 1

        with pytest.raises(ErroAlunoJaCadastrado):
            self.uc(self.aluno)
        assert len(self.armazenamento.armazem) == 1
