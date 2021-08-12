from fastapi import Response

from src.usecases.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

class CDeletarUsuarioPorEmailFastAPI():
    
    def deletarUsuarioPorEmail(self, body: dict, deletarUsuarioPorEmailUC: UCDeletarUsuarioPorEmail):
        """ Estilo do body:
            {
                "email": email string
            }
        """
        
        try:
            deletarUsuarioPorEmailUC.deletarUsuarioPorEmail(body['email'])
            response = Response(content="Usuario deletado com sucesso", status_code=200)
            
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=400)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=400)
            
        return response