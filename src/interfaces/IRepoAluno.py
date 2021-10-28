from abc import ABC, abstractmethod

from devmaua.src.models.aluno import Aluno


class IArmazenamentoAluno(ABC):

    """"
    Interface com os métodos necessários para o gerenciamento de alunos
    """

    @abstractmethod
    def cadastrarAluno(self, aluno: Aluno):
        pass

