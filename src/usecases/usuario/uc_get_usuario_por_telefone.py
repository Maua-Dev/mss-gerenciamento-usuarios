from devmaua.src.models.usuario import Usuario

from src.interfaces.i_repo_usuario import IArmazenamentoUsuario
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste


class UCGetUsuarioPorTelefone:
    usuarioRepo: IArmazenamentoUsuario

    def __init__(self, usuarioRepo: IArmazenamentoUsuario):
        self.usuarioRepo = usuarioRepo

    def __call__(self, ddd: int, numero: str) -> Usuario:
        #Erro é re-levantado pois repo pode ser alterado
        try:
            return self.usuarioRepo.getUsuarioPorTelefone(ddd, numero)
        except:
            raise ErroUsuarioNaoExiste
