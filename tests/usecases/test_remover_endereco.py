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

from src.usecases.uc_remover_endereco import UCRemoverEndereco

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarEnderecoUnico


class TestRemoverEndereco:
    
    def mockUsuario(self) -> Usuario:
        email = Email(email='email@principal.com',
                      tipo=TipoEmail.UNIVERSITARIO,
                      prioridade=1)
        
        end1 = Endereco(logradouro='rua de tal',
                       numero=20,
                       cep='00000-000',
                       tipo=TipoEndereco.RESIDENCIAL)
        end2 = Endereco(logradouro='outra rua',
                       numero=210,
                       cep='00000-098',
                       tipo=TipoEndereco.TRABALHO)
        tel = Telefone(tipo=TipoTelefone.PRIVADO,
                       numero='99999-9999',
                       ddd=11,
                       prioridade=3)
        contato = Contato(emails=[email],
                          telefones=[tel],
                          enderecos=[end1, end2])

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
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = CadastradorUsuario(repositorio)
        usuario = self.mockUsuario()
        cadastrador.cadastrar(usuario)
        return repositorio
    
    def test_remover_endereco(self):
        repositorio = self.mockRepositorio()
        removerEndereco = UCRemoverEndereco(repositorio)
        
        usuario = self.mockUsuario()
        endereco = self.mockEndereco()
                
        removerEndereco.removerEndereco(usuario, endereco)
        
        assert endereco not in repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)).contato.enderecos
        assert repositorio.quantidadeEnderecos(repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23))) == 1
        
    def teste_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        removerEndereco = UCRemoverEndereco(repositorio)
        
        usuario = self.mockUsuario()
        endereco = self.mockEndereco()
        
        with pytest.raises(ErroUsuarioInvalido):
            removerEndereco.removerEndereco(usuario, endereco)
            
    def test_erro_endereco_invalido(self):
        repositorio = self.mockRepositorio()
        removerEndereco = UCRemoverEndereco(repositorio)
        
        usuario = self.mockUsuario()
        endereco = Endereco(logradouro='outra rua errada',
                       numero=210,
                       cep='00000-098',
                       tipo=TipoEndereco.TRABALHO)
                
        with pytest.raises(ErroEnderecoInvalido):
            removerEndereco.removerEndereco(usuario, endereco)
            
    def test_erro_deletar_endereco_unico(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = CadastradorUsuario(repositorio)
        removerEndereco = UCRemoverEndereco(repositorio)
        
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
        cadastrador.cadastrar(usuario)
        
        with pytest.raises(ErroDeletarEnderecoUnico):
            removerEndereco.removerEndereco(usuario, end)