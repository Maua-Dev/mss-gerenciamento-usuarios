from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido


class UCAdicionarTelefone():
    
    alteracaoInfosCadastro: IAlteracaoInfosCadastro

    def __init__(self, alteracaoInfosCadastro: IAlteracaoInfosCadastro):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, telefone: Telefone):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if telefone == None:
            raise ErroTelefoneInvalido
        
        self.alteracaoInfosCadastro.adicionarTelefone(usuario, telefone)
        