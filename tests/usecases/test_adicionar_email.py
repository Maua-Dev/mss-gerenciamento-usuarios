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

from src.usecases.uc_adicionar_email import UCAdicionarEmail

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

class TestAdicionarEmail:
    
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
        
    def mockEmail(self) -> Email:
        return Email(email='email@adicionado.com',
                      tipo=TipoEmail.TRABALHO,
                      prioridade=2)
        
    def test_adicionar_email(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        addEmail = UCAdicionarEmail(repositorio)
        cadastrador = CadastradorUsuario(repositorio)
        
        usuario = self.mockUsuario()
        cadastrador.cadastrar(usuario)
        email_novo = self.mockEmail()
        
        
        addEmail.adicionarEmail(usuario, email_novo)
        
        assert email_novo in repositorio.armazem[repositorio.armazem.index(usuario)].contato.emails
        assert len(repositorio.armazem[0].contato.emails) == 2
        
    def test_erro_usuario_inexistente(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        addEmail = UCAdicionarEmail(repositorio)
        
        usuario = self.mockUsuario()
        email_novo = self.mockEmail()
        
        with pytest.raises(ErroUsuarioInvalido):
            addEmail.adicionarEmail(usuario, email_novo)
            
    def test_erro_email_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        addEmail = UCAdicionarEmail(repositorio)
        cadastrador = CadastradorUsuario(repositorio)
        
        usuario = self.mockUsuario()
        cadastrador.cadastrar(usuario)
        email_novo = None
        
        with pytest.raises(ErroEmailInvalido):
            addEmail.adicionarEmail(usuario, email_novo)
        
        