import pytest
from devmaua.src.enum.roles import Roles
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.cadastrar_usuario import CadastradorUsuario
from src.usecases.erros.erros_usecase import ErroUsuarioExiste





class TestCadastro:


    def mock_usuario(self):
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
                           nascimento='1999-02-23',
                           roles=[Roles.ALUNO])

    def test_cadastrar(self):
        armazenamento = ArmazenamentoUsuarioVolatil()
        cadastrador = CadastradorUsuario(armazenamento)
        usuario1 = self.mock_usuario()


        cadastrador.cadastrar(usuario1)
        assert usuario1 in armazenamento.armazem

    def test_erro_usuario_existente(self):
        armazenamento = ArmazenamentoUsuarioVolatil()
        cadastrador = CadastradorUsuario(armazenamento)
        usuario1 = self.mock_usuario()

        cadastrador.cadastrar(usuario1)
        with pytest.raises(ErroUsuarioExiste):
            cadastrador.cadastrar(usuario1)
        assert len(armazenamento.armazem) == 1





