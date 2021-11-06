from devmaua.src.models.usuario import Usuario

from src.interfaces.i_repo_usuario import IArmazenamentoUsuario
from src.usecases.erros.erros_usecase import ErroUsuarioExiste


class UCCadastrarUsuario():

    usuariosRepo: IArmazenamentoUsuario

    def __init__(self, usuariosRepo: IArmazenamentoUsuario):
        self.usuariosRepo = usuariosRepo

    def __call__(self, usuario: Usuario):
        if self.usuariosRepo.usuarioExiste(usuario):
            raise ErroUsuarioExiste
        self.usuariosRepo.cadastrarUsuario(usuario)

