from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IGerenciamentoUsuarios


class CadastradorUsuario():

    usuarios_repo: IGerenciamentoUsuarios

    def __init__(self, usuarios_repo: IGerenciamentoUsuarios):
        self.usuarios_repo = usuarios_repo

    def cadastrar(self, usuario: Usuario):
        try:
            return self.usuarios_repo.logar_usuario(Usuario)
        except:
            return False

