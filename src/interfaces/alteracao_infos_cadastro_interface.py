from devmaua.src.models.telefone import Telefone        #Importa a classe Telefone do repositorio https://github.com/Maua-Dev/models-devmaua
from devmaua.src.enum.roles import Roles                #Importa o enum de Roles do repositorio https://github.com/Maua-Dev/models-devmaua
from devmaua.src.enum.tipo_telefone import TipoTelefone #Importa o enum de TipoTelefone do repositorio https://github.com/Maua-Dev/models-devmaua

from typing import Optional


class IAlteracaoInfosCadastro:
    
    def adicionar_telefone(self, telefone: Telefone):
        """ Adiciona um novo telefone na lista de telefones de Contato. """
        pass
    
    def remover_telefone(self, telefone: Telefone):
        """ Remove um telefone da lista de telefones de Contato. """
        pass
    
    def editar_telefone(self, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str]):
        """ Edita informacoes de um Telefone"""
        pass
        
    def adicionar_roles(self, roles: list[Roles]):
        """ Adiciona roles a um usuario """
        pass
    
    def remover_roles(self, roles: list[Roles]):
        """ Remove roles de um usuario """
        pass