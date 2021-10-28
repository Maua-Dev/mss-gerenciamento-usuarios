from abc import ABC, abstractmethod
from typing import Optional
from datetime import date

from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_email import TipoEmail


class IArmazenamentoUsuario(ABC):

    """"
    Interface com os métodos necessários para o gerenciamento de usuários
    """

# ================ Getters ================
    @abstractmethod
    def getUsuarioPorRA(self, ra: RA):
        pass

    @abstractmethod
    def getUsuarioPorIdProfessor(self, id:  str):
        pass

# User id não é propriedade de <class Usuario>, dependeria se fosse usada uma db relacional
    @abstractmethod
    def getUsuarioPorUserId(self, id: int):
        pass

# <class Email> não foi usada pois email é um identificador único-> só precisamos que o Email.email seja imputado
    @abstractmethod
    def getUsuarioPorEmail(self, email: str):
        """ Getter com email principal """
        pass

# <class Telefone> possui informações não necessárias. DDD e número são as únicas informações necessárias
# Do jeito que está não conseguimos aproveitar a validação de pydantic pq prioridade e tipo sao obrigatorios
    #TODO: considerar alterar model telefone -> O que define um telefone nao é prioridade e tipo (nao tem validacao disso)
    @abstractmethod
    def getUsuarioPorTelefone(self, ddd: int, numero: str):
        """ getter com telefone principal - A requisição precisa conter DDD e número de telefone"""
        pass

    @abstractmethod
    def getUsuarioPorNomeENascimento(self, nome: str, nascimento: date):
        """ Busca um usuario pelo nome e data de nascimento """
        pass
# =========================================

    @abstractmethod
    def cadastrarUsuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def deletarUsuarioPorEmail(self, email: str):
        """ Remove um usuario a partir do seu email """
        pass

    @abstractmethod
    def usuarioExistePorEmail(self, email: str):
        """ Retorna se um usuario existe """
        pass

    @abstractmethod
    def adicionarTelefone(self, usuario: Usuario, telefone: Telefone):
        """ Adiciona um novo telefone na lista de telefones de Contato. """
        pass

    @abstractmethod
    def removerTelefone(self, usuario: Usuario, telefone: Telefone):
        """ Remove um telefone da lista de telefones de Contato. """
        pass

    @abstractmethod
    def editarTelefone(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int],
                       numero: Optional[str], prioridade: Optional[int]):
        """ Edita informacoes de um Telefone"""
        pass

    @abstractmethod
    def adicionarEmail(self, usuario: Usuario, email: Email):
        """ Adiciona um novo email na lista de emails de Contato. """
        pass

    @abstractmethod
    def removerEmail(self, usuario: Usuario, email: Email):
        """ Remove um email da lista de email de Contato. """
        pass

    @abstractmethod
    def editarEmail(self, usuario: Usuario, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail],
                    prioridade: Optional[int]):
        """ Edita informacoes de um email"""
        pass

    @abstractmethod
    def adicionarEndereco(self, usuario: Usuario, endereco: Endereco):
        """ Adiciona um novo endereco na lista de enderecos de Contato. """
        pass

    @abstractmethod
    def removerEndereco(self, usuario: Usuario, endereco: Endereco):
        """ Remove um endereco da lista de enderecos de Contato. """
        pass

    @abstractmethod
    def editarEndereco(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int],
                       cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        """ Edita informacoes de um endereco"""
        pass

    @abstractmethod
    def quantidadeEmails(self, usuario: Usuario):
        """ Retorna a quantidade de emails que o usuario tem """
        pass

    @abstractmethod
    def quantidadeTelefones(self, usuario: Usuario):
        """ Retorna a quantidade de telefones que o usuario tem """
        pass

    @abstractmethod
    def quantidadeEnderecos(self, usuario: Usuario):
        """ Retorna a quantidade de enderecos que o usuario tem """
        pass

    @abstractmethod
    def usuarioExiste(self, usuario: Usuario):
        """ Retorna se um usuario existe """
        pass


