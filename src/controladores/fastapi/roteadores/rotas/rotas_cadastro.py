from devmaua.src.models.usuario import Usuario
from fastapi import APIRouter


class RotasCadastro(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/cadastro", responses={404: {"description": "Not found"}})

        @self.post("")
        async def cadastro(request: Usuario):
            return _ctrl.cadastrarUsuario(request)
