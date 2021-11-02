from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from fastapi import APIRouter


class RotasAluno(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/aluno", responses={404: {"description": "Not found"}})

        @self.delete("/{email}")
        async def deletar(email: str):
            #TODO ver se tem jeito melhor --> Refatorando models da para usar <Email>
            return _ctrl.deletarAlunoPorEmail(email)

        @self.get("/ra/{ano}/{numero}/{digito}")
        async def getPorRa(ano: str, numero: str, digito: str):
            #TODO Ta meio zoado isso aqui, pensar em jeito melhor
            ra = RA(ano=ano, numero=numero, digito=digito)
            return _ctrl.getPorRa(ra)
