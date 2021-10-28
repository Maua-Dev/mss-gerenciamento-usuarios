from devmaua.src.models.aluno import Aluno

from src.interfaces.IRepoUsuario import IArmazenamentoUsuario


class ArmazenamentoAlunoVolatil():
    armazem: list[Aluno]

    def __init__(self):
        self.armazem = []

    def cadastrarAluno(self, aluno: Aluno):
        self.armazem.append(aluno)


