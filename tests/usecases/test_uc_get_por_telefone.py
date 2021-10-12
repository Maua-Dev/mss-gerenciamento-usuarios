import pytest

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from devmaua.src.models.usuario import Usuario
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.uc_get_por_telefone import UCGetPorTelefone


class TestUCGetPorEmail:
    armazenamento: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    uc: UCGetPorTelefone

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.armazenamento.cadastrarUsuario(self.usuario)
        self.uc = UCGetPorTelefone(self.armazenamento)

        yield

        # Teardown

    def testPadraoGetPorTelefone(self):
        assert self.uc(11, "99999-9999") == self.usuario

    def testErroUsuarioInvalidoErroDDD(self):
        with pytest.raises(ErroUsuarioNaoExiste):
            self.uc(13, "99999-9999")

    def testErroUsuarioInvalidoErroNumero(self):
        with pytest.raises(ErroUsuarioNaoExiste):
            self.uc(11, "19999-9999")