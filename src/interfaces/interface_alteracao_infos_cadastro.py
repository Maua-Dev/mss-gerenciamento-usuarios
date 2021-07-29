from devmaua.src.models.telefone import Telefone        
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_email import TipoEmail

from typing import Optional
from abc import ABC, abstractmethod

class IAlteracaoInfosCadastro(ABC):
    
    """ Interface de modificação de informações de um usuario """
    
    @abstractmethod
    def adicionarTelefone(self, usuario: Usuario, telefone: Telefone) -> bool:
        """ Adiciona um novo telefone na lista de telefones de Contato. """
        pass
    
    @abstractmethod
    def removerTelefone(self, usuario: Usuario, telefone: Telefone) -> bool:
        """ Remove um telefone da lista de telefones de Contato. """
        pass
    
    @abstractmethod
    def editarTelefone(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str]) -> bool:
        """ Edita informacoes de um Telefone"""
        pass
    
    @abstractmethod
    def adicionarEmail(self, usuario: Usuario, email: Email) -> bool:
        """ Adiciona um novo email na lista de emails de Contato. """
        pass
    
    @abstractmethod
    def removerEmail(self, usuario: Usuario, email: Email) -> bool:
        """ Remove um email da lista de email de Contato. """
        pass
    
    @abstractmethod
    def editarEmail(self, usuario: Usuario, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail], prioridade: Optional[int]) -> bool:
        """ Edita informacoes de um email"""
        pass
    
    @abstractmethod
    def adicionarEndereco(self, usuario: Usuario, endereco: Endereco) -> bool:
        """ Adiciona um novo endereco na lista de enderecos de Contato. """
        pass
    
    @abstractmethod
    def removerEndereco(self, usuario: Usuario, endereco: Endereco) -> bool:
        """ Remove um endereco da lista de enderecos de Contato. """
        pass
    
    @abstractmethod
    def editarEndereco(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int], cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]) -> bool:
        """ Edita informacoes de um endereco"""
        pass