from devmaua.src.models.email import Email
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_email import TipoEmail

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarEmailUnico


class UCRemoverEmail():
    
    repositorio: IAlteracaoInfosCadastro
    
    def __init__(self, repositorio: IAlteracaoInfosCadastro):
        self.repositorio = repositorio
        
    def removerEmail(self, usuario: Usuario, email: Email):
        if not(self.repositorio.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if email == None or email not in usuario.contato.emails:
            raise ErroEmailInvalido
        
        if email.tipo == TipoEmail.UNIVERSITARIO:
            raise ErroManipulacaoEmailFaculdade
        
        if len(usuario.contato.emails) == 1:
            raise ErroDeletarEmailUnico
        
        self.repositorio.removerEmail(usuario, email)