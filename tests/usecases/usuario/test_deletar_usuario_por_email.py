import pytest
import datetime

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.ra import RA

from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.usuario.uc_cadastrar_usuario import UCCadastrarUsuario

from src.usecases.usuario.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail

from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste

class TestUCDeletarUsuarioPorEmail:
    
    def mockAluno(self) -> Aluno:
        email = Email(email='teste@teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade = 1)
        end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='00000-000',
                       tipo = TipoEndereco.RESIDENCIAL)
        tel = Telefone(tipo = TipoTelefone.PRIVADO,
                       numero = '99999-9999',
                       ddd=11,
                       prioridade = 3)
        contato = Contato(emails = [email],
                          telefones = [tel],
                          enderecos = [end])
        ra = RA(ano='19',
                numero='02009',
                digito='0')        
        
        return Aluno(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ra = ra,
                          curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                          serie = 3,
                          disciplinas=[CodigoDisciplina.ECM251],
                          periodo=Periodo.DIURNO,
                          listaDPs=[],
                          hasDP=False)
        
    def mockRepositorio(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        aluno = self.mockAluno()
        cadastrador(aluno)
        return repositorio
    
    def test_remover_usuario_por_email(self):
        repositorio = self.mockRepositorio()
        removedorUsuario = UCDeletarUsuarioPorEmail(repositorio)
        
        email = 'teste@teste.com'
                
        assert self.mockAluno() in repositorio.armazem
                
        removedorUsuario(email)
        
        assert repositorio.getUsuarioPorNomeENascimento('Jorge Do Teste', datetime.date(1999, 2, 23)) == []
        
    def teste_erro_usuario_invalido(self):
        repositorio = ArmazenamentoUsuarioVolatil()
        removedorUsuario = UCDeletarUsuarioPorEmail(repositorio)
        
        email = 'teste@teste.com'
        
        with pytest.raises(ErroUsuarioNaoExiste):
            removedorUsuario(email)