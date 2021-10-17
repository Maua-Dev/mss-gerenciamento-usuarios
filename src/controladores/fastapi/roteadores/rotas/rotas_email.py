from fastapi import APIRouter


class RotasEmail(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/email", responses={404: {"description": "Not found"}})

        @self.post("")
        async def adicionarEmail(request: dict):
            return _ctrl.adicionarEmail(request)

        @self.delete("")
        async def removerEmail(request: dict):
            return _ctrl.removerEmail(request)

        @self.put("")
        async def editarEmail(request: dict):
            return _ctrl.editarEmail(request)
