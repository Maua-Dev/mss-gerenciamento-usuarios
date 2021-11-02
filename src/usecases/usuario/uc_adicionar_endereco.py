from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from src.interfaces.i_repo_usuario import IArmazenamentoUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroEnderecoInvalido


class UCAdicionarEndereco():
    
    alteracaoInfosCadastro: IArmazenamentoUsuario

    def __init__(self, alteracaoInfosCadastro: IArmazenamentoUsuario):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, endereco: Endereco):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if endereco == None:
            raise ErroEnderecoInvalido
        
        self.alteracaoInfosCadastro.adicionarEndereco(usuario, endereco)