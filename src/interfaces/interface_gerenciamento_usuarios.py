
from abc import ABC, abstractmethod

from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario


class IArmazenamento(ABC):
    """"
    Interface com os métodos necessários para o gerenciamento de usuários
    """
    @abstractmethod
    def getUsuario(self, ra: RA):
        pass

    @abstractmethod
    def cadastrarUsuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def logarUsuario(self, login: str, senha: str):
        pass

    @abstractmethod
    def usuarioExiste(self, usuario_outro: Usuario):
        pass
