from fastapi import APIRouter


class RotasUsuario(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/usuario", responses={404: {"description": "Not found"}})

        @self.delete("")
        async def deletarUsuarioPorEmail(request: dict):
            return _ctrl.deletarUsuarioPorEmail(request)
