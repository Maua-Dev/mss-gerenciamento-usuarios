from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class UCGetPorEmail:
    usuarioRepo: IArmazenamento

    def __init__(self, usuarioRepo: IArmazenamento):
        self.usuarioRepo = usuarioRepo

    def __call__(self, email: str):
        # Email nao pode ser validado pelo model de email - nao será feito erro de badrequest
        # Erro é re-levantado pois repo pode ser alterado
        try:
            return self.usuarioRepo.getUsuarioPorEmail(email)
        except:
            raise ErroUsuarioInvalido
