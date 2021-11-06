from devmaua.src.models.professor import Professor
from fastapi import APIRouter


class RotasProfessor(APIRouter):


    def __init__(self, _ctrl):

        super().__init__(prefix="/professor", responses={404: {"description": "Not found"}})

        @self.delete("/{email}")
        async def deletar(email: str):
            # TODO ver se tem jeito melhor --> Refatorando models da para usar <Email>
            return _ctrl.deletarProfessorPorEmail(email)

        @self.get("/{profId}")
        async def getPorRa(profId: str):
            # TODO Ta meio zoado isso aqui, pensar em jeito melhor
            return _ctrl.getProfessorPorId(profId)

        @self.put("")
        async def editarProfessor(request: Professor):
            return _ctrl.editarProfessor(request)
