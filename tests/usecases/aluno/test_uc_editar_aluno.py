import pytest
from devmaua.src.enum.periodo import Periodo

from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
import tests.mock_objetos as mo
from src.usecases.aluno.uc_editar_aluno import UCEditarAluno
from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado


class TestUCEditarAluno:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoAlunoVolatil()
        self.aluno = mo.mockAluno()
        self.armazenamento.cadastrarAluno(self.aluno)
        self.uc = UCEditarAluno(self.armazenamento)

        yield
        # Teardown

    def testFuncinamentoPadrao(self):
        novo = mo.mockAluno()
        novo.periodo = Periodo.NOTURNO

        assert self.armazenamento.armazem[0].periodo == Periodo.DIURNO
        self.uc(novo)
        assert self.armazenamento.armazem[0].periodo == Periodo.NOTURNO

    def testRaNaoEncontradoLevantaErroAlunoNaoEncontrado(self):
        novo = mo.mockAluno()
        novo.ra = mo.mockRADiferente()
        novo.periodo = Periodo.NOTURNO

        with pytest.raises(ErroAlunoNaoEncontrado):
            self.uc(novo)
        assert self.armazenamento.armazem[0] == mo.mockAluno()  # Não atualizou periodo