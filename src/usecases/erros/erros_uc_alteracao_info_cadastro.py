class ErroUsuarioNaoExiste(Exception):
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
        
class ErroTelefoneInvalido(Exception):
    def __init__(self):
        super().__init__("Telefone invalido!")
                
class ErroDeletarTelefoneUnico(Exception):
    def __init__(self):
        super().__init__("Nao é possivel deletar o telefone pois ele é o único telefone cadastrado para o usuario")

class ErroEnderecoInvalido(Exception):
    def __init__(self):
        super().__init__("Endereco invalido!")
                
class ErroDeletarEnderecoUnico(Exception):
    def __init__(self):
        super().__init__("Nao é possivel deletar o endereco pois ele é o único endereco cadastrado para o usuario")
