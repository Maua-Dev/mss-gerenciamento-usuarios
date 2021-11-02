from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_telefone import TipoTelefone

from src.interfaces.i_repo_usuario import IArmazenamentoUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste

from typing import Optional


class UCEditarTelefone():
    
    alteracaoInfosCadastro: IArmazenamentoUsuario
    
    def __init__(self, alteracaoInfosCadastro: IArmazenamentoUsuario):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str], prioridade: Optional[int]):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if telefone == None or telefone not in usuario.contato.telefones:
            raise ErroTelefoneInvalido
        
        self.alteracaoInfosCadastro.editarTelefone(usuario, telefone, tipo, ddd, numero, prioridade)