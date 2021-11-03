import pytest

from src.repositorios.mock.armazenamento_professor_volatil import ArmazenamentoProfessorVolatil
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado
from src.usecases.professor.uc_editar_professor import UCEditarProfessor


class TestUCEditarProfessor:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoProfessorVolatil()
        self.prof = mo.mockProfessor()
        self.armazenamento.cadastrarProfessor(self.prof)
        self.uc = UCEditarProfessor(self.armazenamento)

        yield
        # Teardown

    # TODO testar para editar padrao - nao dá agora pois enums do models só tem 1 valor

    def testIDNaoEncontradoLevantaErroProfessorNaoEncontrado(self):
        novo = mo.mockProfessor()
        novo.ID = mo.mockIdDiferente()
        # TODO Alterar algo do prof depois quando der

        with pytest.raises(ErroProfessorNaoEncontrado):
            self.uc(novo)
        # assert self.armazenamento.armazem[0] == mo.mockProfessor()     # Não atualizou repo

