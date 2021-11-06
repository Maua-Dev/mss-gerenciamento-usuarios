import pytest

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from devmaua.src.models.usuario import Usuario
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.usuario.uc_get_usuario_por_email import UCGetUsuarioPorEmail


class TestUCGetPorEmail:
    armazenamento: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    uc: UCGetUsuarioPorEmail

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.armazenamento.cadastrarUsuario(self.usuario)
        self.uc = UCGetUsuarioPorEmail(self.armazenamento)

        yield

        # Teardown

    def testPadraoGetPorEmail(self):
        assert self.uc('teste@teste.com') == self.usuario

    def testErroUsuarioInvalido(self):
        with pytest.raises(ErroUsuarioNaoExiste):
            self.uc("teste@teste.com.br")
