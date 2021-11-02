from devmaua.src.models.usuario import Usuario

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.usuario.c_get_usuario_por_email import CHttpGetUsuarioPorEmailFastAPI
import tests.mock_objetos as mo
import json
import pytest

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste


class TestCGetPorUserId:

    repo: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    c: CHttpGetUsuarioPorEmailFastAPI

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.repo = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.repo.cadastrarUsuario(self.usuario)
        self.c = CHttpGetUsuarioPorEmailFastAPI(self.repo)

        yield

        # Teardown

    def testPadraoGetPorEmail(self):
        res = self.c("teste@teste.com")
        j = json.loads(res.body)
        u = self.usuario

        assert j["nome"] == u.nome and\
               str(j["nascimento"]) == str(u.nascimento)
        assert res.status_code == 200

    def testErroUsuarioInvalido(self):
        res = self.c("teste@teste.com.br")
        assert str(ErroUsuarioNaoExiste()) == res.body.decode()
        assert res.status_code == 404
