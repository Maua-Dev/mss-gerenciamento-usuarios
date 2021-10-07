import pytest

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from devmaua.src.models.usuario import Usuario
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.uc_get_por_email import UCGetPorEmail


class TestUCGetPorEmail:
    armazenamento: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    uc: UCGetPorEmail

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.armazenamento.cadastrarUsuario(self.usuario)
        self.uc = UCGetPorEmail(self.armazenamento)

        yield

        # Teardown

    def testPadraoGetPorEmail(self):
        assert self.uc('teste@teste.com') == self.usuario

    def testErroUsuarioInvalido(self):
        with pytest.raises(ErroUsuarioInvalido):
            self.uc("teste@teste.com.br")
