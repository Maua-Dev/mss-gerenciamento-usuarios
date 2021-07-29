from devmaua.src.models.telefone import Telefone        
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco

from devmaua.src.enum.roles import Roles                
from devmaua.src.enum.tipo_telefone import TipoTelefone 

from typing import Optional


class IAlteracaoInfosCadastro:
    
    def adicionar_telefone(self, telefone: Telefone):
        """ Adiciona um novo telefone na lista de telefones de Contato. """
        pass
    
    def remover_telefone(self, telefone: Telefone):
        """ Remove um telefone da lista de telefones de Contato. """
        pass
    
    def editar_telefone(self, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str]):
        """ Edita informacoes de um Telefone"""
        pass
        
    def adicionar_roles(self, roles: list[Roles]):
        """ Adiciona roles a um usuario """
        pass
    
    def remover_roles(self, roles: list[Roles]):
        """ Remove roles de um usuario """
        pass
    
    def adicionar_email(self, telefone: Email):
        """ Adiciona um novo email na lista de emails de Contato. """
        pass
    
    def remover_email(self, telefone: Email):
        """ Remove um email da lista de email de Contato. """
        pass
    
    def editar_email(self, email: Email, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str]):
        """ Edita informacoes de um email"""
        pass