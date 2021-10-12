from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.uc_get_por_userid import UCGetPorUserId
from fastapi import Response
from http import HTTPStatus
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_usecase import ErroIdInvalido
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging


class CHttpGetPorUserIdFastAPI:
    repo: IArmazenamento
    uc: UCGetPorUserId

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCGetPorUserId(self.repo)

    def __call__(self, userId: int):

        try:
            user = self.uc(userId)
            content = jsonable_encoder(user.__dict__)

            return JSONResponse(content=content, status_code=HTTPStatus.OK)

        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)

        except ErroIdInvalido as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

