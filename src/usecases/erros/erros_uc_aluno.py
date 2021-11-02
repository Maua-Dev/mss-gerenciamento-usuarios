
class ErroAlunoJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Aluno já cadastrado")


class ErroEmailInvalido(Exception):
    def __init__(self):
        super().__init__("Email inválido")


class ErroAlunoNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Aluno não encontrado")