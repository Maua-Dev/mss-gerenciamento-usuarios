import devmaua.src.models as models
from abc import ABC, abstractmethod


class IGerenciamentoUsuarios(ABC):
    """"
    Interface com os métodos necessários para o gerenciamento de usuários
    """
    @abstractmethod
    def get_usuario(self, ra: models.ra.RA):
        pass

    @abstractmethod
    def cadastrar_usuario(self, usuario: models.usuario.Usuario):
        pass

    @abstractmethod
    def logar_usuario(self, login: str, senha: str):
        pass


