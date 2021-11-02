from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from fastapi import APIRouter


class RotasAluno(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/aluno", responses={404: {"description": "Not found"}})

        @self.delete("")
        async def deletar(request: str):
            return _ctrl.deletarAlunoPorEmail(request)

        @self.get("/ra/{ano}/{numero}/{digito}")
        async def getPorRa(ano: str, numero: str, digito: str):
            #TODO Ta meio zoado isso aqui, pensar em jeito melhor
            ra = RA(ano=ano, numero=numero, digito=digito)
            return _ctrl.getPorRa(ra)
