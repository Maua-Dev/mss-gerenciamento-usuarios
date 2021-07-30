from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.usecases.erros.erros_usecase import ErroUsuarioExiste


class CadastradorUsuario():

    usuarios_repo: IArmazenamento

    def __init__(self, usuarios_repo: IArmazenamento):
        self.usuarios_repo = usuarios_repo

    def cadastrar(self, usuario: Usuario):
        if self.usuarios_repo.usuario_existe(usuario):
            raise ErroUsuarioExiste
        self.usuarios_repo.cadastrar_usuario(usuario)