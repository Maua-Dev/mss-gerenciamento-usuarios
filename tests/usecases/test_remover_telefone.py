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

from src.usecases.uc_remover_telefone import UCRemoverTelefone

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarTelefoneUnico


class TestRemoverTelefone:
    
    def mockUsuario(self) -> Usuario:
        email = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
                      prioridade=1)
        
        end = Endereco(logradouro='rua de tal',
                       numero=20,
                       cep='00000-000',
                       tipo=TipoEndereco.RESIDENCIAL)
        tel1 = Telefone(tipo=TipoTelefone.PRIVADO,
                       numero='99999-9999',
                       ddd=11,
                       prioridade=3)
        tel2 = Telefone(tipo=TipoTelefone.TRABALHO,
                       numero='2222-2222',
                       ddd=11,
                       prioridade=3)
        contato = Contato(emails=[email],
                          telefones=[tel1, tel2],
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
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = self.mockUsuario()
        cadastrador(usuario)
        return repositorio
    
    def test_remover_telefone(self):
        repositorio = self.mockRepositorio()
        removerTelefone = UCRemoverTelefone(repositorio)
        
        usuario = self.mockUsuario()
        telefone = self.mockTelefone()
                
        removerTelefone(usuario, telefone)
        
        assert telefone not in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.telefones
        assert repositorio.quantidadeTelefones(repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23))) == 1
        
    def teste_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        removerTelefone = UCRemoverTelefone(repositorio)
        
        usuario = self.mockUsuario()
        telefone = self.mockTelefone()
        
        with pytest.raises(ErroUsuarioInvalido):
            removerTelefone(usuario, telefone)
            
    def test_erro_telefone_invalido(self):
        repositorio = self.mockRepositorio()
        removerTelefone = UCRemoverTelefone(repositorio)
        
        usuario = self.mockUsuario()
        telefone = Telefone(tipo=TipoTelefone.TRABALHO,
                       numero='2222-2223',
                       ddd=11,
                       prioridade=3)
                
        with pytest.raises(ErroTelefoneInvalido):
            removerTelefone(usuario, telefone)
            
    def test_erro_deletar_telefone_unico(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        removerTelefone = UCRemoverTelefone(repositorio)
        
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
        
        with pytest.raises(ErroDeletarTelefoneUnico):
            removerTelefone(usuario, tel)