import pytest
import datetime

from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.roles import Roles
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_telefone import TipoTelefone

from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.cadastrar_usuario import CadastradorUsuario

from src.usecases.uc_remover_email import UCRemoverEmail

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarEmailUnico

class TestRemoverEmail:
    
    def mockUsuario(self) -> Usuario:
        email1 = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
                      prioridade=1)
        email2 = Email(email='teste@teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade=1)
        
        end = Endereco(logradouro='rua de tal',
                       numero=20,
                       cep='00000-000',
                       tipo=TipoEndereco.RESIDENCIAL)
        tel = Telefone(tipo=TipoTelefone.PRIVADO,
                       numero='99999-9999',
                       ddd=11,
                       prioridade=3)
        contato = Contato(emails=[email1, email2],
                          telefones=[tel],
                          enderecos=[end])

        return Usuario(nome='jorge do teste',
                           contato=contato,
                           nascimento= datetime.date(1999, 2, 23),
                           roles=[Roles.ALUNO])
        
    def mockEmail(self) -> Email:
        return Email(email='teste@teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade=1)
        
    def mockRepositorio(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = CadastradorUsuario(repositorio)
        usuario = self.mockUsuario()
        cadastrador.cadastrar(usuario)
        return repositorio
    
    def test_remover_email(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = self.mockEmail()
                
        removerEmail.removerEmail(usuario, email)
        
        assert email not in repositorio.armazem[0].contato.emails
        assert len(repositorio.armazem[0].contato.emails) == 1
        
    def teste_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = self.mockEmail()
        
        with pytest.raises(ErroUsuarioInvalido):
            removerEmail.removerEmail(usuario, email)
            
    def test_erro_email_invalido(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = Email(email='teste@teste1.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade=1)
                
        with pytest.raises(ErroEmailInvalido):
            removerEmail.removerEmail(usuario, email)
            
    def test_erro_erro_manipular_email_faculdade(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
                      prioridade=1)
                
        with pytest.raises(ErroManipulacaoEmailFaculdade):
            removerEmail.removerEmail(usuario, email)
            
    def test_erro_deletar_email_unico(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        email = Email(email='teste@teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade=1)
        
        end = Endereco(logradouro='rua de tal',
                       numero=20,
                       cep='00000-000',
                       tipo=TipoEndereco.RESIDENCIAL)
        tel = Telefone(tipo=TipoTelefone.PRIVADO,
                       numero='99999-9999',
                       ddd=11,
                       prioridade=3)
        contato = Contato(emails=[email],
                          telefones=[tel],
                          enderecos=[end])

        usuario = Usuario(nome='jorge do teste',
                           contato=contato,
                           nascimento= datetime.date(1999, 2, 23),
                           roles=[Roles.ALUNO])
        
        with pytest.raises(ErroDeletarEmailUnico):
            removerEmail.removerEmail(usuario, email)