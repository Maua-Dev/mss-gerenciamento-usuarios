from fastapi import Response

from src.usecases.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

from src.controladores.fastapi.enums.status_code import STATUS_CODE


class CDeletarUsuarioPorEmailFastAPI():

    repo: IArmazenamento

    def __init__(self, repo: IArmazenamento):
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
            response = Response(content="Usuario deletado com sucesso", status_code=STATUS_CODE.OK.value)
            
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        return response