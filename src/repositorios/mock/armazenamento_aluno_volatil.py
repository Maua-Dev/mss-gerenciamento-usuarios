from typing import List

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.models.editar_models import substituirValoresAluno
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado


class ArmazenamentoAlunoVolatil(IArmazenamentoAluno):
    armazem: List[Aluno]

    def __init__(self):
        self.armazem = []

    def cadastrarAluno(self, aluno: Aluno):
        self.armazem.append(aluno)

    def deletarAlunoPorEmail(self, email: str):
        for a in self.armazem:
            for e in a.contato.emails:
                if e.email == email:
                    self.armazem.remove(a)
                    return True
        return False

    def getAlunoPorRA(self, ra: RA) -> Aluno:
        for a in self.armazem:
            if a.ra == ra:
                return a
        raise ErroNaoEncontrado

    def editarAluno(self, aluno: Aluno) -> bool:
        for i, a in enumerate(self.armazem):
            if a.ra == aluno.ra:
                substituirValoresAluno(a, aluno)
                return True
        return False
