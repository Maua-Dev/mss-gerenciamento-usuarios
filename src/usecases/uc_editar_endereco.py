from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_endereco import TipoEndereco

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido

from typing import Optional


class UCEditarEndereco():
    
    alteracaoInfosCadastro: IAlteracaoInfosCadastro
    
    def __init__(self, alteracaoInfosCadastro: IAlteracaoInfosCadastro):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def editarEndereco(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int], cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if endereco == None or endereco not in usuario.contato.enderecos:
            raise ErroEnderecoInvalido
        
        self.alteracaoInfosCadastro.editarEndereco(usuario, endereco, logradouro, numero, cep, complemento, tipo)