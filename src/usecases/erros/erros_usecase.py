

class ErroUsuarioExiste(Exception):
    def __init__(self):
        super().__init__("Usuário já existe!")


