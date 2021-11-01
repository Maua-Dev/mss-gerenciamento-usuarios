
class ErroUsuarioNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("O usuário não foi encontrado")


class ErroAlunoNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("O aluno não foi encontrado")