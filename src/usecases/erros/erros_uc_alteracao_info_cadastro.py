class ErroUsuarioInvalido(Exception):
    def __init__(self):
        super().__init__("Usuario nao existe!")
        
class ErroEmailInvalido(Exception):
    def __init__(self):
        super().__init__("Email invalido!")