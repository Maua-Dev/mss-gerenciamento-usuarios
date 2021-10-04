from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class UCDeletarUsuarioPorEmail():
    
    deletarUsuario: IArmazenamento
    
    def __init__(self, deletarUsuario: IArmazenamento):
        self.deletarUsuario = deletarUsuario
        
    def __call__(self, email: str):
        if not(self.deletarUsuario.usuarioExistePorEmail(email)):
            raise ErroUsuarioInvalido
        
        self.deletarUsuario.deletarUsuarioPorEmail(email)