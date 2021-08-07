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

from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from src.usecases.uc_editar_telefone import UCEditarTelefone

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class TestEditarEmail:
    def mockUsuario(self) -> Usuario:
        email = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
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

        return Usuario(nome='jorge do teste',
                           contato=contato,
                           nascimento= datetime.date(1999, 2, 23),
                           roles=[Roles.ALUNO])
        
    def mockTelefone(self) -> Telefone:
        return Telefone(tipo=TipoTelefone.PRIVADO,
                       numero='99999-9999',
                       ddd=11,
                       prioridade=3)
        
    def mockRepositorio(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = self.mockUsuario()
        cadastrador(usuario)
        return repositorio
    
    def test_editar_telefone(self):
        repositorio = self.mockRepositorio()
        editorTelefone = UCEditarTelefone(repositorio)
        
        usuario = self.mockUsuario()
        telefone = self.mockTelefone()
        
        numero = '99999-8888'
        tipo = TipoTelefone.TRABALHO
        ddd = 12
        prioridade = 3
        
        tel_novo_instanciado = Telefone(tipo = tipo,
                                     ddd = ddd,
                                     numero = numero,
                                     prioridade = prioridade)
        
        editorTelefone.editarTelefone(usuario, telefone, tipo, ddd, numero, prioridade)
        
        assert tel_novo_instanciado in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.telefones
        assert telefone not in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.telefones
        
    def test_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        editorTelefone = UCEditarTelefone(repositorio)
        usuario = self.mockUsuario()
        telefone = self.mockTelefone()
        
        numero = '99999-8888'
        tipo = TipoTelefone.TRABALHO
        ddd = 12
        prioridade = 3
        
        with pytest.raises(ErroUsuarioInvalido):
            editorTelefone.editarTelefone(usuario, telefone, tipo, ddd, numero, prioridade)
            
    def test_erro_telefone_invalido(self):
        repositorio = self.mockRepositorio()
        editorTelefone = UCEditarTelefone(repositorio)
        
        usuario = self.mockUsuario()
        numero = '99999-8888'
        tipo = TipoTelefone.TRABALHO
        ddd = 12
        prioridade = 3
        telefone = Telefone(tipo = tipo,
                                     ddd = ddd,
                                     numero = numero,
                                     prioridade = prioridade)        
        with pytest.raises(ErroTelefoneInvalido):
            editorTelefone.editarTelefone(usuario, telefone, tipo, ddd, numero, prioridade)
        