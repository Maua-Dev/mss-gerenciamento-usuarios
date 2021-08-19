from fastapi import Response

from src.usecases.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail

from src.interfaces.interface_deletar_usuario import IDeletarUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

class CDeletarUsuarioPorEmailFastAPI():

    repo: IDeletarUsuario

    def __init__(self, repo: IDeletarUsuario):
        self.repo = repo
    
    def __call__(self, body: dict):
        """ Estilo do body:
            {
                "email": email string
            }
        """
        
        try:
            deletarUsuarioPorEmailUC = UCDeletarUsuarioPorEmail(self.repo)
            deletarUsuarioPorEmailUC(body['email'])
            response = Response(content="Usuario deletado com sucesso", status_code=200)
            
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=400)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=400)
            
        return response