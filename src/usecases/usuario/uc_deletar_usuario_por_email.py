from src.interfaces.IRepoUsuario import IArmazenamentoUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste


class UCDeletarUsuarioPorEmail():
    
    deletarUsuario: IArmazenamentoUsuario
    
    def __init__(self, deletarUsuario: IArmazenamentoUsuario):
        self.deletarUsuario = deletarUsuario
        
    def __call__(self, email: str):
        if not(self.deletarUsuario.usuarioExistePorEmail(email)):
            raise ErroUsuarioNaoExiste
        
        self.deletarUsuario.deletarUsuarioPorEmail(email)