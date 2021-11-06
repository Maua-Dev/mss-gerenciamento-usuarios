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

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.usuario.uc_cadastrar_usuario import UCCadastrarUsuario

from src.usecases.usuario.uc_remover_email import UCRemoverEmail

from src.usecases.erros.erros_usecase import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroManipulacaoEmailFaculdade
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroDeletarEmailUnico

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
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = self.mockUsuario()
        cadastrador(usuario)
        return repositorio
    
    def test_remover_email(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = self.mockEmail()
                
        removerEmail(usuario, email)
        
        assert email not in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.emails
        assert repositorio.quantidadeEmails(repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)))
        
    def teste_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = self.mockEmail()
        
        with pytest.raises(ErroUsuarioNaoExiste):
            removerEmail(usuario, email)
            
    def test_erro_email_invalido(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = Email(email='teste@teste1.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade=1)
                
        with pytest.raises(ErroEmailInvalido):
            removerEmail(usuario, email)
            
    def test_erro_erro_manipular_email_faculdade(self):
        repositorio = self.mockRepositorio()
        removerEmail = UCRemoverEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
                      prioridade=1)
                
        with pytest.raises(ErroManipulacaoEmailFaculdade):
            removerEmail(usuario, email)
            
    def test_erro_deletar_email_unico(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
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
        cadastrador(usuario)
        with pytest.raises(ErroDeletarEmailUnico):
            removerEmail(usuario, email)