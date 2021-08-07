from src.interfaces.interface_deletar_usuario import IDeletarUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class UCDeletarUsuarioPorEmail():
    
    deletarUsuario: IDeletarUsuario
    
    def __init__(self, deletarUsuario: IDeletarUsuario):
        self.deletarUsuario = deletarUsuario
        
    def deletarUsuarioPorEmail(self, email: str):
        if not(self.deletarUsuario.usuarioExistePorEmail(email)):
            raise ErroUsuarioInvalido
        
        self.deletarUsuario.deletarUsuarioPeloEmail(email)