
class ErroAlunoJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Aluno já cadastrado")


class ErroAlunoNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Aluno não encontrado")