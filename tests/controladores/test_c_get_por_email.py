from devmaua.src.models.usuario import Usuario

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.c_get_por_email import CHttpGetPorEmailFastAPI
import tests.mock_objetos as mo
import json
import pytest


class TestCGetPorUserId:

    repo: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    c: CHttpGetPorEmailFastAPI

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.repo = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.repo.cadastrarUsuario(self.usuario)
        self.c = CHttpGetPorEmailFastAPI(self.repo)

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
        assert "Usuario nao existe!" == res.body.decode()
        assert res.status_code == 404
