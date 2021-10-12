from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.uc_get_por_email import UCGetPorEmail
from fastapi import Response
from http import HTTPStatus
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging


class CHttpGetPorEmailFastAPI:
    repo: IArmazenamento
    uc: UCGetPorEmail

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCGetPorEmail(self.repo)

    def __call__(self, email: str):

        try:
            user = self.uc(email)
            content = jsonable_encoder(user.__dict__)

            return JSONResponse(content=content, status_code=HTTPStatus.OK)

        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

