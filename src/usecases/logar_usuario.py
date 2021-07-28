from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IGerenciamentoUsuarios


class LogadorUsuario():

    usuarios_repo: IGerenciamentoUsuarios

    def __init__(self, usuarios_repo: IGerenciamentoUsuarios):
        self.usuarios_repo = usuarios_repo

    def logar(self, login: str, senha: str):
        try:
            return self.usuarios_repo.logar_usuario(login, senha)
        except:
            return False
