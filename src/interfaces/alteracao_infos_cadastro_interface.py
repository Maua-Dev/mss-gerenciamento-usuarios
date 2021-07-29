from devmaua.src.models.telefone import Telefone  #Importa todos as classes do repositorio https://github.com/Maua-Dev/models-devmaua
from devmaua.src.enum.tipo_telefone import TipoTelefone    #Importa todos os enums do repositorio https://github.com/Maua-Dev/models-devmaua
from typing import Optional


class AlteracaoInfosCadastroInterface:
    
    def adicionar_telefone(self, telefone: Telefone):
        """ Adiciona um novo telefone na lista de telefones de Contato. """
        pass
    
    def remover_telefone(self, telefone: Telefone):
        """ Remove um telefone da lista de telefones de Contato. """
        pass
    
    def editar_telefone(self, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str]):
        """ Edita informacoes de um Telefone"""
        pass
        