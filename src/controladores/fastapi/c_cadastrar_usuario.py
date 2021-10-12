from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.usuario import Usuario
from fastapi import Response

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_usecase import ErroUsuarioExiste
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from http import HTTPStatus
import logging


class ControllerHTTPCadastrarUsuario:
    repo: IArmazenamento
    uc: UCCadastrarUsuario

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCCadastrarUsuario(self.repo)

    def __call__(self, body: dict):

        try:
            usuario = Usuario.criarUsuarioPorDict(body)
            self.uc(usuario)

            return Response(content="Usuário criado com sucesso", status_code=HTTPStatus.OK)

        except (ErroDadosUsuarioInvalidos, ErroUsuarioExiste) as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
