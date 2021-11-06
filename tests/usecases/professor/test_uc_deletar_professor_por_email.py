import pytest

from src.repositorios.mock.armazenamento_professor_volatil import ArmazenamentoProfessorVolatil
from src.usecases.erros.erros_usecase import ErroEmailInvalido
from src.usecases.professor.uc_deletar_professor_por_email import UCDeletarProfessorPorEmail
from tests import mock_objetos as mo

class TestUCDeletarProfessorPorEmail:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoProfessorVolatil()
        self.prof = mo.mockProfessor()
        self.armazenamento.cadastrarProfessor(self.prof)
        self.uc = UCDeletarProfessorPorEmail(self.armazenamento)

        yield
        # Teardown

    def testFuncinamentoPadrao(self):
        assert len(self.armazenamento.armazem) == 1

        self.uc(self.prof.contato.emails[0].email)

        assert len(self.armazenamento.armazem) == 0

    def testEmailNoneLevantaErroEmailInvalido(self):
        with pytest.raises(ErroEmailInvalido):
            self.uc(None)

        assert len(self.armazenamento.armazem) == 1

    def testEmailVazioLevantaErroEmailInvalido(self):
        with pytest.raises(ErroEmailInvalido):
            self.uc("")

        assert len(self.armazenamento.armazem) == 1