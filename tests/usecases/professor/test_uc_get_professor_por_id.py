import pytest

import tests.mock_objetos as mo
from src.repositorios.mock.armazenamento_professor_volatil import ArmazenamentoProfessorVolatil
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado
from src.usecases.professor.uc_get_professor_por_id import UCGetProfessorPorID


class TestUCGetProfessorPorID:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoProfessorVolatil()
        self.prof = mo.mockProfessor()
        self.armazenamento.cadastrarProfessor(self.prof)
        self.uc = UCGetProfessorPorID(self.armazenamento)

        yield
        # Teardown

    def testRodaPadrao(self):
        p = self.uc(self.prof.ID)

        assert p == self.prof

    def testErroAlunoNaoEncontrado(self):
        with pytest.raises(ErroProfessorNaoEncontrado):
            self.uc(mo.mockIdDiferente())
