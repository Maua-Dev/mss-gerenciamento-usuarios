from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento


class LogarUsuario():

    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def logar(self, login: str, senha: str):
        try:
            return self.usuariosRepo.logar_usuario(login, senha)
        except:
            return False
