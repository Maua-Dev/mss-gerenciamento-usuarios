from devmaua.src.models.aluno import Aluno
from devmaua.src.models.professor import Professor


def substituirValoresAluno(alunoAntigo: Aluno, alunoNovo: Aluno):
    # não substituido: dados usuário, ra, roles

    # atributos a substituir em <Aluno>
    sub = ["curso", "serie", "disciplinas", "periodo", "listaDPs", "hasDP"]

    for atr in sub:
        getNovo = getattr(alunoNovo, atr)
        if getNovo is not None:
            # alunoAntigo.atr = alunoNovo.atr
            setattr(alunoAntigo, atr, getNovo)


def substituirValoresProfessor(profAntigo: Professor, profNovo: Professor):
    # não substituido: dados usuário, ID, roles

    # atributos a substituir em <Professor>
    sub = ["troncos", "cursos", "disciplinas"]

    for atr in sub:
        getNovo = getattr(profNovo, atr)
        if getNovo is not None:
            # alunoAntigo.atr = alunoNovo.atr
            setattr(profAntigo, atr, getNovo)
