from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.periodo import Periodo

from src.models.editar_models import substituirValoresAluno
import tests.mock_objetos as mo

class TestEditarModels:

    def testSubstituirAlunoComTodasVariaveisPossiveis(self):

        aluno = mo.mockAluno()

        #FEITO DESSA FORMA PQ para model precisa passar tudo **problema -> um saco fazer qualquer request
        #Nao podemos so criar um Aluno com as infos que queremos trocar
        novo = mo.mockAluno()

        # novo.curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO       # Nao tem outro no models...
        novo.serie = 2
        # novo.disciplinas = [CodigoDisciplina.ECM251]          # Nao tem outro no models...
        novo.periodo = Periodo.NOTURNO
        novo.listaDPs = [CodigoDisciplina.ECM251]
        novo.hasDP = True

        assert aluno == mo.mockAluno()

        substituirValoresAluno(aluno, novo)

        # "novo" usado aqui pois todos os atributos vao ser alterados
        assert aluno == novo

    def testSubstituirAlunoNovoComAtributoNoneNaoDeveSubstituir(self):
        aluno = mo.mockAluno()

        # FEITO DESSA FORMA PQ para model precisa passar tudo **problema -> um saco fazer qualquer request
        # Nao podemos so criar um Aluno com as infos que queremos trocar
        novo = mo.mockAluno()

        # novo.curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO       # Nao tem outro no models...
        novo.serie = 2
        # novo.disciplinas = [CodigoDisciplina.ECM251]          # Nao tem outro no models...
        novo.periodo = None
        novo.listaDPs = [CodigoDisciplina.ECM251]
        novo.hasDP = True

        assert aluno == mo.mockAluno()
        assert novo.periodo is None

        substituirValoresAluno(aluno, novo)

        # Periodo era None anteriormente. Usando "novo" para facilitar código
        novo.periodo = aluno.periodo    # mostrar que não foi alterado.
        assert aluno == novo

    def testSubstituirAlunoNovoComAtributoFalseOuListaVaziaDeveSubstituir(self):
        aluno = mo.mockAlunoComDP()

        # FEITO DESSA FORMA PQ para model precisa passar tudo **problema -> um saco fazer qualquer request
        # Nao podemos so criar um Aluno com as infos que queremos trocar
        novo = mo.mockAluno()

        # novo.curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO       # Nao tem outro no models...
        novo.serie = 2
        # novo.disciplinas = [CodigoDisciplina.ECM251]          # Nao tem outro no models...
        novo.periodo = Periodo.NOTURNO

        novo.listaDPs = []
        novo.hasDP = False

        assert aluno == mo.mockAlunoComDP()
        substituirValoresAluno(aluno, novo)
        assert aluno == novo

#TODO testar para professores - nao dá agora pois enums do models só tem 1 valor