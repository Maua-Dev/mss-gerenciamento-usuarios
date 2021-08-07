from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.usecases.erros.erros_usecase import ErroUsuarioExiste


class UCCadastrarUsuario():

    usuarios_repo: IArmazenamento

    def __init__(self, usuarios_repo: IArmazenamento):
        self.usuarios_repo = usuarios_repo

    def __call__(self, usuario: Usuario):
        if self.usuarios_repo.usuarioExiste(usuario):
            raise ErroUsuarioExiste
        self.usuarios_repo.cadastrarUsuario(usuario)