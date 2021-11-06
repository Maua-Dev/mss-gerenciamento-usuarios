import pytest
from devmaua.src.models.aluno import Aluno
from devmaua.src.models.professor import Professor

from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
import tests.mock_objetos as mo
from src.repositorios.mock.armazenamento_professor_volatil import ArmazenamentoProfessorVolatil


class TestArmazenamentoProfessorVolatil:
    armazenamento: ArmazenamentoProfessorVolatil
    prof: Professor

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoProfessorVolatil()
        self.professor = mo.mockProfessor()
        self.armazenamento.cadastrarProfessor(self.professor)

        yield
        # Teardown

    def testDeletarPorEmail(self):
        email = mo.mockProfessor().contato.emails[0].email

        assert len(self.armazenamento.armazem) == 1

        self.armazenamento.deletarProfessorPorEmail(email)

        assert len(self.armazenamento.armazem) == 0

    def testDeletarProfessorPorEmailProfessorNaoEncontrado(self):
        v = self.armazenamento.deletarProfessorPorEmail("emailErrado@mail.com")
        assert not v

    def testGetProfessorPorID(self):
        profId = mo.mockProfessor().ID

        p = self.armazenamento.getProfessorPorId(profId)

        assert p == self.professor

    def testGetProfessorPorIDErroProfessorNaoEncontrado(self):
        with pytest.raises(ErroNaoEncontrado):
            self.armazenamento.getProfessorPorId(mo.mockIdDiferente())

#TODO testar para professores - nao dá agora pois enums do models só tem 1 valor

    def testEditarProfessorNaoEncontradoRetornaFalse(self):
        novo = mo.mockProfessor()
        novo.ID = mo.mockIdDiferente()
        # TODO Alterar algo do prof depois quando der

        cond = self.armazenamento.editarProfessor(novo)
        assert not cond
        # assert self.armazenamento.armazem[0] == mo.mockProfessor()     # Não atualizou repo
