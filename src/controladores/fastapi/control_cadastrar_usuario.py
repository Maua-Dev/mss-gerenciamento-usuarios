from devmaua.src.models.usuario import Usuario
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.usuario import Usuario
from fastapi import Response

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento

from src.usecases.erros.erros_usecase import ErroUsuarioExiste
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

class ControllerHTTPCadastrarUsuario():

    repo: IArmazenamento

    def __init__(self, repo: IArmazenamento):
        self.repo = repo

    def __call__(self, body: dict):

        try:
            cadastrarUsuarioUC = UCCadastrarUsuario(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body)
            cadastrarUsuarioUC(usuario)
            response = Response(content="Usuario criado com sucesso", status_code=200)

        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=400)

        except ErroUsuarioExiste:
            response = Response(content=str(ErroUsuarioExiste), status_code=400)

        return response



