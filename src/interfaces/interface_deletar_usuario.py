from abc import ABC, abstractmethod

from devmaua.src.models.ra import RA


class IDeletarUsuario(ABC):
    """" Interface para deletar um usuario cadastrado no sistema """
    
    @abstractmethod
    def removerAlunoPorRA(self, ra: RA):
        """ Remove um usuario com a role 'Aluno' da base de usuarios """
        pass
    
    @abstractmethod
    def alunoExiste(self, ra: RA):
        """ Retorna se um aluno existe """
        pass