
class ErroUsuarioNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("O usuário não foi encontrado")


class ErroNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Não encotrado encontrado")