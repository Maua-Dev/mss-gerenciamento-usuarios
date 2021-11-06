from abc import ABC, abstractmethod

from devmaua.src.models.professor import Professor


class IArmazenamentoProfessor(ABC):

    """"
    Interface com os métodos necessários para o gerenciamento de professores
    """

    @abstractmethod
    def cadastrarProfessor(self, professor: Professor):
        pass

    #TODO metodos de editar

    #TODO Validar se não é melhor fazer por id
    # ! Classe model <Email> está mal feita, nao podemos usar para validaao de email
    @abstractmethod
    def deletarProfessorPorEmail(self, email: str) -> bool:
        pass

    @abstractmethod
    def getProfessorPorId(self, profId: str) -> Professor:
        pass

    @abstractmethod
    def editarProfessor(self, professor: Professor) -> bool:
        pass
