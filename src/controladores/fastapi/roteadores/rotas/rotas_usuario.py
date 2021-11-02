from fastapi import APIRouter


class RotasUsuario(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/usuario", responses={404: {"description": "Not found"}})

        @self.delete("")
        async def deletarUsuarioPorEmail(request: dict):
            return _ctrl.deletarUsuarioPorEmail(request)

        @self.get("/{userId}")
        async def getUsuarioPorUserId(userId: int):
            return _ctrl.getUsuarioPorUserId(userId)

        @self.get("/email/{email}")
        async def getUsuarioPorEmail(email: str):
            return _ctrl.getUsuarioPorEmail(email)

        @self.get("/telefone/{ddd}/{numero}")
        async def getUsuarioPorTelefone(ddd: int, numero: str):
            return _ctrl.getUsuarioPorTelefone(ddd, numero)
