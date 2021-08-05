from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento


class UCLogarUsuario():

    usuarios_repo: IArmazenamento

    def __init__(self, usuarios_repo: IArmazenamento):
        self.usuarios_repo = usuarios_repo

    def logar(self, login: str, senha: str):
        try:
            return self.usuarios_repo.logar_usuario(login, senha)
        except:
            return False
