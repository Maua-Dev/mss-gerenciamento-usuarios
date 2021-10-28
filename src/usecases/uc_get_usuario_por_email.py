from src.interfaces.IRepoUsuario import IArmazenamentoUsuario
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste


class UCGetUsuarioPorEmail:
    usuarioRepo: IArmazenamentoUsuario

    def __init__(self, usuarioRepo: IArmazenamentoUsuario):
        self.usuarioRepo = usuarioRepo

    def __call__(self, email: str):
        # Email nao pode ser validado pelo model de email - nao será feito erro de badrequest
        # Erro é re-levantado pois repo pode ser alterado
        try:
            return self.usuarioRepo.getUsuarioPorEmail(email)
        except:
            raise ErroUsuarioNaoExiste
