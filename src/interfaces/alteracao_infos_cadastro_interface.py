from devmaua.src.models.telefone import Telefone        
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco

from devmaua.src.enum.roles import Roles                
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_email import TipoEmail

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
    
    def adicionar_email(self, email: Email):
        """ Adiciona um novo email na lista de emails de Contato. """
        pass
    
    def remover_email(self, email: Email):
        """ Remove um email da lista de email de Contato. """
        pass
    
    def editar_email(self, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail], prioridade: Optional[int]):
        """ Edita informacoes de um email"""
        pass
    
    def adicionar_endereco(self, endereco: Endereco):
        """ Adiciona um novo endereco na lista de enderecos de Contato. """
        pass
    
    def remover_endereco(self, endereco: Endereco):
        """ Remove um endereco da lista de enderecos de Contato. """
        pass
    
    def editar_endereco(self, endereco: Endereco, logradouro: Optional[str], numero: Optional[int], cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        """ Edita informacoes de um endereco"""
        pass