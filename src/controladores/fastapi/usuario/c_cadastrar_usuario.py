from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.usuario import Usuario
from fastapi import Response, status

from src.interfaces.i_repo_usuario import IArmazenamentoUsuario

from src.usecases.erros.erros_usecase import ErroUsuarioExiste
from src.usecases.usuario.uc_cadastrar_usuario import UCCadastrarUsuario
from src.usecases.erros.erros_usecase import ErroInesperado

import logging


class ControllerHTTPCadastrarUsuario:
    repo: IArmazenamentoUsuario
    uc: UCCadastrarUsuario

    def __init__(self, repo: IArmazenamentoUsuario):
        self.repo = repo
        self.uc = UCCadastrarUsuario(self.repo)

    def __call__(self, usuario: Usuario):

        try:
            # usuario = Usuario.criarUsuarioPorDict(body)
            self.uc(usuario)

            return Response(content="Usuário criado com sucesso", status_code=status.HTTP_200_OK)
        # ErroDadosUsuarioInvalidos
        except (ErroUsuarioExiste, ValueError) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
