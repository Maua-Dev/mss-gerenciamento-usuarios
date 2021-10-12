from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_usecase import ErroIdInvalido


class UCGetPorUserId:
    usuarioRepo: IArmazenamento

    def __init__(self, usuarioRepo: IArmazenamento):
        self.usuarioRepo = usuarioRepo

    def __call__(self, userId: int):
        if(userId < 0):
            raise ErroIdInvalido
        #Erro é re-levantado pois repo pode ser alterado
        try:
            return self.usuarioRepo.getUsuarioPorUserId(userId)
        except:
            raise ErroUsuarioNaoExiste
