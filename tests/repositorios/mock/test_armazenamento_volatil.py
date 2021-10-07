import pytest

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from devmaua.src.models.usuario import Usuario
import tests.mock_objetos as mo
from src.repositorios.erros.erros_armazem_volatil import ErroUsuarioNaoEncontrado


class TestArmazenamentoVolatil:
    armazenamento: ArmazenamentoUsuarioVolatil
    usuario: Usuario

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.armazenamento.cadastrarUsuario(self.usuario)

        yield

        # Teardown

    def testPadraoGetPorUserId(self):
        assert self.armazenamento.getUsuarioPorUserId(0) == self.usuario

    def testErroNaoEncontradoGetPorUserId(self):
        with pytest.raises(ErroUsuarioNaoEncontrado):
            self.armazenamento.getUsuarioPorUserId(1)

    def testPadraoGettPorEmail(self):
        assert self.armazenamento.getUsuarioPorEmail('teste@teste.com') == self.usuario

    def testErroNaoEncontradoGetPorEmail(self):
        with pytest.raises(ErroUsuarioNaoEncontrado):
            self.armazenamento.getUsuarioPorEmail("test@teste.com.br")

    def testPadraoGetPorTelefone(self):
        assert self.armazenamento.getUsuarioPorTelefone(ddd=11, numero='99999-9999') == self.usuario

    def testErroNaoEncontradoGetPorTelefoneDDDErrado(self):
        with pytest.raises(ErroUsuarioNaoEncontrado):
            self.armazenamento.getUsuarioPorTelefone(ddd=13, numero='99999-9999')

    def testErroNaoEncontradoGetPorTelefoneNumeroErrado(self):
        with pytest.raises(ErroUsuarioNaoEncontrado):
            self.armazenamento.getUsuarioPorTelefone(ddd=11, numero='99992-9999')
