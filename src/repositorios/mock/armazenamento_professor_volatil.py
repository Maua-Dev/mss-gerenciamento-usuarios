from typing import List

from devmaua.src.models.professor import Professor

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado


class ArmazenamentoProfessorVolatil(IArmazenamentoProfessor):
    armazem: List[Professor]

    def __init__(self):
        self.armazem = []

    def cadastrarProfessor(self, professor: Professor):
        self.armazem.append(professor)

    def deletarProfessorPorEmail(self, email: str):
        for p in self.armazem:
            for e in p.contato.emails:
                if e.email == email:
                    self.armazem.remove(p)
                    return True
        return False

    def getProfessorPorId(self, profId: str) -> Professor:
        for p in self.armazem:
            if p.ID == profId:
                return p
        raise ErroNaoEncontrado
