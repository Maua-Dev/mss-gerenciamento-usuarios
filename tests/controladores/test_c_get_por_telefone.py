from devmaua.src.models.usuario import Usuario

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.c_get_por_telefone import CHttpGetPorTelefoneFastAPI
import tests.mock_objetos as mo
import json
import pytest

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste


class TestCGetPorTelefone:

    repo: ArmazenamentoUsuarioVolatil
    usuario: Usuario
    c: CHttpGetPorTelefoneFastAPI

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.repo = ArmazenamentoUsuarioVolatil()
        self.usuario = mo.mockUsuario()
        self.repo.cadastrarUsuario(self.usuario)
        self.c = CHttpGetPorTelefoneFastAPI(self.repo)

        yield

        # Teardown

    def testPadraoGetPorEmail(self):
        res = self.c(11, "99999-9999")
        j = json.loads(res.body)
        u = self.usuario

        assert j["nome"] == u.nome and\
               str(j["nascimento"]) == str(u.nascimento)
        assert res.status_code == 200

    def testErroUsuarioInvalidoErroDDD(self):
        res = self.c(13, "99999-9999")
        assert str(ErroUsuarioNaoExiste()) == res.body.decode()
        assert res.status_code == 404

    def testErroUsuarioInvalidoErroNumero(self):
        res = self.c(11, "99299-9999")
        assert str(ErroUsuarioNaoExiste()) == res.body.decode()
        assert res.status_code == 404
