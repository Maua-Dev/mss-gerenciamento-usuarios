from devmaua.src.models.email import Email
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_email import TipoEmail

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade

from typing import Optional


class UCEditarEmail():
    
    alteracaoInfosCadastro: IArmazenamento
    
    def __init__(self, alteracaoInfosCadastro: IArmazenamento):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail], prioridade: Optional[int]):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if email == None or email not in usuario.contato.emails:
            raise ErroEmailInvalido
        
        if email.tipo == TipoEmail.UNIVERSITARIO:
            raise ErroManipulacaoEmailFaculdade
        
        self.alteracaoInfosCadastro.editarEmail(usuario, email, email_novo, tipo, prioridade)