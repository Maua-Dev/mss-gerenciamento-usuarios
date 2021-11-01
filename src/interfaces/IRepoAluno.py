from abc import ABC, abstractmethod

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA


class IArmazenamentoAluno(ABC):

    """"
    Interface com os métodos necessários para o gerenciamento de alunos
    """

    @abstractmethod
    def cadastrarAluno(self, aluno: Aluno):
        pass

    #TODO metodos de editar

    #TODO Validar se não é melhor fazer por RA
    # ! Classe model <Email> está mal feita, nao podemos usar para validaao de email
    @abstractmethod
    def deletarAlunoPorEmail(self, email: str):
        pass

    @abstractmethod
    def getAlunoPorRA(self, ra: RA):
        pass

