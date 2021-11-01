from fastapi import Response, status

from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.usuario.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail

from src.interfaces.IRepoUsuario import IArmazenamentoUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste

import logging


class CDeletarUsuarioPorEmailFastAPI:
    repo: IArmazenamentoUsuario
    uc: UCDeletarUsuarioPorEmail

    def __init__(self, repo: IArmazenamentoUsuario):
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

            return Response(content="Usuario deletado com sucesso", status_code=status.HTTP_200_OK)

        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
