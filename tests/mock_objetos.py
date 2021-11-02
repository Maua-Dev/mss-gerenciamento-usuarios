from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.tronco import Tronco
from devmaua.src.models.aluno import Aluno
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.professor import Professor
from devmaua.src.models.ra import RA
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.roles import Roles
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_telefone import TipoTelefone

import datetime


def mockUsuario() -> Usuario:
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
                   nascimento=datetime.date(1999, 2, 23),
                   roles=[Roles.ALUNO])

# ====== Mocks específicos - para ter um diferente do usuario ========


def mockEmail() -> Email:
    return Email(email='email@mail.com',
                 tipo=TipoEmail.TRABALHO,
                 prioridade=2)


def mockEndereco() -> Endereco:
    return Endereco(logradouro='outra rua',
                    numero=210,
                    cep='00000-098',
                    tipo=TipoEndereco.TRABALHO)


def mockTelefone() -> Telefone:
    return Telefone(tipo=TipoTelefone.TRABALHO,
                    numero='2222-2222',
                    ddd=11,
                    prioridade=3)

# ===== MOCK ALUNO ======

def mockRA() -> RA:
    return RA(ano="18", numero="01234", digito="0")

def mockRADiferente() -> RA:
    return RA(ano="17", numero="01234", digito="0")


# Considerar que Usuário já foi cadastrado
def mockAluno() -> Aluno:
    u = mockUsuario()
    nome = u.nome
    contato = u.contato
    nascimento = u.nascimento

    ra = mockRA()
    curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO
    serie = 4
    disciplinas = [CodigoDisciplina.ECM251]
    periodo = Periodo.DIURNO
    listaDPs = []
    hasDP = False
    roles = u.roles

    return Aluno(
        nome=nome, contato=contato, nascimento=nascimento, roles=roles,
        ra=ra, curso=curso, serie=serie, disciplinas=disciplinas, listaDPs=listaDPs, periodo=periodo, hasDP=hasDP
    )


# ===== MOCK PROFESSOR ======

def mockProfessor() -> Professor:
    u = mockUsuario()
    nome = u.nome
    contato = u.contato
    nascimento = u.nascimento

    ID = mockId()
    troncos = [Tronco.ELETRICA]
    cursos = [NomeCurso.ENGENHARIA_DA_COMPUTACAO]
    disciplinas = [CodigoDisciplina.ECM251]
    # Roles - Professor

    return Professor(
        nome=nome, contato=contato, nascimento=nascimento,
        ID=ID, troncos=troncos, cursos=cursos, disciplinas=disciplinas
    )

def mockIdDiferente() -> str:
    return '0003'

def mockId() -> str:
    return '0002'
