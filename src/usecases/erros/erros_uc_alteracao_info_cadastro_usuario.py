class ErroUsuarioNaoExiste(Exception):
    def __init__(self):
        super().__init__("Usuário não existe!")


class ErroManipulacaoEmailFaculdade(Exception):
    def __init__(self):
        super().__init__("Email da faculdade não pode ser modificado")
        
class ErroDeletarEmailUnico(Exception):
    def __init__(self):
        super().__init__("Não é possível deletar o email pois ele é o único email cadastrado para o usuário")
        
class ErroTelefoneInvalido(Exception):
    def __init__(self):
        super().__init__("Telefone inválido!")
                
class ErroDeletarTelefoneUnico(Exception):
    def __init__(self):
        super().__init__("Não é possível deletar o telefone pois ele é o único telefone cadastrado para o usuário")

class ErroEnderecoInvalido(Exception):
    def __init__(self):
        super().__init__("Endereço inválido!")
                
class ErroDeletarEnderecoUnico(Exception):
    def __init__(self):
        super().__init__("Não é possível deletar o endereço pois ele é o único endereço cadastrado para o usuário")
