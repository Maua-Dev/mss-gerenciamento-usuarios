from devmaua.src.models.aluno import Aluno


def substituirValoresAluno(alunoAntigo: Aluno, alunoNovo: Aluno):
    # não substituido: dados usuário, ra, roles

    # atributos a substituir em <Aluno>
    sub = ["curso", "serie", "disciplinas", "periodo", "listaDPs", "hasDP"]

    for atr in sub:
        getNovo = getattr(alunoNovo, atr)
        # Se alunoAntigo.atr não None ou vazio
        if getNovo:
            # alunoAntigo.atr = alunoNovo.atr
            setattr(alunoAntigo, atr, getNovo)