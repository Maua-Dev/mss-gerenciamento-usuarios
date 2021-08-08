from abc import ABC, abstractmethod

from devmaua.src.models.ra import RA


class IDeletarUsuario(ABC):
    """" Interface para deletar um usuario cadastrado no sistema """
    
    @abstractmethod
    def deletarUsuarioPorEmail(self, email: str):
        """ Remove um usuario a partir do seu email """
        pass
    
    @abstractmethod
    def usuarioExistePorEmail(self, email:str):
        """ Retorna se um usuario existe """
        pass