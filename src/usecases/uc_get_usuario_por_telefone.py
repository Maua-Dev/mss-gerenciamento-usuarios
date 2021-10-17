from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste


class UCGetUsuarioPorTelefone:
    usuarioRepo: IArmazenamento

    def __init__(self, usuarioRepo: IArmazenamento):
        self.usuarioRepo = usuarioRepo

    def __call__(self, ddd: int, numero: str):
        #Erro é re-levantado pois repo pode ser alterado
        try:
            return self.usuarioRepo.getUsuarioPorTelefone(ddd, numero)
        except:
            raise ErroUsuarioNaoExiste
