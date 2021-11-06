from src.controladores.fastapi.usuario.c_cadastrar_usuario import ControllerHTTPCadastrarUsuario
from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
import tests.mock_objetos as mo


class TestControllerCadastrarUsuario:
    repoVolatil = ArmazenamentoUsuarioVolatil()
    c = ControllerHTTPCadastrarUsuario(repoVolatil)

    def test_controller_cadastrar_usuario(self):
        usuario = mo.mockUsuario()
        response = self.c(usuario)

        assert response.status_code == 200
