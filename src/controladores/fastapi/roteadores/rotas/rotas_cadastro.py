from fastapi import APIRouter


class RotasCadastro(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/cadastro", responses={404: {"description": "Not found"}})

        @self.post("")
        async def cadastro(request: dict):
            return _ctrl.cadastrarUsuario(request)
