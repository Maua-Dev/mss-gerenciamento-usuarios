from devmaua.src.models.email import Email
from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class UCAdicionarEmail():
    
    repositorio: IAlteracaoInfosCadastro
    
    def __init__(self, repositorio: IAlteracaoInfosCadastro):
        self.repositorio = repositorio
        
    def adicionarEmail(self, usuario: Usuario, email: Email):
        if not(self.repositorio.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if email == None:
            raise ErroEmailInvalido
        
        self.repositorio.adicionarEmail(usuario, email)
        