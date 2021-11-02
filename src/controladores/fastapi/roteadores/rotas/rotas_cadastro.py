from devmaua.src.models.aluno import Aluno
from devmaua.src.models.professor import Professor
from devmaua.src.models.usuario import Usuario
from fastapi import APIRouter


class RotasCadastro(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/cadastro", responses={404: {"description": "Not found"}})

        @self.post("/usuario")
        async def cadastroUsuario(request: Usuario):
            return _ctrl.cadastrarUsuario(request)

        @self.post("/aluno")
        async def cadastroAluno(request: Aluno):
            return _ctrl.cadastrarAluno(request)

        @self.post("/professor")
        async def cadastroProfessor(request: Professor):
            return _ctrl.cadastrarProfessor(request)
