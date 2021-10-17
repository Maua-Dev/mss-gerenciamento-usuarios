from fastapi import APIRouter


class RotasEndereco(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/endereco", responses={404: {"description": "Not found"}})

        @self.post("")
        async def adicionarEndereco(request: dict):
            return _ctrl.adicionarEndereco(request)

        @self.delete("")
        async def removerEndereco(request: dict):
            return _ctrl.removerEndereco(request)

        @self.put("")
        async def editarEndereco(request: dict):
            return _ctrl.editarEndereco(request)
