from typing import List

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
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
