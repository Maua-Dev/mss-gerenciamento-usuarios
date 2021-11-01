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

from src.usecases.usuario.uc_adicionar_endereco import UCAdicionarEndereco

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido


class TestAdicionarEndereco:
    
    def mockUsuario(self) -> Usuario:
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

        return Usuario(nome='jorge do teste',
                           contato=contato,
                           nascimento= datetime.date(1999, 2, 23),
                           roles=[Roles.ALUNO])
        
    def mockEndereco(self) -> Endereco:
        return Endereco(logradouro='outra rua',
                       numero=210,
                       cep='00000-098',
                       tipo=TipoEndereco.TRABALHO)
        
    def mockRepositorio(self) -> ArmazenamentoUsuarioVolatil:
        armazenamentoUsuarioVolatil = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(armazenamentoUsuarioVolatil)
        usuario = self.mockUsuario()
        cadastrador(usuario)
        return armazenamentoUsuarioVolatil
        
    def test_adicionar_endereco(self):
        armazenamentoUsuarioVolatil = self.mockRepositorio()
        adicionarEndereco = UCAdicionarEndereco(armazenamentoUsuarioVolatil)
        
        usuario = self.mockUsuario()
        endereco = self.mockEndereco()
                
        adicionarEndereco(usuario, endereco)
        
        assert endereco in armazenamentoUsuarioVolatil.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.enderecos
        assert armazenamentoUsuarioVolatil.quantidadeEnderecos(armazenamentoUsuarioVolatil.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23))) == 2
        
    def test_erro_usuario_inexistente(self):
        armazenamentoUsuarioVolatil = ArmazenamentoUsuarioVolatil()
        adicionarEndereco = UCAdicionarEndereco(armazenamentoUsuarioVolatil)
        
        usuario = self.mockUsuario()
        endereco = self.mockEndereco()
        
        with pytest.raises(ErroUsuarioNaoExiste):
            adicionarEndereco(usuario, endereco)
            
    def test_erro_telefone_invalido(self):
        armazenamentoUsuarioVolatil = self.mockRepositorio()
        adicionarEndereco = UCAdicionarEndereco(armazenamentoUsuarioVolatil)
        
        usuario = self.mockUsuario()
        endereco = None
        
        with pytest.raises(ErroEnderecoInvalido):
            adicionarEndereco(usuario, endereco)
            
        