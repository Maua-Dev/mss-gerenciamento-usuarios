from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_telefone import TipoTelefone

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

from typing import Optional


class UCEditarTelefone():
    
    alteracaoInfosCadastro: IAlteracaoInfosCadastro
    
    def __init__(self, alteracaoInfosCadastro: IAlteracaoInfosCadastro):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def editarTelefone(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str], prioridade: Optional[int]):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioInvalido
        
        if telefone == None or telefone not in usuario.contato.telefones:
            raise ErroTelefoneInvalido
        
        self.alteracaoInfosCadastro.editarTelefone(usuario, telefone, tipo, ddd, numero, prioridade)