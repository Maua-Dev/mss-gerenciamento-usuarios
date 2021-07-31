from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarTelefoneUnico


class UCRemoverTelefone():
    
    alteracaoInfosCadastro: IAlteracaoInfosCadastro
    
    def __init__(self, alteracaoInfosCadastro: IAlteracaoInfosCadastro):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def removerTelefone(self, usuario: Usuario, telefone: Telefone):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if telefone == None or telefone not in usuario.contato.telefones:
            raise ErroTelefoneInvalido
        
        if self.alteracaoInfosCadastro.quantidadeTelefones(usuario) == 1:
            raise ErroDeletarTelefoneUnico
        
        self.alteracaoInfosCadastro.removerTelefone(usuario, telefone)