
class ErroUsuarioExiste(Exception):
    def __init__(self):
        super().__init__("Usuário já existe!")


class ErroIdInvalido(Exception):
    def __init__(self):
        super().__init__("Id inválido")


# considerar adicionar esse erro em controladores ao inves de uc
class ErroInesperado(Exception):
    def __init__(self):
        super().__init__("Erro inesperado")
