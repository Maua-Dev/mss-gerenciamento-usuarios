
class ErroUsuarioNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("O usuário não foi encontrado")