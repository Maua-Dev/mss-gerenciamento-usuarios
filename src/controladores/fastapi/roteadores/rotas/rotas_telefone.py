from fastapi import APIRouter


class RotasTelefone(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/telefone", responses={404: {"description": "Not found"}})

        @self.post("")
        async def adicionarTelefone(request: dict):
            return _ctrl.adicionarTelefone(request)

        @self.delete("")
        async def removerTelefone(request: dict):
            return _ctrl.removerTelefone(request)

        @self.put("")
        async def editarTelefone(request: dict):
            return _ctrl.editarTelefone(request)
