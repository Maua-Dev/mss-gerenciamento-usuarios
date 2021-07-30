class ErroUsuarioInvalido(Exception):
    def __init__(self):
        super().__init__("Usuario nao existe!")
        
class ErroEmailInvalido(Exception):
    def __init__(self):
        super().__init__("Email invalido!")
        
class ErroManipulacaoEmailFaculdade(Exception):
    def __init__(self):
        super().__init__("Email da faculdade nao pode ser modificado")
        
class ErroDeletarEmailUnico(Exception):
    def __init__(self):
        super().__init__("Nao é possivel deletar o email pois ele é o único email cadastrado para o usuario")