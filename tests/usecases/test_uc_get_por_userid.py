import pytest

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from devmaua.src.models.usuario import Usuario
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_usecase import ErroIdInvalido
from src.usecases.uc_get_por_userid import UCGetPorUserId


class TestUCGetPorUserId:
    armazenamento: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    uc: UCGetPorUserId

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.armazenamento.cadastrarUsuario(self.usuario)
        self.uc = UCGetPorUserId(self.armazenamento)

        yield

        # Teardown

    def testPadraoGetPorId(self):
        assert self.uc(0) == self.usuario

    def testErroUsuarioInvalido(self):
        with pytest.raises(ErroUsuarioInvalido):
            self.uc(1)

    def testErroIdInvalido(self):
        with pytest.raises(ErroIdInvalido):
            self.uc(-2)
