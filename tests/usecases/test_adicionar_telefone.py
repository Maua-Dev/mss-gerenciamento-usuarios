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

from src.usecases.uc_adicionar_telefone import UCAdicionarTelefone

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

class TestAdicionarTelefone:
    
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
        
    def mockTelefone(self) -> Telefone:
        return Telefone(tipo=TipoTelefone.TRABALHO,
                       numero='2222-2222',
                       ddd=11,
                       prioridade=3)
        
    def mockRepositorio(self) -> ArmazenamentoUsuarioVolatil:
        armazenamentoUsuarioVolatil = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(armazenamentoUsuarioVolatil)
        usuario = self.mockUsuario()
        cadastrador(usuario)
        return armazenamentoUsuarioVolatil
        
    def test_adicionar_telefone(self):
        armazenamentoUsuarioVolatil = self.mockRepositorio()
        addEmail = UCAdicionarTelefone(armazenamentoUsuarioVolatil)
        
        usuario = self.mockUsuario()
        telefone = self.mockTelefone()
                
        addEmail(usuario, telefone)
        
        assert telefone in armazenamentoUsuarioVolatil.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.telefones
        assert armazenamentoUsuarioVolatil.quantidadeTelefones(armazenamentoUsuarioVolatil.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23))) == 2
        
    def test_erro_usuario_inexistente(self):
        armazenamentoUsuarioVolatil = ArmazenamentoUsuarioVolatil()
        addEmail = UCAdicionarTelefone(armazenamentoUsuarioVolatil)
        
        usuario = self.mockUsuario()
        telefone = self.mockTelefone()
        
        with pytest.raises(ErroUsuarioInvalido):
            addEmail(usuario, telefone)
            
    def test_erro_telefone_invalido(self):
        armazenamentoUsuarioVolatil = self.mockRepositorio()
        addEmail = UCAdicionarTelefone(armazenamentoUsuarioVolatil)
        
        usuario = self.mockUsuario()
        telefone = None
        
        with pytest.raises(ErroTelefoneInvalido):
            addEmail(usuario, telefone)
        
        