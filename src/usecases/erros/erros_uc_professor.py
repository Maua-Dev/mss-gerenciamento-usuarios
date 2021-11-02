

class ErroProfessorJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Professor já cadastrado")


class ErroProfessorNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Professor não encontrado")