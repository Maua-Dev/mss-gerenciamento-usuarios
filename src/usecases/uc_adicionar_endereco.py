from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido


class UCAdicionarEndereco():
    
    alteracaoInfosCadastro: IAlteracaoInfosCadastro

    def __init__(self, alteracaoInfosCadastro: IAlteracaoInfosCadastro):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, endereco: Endereco):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if endereco == None:
            raise ErroEnderecoInvalido
        
        self.alteracaoInfosCadastro.adicionarEndereco(usuario, endereco)