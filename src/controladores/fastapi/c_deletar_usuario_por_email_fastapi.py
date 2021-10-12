from fastapi import Response

from src.usecases.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste

from http import HTTPStatus
import logging


class CDeletarUsuarioPorEmailFastAPI:
    repo: IArmazenamento
    uc: UCDeletarUsuarioPorEmail

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCDeletarUsuarioPorEmail(self.repo)
    
    def __call__(self, body: dict):
        """ Estilo do body:
            {
                "email": email string
            }
        """
        
        try:
            self.uc(body['email'])

            return Response(content="Usuario deletado com sucesso", status_code=HTTPStatus.OK)

        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)

        except KeyError as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
