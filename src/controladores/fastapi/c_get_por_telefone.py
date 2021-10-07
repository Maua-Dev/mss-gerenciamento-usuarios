from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.uc_get_por_telefone import UCGetPorTelefone
from fastapi import Response
from http import HTTPStatus
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class CHttpGetPorTelefoneFastAPI:
    repo: IArmazenamento
    uc: UCGetPorTelefone

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCGetPorTelefone(self.repo)

    def __call__(self, ddd: int, numero: str):

        try:
            user = self.uc(ddd, numero)
            content = jsonable_encoder(user.__dict__)

            return JSONResponse(content=content, status_code=HTTPStatus.OK)

        except ErroUsuarioInvalido as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)

        except Exception as e:
            print(e)
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
