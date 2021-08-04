from devmaua.src.models.ra import RA

from src.interfaces.interface_deletar_usuario import IDeletarUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class UCRemoverAlunoPorRA():
    
    deletarUsuario: IDeletarUsuario
    
    def __init__(self, deletarUsuario: IDeletarUsuario):
        self.deletarUsuario = deletarUsuario
        
    def removerAlunoPorRA(self, ra: RA):
        if not(self.deletarUsuario.alunoExiste(ra)):
            raise ErroUsuarioInvalido
        
        self.deletarUsuario.removerAlunoPorRA(ra)