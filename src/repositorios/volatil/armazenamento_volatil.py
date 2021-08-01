from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento


class ArmazenamentoUsuarioVolatil(IArmazenamento):
    armazem: list[Usuario]

    def __init__(self):
        self.armazem = []


    def usuarioExiste(self, outro_usuario: Usuario):
        for u in self.armazem:
            if u.nome == outro_usuario.nome and u.nascimento == outro_usuario.nascimento:
                return True
        return False

    def cadastrarUsuario(self, usuario: Usuario):
        self.armazem.append(usuario)


    def getUsuario(self, ra: RA):
        pass


    def logarUsuario(self, login: str, senha: str):
        pass




