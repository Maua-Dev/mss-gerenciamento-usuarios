from devmaua.src.models.usuario import Usuario

from src.interfaces.IRepoUsuario import IArmazenamento


class UCLogarUsuario():

    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def __call__(self, login: str, senha: str):
        try:
            return self.usuariosRepo.logarUsuario(login, senha)

