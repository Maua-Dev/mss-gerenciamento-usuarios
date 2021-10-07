
class ErroUsuarioExiste(Exception):
    def __init__(self):
        super().__init__("Usuário já existe!")


class ErroIdInvalido(Exception):
    def __init__(self):
        super().__init__("Id inválido")