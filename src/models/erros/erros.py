class ErroControladorInvalido(Exception):
    def __init__(self):
        super().__init__("Tipo de controlador invalido")

class ErroRepositorioInvalido(Exception):
    def __init__(self):
        super().__init__("Tipo de repositorio invalido")