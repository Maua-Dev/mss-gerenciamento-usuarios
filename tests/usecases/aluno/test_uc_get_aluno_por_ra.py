import pytest

from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
import tests.mock_objetos as mo
from src.usecases.aluno.uc_get_aluno_por_ra import UCGetAlunoPorRA
from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado


class TestUCGetAlunoPorRA:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoAlunoVolatil()
        self.aluno = mo.mockAluno()
        self.armazenamento.cadastrarAluno(self.aluno)
        self.uc = UCGetAlunoPorRA(self.armazenamento)

        yield
        # Teardown

    def testRodaPadrao(self):
        a = self.uc(self.aluno.ra)

        assert a == self.aluno

    def testRodaPadrao(self):
        with pytest.raises(ErroAlunoNaoEncontrado):
            self.uc(mo.mockRADiferente())
