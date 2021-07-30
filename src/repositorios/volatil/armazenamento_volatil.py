from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone        
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco

from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_email import TipoEmail


from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from typing import Optional
from datetime import date

class ArmazenamentoUsuarioVolatil(IArmazenamento, IAlteracaoInfosCadastro):
    armazem: list[Usuario]

    def __init__(self):
        self.armazem = []


    def usuario_existe(self, outro_usuario: Usuario):
        for u in self.armazem:
            if u.nome == outro_usuario.nome and u.nascimento == outro_usuario.nascimento:
                return True
        return False

    def cadastrar_usuario(self, usuario: Usuario):
        self.armazem.append(usuario)


    def get_usuario(self, ra: RA):
        pass


    def logar_usuario(self, login: str, senha: str):
        pass
    
    def adicionarTelefone(self, usuario: Usuario, telefone: Telefone):
        self.armazem[self.armazem.index(usuario)].contato.telefones.append(telefone)
        
    def removerTelefone(self, usuario: Usuario, telefone: Telefone):
        self.armazem[self.armazem.index(usuario)].contato.telefones.remove(telefone)
        
    def editarTelefone(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str]):
        self.armazem[self.armazem.index(usuario)].contato.telefones[self.armazem[self.armazem.index(usuario)].contato.telefones.index(telefone)].tipo = tipo
        self.armazem[self.armazem.index(usuario)].contato.telefones[self.armazem[self.armazem.index(usuario)].contato.telefones.index(telefone)].numero = numero
        self.armazem[self.armazem.index(usuario)].contato.telefones[self.armazem[self.armazem.index(usuario)].contato.telefones.index(telefone)].ddd = ddd
        
    def adicionarEmail(self, usuario: Usuario, email: Email):
        self.armazem[self.armazem.index(usuario)].contato.emails.append(email)
        
    def removerEmail(self, usuario: Usuario, email: Email):
        self.armazem[self.armazem.index(usuario)].contato.emails.remove(email)
        
    def editarEmail(self, usuario: Usuario, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail], prioridade: Optional[int]):
        self.armazem[self.armazem.index(usuario)].contato.emails[self.armazem[self.armazem.index(usuario)].contato.emails.index(email)].email = email_novo
        self.armazem[self.armazem.index(usuario)].contato.emails[self.armazem[self.armazem.index(usuario)].contato.emails.index(email)].tipo = tipo
        self.armazem[self.armazem.index(usuario)].contato.emails[self.armazem[self.armazem.index(usuario)].contato.emails.index(email)].prioridade = prioridade
        
    def adicionarEndereco(self, usuario: Usuario, endereco: Endereco):
        self.armazem[self.armazem.index(usuario)].contato.enderecos.append(endereco)
        
    def removerEndereco(self, usuario: Usuario, endereco: Endereco):
        self.armazem[self.armazem.index(usuario)].contato.enderecos.remove(endereco)
        
    def editarEndereco(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int], cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        self.armazem[self.armazem.index(usuario)].contato.enderecos[self.armazem[self.armazem.index(usuario)].contato.enderecos.index(endereco)].logradouro = logradouro
        self.armazem[self.armazem.index(usuario)].contato.enderecos[self.armazem[self.armazem.index(usuario)].contato.enderecos.index(endereco)].numero = numero
        self.armazem[self.armazem.index(usuario)].contato.enderecos[self.armazem[self.armazem.index(usuario)].contato.enderecos.index(endereco)].cep = cep
        self.armazem[self.armazem.index(usuario)].contato.enderecos[self.armazem[self.armazem.index(usuario)].contato.enderecos.index(endereco)].complemento = complemento
        self.armazem[self.armazem.index(usuario)].contato.enderecos[self.armazem[self.armazem.index(usuario)].contato.enderecos.index(endereco)].tipo = tipo
        
    def quantidadeEmails(self, usuario: Usuario):
        return len(self.armazem[self.armazem.index(usuario)].contato.emails)
    
    def quantidadeEnderecos(self, usuario: Usuario):
        return len(self.armazem[self.armazem.index(usuario)].contato.enderecos)
    
    def quantidadeTelefones(self, usuario: Usuario):
        return len(self.armazem[self.armazem.index(usuario)].contato.telefones)
    
    def usuarioExiste(self, usuario: Usuario):
        for u in self.armazem:
            if u.nome == usuario.nome and u.nascimento == usuario.nascimento:
                return True
        return False
    
    def getUsuarioPorNomeENascimento(self, nome: str, nascimento: date):
        for usuario in self.armazem:
            if usuario.nome == nome and usuario.nascimento == nascimento:
                return usuario