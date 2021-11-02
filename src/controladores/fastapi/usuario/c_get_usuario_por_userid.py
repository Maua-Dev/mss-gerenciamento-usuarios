from src.interfaces.IRepoUsuario import IArmazenamentoUsuario
from src.usecases.usuario.uc_get_usuario_por_userid import UCGetUsuarioPorUserId
from fastapi import Response, status
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_usecase import ErroIdInvalido, ErroInesperado
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging


class CHttpGetUsuarioPorUserIdFastAPI:
    repo: IArmazenamentoUsuario
    uc: UCGetUsuarioPorUserId

    def __init__(self, repo: IArmazenamentoUsuario):
        self.repo = repo
        self.uc = UCGetUsuarioPorUserId(self.repo)

    def __call__(self, userId: int):

        try:
            user = self.uc(userId)
            content = jsonable_encoder(user.__dict__)

            return JSONResponse(content=content, status_code=status.HTTP_200_OK)

        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except ErroIdInvalido as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

