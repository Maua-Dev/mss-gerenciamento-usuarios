from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.usecases.erros.erros_usecase import ErroUsuarioExiste


class CadastrarUsuario():

    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def cadastrar(self, usuario: Usuario):
        if self.usuariosRepo.usuario_existe(usuario):
            raise ErroUsuarioExiste
        self.usuariosRepo.cadastrar_usuario(usuario)


