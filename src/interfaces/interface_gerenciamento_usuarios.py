
from abc import ABC, abstractmethod

from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario


class IArmazenamento(ABC):
    """"
    Interface com os métodos necessários para o gerenciamento de usuários
    """
    @abstractmethod
    def get_usuario(self, ra: RA):
        pass

    @abstractmethod
    def cadastrar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def logar_usuario(self, login: str, senha: str):
        pass

    @abstractmethod
    def usuario_existe(self, usuario_outro: Usuario):
        pass