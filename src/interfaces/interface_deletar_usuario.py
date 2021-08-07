from abc import ABC, abstractmethod

from devmaua.src.models.ra import RA


class IDeletarUsuario(ABC):
    """" Interface para deletar um usuario cadastrado no sistema """
    
    @abstractmethod
    def removerUsuarioPeloEmail(self, email: str):
        """ Remove um usuario com a role 'Aluno' da base de usuarios """
        pass
    
    @abstractmethod
    def usuarioExistePorEmail(self, email:str):
        """ Retorna se um aluno existe """
        pass