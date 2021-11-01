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

from src.usecases.usuario.uc_editar_email import UCEditarEmail

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroManipulacaoEmailFaculdade


class TestEditarEmail:
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
    
    def test_editar_email(self):
        repositorio = self.mockRepositorio()
        editorEmail = UCEditarEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = self.mockEmail()
        
        email_novo = 'email@alterado.com'
        tipo = TipoEmail.PRIVADO
        prioridade = 2
        
        email_novo_instanciado = Email(email = email_novo,
                                       tipo = tipo,
                                       prioridade = prioridade)
        
        editorEmail(usuario, email, email_novo, tipo, prioridade)
        
        assert email_novo_instanciado in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.emails
        assert email not in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.emails
        
    def test_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        editorEmail = UCEditarEmail(repositorio)
        usuario = self.mockUsuario()
        email = self.mockEmail()
        
        email_novo = 'email@alterado.com'
        tipo = None
        prioridade = 2
        
        with pytest.raises(ErroUsuarioNaoExiste):
            editorEmail(usuario, email, email_novo, tipo, prioridade)
            
    def test_erro_email_invalido(self):
        repositorio = self.mockRepositorio()
        editorEmail = UCEditarEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = Email(email = 'nadave@teste.com',
                      tipo = TipoEmail.PRIVADO,
                      prioridade = 3)
        
        email_novo = 'email@alterado.com'
        tipo = TipoEmail.PRIVADO
        prioridade = 2
        
        with pytest.raises(ErroEmailInvalido):
            editorEmail(usuario, email, email_novo, tipo, prioridade)
        
    def test_erro_editar_email_universitario(self):
        repositorio = self.mockRepositorio()
        editorEmail = UCEditarEmail(repositorio)
        
        usuario = self.mockUsuario()
        email = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
                      prioridade=1)
        
        email_novo = 'email@alterado.com'
        tipo = TipoEmail.PRIVADO
        prioridade = 2
        
        with pytest.raises(ErroManipulacaoEmailFaculdade):
            editorEmail(usuario, email, email_novo, tipo, prioridade)
        