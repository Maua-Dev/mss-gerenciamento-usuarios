import pytest

from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
from src.usecases.aluno.uc_deletar_aluno_por_email import UCDeletarAlunoPorEmail
from src.usecases.erros.erros_usecase import ErroEmailInvalido
from tests import mock_objetos as mo

class TestUCDeletarAlunoPorEmail:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoAlunoVolatil()
        self.aluno = mo.mockAluno()
        self.armazenamento.cadastrarAluno(self.aluno)
        self.uc = UCDeletarAlunoPorEmail(self.armazenamento)

        yield
        # Teardown

    def testFuncinamentoPadrao(self):
        assert len(self.armazenamento.armazem) == 1

        self.uc(self.aluno.contato.emails[0].email)

        assert len(self.armazenamento.armazem) == 0

    def testEmailNoneLevantaErroEmailInvalido(self):
        with pytest.raises(ErroEmailInvalido):
            self.uc(None)

        assert len(self.armazenamento.armazem) == 1

    def testEmailVazioLevantaErroEmailInvalido(self):
        with pytest.raises(ErroEmailInvalido):
            self.uc("")

        assert len(self.armazenamento.armazem) == 1