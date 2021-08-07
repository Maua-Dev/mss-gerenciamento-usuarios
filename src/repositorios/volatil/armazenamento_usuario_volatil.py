from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone        
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.aluno import Aluno

from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.roles import Roles

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro
from src.interfaces.interface_deletar_usuario import IDeletarUsuario

from typing import Optional
from datetime import date

class ArmazenamentoUsuarioVolatil(IArmazenamento, IAlteracaoInfosCadastro, IDeletarUsuario):
    armazem: list[Usuario]

    def __init__(self):
        self.armazem = []


    def usuarioExiste(self, outro_usuario: Usuario):
        for u in self.armazem:
            if u.nome == outro_usuario.nome and u.nascimento == outro_usuario.nascimento:
                return True
        return False

    def cadastrarUsuario(self, usuario: Usuario):
        self.armazem.append(usuario)


    def getUsuario(self, ra: RA):
        pass


    def logarUsuario(self, login: str, senha: str):
        pass
    
    def adicionarTelefone(self, usuario: Usuario, telefone: Telefone):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            u[0].contato.telefones.append(telefone)
        
    def removerTelefone(self, usuario: Usuario, telefone: Telefone):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            u[0].contato.telefones.remove(telefone)
        
    def editarTelefone(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int], numero: Optional[str], prioridade: Optional[int]):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            t = [t for t in u[0].contato.telefones if (t.numero == telefone.numero and t.ddd == telefone.ddd)]
            if t != []:
                if tipo != None:
                    t[0].tipo = tipo
                if ddd != None:
                    t[0].numero = numero
                if numero != None:
                    t[0].ddd = ddd
                if prioridade != None:
                    t[0].prioridade = prioridade
        
    def adicionarEmail(self, usuario: Usuario, email: Email):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            u[0].contato.emails.append(email)
        
    def removerEmail(self, usuario: Usuario, email: Email):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            u[0].contato.emails.remove(email)
        
    def editarEmail(self, usuario: Usuario, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail], prioridade: Optional[int]):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            e = [e for e in u[0].contato.emails if (e.email == email.email and e.tipo == email.tipo)]            
            if e != []:        
                if email_novo != None:
                    e[0].email = email_novo
                if tipo != None:
                    e[0].tipo = tipo
                if prioridade != None:
                    e[0].prioridade = prioridade
        
    def adicionarEndereco(self, usuario: Usuario, endereco: Endereco):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            u[0].contato.enderecos.append(endereco)
        
    def removerEndereco(self, usuario: Usuario, endereco: Endereco):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            u[0].contato.enderecos.remove(endereco)
        
    def editarEndereco(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int], cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            e = [e for e in u[0].contato.enderecos if (e.logradouro == endereco.logradouro and e.cep == endereco.cep)]
            if e != []:
                if logradouro != None:
                    e[0].logradouro = logradouro
                if numero != None:
                    e[0].numero = numero
                if cep != None:
                    e[0].cep = cep
                if complemento != None:
                    e[0].complemento = complemento
                if tipo != None:
                    e[0].tipo = tipo
        
    def quantidadeEmails(self, usuario: Usuario):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            return len(u[0].contato.emails)
        return []
    
    def quantidadeEnderecos(self, usuario: Usuario):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            return len(u[0].contato.enderecos)
        return []
    
    def quantidadeTelefones(self, usuario: Usuario):
        u = [u for u in self.armazem if (u.nome == usuario.nome and u.nascimento == usuario.nascimento)]
        if u != []:
            return len(u[0].contato.telefones)
        return []
    
    def usuarioExiste(self, usuario: Usuario):
        for u in self.armazem:
            if u.nome == usuario.nome and u.nascimento == usuario.nascimento:
                return True
        return False
    
    def getUsuarioPorNomeENascimento(self, nome: str, nascimento: date):
        u = [u for u in self.armazem if (u.nome == nome and u.nascimento == nascimento)]
        if u != []:
            return u[0]
        return []
    
    def removerAlunoPorRA(self, ra: RA):
        for u in self.armazem:
            if Roles.ALUNO in u.roles:
                if u.ra == ra:
                    self.armazem.remove(u)
                    return True
        return False
    
    def alunoExiste(self, ra: RA):
        for u in self.armazem:
            if Roles.ALUNO in u.roles:
                if u.ra == ra:
                    return True
        return False