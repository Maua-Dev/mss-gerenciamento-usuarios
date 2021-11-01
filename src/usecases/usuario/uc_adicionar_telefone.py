from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from src.interfaces.IRepoUsuario import IArmazenamentoUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroTelefoneInvalido


class UCAdicionarTelefone():
    
    alteracaoInfosCadastro: IArmazenamentoUsuario

    def __init__(self, alteracaoInfosCadastro: IArmazenamentoUsuario):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, telefone: Telefone):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if telefone == None:
            raise ErroTelefoneInvalido
        
        self.alteracaoInfosCadastro.adicionarTelefone(usuario, telefone)
        