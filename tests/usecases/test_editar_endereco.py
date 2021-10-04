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
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from src.usecases.uc_editar_endereco import UCEditarEndereco

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido


class TestEditarEndereco:
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
        
    def mockEndereco(self) -> Endereco:
        return Endereco(logradouro='rua de tal',
                       numero=20,
                       cep='00000-000',
                       tipo=TipoEndereco.RESIDENCIAL)
        
    def mockRepositorio(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = self.mockUsuario()
        cadastrador(usuario)
        return repositorio
    
    def test_editar_endereco(self):
        repositorio = self.mockRepositorio()
        editorEndereco = UCEditarEndereco(repositorio)
        
        usuario = self.mockUsuario()
        endereco = self.mockEndereco()
        
        logradouro = 'Rua ABC'
        numero = 23
        cep = '00000-010'
        complemento = 'atras da rua tal'
        tipo = TipoEndereco.RESIDENCIAL
        
        end_novo_instanciado = Endereco(logradouro = logradouro,
                                        numero = numero,
                                        cep = cep,
                                        complemento = complemento,
                                        tipo = tipo)
        
        editorEndereco(usuario, endereco, logradouro, numero, cep, complemento, tipo)
        
        assert end_novo_instanciado in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.enderecos
        assert endereco not in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.telefones
        
    def test_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        editorEndereco = UCEditarEndereco(repositorio)
        
        usuario = self.mockUsuario()
        endereco = self.mockEndereco()
        
        logradouro = 'Rua ABC'
        numero = 23
        cep = '00000-010'
        complemento = 'atras da rua tal'
        tipo = TipoEndereco.RESIDENCIAL
        
        with pytest.raises(ErroUsuarioInvalido):
            editorEndereco(usuario, endereco, logradouro, numero, cep, complemento, tipo)
        
    def test_erro_endereco_invalido(self):
        repositorio = self.mockRepositorio()
        editorEndereco = UCEditarEndereco(repositorio)
        
        usuario = self.mockUsuario()
        
        logradouro = 'Rua ABC'
        numero = 23
        cep = '00000-010'
        complemento = 'atras da rua tal'
        tipo = TipoEndereco.RESIDENCIAL
        
        endereco = Endereco(logradouro = logradouro,
                                        numero = numero,
                                        cep = cep,
                                        complemento = complemento,
                                        tipo = tipo)
        
        with pytest.raises(ErroEnderecoInvalido):
            editorEndereco(usuario, endereco, logradouro, numero, cep, complemento, tipo)
        