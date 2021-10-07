from devmaua.src.models.usuario import Usuario

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.c_get_por_userid import CHttpGetPorUserIdFastAPI
import tests.mock_objetos as mo
import json
import pytest


class TestCGetPorUserId:

    repo: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    c: CHttpGetPorUserIdFastAPI

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.repo = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.repo.cadastrarUsuario(self.usuario)
        self.c = CHttpGetPorUserIdFastAPI(self.repo)

        yield

        # Teardown

    def testPadraoGetPorUserId(self):
        res = self.c(0)
        j = json.loads(res.body)
        u = self.usuario

        assert j["nome"] == u.nome and\
               str(j["nascimento"]) == str(u.nascimento)
        assert res.status_code == 200

    def testErroUsuarioInvalido(self):
        res = self.c(1)
        assert "Usuario nao existe!" == res.body.decode()
        assert res.status_code == 404

    def testErroIdInvalido(self):
        res = self.c(-1)
        assert "Id inválido" == res.body.decode()
        assert res.status_code == 400
