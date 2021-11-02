from devmaua.src.models.usuario import Usuario

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.usuario.c_get_usuario_por_userid import CHttpGetUsuarioPorUserIdFastAPI
import tests.mock_objetos as mo
import json
import pytest

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_usecase_usuario import ErroIdInvalido


class TestCGetPorUserId:

    repo: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    c: CHttpGetUsuarioPorUserIdFastAPI

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.repo = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.repo.cadastrarUsuario(self.usuario)
        self.c = CHttpGetUsuarioPorUserIdFastAPI(self.repo)

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
        assert str(ErroUsuarioNaoExiste()) == res.body.decode()
        assert res.status_code == 404

    def testErroIdInvalido(self):
        res = self.c(-1)
        assert str(ErroIdInvalido()) == res.body.decode()
        assert res.status_code == 400
