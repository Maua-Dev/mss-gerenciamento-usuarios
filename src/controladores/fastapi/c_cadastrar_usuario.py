from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.usuario import Usuario
from fastapi import Response, status

from src.interfaces.IRepoUsuario import IArmazenamentoUsuario

from src.usecases.erros.erros_usecase import ErroUsuarioExiste
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario
from src.usecases.erros.erros_usecase import ErroInesperado

import logging


class ControllerHTTPCadastrarUsuario:
    repo: IArmazenamentoUsuario
    uc: UCCadastrarUsuario

    def __init__(self, repo: IArmazenamentoUsuario):
        self.repo = repo
        self.uc = UCCadastrarUsuario(self.repo)

    def __call__(self, body: dict):

        try:
            usuario = Usuario.criarUsuarioPorDict(body)
            self.uc(usuario)

            return Response(content="Usuário criado com sucesso", status_code=status.HTTP_200_OK)

        except (ErroDadosUsuarioInvalidos, ErroUsuarioExiste) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(str(ErroInesperado()))
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
