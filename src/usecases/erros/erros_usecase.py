

class ErroUsuarioExiste(Exception):
    def __init__(self):
        super().__init__("Usuário já existe!")


class ErroDadosUsuarioInvalidos(Exception):
    def __init__(self):
        super().__init__("Os dados fornecidos não puderam ser convertidos em um Usuario válido")

