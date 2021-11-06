from devmaua.src.models.email import Email
from devmaua.src.models.usuario import Usuario

from src.interfaces.i_repo_usuario import IArmazenamentoUsuario

from src.usecases.erros.erros_usecase import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste


class UCAdicionarEmail():
    
    alteracaoInfosCadastro: IArmazenamentoUsuario
    
    def __init__(self, alteracaoInfosCadastro: IArmazenamentoUsuario):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, email: Email):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if email == None:
            raise ErroEmailInvalido
        
        self.alteracaoInfosCadastro.adicionarEmail(usuario, email)
        