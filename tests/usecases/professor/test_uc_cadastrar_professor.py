import pytest

import tests.mock_objetos as mo
from src.repositorios.mock.armazenamento_professor_volatil import ArmazenamentoProfessorVolatil

from src.usecases.erros.erros_uc_professor import ErroProfessorJaCadastrado
from src.usecases.professor.uc_cadastrar_professor import UCCadastrarProfessor


class TestUCCadastrarProfessor:

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoProfessorVolatil()
        self.prof = mo.mockProfessor()
        self.uc = UCCadastrarProfessor(self.armazenamento)

        yield
        # Teardown

    def testFuncionamentoNormal(self):
        assert len(self.armazenamento.armazem) == 0

        self.uc(self.prof)

        assert len(self.armazenamento.armazem) == 1

    def testCadastrarComErroAlunoJaCadastrado(self):
        self.armazenamento.cadastrarProfessor(self.prof)

        assert len(self.armazenamento.armazem) == 1

        with pytest.raises(ErroProfessorJaCadastrado):
            self.uc(self.prof)
        assert len(self.armazenamento.armazem) == 1
