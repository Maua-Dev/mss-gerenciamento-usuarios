import pytest
from devmaua.src.models.aluno import Aluno

from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
import tests.mock_objetos as mo


class TestArmazenamentoAlunoVolatil:
    armazenamento: ArmazenamentoAlunoVolatil
    aluno: Aluno

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoAlunoVolatil()
        self.aluno = mo.mockAluno()
        self.armazenamento.cadastrarAluno(self.aluno)

        yield

        # Teardown

    def testDeletarPorEmail(self):
        email = mo.mockUsuario().contato.emails[0].email

        assert len(self.armazenamento.armazem) == 1

        self.armazenamento.deletarAlunoPorEmail(email)

        assert len(self.armazenamento.armazem) == 0

    def testDeletarAlunoPorEmailErroAlunoNaoEncontrado(self):
        v = self.armazenamento.deletarAlunoPorEmail("emailErrado@mail.com")
        assert not v

    def testGetAlunoPorRA(self):
        ra = mo.mockRA()

        a = self.armazenamento.getAlunoPorRA(ra)

        assert a == self.aluno

    def testGetAlunoPorRAErroAlunoNaoEncontrado(self):
        with pytest.raises(ErroNaoEncontrado):
            self.armazenamento.getAlunoPorRA(mo.mockRADiferente())
