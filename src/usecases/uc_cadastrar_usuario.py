from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.usecases.erros.erros_usecase import ErroUsuarioExiste


class UCCadastrarUsuario():

    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def cadastrar(self, usuario: Usuario):
        if self.usuariosRepo.usuarioExiste(usuario):
            raise ErroUsuarioExiste
        self.usuariosRepo.cadastrarUsuario(usuario)


